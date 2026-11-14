# HUD në stilin e viteve '80 (homazh): ora, paratë, jeta, yjet e kërkimit, arma, minimapa, "mission passed".
# Del si sekuencë PNG 1080x1920 me alfa, 24 fps. Përdorim: python3 hud_vc.py <out_dir> <timeline.json>
import json, math, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
OUT=sys.argv[1]; T=json.load(open(sys.argv[2])); os.makedirs(OUT, exist_ok=True)
FPS=24; W,H=1080,1920
FONT=os.path.join(os.path.dirname(__file__),'fonts','TitanOne-Regular.ttf')
f_clock=ImageFont.truetype(FONT,54); f_money=ImageFont.truetype(FONT,54); f_small=ImageFont.truetype(FONT,40)
f_mp=ImageFont.truetype(FONT,96); f_mp2=ImageFont.truetype(FONT,84)
BLUE=(150,205,255); GREEN=(70,205,95); PINK=(255,120,200); OUTL=(12,10,30); NAVY=(30,55,115)

def star(cx,cy,r,k=0.45):
    return [(cx+(r if i%2==0 else r*k)*math.cos(-math.pi/2+i*math.pi/5),
             cy+(r if i%2==0 else r*k)*math.sin(-math.pi/2+i*math.pi/5)) for i in range(10)]
def rtext(d,xr,y,s,font,fill,sw=5):
    w=d.textlength(s,font=font); d.text((xr-w,y),s,font=font,fill=fill,stroke_width=sw,stroke_fill=OUTL)

def weapon_box():
    S=150; im=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((4,4,S-4,S-4),18,fill=(255,170,90,235),outline=(255,90,190,255),width=7)
    d.rounded_rectangle((14,14,S-14,S-14),12,fill=(255,200,120,120))
    # pistolë e thjeshtuar
    g=[(26,52),(124,52),(124,74),(80,74),(74,118),(46,118),(54,74),(26,74)]
    d.polygon(g,fill=(55,35,85,255),outline=(255,255,255,255),width=3)
    d.rectangle((108,44,118,52),fill=(55,35,85,255),outline=(255,255,255,255))
    d.arc((60,70,92,100),0,180,fill=(255,255,255,255),width=3)
    return im
WEAPON=weapon_box()

def radar(angle):
    R=135; S=2*R+30; im=Image.new('RGBA',(S,S),(0,0,0,0))
    m=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(m); c=S//2
    d.ellipse((c-R,c-R,c+R,c+R),fill=(20,45,40,215))
    d.polygon([(c-R,c-30),(c-20,c-R),(c+40,c-R),(c-R+10,c+60)],fill=(40,120,70,200))     # park
    d.polygon([(c+R,c+20),(c+60,c+R),(c+R,c+R)],fill=(60,140,200,200))                    # ujë
    for x in range(-R,R,46): d.line((c+x,c-R,c+x+30,c+R),fill=(235,235,235,230),width=7)
    for y in range(-R,R,58): d.line((c-R,c+y,c+R,c+y-18),fill=(235,235,235,230),width=7)
    d.line((c-R,c+R//2,c+R,c-R//3),fill=(255,230,120,240),width=10)                        # bulevardi
    m=m.rotate(angle,resample=Image.BICUBIC,center=(c,c))
    mask=Image.new('L',(S,S),0); ImageDraw.Draw(mask).ellipse((c-R,c-R,c+R,c+R),fill=255)
    im.paste(m,(0,0),mask); d=ImageDraw.Draw(im)
    d.ellipse((c-R,c-R,c+R,c+R),outline=(255,110,200,255),width=9)
    d.ellipse((c-R-4,c-R-4,c+R+4,c+R+4),outline=OUTL,width=3)
    d.polygon([(c,c-16),(c+11,c+12),(c,c+5),(c-11,c+12)],fill=(255,255,255,255),outline=OUTL)  # lojtari
    na=math.radians(-angle-90); nx=c+R*math.cos(na); ny=c+R*math.sin(na)
    d.ellipse((nx-17,ny-17,nx+17,ny+17),fill=(20,20,30,255),outline=(255,255,255,255),width=3)
    d.text((nx,ny),'N',font=f_small.font_variant(size=24),fill=(255,255,255),anchor='mm')
    return im

def at(t,a,b): return a<=t<b
hud_on=T['hud_on']; end=T['end']; stars=T['stars']; blink=T['blink']; mp=T['mission']
N=int(round(T['duration']*FPS))
for i in range(N):
    t=i/FPS; im=Image.new('RGBA',(W,H),(0,0,0,0))
    if hud_on<=t<end:
        d=ImageDraw.Draw(im); xr=W-46-150-26
        mins=41+int(t-hud_on); clock=f"{23+(mins//60)%24:02d}:{mins%60:02d}"
        money=1986
        if t>=mp[0]: money=1986+int(min(1,(t-mp[0])/0.8)*2000)
        rtext(d,xr,60,clock,f_clock,BLUE)
        rtext(d,xr,122,f"${money:08d}",f_money,GREEN)
        # jeta / mburoja
        rtext(d,xr,188,"100",f_small,PINK,4); hx=xr-d.textlength("100",font=f_small)-40
        d.polygon([(hx,212),(hx-16,198),(hx-16,190),(hx-8,184),(hx,190),(hx+8,184),(hx+16,190),(hx+16,198)],fill=PINK,outline=OUTL)
        ax=hx-40; rtext(d,ax,188,"000",f_small,BLUE,4); sx=ax-d.textlength("000",font=f_small)-30
        d.polygon([(sx-14,190),(sx+14,190),(sx+14,204),(sx,218),(sx-14,204)],fill=(170,190,210),outline=OUTL)
        # yjet (6, nga e djathta)
        n=sum(1 for s in stars if t>=s)
        if t>=mp[0]: n=0
        show=True
        if blink[0]<=t<blink[1]: show=((t-blink[0])%0.5)<0.25
        for k in range(6):
            cx=xr-22-k*48; cy=268
            filled=(5-k)<n and show
            p=star(cx,cy,22)
            d.polygon(p,fill=(235,245,255,255) if filled else NAVY+(230,),outline=OUTL)
            d.line(p+[p[0]],fill=(200,225,255,255) if not filled else (255,255,255,255),width=2)
        im.alpha_composite(WEAPON,(W-46-150,60))
        ang=T['radar'][0]+(T['radar'][1]-T['radar'][0])*max(0,min(1,(t-T['radar'][2])/(T['radar'][3]-T['radar'][2])))
        rd=radar(ang); im.alpha_composite(rd,(40,H-rd.size[1]-300))
    if mp[0]<=t<mp[1]:
        k=min(1,(t-mp[0])/0.15); sc=1.18-0.18*k
        a=1.0 if t<mp[1]-0.3 else (mp[1]-t)/0.3
        layer=Image.new('RGBA',(W,400),(0,0,0,0)); d=ImageDraw.Draw(layer)
        d.text((W/2,120),"mission passed!",font=f_mp,fill=PINK,anchor='mm',stroke_width=9,stroke_fill=OUTL)
        d.text((W/2,240),"$2000",font=f_mp2,fill=PINK,anchor='mm',stroke_width=9,stroke_fill=OUTL)
        layer=layer.resize((int(W*sc),int(400*sc)),Image.LANCZOS)
        if a<1: layer.putalpha(layer.getchannel('A').point(lambda v:int(v*a)))
        im.alpha_composite(layer,(int((W-layer.size[0])/2),int(330-(layer.size[1]-400)/2)))
    im.save(f"{OUT}/hud_{i:04d}.png")
print(N)
