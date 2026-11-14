# Krijon grafikën e wanted level (5 yje, stil i yni, jo UI e lojës) për 1080x1920.
import math, sys
from PIL import Image, ImageDraw, ImageFilter
out = sys.argv[1]
S = 4                      # supersampling
R = 26                     # rrezja e yllit në px (në 1080 wide)
GAP = 18
W = 5*(2*R) + 4*GAP + 40
H = 2*R + 40
def star(cx, cy, r):
    pts=[]
    for i in range(10):
        a = -math.pi/2 + i*math.pi/5
        rr = r if i%2==0 else r*0.42
        pts.append((cx+rr*math.cos(a), cy+rr*math.sin(a)))
    return pts
for n in range(0,6):
    big = Image.new('RGBA',(W*S,H*S),(0,0,0,0))
    glow = Image.new('RGBA',(W*S,H*S),(0,0,0,0))
    d = ImageDraw.Draw(big); g = ImageDraw.Draw(glow)
    for i in range(5):
        cx = (20 + R + i*(2*R+GAP))*S; cy = (20+R)*S
        p = star(cx,cy,R*S)
        # pozicioni nga e djathta: yjet mbushen nga e majta në të djathtë
        if i < n:
            d.polygon(p, fill=(255,255,255,255))
            g.polygon(p, fill=(255,255,255,200))
        else:
            d.line(p+[p[0]], fill=(255,255,255,95), width=int(2.2*S), joint='curve')
    glow = glow.filter(ImageFilter.GaussianBlur(9*S))
    comp = Image.alpha_composite(glow, big).resize((W,H), Image.LANCZOS)
    comp.save(f"{out}/stars_{n}.png")
print(W,H)
