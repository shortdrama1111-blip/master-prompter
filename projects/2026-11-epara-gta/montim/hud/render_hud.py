"""Render GTA-style HUD overlays as full-frame 720x1280 RGBA PNGs (drawn at 2x, downscaled)."""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

LOGO = sys.argv[1]
OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)
W, H, K = 720, 1280, 2
BAHN = "C:/Windows/Fonts/bahnschrift.ttf"
SYM = "C:/Windows/Fonts/seguisym.ttf"


def font(size, var):
    f = ImageFont.truetype(BAHN, size * K)
    f.set_variation_by_name(var)
    return f


def canvas():
    return Image.new("RGBA", (W * K, H * K), (0, 0, 0, 0))


def save(im, name):
    im.resize((W, H), Image.LANCZOS).save(os.path.join(OUT, name))


def shadow_layer(size, draw_fn, blur=10, alpha=150):
    sh = Image.new("RGBA", size, (0, 0, 0, 0))
    draw_fn(ImageDraw.Draw(sh), (0, 0, 0, alpha))
    return sh.filter(ImageFilter.GaussianBlur(blur))


def text_w(f, s, spacing=0):
    return sum(f.getlength(c) for c in s) + spacing * K * (len(s) - 1)


def draw_spaced(d, xy, s, f, fill, spacing=0):
    x, y = xy
    for c in s:
        d.text((x, y), c, font=f, fill=fill)
        x += f.getlength(c) + spacing * K


def pill(im, box, radius=26, fill=(8, 8, 16, 165), outline=(255, 255, 255, 38)):
    x0, y0, x1, y1 = [v * K for v in box]
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((x0, y0 + 6, x1, y1 + 10), radius=radius * K, fill=(0, 0, 0, 120))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
    ImageDraw.Draw(im).rounded_rectangle((x0, y0, x1, y1), radius=radius * K, fill=fill, outline=outline, width=K)


def gradient_bar(im, box, c0=(210, 0, 127), c1=(49, 39, 131), vertical=True):
    x0, y0, x1, y1 = [round(v * K) for v in box]
    g = Image.new("RGBA", (x1 - x0, y1 - y0))
    gd = ImageDraw.Draw(g)
    n = (y1 - y0) if vertical else (x1 - x0)
    for i in range(n):
        t = i / max(1, n - 1)
        c = tuple(round(a + (b - a) * t) for a, b in zip(c0, c1)) + (255,)
        if vertical:
            gd.line([(0, i), (x1 - x0, i)], fill=c)
        else:
            gd.line([(i, 0), (i, y1 - y0)], fill=c)
    im.alpha_composite(g, (x0, y0))


def star_pts(cx, cy, r):
    import math
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.46
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return pts


def star(im, cx, cy, r, ring):
    """Empty star as a clean ring: outer star minus inner star."""
    m = Image.new("L", im.size, 0)
    md = ImageDraw.Draw(m)
    md.polygon(star_pts(cx, cy, r), fill=255)
    md.polygon(star_pts(cx, cy + ring * 0.15, r - ring * 1.9), fill=0)
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sh.putalpha(m.filter(ImageFilter.GaussianBlur(4)).point(lambda v: v * 0.6))
    im.alpha_composite(sh)
    w = Image.new("RGBA", im.size, (255, 255, 255, 0))
    w.putalpha(m.point(lambda v: v * 0.9))
    im.alpha_composite(w)


# wallet icon from the real logo
logo = Image.open(LOGO).convert("RGBA")
icon = logo.crop((25, 0, 735, 965))
ImageDraw.Draw(icon).rectangle((330, 575, 710, 965), fill=(0, 0, 0, 0))
icon = icon.resize((round(icon.width * 52 * K / icon.height), 52 * K), Image.LANCZOS)

RIGHT = 28   # right margin
TOP = 44


def hud_base(balance, name):
    im = canvas()
    fb = font(40, "SemiBold SemiCondensed")
    fl = font(26, "SemiBold SemiCondensed")
    tw = fb.getlength(balance) / K
    lw = fl.getlength("L") / K
    inner = icon.width / K + 14 + tw + 8 + lw
    x1 = W - RIGHT
    x0 = x1 - inner - 2 * 18
    y0, y1 = TOP, TOP + 72
    pill(im, (x0, y0, x1, y1))
    im.alpha_composite(icon, (round((x0 + 18) * K), round((y0 + 10) * K)))
    d = ImageDraw.Draw(im)
    tx = x0 + 18 + icon.width / K + 14
    d.text((tx * K, (y0 + 12) * K), balance, font=fb, fill=(255, 255, 255, 255))
    d.text(((tx + tw + 8) * K, (y0 + 25) * K), "L", font=fl, fill=(255, 255, 255, 170))
    # wanted level: 5 empty stars, right aligned under the pill
    r, gap = 13, 9
    cy = y1 + 26
    for i in range(5):
        cx = x1 - 14 - r - i * (2 * r + gap)
        star(im, cx * K, cy * K, r * K, 2 * K)
    save(im, name)


