"""Animated flat GTA-style radar: stylised top-down maps per scene, player arrow moving along keyframed paths.

render(events, t_end, out_dir) writes radar_00000.png ... (RADAR_PX x RADAR_PX, RGBA) at 24 fps from t=0.
events: dict of absolute times (seconds) computed by the build from the clip timeline.
"""
import math, os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

K = 2
D = 236                 # visible circle diameter (display px)
PAD = 40                # room for ring, N badge, shadow
RADAR_PX = D + 2 * PAD  # overlay size (display px)
FPS = 24

ROAD = (138, 150, 164, 255)
ROAD_EDGE = (98, 108, 120, 255)
BLOCK = (44, 52, 64, 255)
BUILD = (62, 72, 86, 255)
PARK = (58, 112, 74, 255)
WATER = (52, 118, 196, 255)
PLAZA = (92, 100, 112, 255)
BG = (36, 43, 54, 255)
ROUTE = (255, 158, 28, 255)
PIN = (120, 40, 160, 255)

BAHN = "C:/Windows/Fonts/bahnschrift.ttf"


def _f(size, var="Bold"):
    f = ImageFont.truetype(BAHN, size)
    f.set_variation_by_name(var)
    return f


S_MAP = D * K / 1000.0  # map units -> px at 2x


def P(x, y):
    return (x * S_MAP, y * S_MAP)


def rect(d, x0, y0, x1, y1, fill):
    d.rectangle((*P(x0, y0), *P(x1, y1)), fill=fill)


def road(d, pts, w):
    d.line([P(*p) for p in pts], fill=ROAD_EDGE, width=round((w + 8) * S_MAP), joint="curve")
    d.line([P(*p) for p in pts], fill=ROAD, width=round(w * S_MAP), joint="curve")


def icon(d, x, y, letter, color):
    r = 26 * S_MAP
    cx, cy = P(x, y)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color, outline=(15, 15, 15, 255), width=2 * K)
    f = _f(round(30 * S_MAP))
    d.text((cx, cy + 1), letter, font=f, fill=(255, 255, 255, 255), anchor="mm")


def label(d, x, y, text, size=26):
    f = _f(round(size * S_MAP), "SemiBold Condensed")
    d.text(P(x, y), text, font=f, fill=(225, 230, 238, 210), anchor="mm")


def map_blloku():
    im = Image.new("RGBA", (D * K, D * K), BG)
    d = ImageDraw.Draw(im)
    for x0, x1 in [(0, 150), (195, 465), (535, 805), (850, 1000)]:
        for y0, y1 in [(0, 225), (275, 545), (605, 875), (925, 1000)]:
            rect(d, x0, y0, x1, y1, BLOCK)
            for bx in range(x0 + 18, x1 - 40, 70):
                for by in range(y0 + 18, y1 - 40, 66):
                    rect(d, bx, by, bx + 52, by + 48, BUILD)
    rect(d, 600, 640, 760, 840, PARK)
    rect(d, 230, 300, 330, 400, PARK)
    for x in (172, 500, 828):
        road(d, [(x, -20), (x, 1020)], 46 if x != 500 else 70)
    for y in (250, 575, 900):
        road(d, [(-20, y), (1020, y)], 48)
    label(d, 500, 120, "BLLOKU", 34)
    icon(d, 610, 620, "H", (64, 150, 90, 255))   # home
    icon(d, 395, 620, "S", (36, 132, 236, 255))  # sneaker store
    return im


def map_bulevardi():
    im = Image.new("RGBA", (D * K, D * K), BG)
    d = ImageDraw.Draw(im)
    for x0, x1 in [(0, 360), (650, 1000)]:
        for y0, y1 in [(0, 300), (340, 640), (680, 1000)]:
            rect(d, x0, y0, x1, y1, BLOCK)
            for bx in range(x0 + 20, x1 - 40, 80):
                for by in range(y0 + 20, y1 - 40, 74):
                    rect(d, bx, by, bx + 58, by + 54, BUILD)
    rect(d, 520, -20, 650, 1020, PARK)
    rect(d, 560, -20, 600, 1020, WATER)
    road(d, [(440, -20), (440, 1020)], 130)
    d.line([P(440, -20), P(440, 1020)], fill=(200, 205, 212, 255), width=max(1, round(4 * S_MAP)))
    for y in (320, 660):
        road(d, [(-20, y), (520, y)], 46)
        road(d, [(650, y), (1020, y)], 46)
    # pyramid
    cx, cy = 760, 800
    d.polygon([P(cx, cy - 90), P(cx + 90, cy), P(cx, cy + 90), P(cx - 90, cy)], fill=(176, 182, 190, 255),
              outline=(120, 126, 134, 255))
    label(d, 760, 930, "PIRAMIDA", 24)
    label(d, 300, 120, "BULEVARDI", 30)
    return im


