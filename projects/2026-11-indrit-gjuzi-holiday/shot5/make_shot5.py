"""Shot 5 v4: kompozimi i kutise (shot5/box, nga box_blender.py) mbi plate-in me afer.

- holdout: pjesa perpara e qeses (poligoni nen buze + ana djathtas) dhe fjongoja e bardhe mbi buze,
  qe kutia te futet PAS buzes;
- hije e bute mbi kutine afer buzes pas goditjes (hyrja ne qese);
- dridhje e lehte e kamerase ne goditje (4 px, shuhet per 0.25 s);
- dalja 1080x1920, 24 fps.

python shot5/make_shot5.py
"""
import os, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
FPS, NF = 24, 72
OUT_W, OUT_H = 1080, 1920

plate = np.asarray(Image.open(os.path.join(PROJ, 'refs', 'shot5-startframe-closer-v2.jpg')).convert('RGB'), np.float32)
PH, PW = plate.shape[:2]

# buza e perparme e qeses: (232,690) -> (745,666); ana djathtas (745,666) -> (796,681)
hold = Image.new('L', (PW, PH), 0)
d = ImageDraw.Draw(hold)
d.polygon([(232, 690), (745, 666), (796, 681), (796, 1185), (232, 1192)], fill=255)
hold = np.asarray(hold.filter(ImageFilter.GaussianBlur(1.0)), np.float32) / 255
# fjongoja e bardhe qe ngrihet mbi buze (para kutise)
r, g, b = plate[..., 0], plate[..., 1], plate[..., 2]
white = ((r > 200) & (g > 185) & (b > 180)).astype(np.float32)
band = np.zeros_like(white); band[640:700, 370:620] = 1
hold = np.maximum(hold, np.asarray(Image.fromarray((white * band * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8)), np.float32) / 255)

f_imp = float(open(os.path.join(HERE, 'box', 'timing.txt')).read().split()[0])
yy = np.arange(PH, dtype=np.float32)[:, None]
xx = np.arange(PW, dtype=np.float32)[None, :]
rim = 690 + (xx - 232) * (666 - 690) / (745 - 232)          # y e buzes per cdo x
above = np.clip((rim - yy), 0, None)
rim_shadow = np.exp(-above / 26.0) * (yy < rim)            # hija brenda gojes se qeses, mbi kutine

frames_dir = os.path.join(HERE, 'frames'); os.makedirs(frames_dir, exist_ok=True)
s = OUT_W / PW
crop_h = OUT_H / s
y_off = (PH - crop_h) / 2
for f in range(1, NF + 1):
    box = np.asarray(Image.open(os.path.join(HERE, 'box', f'b{f:04d}.png')).convert('RGBA'), np.float32)
    a = box[..., 3:] / 255 * (1 - hold[..., None])
    rgb = box[..., :3]
    k = np.clip((f - f_imp + 1) / 3.0, 0, 1)                  # hija hyn pas goditjes
    rgb = rgb * (1 - 0.55 * k * rim_shadow[..., None])
    frame = plate * (1 - a) + rgb * a
    # dridhja e kamerase
    t = (f - f_imp) / FPS
    dy = 4.0 * np.exp(-t / 0.08) * np.cos(2 * np.pi * 13 * t) if t >= 0 else 0.0
    dx = 1.5 * np.exp(-t / 0.08) * np.sin(2 * np.pi * 11 * t) if t >= 0 else 0.0
    im = Image.fromarray(np.clip(frame, 0, 255).astype(np.uint8))
    sc = s * 1.006                                            # pak zoom qe dridhja s'nxjerr buze
    w2, h2 = PW * sc, PH * sc
    im = im.resize((round(w2), round(h2)), Image.LANCZOS)
    x0 = (w2 - OUT_W) / 2 + dx; y0 = (h2 - OUT_H) / 2 + dy
    im = im.crop((round(x0), round(y0), round(x0) + OUT_W, round(y0) + OUT_H))
    im.save(os.path.join(frames_dir, f'f{f:03d}.png'))
out = os.path.join(HERE, 'shot5-v4.mp4')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(FPS), '-i', os.path.join(frames_dir, 'f%03d.png'),
                '-c:v', 'libx264', '-crf', '14', '-preset', 'slow', '-pix_fmt', 'yuv420p', out], check=True)
print(out, 'impact', f_imp)