def toast(amount, label, color, name, y=164):
    im = canvas()
    fa = font(34, "Bold SemiCondensed")
    fs = font(17, "SemiBold")
    aw = fa.getlength(amount) / K
    sw = text_w(fs, label, 2) / K
    inner = max(aw, sw)
    x1 = W - RIGHT
    x0 = x1 - inner - 18 - 26
    y0, y1 = y, y + 78
    pill(im, (x0, y0, x1, y1), radius=18)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(((x0 + 10) * K, (y0 + 14) * K, (x0 + 15) * K, (y1 - 14) * K), radius=3 * K, fill=color + (255,))
    d.text(((x1 - 18 - aw) * K, (y0 + 8) * K), amount, font=fa, fill=color + (255,))
    draw_spaced(d, ((x1 - 18 - sw) * K, (y0 + 50) * K), label, fs, (255, 255, 255, 190), 2)
    save(im, name)


def location(area, city, name):
    im = canvas()
    ft = font(64, "Bold Condensed")
    fc = font(20, "SemiBold")
    x, ybase = 34, H - 230
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh)
    draw_spaced(sd, ((x + 18) * K, ybase * K), city, fc, (0, 0, 0, 170), 6)
    sd.text(((x + 18) * K, (ybase + 26) * K), area, font=ft, fill=(0, 0, 0, 170))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(9)))
    gradient_bar(im, (x, ybase + 4, x + 5, ybase + 98))
    d = ImageDraw.Draw(im)
    draw_spaced(d, ((x + 18) * K, ybase * K), city, fc, (255, 255, 255, 200), 6)
    d.text(((x + 18) * K, (ybase + 26) * K), area, font=ft, fill=(255, 255, 255, 255))
    save(im, name)


def mission(name):
    im = canvas()
    cy = H * 0.42
    band_h = 230
    band = Image.new("RGBA", (W * K, band_h * K), (0, 0, 0, 0))
    bd = ImageDraw.Draw(band)
    for i in range(band_h * K):
        t = abs(i / (band_h * K) - 0.5) * 2
        bd.line([(0, i), (W * K, i)], fill=(0, 0, 0, round(175 * (1 - t ** 2))))
    im.alpha_composite(band, (0, round((cy - band_h / 2) * K)))
    fm = font(30, "SemiBold SemiCondensed")
    fp = font(96, "Bold Condensed")
    fr = font(22, "SemiBold")
    d = ImageDraw.Draw(im)
    s1 = "MISSION"
    w1 = text_w(fm, s1, 10) / K
    draw_spaced(d, ((W - w1) / 2 * K, (cy - 92) * K), s1, fm, (255, 255, 255, 230), 10)
    s2 = "PASSED"
    w2 = text_w(fp, s2, 4) / K
    # gold gradient text
    mask = Image.new("L", im.size, 0)
    draw_spaced(ImageDraw.Draw(mask), ((W - w2) / 2 * K, (cy - 60) * K), s2, fp, 255, 4)
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sh.putalpha(mask.filter(ImageFilter.GaussianBlur(12)).point(lambda v: v * 0.7))
    im.alpha_composite(sh)
    gold = Image.new("RGBA", im.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(gold)
    top, bot = round((cy - 50) * K), round((cy + 50) * K)
    for y in range(top, bot):
        t = (y - top) / (bot - top)
        c = (round(255 - 10 * t), round(226 - 60 * t), round(140 - 95 * t), 255)
        gd.line([(0, y), (W * K, y)], fill=c)
    gold.putalpha(mask)
    im.alpha_composite(gold)
    d = ImageDraw.Draw(im)
    lw = 300
    gradient_bar(im, ((W - lw) / 2, cy + 58, (W + lw) / 2, cy + 60), c0=(255, 210, 110), c1=(242, 179, 61), vertical=False)
    s3 = "RESPECT +"
    w3 = text_w(fr, s3, 6) / K
    draw_spaced(d, ((W - w3) / 2 * K, (cy + 72) * K), s3, fr, (255, 255, 255, 235), 6)
    save(im, name)


hud_base("25,000", "hud_25000.png")
hud_base("16,278", "hud_16278.png")
hud_base("14,278", "hud_14278.png")
hud_base("12,278", "hud_12278.png")
toast("-8,900 L", "CARD PAYMENT", (255, 92, 96), "toast_pay.png")
toast("+178 L", "CASHBACK", (64, 224, 150), "toast_cashback.png", y=252)
toast("-2,000 L", "SENT TO ARBI", (255, 92, 96), "toast_sent.png")
toast("-2,000 L", "ATM WITHDRAWAL", (255, 92, 96), "toast_atm.png")
location("BLLOKU", "TIRANA", "loc_blloku.png")
location("BULEVARDI", "TIRANA", "loc_bulevardi.png")
location("AIR ALBANIA", "STADIUMI", "loc_stadiumi.png")
mission("mission.png")
print("ok")
