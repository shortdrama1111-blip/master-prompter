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


FONTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fonts")
LUCKY = os.path.join(FONTS_DIR, "LuckiestGuy-Regular.ttf")


def location(area, city, name):
    """GTA style: bottom right, right aligned, above nothing (radar is bottom left)."""
    im = canvas()
    ft = font(60, "Bold Condensed")
    fc = font(20, "SemiBold")
    right, ybase = W - 34, H - 210
    aw = ft.getlength(area) / K
    cw = text_w(fc, city, 6) / K
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh)
    draw_spaced(sd, ((right - 18 - cw) * K, ybase * K), city, fc, (0, 0, 0, 170), 6)
    sd.text(((right - 18 - aw) * K, (ybase + 26) * K), area, font=ft, fill=(0, 0, 0, 170))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(9)))
    gradient_bar(im, (right - 5, ybase + 4, right, ybase + 94))
    d = ImageDraw.Draw(im)
    draw_spaced(d, ((right - 18 - cw) * K, ybase * K), city, fc, (255, 255, 255, 200), 6)
    d.text(((right - 18 - aw) * K, (ybase + 26) * K), area, font=ft, fill=(255, 255, 255, 255))
    save(im, name)


def outlined_text(im, xy, text, f, fill, stroke, sw, grad=None, shadow=True):
    x, y = xy
    if shadow:
        sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).text((x + 6 * K, y + 8 * K), text, font=f, fill=(0, 0, 0, 160), stroke_width=sw, stroke_fill=(0, 0, 0, 160))
        im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6)))
    ImageDraw.Draw(im).text((x, y), text, font=f, fill=stroke, stroke_width=sw, stroke_fill=stroke)
    if grad:
        mask = Image.new("L", im.size, 0)
        ImageDraw.Draw(mask).text((x, y), text, font=f, fill=255)
        bb = mask.getbbox()
        g = Image.new("RGBA", im.size, (0, 0, 0, 0))
        gd = ImageDraw.Draw(g)
        for yy in range(bb[1], bb[3]):
            t = (yy - bb[1]) / max(1, bb[3] - bb[1] - 1)
            gd.line([(bb[0], yy), (bb[2], yy)], fill=tuple(round(a + (b - a) * t) for a, b in zip(grad[0], grad[1])) + (255,))
        g.putalpha(mask)
        im.alpha_composite(g)
    else:
        ImageDraw.Draw(im).text((x, y), text, font=f, fill=fill)


def mission(name):
    """Classic GTA 'mission passed!' look: chunky orange letters, thick black outline, white respect line."""
    im = canvas()
    f1 = ImageFont.truetype(LUCKY, 74 * K)
    f2 = ImageFont.truetype(LUCKY, 50 * K)
    cy = H * 0.40
    t1, t2 = "MISSION PASSED!", "RESPECT +"
    w1 = f1.getlength(t1) / K
    w2 = f2.getlength(t2) / K
    outlined_text(im, ((W - w1) / 2 * K, (cy - 70) * K), t1, f1, None, (0, 0, 0, 255), 6 * K,
                  grad=((255, 196, 64), (238, 132, 20)))
    outlined_text(im, ((W - w2) / 2 * K, (cy + 22) * K), t2, f2, (255, 255, 255, 255), (0, 0, 0, 255), 5 * K)
    save(im, name)


