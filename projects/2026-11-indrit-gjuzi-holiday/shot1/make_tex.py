"""Shot 1 v7: teksturat e shisheve mask/cond per blender_cards.py, nga fotot origjinale (sfond i zi).

Per cdo rresht: gjen gjeresine reale te shishes, heq 2 px buze (antialias me sfondin e zi) dhe e
shtrin rreshtin mbi gjeresine e profilit te zbutur (e njejta mediane 31 rreshta si te blender_cards.py).
Keshtu siperfaqja 3D nuk merr kurre piksel te zi ose te perseritur anash -> pa vija horizontale.

python shot1/make_tex.py
Dalja: shot1/assets/<emri>_tex.png + <emri>_radius.npy
"""
import os
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
A = os.path.join(HERE, 'assets')
SRC = {'mask': 'refs/image2-peptide-mask.jpg', 'cond': 'refs/image3-conditioner.jpg'}
WARM = np.array([1.0, 0.965, 0.92], np.float32)
INSET = 2.0


def bilateral(r, k=12, tol=2.5, it=3):
    """mesatare vetem me fqinjet me diference < tol px: heq dridhjen 0.5 px, ruan shkallet."""
    r = np.asarray(r, np.float64)
    for _ in range(it):
        pad = np.pad(r, k, mode='edge'); out = np.empty_like(r)
        for i in range(len(r)):
            w = pad[i:i + 2 * k + 1]; sel = np.abs(w - r[i]) < tol
            out[i] = w[sel].mean()
        r = out
    return r


def smooth(r, k=15):
    pad = np.pad(r, k, mode='edge')
    return bilateral(np.array([np.median(pad[i:i + 2 * k + 1]) for i in range(len(r))]))


def build(name):
    a = np.asarray(Image.open(os.path.join(PROJ, SRC[name])).convert('RGB'), np.float32)
    m = a.mean(2) > 30
    ys = np.nonzero(m.any(1))[0]
    y0, y1 = ys[0], ys[-1] + 1
    a, m = a[y0:y1], m[y0:y1]
    H = a.shape[0]
    left = np.array([np.argmax(r) for r in m], np.float32)
    right = np.array([len(r) - np.argmax(r[::-1]) for r in m], np.float32)
    r_row = (right - left) / 2
    c_row = (right + left) / 2
    r_s = smooth(r_row)
    W = int(np.ceil(2 * r_s.max())) + 4
    out = np.zeros((H, W, 3), np.float32)
    xs = np.arange(W, dtype=np.float32) + 0.5 - W / 2           # koordinata e daljes nga qendra
    for y in range(H):
        rs, rr = max(r_s[y], 1.0), max(r_row[y] - INSET, 1.0)
        src_x = c_row[y] + np.clip(xs / rs, -1, 1) * rr - 0.5
        x0 = np.clip(np.floor(src_x).astype(int), 0, a.shape[1] - 2)
        f = (src_x - x0)[:, None]
        out[y] = a[y, x0] * (1 - f) + a[y, x0 + 1] * f
    out = np.clip(out * WARM, 0, 255).astype(np.uint8)
    Image.fromarray(out).save(os.path.join(A, f'{name}_tex.png'))
    np.save(os.path.join(A, f'{name}_radius.npy'), r_row)
    print(name, out.shape, 'r max', r_row.max())


for n in SRC:
    build(n)
