"""Shot 1 v5: raftet-ashensor, animim 2D pa gjenerim video.

Plate: refs/shot1-plate-empty.webp (1116x2000, raftet bosh, Nano Banana Pro).
Produktet: fotot reale te refs/ (etiketa te sakta), te ngjyrosura sipas frame-it te klientit.
Levizja si te ref-shot1: konstante, anesoret poshte ~0.33 kat/s, mesi lart ~0.41 kat/s.
Zoom 1.35x, dalja 1080x1920, 30 fps.

python3 shot1/make_shot1.py [--still]
"""
import sys, os, subprocess
import numpy as np
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
R = lambda p: os.path.join(PROJ, p)

OUT_W, OUT_H, FPS, DUR = 1080, 1920, 30, 2.0
ZOOM = 1.0                           # v5 ishte 1.35; v6: tre kolonat me kornizat e jashtme
PERIOD = 559.0                       # hapi i rafteve ne plate (px)
SPEED = {'L': +0.33, 'M': -0.41, 'R': +0.33}   # kate/s, + = poshte
SUBSAMPLES = 4                       # motion blur (shutter 180)

_plate = np.asarray(Image.open(R('refs/shot1-plate-empty.webp')).convert('RGB'), np.float32)
_PH, _PW = _plate.shape[:2]


def extend_rows(src, ext, bw=60):
    """zgjat lart/poshte me perseritje me hapin PERIOD; qepje e bute bw px."""
    H = src.shape[0]
    out = np.zeros((H + 2 * ext,) + src.shape[1:], np.float32)
    out[ext:ext + H] = src
    out[:ext] = src[0:ext]
    out[ext + H:] = src[H - ext:H]
    for y in range(bw):
        w = y / bw
        out[ext + y] = (1 - w) * src[y + ext] + w * src[y]
        yb = H - 1 - y
        out[ext + yb] = (1 - w) * src[yb - ext] + w * src[yb]
    return out


# bota: plate-i i zgjatur vertikalisht + korniza te plota champagne te jashtme + sfond i erret anash
MX, EXT = 40, int(PERIOD)
_E = extend_rows(_plate, EXT)
plate = np.zeros((_E.shape[0], _PW + 2 * MX, 3), np.float32)
_dark = np.array([34, 24, 19], np.float32)
plate[:] = _dark
plate[:, MX:MX + _PW] = _E
_post = _E[:, 363:380]                                  # tekstura e shtylles se brendshme


def _put_post(x0, x1):
    w = x1 - x0
    tex = np.stack([np.asarray(Image.fromarray(_post[..., i], 'F').resize((w, _post.shape[0]), Image.LANCZOS)) for i in range(3)], -1)
    plate[:, x0:x1] = tex
    # hije e bute ne sfondin e erret prane shtylles
    for d in range(1, 18):
        k = 1 - 0.5 * (1 - d / 18)
        if x0 - d >= 0 and x0 - d < MX - 15:
            plate[:, x0 - d] = _dark * k
        if x1 - 1 + d < plate.shape[1] and x1 - 1 + d >= MX + _PW + 10:
            plate[:, x1 - 1 + d] = _dark * k


_put_post(MX - 15, MX + 9)
_put_post(MX + 1103, MX + 1127)
PH, PW = plate.shape[:2]
CROP_W = PW / ZOOM
CROP_H = CROP_W * OUT_H / OUT_W
CX0 = (PW - CROP_W) / 2
CY0 = EXT + _PH / 2 - CROP_H / 2
S = OUT_W / CROP_W                   # bota px -> output px

# kolonat levizese (midis shtyllave champagne), koordinata te botes
COLS = {'L': (MX + 9, MX + 363), 'M': (MX + 380, MX + 733), 'R': (MX + 742, MX + 1103)}
LIP0 = {'L': EXT + 107.0, 'M': EXT + 219.0, 'R': EXT + 115.0}      # buza e pare e raftit
CENTER = {'L': MX + 196.0, 'M': MX + 556.0, 'R': MX + 918.0}

# renditja e produkteve sipas frame-it te klientit, k = indeksi i raftit
LAYOUT = {
    'L': {-1: 'mask', 0: 'box', 1: 'oil', 2: 'box', 3: 'oil', 4: 'cond'},
    'M': {-1: 'oil', 0: 'box', 1: 'box', 2: 'mask', 3: 'box', 4: 'oil', 5: 'box'},
    'R': {-1: 'box', 0: 'oil', 1: 'oil', 2: 'cond', 3: 'box', 4: 'cond'},
}
HEIGHT = {'oil': 340, 'box': 405, 'mask': 450, 'cond': 450}   # plate px

