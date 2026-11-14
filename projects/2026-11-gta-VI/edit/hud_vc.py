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

# ---- harta e lëvizshme (stil radar i viteve '80): qyteti bregdetar, bulevardi drejt veriut ----
import random
SC=1.6   # px për metër
def build_map():
    random.seed(7); MW,MH=1600,4200; m=Image.new('RGBA',(MW,MH),(126,168,104,255)); d=ImageDraw.Draw(m)
    d.rectangle((1060,0,MW,MH),fill=(59,111,182,255))            # oqeani në lindje
    d.rectangle((990,0,1060,MH),fill=(232,217,160,255))           # rëra
    for y in range(0,MH,120):                                     # blloqet e ndërtesave
        for x in range(60,880,140):
            if random.random()<0.85: d.rectangle((x+18,y+18,x+122,y+102),fill=(156,191,134,255))
    for y in range(0,MH,120): d.rectangle((0,y,990,y+18),fill=(70,70,70,255)); d.rectangle((0,y+3,990,y+15),fill=(205,205,205,255))
    for x in range(60,900,140): d.rectangle((x,0,x+18,MH),fill=(70,70,70,255)); d.rectangle((x+3,0,x+15,MH),fill=(205,205,205,255))
    d.rectangle((880,0,990,MH),fill=(60,60,60,255))               # bulevardi bregdetar (2 karrexhata)
    d.rectangle((886,0,930,MH),fill=(215,215,215,255)); d.rectangle((940,0,984,MH),fill=(215,215,215,255))
    d.rectangle((930,0,940,MH),fill=(90,150,80,255))              # mediana me palma
    for y in range(400,MH,520): d.rectangle((930,y,940,y+40),fill=(215,215,215,255))   # hapjet e medianës
    d.rectangle((886,120,984,230),fill=(40,40,40,255))            # tuneli në veri (fundi i rrugës)
    return m
MAP=build_map()
def player_pos(t):
    hud_on=T['hud_on']; v=95                                        # px/s në hartë (~40 px/s në radar)
    y=3500-max(0,t-hud_on)*v
    tr0,tr1=T['radar'][2],T['radar'][3]
    k=max(0,min(1,(t-tr0)/(tr1-tr0)))
    x=962-50*(3*k*k-2*k*k*k)                                      # kalon nga karrexhata e djathtë në të majtën
    head=0 if (t<tr0 or t>tr1+0.4) else (-T['radar'][1]*math.sin(math.pi*min(1,(t-tr0)/(tr1-tr0+0.4))))
    return x,y,head
def radar(t):
    R=135; S=2*R+30; c=S//2
    px,py,head=player_pos(t)
    Z=2.4; Rz=int(R*Z)
    crop=MAP.crop((int(px-Rz*1.5),int(py-Rz*1.5),int(px+Rz*1.5),int(py+Rz*1.5))).rotate(head,resample=Image.BICUBIC)
    cs=crop.size[0]; crop=crop.crop((cs//2-Rz,cs//2-Rz,cs//2+Rz,cs//2+Rz)).resize((2*R,2*R),Image.LANCZOS)
    im=Image.new('RGBA',(S,S),(0,0,0,0)); mask=Image.new('L',(2*R,2*R),0); ImageDraw.Draw(mask).ellipse((0,0,2*R-1,2*R-1),fill=255)
    im.paste(crop,(c-R,c-R),mask); d=ImageDraw.Draw(im)
    # policia: pika që pulsojnë kuq/blu prapa lojtarit
    pol=[p for p in T.get('police',[]) if p[0]<=t<p[1]]
    blink=(int(t*8)%2==0)
    for i,(a,b,dist) in enumerate(pol):
        col=(230,40,40,255) if (blink^(i%2==1)) else (50,90,255,255)
        bx=c+(5 if i%2 else -5); by=c+dist*0.7
        d.rectangle((bx-7,by-7,bx+7,by+7),fill=col,outline=OUTL)
    d.ellipse((c-R,c-R,c+R,c+R),outline=(20,20,20,255),width=10)
    d.ellipse((c-R+4,c-R+4,c+R-4,c+R-4),outline=(255,120,200,255),width=4)
    d.polygon([(c,c-17),(c+12,c+13),(c,c+6),(c-12,c+13)],fill=(255,255,255,255),outline=OUTL)
    na=math.radians(-head-90); nx=c+(R-2)*math.cos(na); ny=c+(R-2)*math.sin(na)
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
        rd=radar(t); im.alpha_composite(rd,(40,H-rd.size[1]-300))
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