def radar(plate, crop_box, name, route=None, pin=None, rotate=0):
    """GTA VI style circular radar bottom left, filled with our own aerial plate."""
    im = canvas()
    D = 236
    cx, cy = 34 + D / 2, H - 40 - D / 2
    src = Image.open(plate).convert("RGB").crop(crop_box)
    if rotate:
        src = src.rotate(rotate, expand=False)
    src = src.resize((D * K, D * K), Image.LANCZOS)
    from PIL import ImageEnhance
    src = ImageEnhance.Color(src).enhance(1.25)
    src = ImageEnhance.Brightness(src).enhance(0.92).convert("RGBA")
    # route + waypoint inside the map
    md = ImageDraw.Draw(src)
    if route:
        pts = [(x * D * K, y * D * K) for x, y in route]
        md.line(pts, fill=(0, 0, 0, 255), width=13 * K // 2, joint="curve")
        md.line(pts, fill=(255, 158, 28, 255), width=9 * K // 2, joint="curve")
    if pin:
        px, py = pin[0] * D * K, pin[1] * D * K
        r = 13 * K
        md.ellipse((px - r, py - 2.2 * r, px + r, py), fill=(120, 40, 160, 255), outline=(0, 0, 0, 255), width=2 * K)
        md.polygon([(px - r * 0.6, py - r * 0.6), (px + r * 0.6, py - r * 0.6), (px, py + r * 0.5)], fill=(120, 40, 160, 255))
        md.ellipse((px - r * 0.38, py - 1.48 * r, px + r * 0.38, py - 0.72 * r), fill=(255, 255, 255, 255))
    # player arrow at bottom centre
    ax, ay = D * K / 2, D * K * 0.74
    a = 17 * K
    arrow = [(ax, ay - a), (ax + a * 0.75, ay + a * 0.8), (ax, ay + a * 0.35), (ax - a * 0.75, ay + a * 0.8)]
    md.polygon(arrow, fill=(255, 255, 255, 255), outline=(20, 20, 20, 255), width=2 * K)
    mask = Image.new("L", (D * K, D * K), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, D * K - 1, D * K - 1), fill=255)
    x0, y0 = round((cx - D / 2) * K), round((cy - D / 2) * K)
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse((x0 - 6 * K, y0 + 4 * K, x0 + D * K + 6 * K, y0 + D * K + 14 * K), fill=(0, 0, 0, 150))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
    im.paste(src, (x0, y0), mask)
    d = ImageDraw.Draw(im)
    ring = 9
    box = (x0 - ring * K, y0 - ring * K, x0 + D * K + ring * K, y0 + D * K + ring * K)
    d.ellipse((box[0] - 3 * K, box[1] - 3 * K, box[2] + 3 * K, box[3] + 3 * K), outline=(10, 10, 10, 255), width=3 * K)
    d.arc(box, 90, 270, fill=(64, 214, 96, 255), width=ring * K)      # health, left half
    d.arc(box, 270, 450, fill=(36, 132, 236, 255), width=ring * K)    # armour, right half
    d.ellipse((x0 - 1 * K, y0 - 1 * K, x0 + D * K + 1 * K, y0 + D * K + 1 * K), outline=(10, 10, 10, 255), width=2 * K)
    # N badge
    nr = 21 * K
    nx, ny = cx * K, (cy - D / 2 - ring / 2) * K
    d.ellipse((nx - nr, ny - nr, nx + nr, ny + nr), fill=(14, 14, 14, 255), outline=(255, 255, 255, 230), width=2 * K)
    fn = font(26, "Bold")
    tw = fn.getlength("N")
    d.text((nx - tw / 2, ny - 17 * K), "N", font=fn, fill=(255, 255, 255, 255))
    save(im, name)


hud_base("25,000.00", "hud_25000.png")
hud_base("16,108.90", "hud_16108.png")
hud_base("14,108.90", "hud_14108.png")
hud_base("12,108.90", "hud_12108.png")
toast("-8,900 L", "CARD PAYMENT", (255, 92, 96), "toast_pay.png")
toast("+8.90 L", "CASHBACK", (64, 224, 150), "toast_cashback.png", y=252)
toast("-2,000 L", "SENT TO ARBI", (255, 92, 96), "toast_sent.png")
toast("-2,000 L", "ATM WITHDRAWAL", (255, 92, 96), "toast_atm.png")
location("BLLOKU", "TIRANA", "loc_blloku.png")
location("BULEVARDI", "TIRANA", "loc_bulevardi.png")
location("AIR ALBANIA", "STADIUMI", "loc_stadiumi.png")
mission("mission.png")
PL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "plates")
radar(os.path.join(PL, "blloku_dron-60_v4.jpg"), (230, 620, 890, 1280), "radar_blloku.png",
      route=[(0.5, 0.74), (0.5, 0.55), (0.33, 0.52)], pin=(0.33, 0.52))
radar(os.path.join(PL, "bulevardi_dron-60_v2-edit.jpg"), (120, 560, 620, 1060), "radar_bulevardi.png",
      route=[(0.5, 0.74), (0.52, 0.45), (0.58, 0.2)], pin=(0.58, 0.2))
radar(os.path.join(PL, "frame_23_fundi_ajrore.png"), (40, 380, 680, 1020), "radar_stadiumi.png",
      route=[(0.5, 0.74), (0.46, 0.5), (0.38, 0.4)], pin=(0.38, 0.4))
print("ok")