# ngjyra: frame-i i klientit / foto e produktit (per kanal)
GAIN = {
    'box': np.array([231, 204, 179]) / np.array([246, 218, 181]),
    'mask': np.array([219, 202, 192]) / np.array([226, 213, 203]),
    'cond': np.array([214, 194, 180]) / np.array([225, 211, 200]),
}


def fill_rows(m):
    """mbush cdo rresht midis pikes se pare dhe te fundit (silueta konvekse)."""
    out = np.zeros_like(m)
    for y in range(m.shape[0]):
        xs = np.nonzero(m[y])[0]
        if len(xs) > 1:
            out[y, xs[0]:xs[-1] + 1] = True
    return out


def soft(mask, r=1.2):
    im = Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3))
    return np.asarray(im.filter(ImageFilter.GaussianBlur(r)), np.float32) / 255


def load_products():
    P = {}
    a = np.asarray(Image.open(R('refs/image1-hair-oil.jpg')).convert('RGB'), np.float32)
    # kutia
    sat = (a[..., 0] - a[..., 2]) > 30
    ys, xs = np.nonzero(sat[:, :380])
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    rgb = a[y0:y1, x0:x1]
    P['box'] = dict(rgb=rgb * GAIN['box'], alpha=soft(fill_rows(sat[y0:y1, x0:x1]), 0.8), kind='solid')
    # shishja e vajit (xham transparent mbi te bardhe)
    nw = (255 - a.min(2)) > 10
    nw[:, :380] = False
    ys, xs = np.nonzero(nw[300:1000]); ys = ys + 300
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    rgb = a[y0:y1, x0:x1]
    P['oil'] = dict(rgb=rgb, alpha=soft(fill_rows(nw[y0:y1, x0:x1]), 0.8), kind='glass')
    for key, path in (('mask', 'refs/image2-peptide-mask.jpg'), ('cond', 'refs/image3-conditioner.jpg')):
        a = np.asarray(Image.open(R(path)).convert('RGB'), np.float32)
        m = a.mean(2) > 30
        ys, xs = np.nonzero(m)
        y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
        P[key] = dict(rgb=a[y0:y1, x0:x1] * GAIN[key], alpha=soft(fill_rows(m[y0:y1, x0:x1]), 1.0), kind='solid')
    return P


def resize(arr, w, h):
    if arr.ndim == 2:
        return np.asarray(Image.fromarray(arr.astype(np.float32), 'F').resize((w, h), Image.LANCZOS))
    ch = [np.asarray(Image.fromarray(arr[..., i].astype(np.float32), 'F').resize((w, h), Image.LANCZOS)) for i in range(3)]
    return np.stack(ch, -1)


def build_strip(col, products):
    """shirit vertikal i kolones ne shkallen e daljes, me shtrirje lart/poshte (perseritje me hapin PERIOD)."""
    x0, x1 = COLS[col]
    ext = int(PERIOD)
    src = plate[:, x0:x1]
    H = PH + 2 * ext
    strip = np.zeros((H, x1 - x0, 3), np.float32)
    strip[ext:ext + PH] = src
    strip[:ext] = src[0:ext]                 # y<0  -> plate(y+PERIOD)
    strip[ext + PH:] = src[PH - ext:PH]      # y>=PH -> plate(y-PERIOD)
    # qepje e bute: brenda plate-it, 60 px kalim drejt kopjes se perseritur
    bw = 60
    for y in range(bw):
        w = y / bw
        strip[ext + y] = (1 - w) * src[y + ext] + w * src[y]
        yb = PH - 1 - y
        strip[ext + yb] = (1 - w) * src[yb - ext] + w * src[yb]
    # shkalla e daljes
    Hs, Ws = int(round(H * S)), int(round((x1 - x0) * S))
    out = resize(strip, Ws, Hs)
    # produktet
    for k, name in LAYOUT[col].items():
        lip = LIP0[col] + k * PERIOD
        depth = float(np.clip((lip - EXT - 700) * 0.02, 0, 25))
        base = lip - depth
        p = products[name]
        h = HEIGHT[name] * S
        w = h * p['rgb'].shape[1] / p['rgb'].shape[0]
        hi, wi = int(round(h)), int(round(w))
        rgb = resize(p['rgb'], wi, hi)
        al = np.clip(resize(p['alpha'], wi, hi), 0, 1)
        cx = (CENTER[col] - x0) * S
        by = (base + ext) * S
        px0, py0 = int(round(cx - wi / 2)), int(round(by - hi))
        composite(out, rgb, al, px0, py0, p['kind'])
    return out, ext * S


