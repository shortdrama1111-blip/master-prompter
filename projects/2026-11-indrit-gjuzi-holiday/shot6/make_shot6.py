"""Shot 6: handwritten "Gëzuar Festat" written onto the gift tag + slow push-in.
Usage: python -I make_shot6.py <project_dir>
"""
import sys, os, math
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

P = sys.argv[1]
OUT = os.path.join(P, "shot6", "frames")
os.makedirs(OUT, exist_ok=True)

FPS = 24
DUR = 4.0
N = int(FPS * DUR)

plate = cv2.imread(os.path.join(P, "refs", "shot6-startframe.jpg")).astype(np.float32) / 255.0
H, W = plate.shape[:2]  # 2000 x 1116

# --- tag geometry (measured on the 1116x2000 plate) ---
CX, CY = 560.0, 1385.0          # writing center on tag face
ANG = -27.6                      # text baseline rotation (deg, rising to the right)
FONT = "C:/Windows/Fonts/Inkfree.ttf"
INK = np.array([28, 22, 20], np.float32) / 255.0   # near-black brown, BGR-ish neutral

# --- lines: (text, font size, x offset, y offset) in tag-local px, baseline layout
LINES = [
    ("Gëzuar", 112, -12, -105),
    ("Festat", 112, 18, 15),
    ("xx",      72, 105, 125),
]
# timing (seconds): start, then per-line durations with small pauses
T0 = 0.45
LINE_DUR = [1.05, 0.95, 0.40]
GAP = 0.18

S = 900  # local canvas size
def render_line(text, size):
    font = ImageFont.truetype(FONT, size)
    img = Image.new("L", (S, S), 0)
    d = ImageDraw.Draw(img)
    bbox = d.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]; h = bbox[3] - bbox[1]
    # glyph x-boundaries for per-letter pacing
    xs = []
    acc = 0
    for i in range(len(text)):
        xs.append(d.textlength(text[: i + 1], font=font))
    return font, w, h, bbox, xs

layers = []
t = T0
for (text, size, ox, oy), dur in zip(LINES, LINE_DUR):
    font, w, h, bbox, xs = render_line(text, size)
    img = Image.new("L", (S, S), 0)
    d = ImageDraw.Draw(img)
    x0 = S / 2 - w / 2 + ox - bbox[0]
    y0 = S / 2 - h / 2 + oy - bbox[1]
    d.text((x0, y0), text, font=font, fill=255)
    a = np.asarray(img).astype(np.float32) / 255.0
    a = cv2.GaussianBlur(a, (0, 0), 0.7)          # soft ink edge
    # glyph timing: each glyph gets time proportional to its width, eased inside
    widths = np.diff([0] + xs)
    tw = widths / widths.sum()
    layers.append(dict(a=a, x0=x0 + bbox[0], xs=[0] + list(xs), tw=tw, t0=t, dur=dur))
    t += dur + GAP

def reveal_x(L, tt):
    """local x (from line start) revealed at time tt, letter-by-letter with ease."""
    if tt <= L["t0"]:
        return -1e9
    p = (tt - L["t0"]) / L["dur"]
    if p >= 1:
        return 1e9
    cum = np.concatenate([[0], np.cumsum(L["tw"])])
    i = int(np.searchsorted(cum, p, side="right") - 1)
    i = min(i, len(L["tw"]) - 1)
    q = (p - cum[i]) / L["tw"][i]
    q = q * q * (3 - 2 * q)                        # ease within each glyph (pen slows at ends)
    xa, xb = L["xs"][i], L["xs"][i + 1]
    return xa + (xb - xa) * q

M = cv2.getRotationMatrix2D((S / 2, S / 2), -ANG, 1.0)   # cv2 positive = CCW; we want rising right
M[0, 2] += CX - S / 2
M[1, 2] += CY - S / 2

def smooth(p):
    return p * p * (3 - 2 * p)

xx = np.arange(S, dtype=np.float32)[None, :]
FR = [N-1] if len(sys.argv) > 2 and sys.argv[2] == "test" else range(N)
for f in FR:
    tt = f / FPS
    alpha = np.zeros((S, S), np.float32)
    for L in layers:
        rx = reveal_x(L, tt)
        if rx < -1e8:
            continue
        edge = L["x0"] + rx
        m = np.clip((edge - xx) / 10.0 + 0.5, 0, 1)   # 10px soft pen front
        alpha = np.maximum(alpha, L["a"] * m)
    A = cv2.warpAffine(alpha, M, (W, H), flags=cv2.INTER_LINEAR)
    A = (A * 0.88)[..., None]
    frame = plate * (1 - A) + (plate * INK * 0.35 + INK * 0.65) * A   # ink sits in paper, keeps texture
    # push-in: scale 1.0 -> 0.80 around tag, eased
    p = smooth(min(1.0, tt / DUR))
    s = 1.0 - 0.20 * p
    cw, ch = 1116 * s, 1984 * s
    cx = (1 - p) * (W / 2) + p * CX
    cy = (1 - p) * (H / 2) + p * (CY - 60)
    x1 = np.clip(cx - cw / 2, 0, W - cw); y1 = np.clip(cy - ch / 2, 0, H - ch)
    Mc = np.array([[720 / cw, 0, -x1 * 720 / cw], [0, 1280 / ch, -y1 * 1280 / ch]], np.float32)
    out = cv2.warpAffine(frame, Mc, (720, 1280), flags=cv2.INTER_AREA if s > 0.9 else cv2.INTER_CUBIC)
    cv2.imwrite(os.path.join(OUT, f"f_{f:04d}.png"), np.clip(out * 255, 0, 255).astype(np.uint8))
print("frames", N, "text_end", t)