def map_stadium():
    im = Image.new("RGBA", (D * K, D * K), BG)
    d = ImageDraw.Draw(im)
    rect(d, 0, 0, 1000, 1000, BLOCK)
    for bx in range(20, 980, 86):
        for by in range(20, 980, 80):
            if not (230 < bx < 860 and 150 < by < 900):
                rect(d, bx, by, bx + 62, by + 56, BUILD)
    rect(d, 250, 540, 860, 900, PLAZA)
    road(d, [(200, -20), (200, 1020)], 60)
    road(d, [(-20, 940), (1020, 940)], 60)
    road(d, [(900, -20), (900, 1020)], 50)
    # stadium
    x0, y0, x1, y1 = 330, 170, 790, 520
    rect(d, x0, y0, x1, y1, (176, 40, 40, 255))
    rect(d, x0 + 40, y0 + 40, x1 - 40, y1 - 40, (70, 74, 82, 255))
    rect(d, x0 + 90, y0 + 85, x1 - 90, y1 - 85, (72, 150, 70, 255))
    rect(d, 280, 140, 360, 220, (236, 196, 52, 255))  # tower
    label(d, 560, 120, "AIR ALBANIA", 26)
    icon(d, 700, 610, "$", (64, 170, 90, 255))        # ATM
    icon(d, 610, 700, "C", (232, 128, 32, 255))       # chestnut cart
    return im


def lerp(a, b, t):
    return a + (b - a) * t


def path_at(keys, t):
    """keys: list of (time, (x, y)). Returns position and heading (deg, 0 = up) at time t."""
    if t <= keys[0][0]:
        return keys[0][1], None
    for (t0, p0), (t1, p1) in zip(keys, keys[1:]):
        if t0 <= t <= t1:
            u = 0 if t1 == t0 else (t - t0) / (t1 - t0)
            u = u * u * (3 - 2 * u)
            pos = (lerp(p0[0], p1[0], u), lerp(p0[1], p1[1], u))
            if p0 != p1:
                return pos, math.degrees(math.atan2(p1[0] - p0[0], -(p1[1] - p0[1])))
            return pos, None
    return keys[-1][1], None


def draw_arrow(d, pos, heading):
    cx, cy = P(*pos)
    a = 17 * K
    pts = [(0, -a), (a * 0.75, a * 0.8), (0, a * 0.35), (-a * 0.75, a * 0.8)]
    r = math.radians(heading)
    rot = [(cx + x * math.cos(r) - y * math.sin(r), cy + x * math.sin(r) + y * math.cos(r)) for x, y in pts]
    d.polygon(rot, fill=(255, 255, 255, 255), outline=(15, 15, 15, 255), width=2 * K)


def draw_pin(d, pos):
    px, py = P(*pos)
    r = 13 * K
    d.ellipse((px - r, py - 2.2 * r, px + r, py), fill=PIN, outline=(0, 0, 0, 255), width=2 * K)
    d.polygon([(px - r * 0.6, py - r * 0.6), (px + r * 0.6, py - r * 0.6), (px, py + r * 0.5)], fill=PIN)
    d.ellipse((px - r * 0.38, py - 1.48 * r, px + r * 0.38, py - 0.72 * r), fill=(255, 255, 255, 255))


