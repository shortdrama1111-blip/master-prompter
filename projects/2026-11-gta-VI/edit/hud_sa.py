# HUD homazh i viteve '90 (San Andreas): grusht, ora, shiriti i jetës, paratë, yjet, radar që lëviz,
# "mission passed! / RESPECT +". Sekuencë PNG 1080x1920 me alfa, 24 fps.
# Përdorim: python3 hud_sa.py <out_dir> <timeline.json>
import json, math, os, sys, random
from PIL import Image, ImageDraw, ImageFont
OUT=sys.argv[1]; T=json.load(open(sys.argv[2])); os.makedirs(OUT, exist_ok=True)
FPS=24; W,H=1080,1920; D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'fonts')
BLK=ImageFont.truetype(os.path.join(D,'BlackOpsOne-Regular.ttf'),66)
BLKs=ImageFont.truetype(os.path.join(D,'BlackOpsOne-Regular.ttf'),60)
TIT=ImageFont.truetype(os.path.join(D,'TitanOne-Regular.ttf'),96)
RES=ImageFont.truetype(os.path.join(D,'BlackOpsOne-Regular.ttf'),78)
NF=ImageFont.truetype(os.path.join(D,'BlackOpsOne-Regular.ttf'),26)
K=(0,0,0); WHT=(240,240,240); GRN=(88,140,72); ORA=(232,150,40); GOLD=(225,170,50)

def fist_box():
    S=150; im=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((4,4,S-4,S-4),24,fill=(245,245,245,255),outline=K,width=8)
    g=(70,70,70,255); l=(200,200,200,255)
    for i in range(4):                                   # gishtat
        d.rounded_rectangle((38+i*20,40,58+i*20,82),9,fill=l,outline=g,width=3)
    d.rounded_rectangle((36,70,118,118),16,fill=l,outline=g,width=3)   # pëllëmba
    d.rounded_rectangle((28,74,62,96),10,fill=l,outline=g,width=3)     # gishti i madh
    return im
FIST=fist_box()

def star(cx,cy,r,k=0.45):
    return [(cx+(r if i%2==0 else r*k)*math.cos(-math.pi/2+i*math.pi/5),
             cy+(r if i%2==0 else r*k)*math.sin(-math.pi/2+i*math.pi/5)) for i in range(10)]
def rtext(d,xr,y,s,font,fill,sw=6):
    w=d.textlength(s,font=font); d.text((xr-w,y),s,font=font,fill=fill,stroke_width=sw,stroke_fill=K); return w

def build_map():
    random.seed(11); MW,MH=2400,2400; m=Image.new('RGBA',(MW,MH),(150,150,145,255)); d=ImageDraw.Draw(m)
    for y in range(0,MH,110):
        for x in range(0,MW,110):
            r=random.random()
            col=(82,130,78,255) if r<0.12 else (214,214,210,255) if r<0.75 else (180,180,175,255)
            d.rectangle((x+14,y+14,x+96,y+96),fill=col)
    for y in range(0,MH,110): d.rectangle((0,y,MW,y+14),fill=(45,45,45,255))
    for x in range(0,MW,110): d.rectangle((x,0,x+14,MH),fill=(45,45,45,255))
    d.rectangle((1196,0,1218,MH),fill=(120,35,35,255))        # rruga kryesore (veri–jug)
    d.rectangle((0,1196,MW,1218),fill=(120,35,35,255))        # rruga tërthore (kryqëzimi i driftit)
    return m
MAP=build_map()
def pose(t):
    # A: drejt veriut; B (drift): kthesë 90° majtas në kryqëzim; pastaj drejt perëndimit
    v=70; b0,b1=T['drift']
    if t<b0: return 1207, 1207+(b0-t)*v, 0
    if t<b1:
        k=(t-b0)/(b1-b0); s=3*k*k-2*k*k*k
        return 1207-s*40, 1207-(1-s)*0, 90*s
    return 1207-40-(t-b1)*v, 1207, 90