def composite(dst, rgb, al, x0, y0, kind):
    h, w = al.shape
    H, W = dst.shape[:2]
    # hija: kontakt + hije e bute mbi murin
    sh = Image.fromarray((al * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(14))
    sh = np.asarray(sh, np.float32) / 255
    pad = 40
    def paste_mul(arr, ox, oy, strength):
        ys, xs = slice(max(0, oy), min(H, oy + arr.shape[0])), slice(max(0, ox), min(W, ox + arr.shape[1]))
        if ys.stop <= ys.start or xs.stop <= xs.start:
            return
        a = arr[ys.start - oy:ys.stop - oy, xs.start - ox:xs.stop - ox]
        dst[ys, xs] *= (1 - strength * a)[..., None]
    paste_mul(sh, x0 + 6, y0 + 18, 0.45)
    # hije kontakti eliptike ne baze
    cw, ch = int(w * 1.3), 26
    yy, xx = np.mgrid[0:ch, 0:cw]
    e = np.clip(1 - (((xx - cw / 2) / (cw / 2)) ** 2 + ((yy - ch / 2) / (ch / 2)) ** 2), 0, 1) ** 1.5
    paste_mul(e.astype(np.float32), x0 + w // 2 - cw // 2, y0 + h - ch // 2, 0.55)

    ys, xs = slice(max(0, y0), min(H, y0 + h)), slice(max(0, x0), min(W, x0 + w))
    if ys.stop <= ys.start or xs.stop <= xs.start:
        return
    sy, sx = slice(ys.start - y0, ys.stop - y0), slice(xs.start - x0, xs.stop - x0)
    bg = dst[ys, xs]
    a = al[sy, sx][..., None]
    src = rgb[sy, sx]
    hh, ww = src.shape[:2]
    if kind == 'glass':
        t = np.clip(src / 232.0, 0, 1)
        warm = np.array([255, 236, 212], np.float32)
        # xhami: sfondi kalon pothuajse i plote, me nje shkelqim te bute vertikal
        xr0 = np.linspace(0, 1, ww)[None, :, None]
        sheen = 0.16 * np.exp(-((xr0 - 0.30) / 0.12) ** 2) + 0.12
        fill = bg * 0.92 + (warm - bg * 0.92) * sheen
        body = fill * (t ** 1.2)
        # vija te bardha vertikale te dy anet e xhamit (blloku i drites)
        lum = t.mean(2)
        cap = lum < 0.25
        xr = np.linspace(0, 1, ww)[None, :]
        edge = np.exp(-((xr - 0.07) / 0.03) ** 2) + np.exp(-((xr - 0.93) / 0.03) ** 2)
        edge = edge * (~cap) * 0.9
        body = body + (255 - body) * edge[..., None]
        # shkelqim i bute vertikal ne kapakun e zi
        capg = np.exp(-((xr - 0.25) / 0.06) ** 2) * cap * 0.18
        body = body + (255 - body) * capg[..., None]
        out = body
    else:
        # drite: pak me e ndritshme lart (LED nga rafti siper), pak me e erret poshte
        ramp = np.linspace(1.04, 0.93, hh)[:, None, None] if hh > 1 else 1.0
        out = src * ramp
    dst[ys, xs] = bg * (1 - a) + out * a


def main():
    still = '--still' in sys.argv
    products = load_products()
    strips = {c: build_strip(c, products) for c in COLS}
    base = resize(plate, int(round(PW * S)), int(round(PH * S)))
    ox, oy = int(round(CX0 * S)), int(round(CY0 * S))
    nframes = 1 if still else int(round(DUR * FPS))
    os.makedirs(os.path.join(HERE, 'frames'), exist_ok=True)
    for f in range(nframes):
        acc = np.zeros((OUT_H, OUT_W, 3), np.float32)
        for s in range(SUBSAMPLES):
            t = (f + 0.5 * s / SUBSAMPLES) / FPS
            frame = base.copy()
            for c, (x0, x1) in COLS.items():
                strip, ext = strips[c]
                shift = SPEED[c] * PERIOD * S * t        # + = permbajtja zbret
                ytop = ext - shift                         # rreshti i shiritit ne y=0 te plate-it te shkallezuar
                i0 = int(np.floor(ytop)); fr = ytop - i0
                Hs = frame.shape[0]
                seg = strip[i0:i0 + Hs + 1]
                seg = seg[:-1] * (1 - fr) + seg[1:] * fr
                xs0 = int(round(x0 * S))
                frame[:, xs0:xs0 + seg.shape[1]] = seg[:, :frame.shape[1] - xs0]
            acc += frame[oy:oy + OUT_H, ox:ox + OUT_W]
        img = np.clip(acc / SUBSAMPLES, 0, 255).astype(np.uint8)
        Image.fromarray(img).save(os.path.join(HERE, 'frames', f'f{f:03d}.png'))
    if still:
        return
    out = os.path.join(HERE, 'shot1-v6.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), '-i', os.path.join(HERE, 'frames', 'f%03d.png'),
                    '-c:v', 'libx264', '-crf', '14', '-preset', 'slow', '-pix_fmt', 'yuv420p', out], check=True)
    print(out)


if __name__ == '__main__':
    main()