def frame_shell(content):
    """Circle-mask the content and add ring + centred N badge. Returns RADAR_PX x RADAR_PX image at 2x."""
    size = RADAR_PX * K
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    x0 = y0 = PAD * K
    sh = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse((x0 - 6 * K, y0 + 4 * K, x0 + D * K + 6 * K, y0 + D * K + 14 * K), fill=(0, 0, 0, 150))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
    mask = Image.new("L", (D * K, D * K), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, D * K - 1, D * K - 1), fill=255)
    im.paste(content, (x0, y0), mask)
    d = ImageDraw.Draw(im)
    ring = 9
    box = (x0 - ring * K, y0 - ring * K, x0 + D * K + ring * K, y0 + D * K + ring * K)
    d.ellipse((box[0] - 3 * K, box[1] - 3 * K, box[2] + 3 * K, box[3] + 3 * K), outline=(10, 10, 10, 255), width=3 * K)
    d.arc(box, 90, 270, fill=(64, 214, 96, 255), width=ring * K)
    d.arc(box, 270, 450, fill=(36, 132, 236, 255), width=ring * K)
    d.ellipse((x0 - K, y0 - K, x0 + D * K + K, y0 + D * K + K), outline=(10, 10, 10, 255), width=2 * K)
    nr = 21 * K
    nx, ny = size / 2, y0 - ring / 2 * K
    d.ellipse((nx - nr, ny - nr, nx + nr, ny + nr), fill=(14, 14, 14, 255), outline=(255, 255, 255, 230), width=2 * K)
    d.text((nx, ny), "N", font=_f(26 * K), fill=(255, 255, 255, 255), anchor="mm")
    return im


def render(ev, t_end, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    maps = {"blloku": map_blloku(), "bulevardi": map_bulevardi(), "stadium": map_stadium()}
    home, store = (610, 640), (395, 640)
    paths = {
        "blloku": [(0, home), (ev["walk_start"], home), (ev["store_enter"], store),
                   (ev["exit_store"], store), (ev["exit_store"] + 3.0, (430, 700)), (ev["exit_store"] + 6.0, (500, 840))],
        "bulevardi": [(0, (440, 860)), (ev["green"], (440, 860)), (ev["green"] + 1.6, (440, 650))],
        "stadium": [(0, (560, 860)), (ev["atm_walk"], (560, 860)), (ev["atm_walk"] + 2.0, (690, 640)),
                    (ev["cart_walk"], (690, 640)), (ev["cart_walk"] + 1.6, (630, 690))],
    }
    pins = {"blloku": (store, ev["store_enter"]), "bulevardi": ((440, 120), 1e9), "stadium": ((690, 630), ev["atm_walk"] + 2.0)}
    heading = {"blloku": 270.0, "bulevardi": 0.0, "stadium": 45.0}
    sched = [("blloku", 0, ev["s2"]), ("bulevardi", ev["s2"], ev["s3"]), ("stadium", ev["s3"], t_end)]
    cache = {}
    n = int(round(t_end * FPS))
    for i in range(n):
        t = i / FPS
        for name, a, b in sched:
            if a <= t < b:
                break
        pos, h = path_at(paths[name], t)
        if h is not None:
            heading[name] = h
        content = maps[name].copy()
        d = ImageDraw.Draw(content)
        pin, pin_until = pins[name]
        if t < pin_until:
            d.line([P(*pos), P(*pin)], fill=(0, 0, 0, 255), width=round(14 * S_MAP))
            d.line([P(*pos), P(*pin)], fill=ROUTE, width=round(9 * S_MAP))
            draw_pin(d, pin)
        draw_arrow(d, pos, heading[name])
        key = (name, round(pos[0], 1), round(pos[1], 1), round(heading[name], 1), t < pin_until)
        if key not in cache:
            cache.clear()
            cache[key] = frame_shell(content).resize((RADAR_PX, RADAR_PX), Image.LANCZOS)
        out = cache[key]
        # fade in at start, crossfade-ish dip at scene switches, fade out at end
        alpha = 1.0
        for edge in (ev["s2"], ev["s3"]):
            if abs(t - edge) < 0.15:
                alpha = min(alpha, abs(t - edge) / 0.15)
        alpha = min(alpha, max(0.0, min(1.0, (t - 0.6) / 0.3)), max(0.0, min(1.0, (t_end - t) / 0.3)))
        if alpha < 1:
            o = out.copy()
            o.putalpha(o.getchannel("A").point(lambda v: round(v * alpha)))
            o.save(os.path.join(out_dir, f"radar_{i:05d}.png"))
        else:
            out.save(os.path.join(out_dir, f"radar_{i:05d}.png"))
    return n