def radar(t):
    R=135; S=2*R+30; c=S//2; px,py,head=pose(t); Z=2.2; Rz=int(R*Z)
    crop=MAP.crop((int(px-Rz*1.5),int(py-Rz*1.5),int(px+Rz*1.5),int(py+Rz*1.5))).rotate(-head,resample=Image.BICUBIC)
    cs=crop.size[0]; crop=crop.crop((cs//2-Rz,cs//2-Rz,cs//2+Rz,cs//2+Rz)).resize((2*R,2*R),Image.LANCZOS)
    im=Image.new('RGBA',(S,S),(0,0,0,0)); mask=Image.new('L',(2*R,2*R),0); ImageDraw.Draw(mask).ellipse((0,0,2*R-1,2*R-1),fill=255)
    im.paste(crop,(c-R,c-R),mask); d=ImageDraw.Draw(im)
    blink=(int(t*8)%2==0)
    for i,(a,b,dist,grow) in enumerate(T['police']):
        if a<=t<b:
            dd=dist+max(0,t-grow)*35
            col=(220,40,40,255) if (blink^(i%2==1)) else (40,80,255,255)
            bx=c+(5 if i%2 else -5); by=c+dd*0.7
            if by<c+R-8: d.rectangle((bx-7,by-7,bx+7,by+7),fill=col,outline=K)
    d.ellipse((c-R,c-R,c+R,c+R),outline=K,width=14)
    d.polygon([(c,c-17),(c+12,c+13),(c,c+6),(c-12,c+13)],fill=(255,255,255,255),outline=K)
    na=math.radians(-90+head); nx=c+(R-2)*math.cos(na); ny=c+(R-2)*math.sin(na)
    d.ellipse((nx-17,ny-17,nx+17,ny+17),fill=(255,255,255,255),outline=K,width=4)
    d.text((nx,ny),'N',font=NF,fill=K,anchor='mm')
    return im

N=int(round(T['duration']*FPS)); RE=W-46
for i in range(N):
    t=i/FPS; im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    if T['hud_on']<=t<T['end']:
        mins=T['clock'][1]+int(t); clock=f"{(T['clock'][0]+mins//60)%24:02d}:{mins%60:02d}"
        cw=rtext(d,RE,64,clock,BLK,WHT)
        fx=int(RE-cw-24-150); im.alpha_composite(FIST,(fx,46))
        d.rectangle((fx,214,RE,244),fill=K); d.rectangle((fx+5,219,RE-5,239),fill=(176,60,60))
        rtext(d,RE,258,f"${T['money']:08d}",BLKs,GRN)
        n=T['stars'] if t<T['clear'] else 0
        show=True
        if T['blink'][0]<=t<T['blink'][1]: show=((t-T['blink'][0])%0.5)<0.25
        for k in range(6):
            cx=RE-24-k*50; cy=362; filled=(5-k)<n and show; p=star(cx,cy,23)
            d.polygon(p,fill=GOLD+(255,) if filled else (60,60,60,170),outline=K)
            d.line(p+[p[0]],fill=K,width=3)
        rd=radar(t); im.alpha_composite(rd,(40,H-rd.size[1]-300))
    a0,a1=T['mission']
    if a0<=t<a1:
        k=min(1,(t-a0)/0.15); sc=1.15-0.15*k; al=1.0 if t<a1-0.3 else (a1-t)/0.3
        L=Image.new('RGBA',(W,420),(0,0,0,0)); e=ImageDraw.Draw(L)
        e.text((W/2,130),"mission passed!",font=TIT,fill=ORA,anchor='mm',stroke_width=9,stroke_fill=K)
        e.text((W/2,265),"RESPECT +",font=RES,fill=WHT,anchor='mm',stroke_width=8,stroke_fill=K)
        L=L.resize((int(W*sc),int(420*sc)),Image.LANCZOS)
        if al<1: L.putalpha(L.getchannel('A').point(lambda v:int(v*al)))
        im.alpha_composite(L,(int((W-L.size[0])/2),int(560-(L.size[1]-420)/2)))
    im.save(f"{OUT}/hud_{i:04d}.png")
print(N)
