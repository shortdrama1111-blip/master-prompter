# HUD homazh i viteve 2010 (stil "LA sot"): radar drejtkëndësh me qoshe të rrumbullakëta poshtë majtas,
# shiritat e jetës/armaturës, radari që pulson kuq/blu kur je i kërkuar, yjet e bardhë dhe paratë lart djathtas.
# Sekuencë PNG 1080x1920 me alfa, 24 fps. Përdorim: python3 hud_v.py <out_dir> <timeline.json>
import json, math, os, sys, random
from PIL import Image, ImageDraw, ImageFont
OUT=sys.argv[1]; T=json.load(open(sys.argv[2])); os.makedirs(OUT, exist_ok=True)
FPS=24; W,H=1080,1920
MON=ImageFont.truetype('/usr/share/fonts/opentype/inter/InterDisplay-BlackItalic.otf',62)
K=(0,0,0)

def star(cx,cy,r,k=0.42):
    return [(cx+(r if i%2==0 else r*k)*math.cos(-math.pi/2+i*math.pi/5),
             cy+(r if i%2==0 else r*k)*math.sin(-math.pi/2+i*math.pi/5)) for i in range(10)]

def build_map():
    random.seed(5); MW,MH=1400,6000; m=Image.new('RGBA',(MW,MH),(96,104,96,255)); d=ImageDraw.Draw(m)
    for y in range(0,MH,90):                                   # blloqe qyteti
        for x in range(0,MW,90):
            r=random.random(); col=(118,128,112,255) if r<0.55 else (104,114,100,255) if r<0.85 else (88,120,84,255)
            d.rectangle((x+10,y+10,x+80,y+80),fill=col)
    for y in range(0,MH,180): d.rectangle((0,y,MW,y+8),fill=(150,150,140,255))
    for x in range(0,MW,180): d.rectangle((x,0,x+8,MH),fill=(150,150,140,255))
    d.rectangle((640,0,760,MH),fill=(186,186,178,255))         # autostrada
    for y in range(0,MH,40): d.rectangle((698,y,702,y+20),fill=(225,225,215,255))
    for y in (1400,2600,3800):                                 # rampa
        d.polygon([(760,y),(900,y-260),(920,y-250),(780,y+20)],fill=(170,170,162,255))
    return m
MAP=build_map()

def radar(t,wanted):
    RW,RH=400,250; Z=1.0; v=T['radar_v']
    px=700; py=T['radar_y0']-t*v
    crop=MAP.crop((int(px-RW/2*Z),int(py-RH*0.7*Z),int(px+RW/2*Z),int(py+RH*0.3*Z))).resize((RW,RH),Image.LANCZOS)
    im=Image.new('RGBA',(RW+12,RH+12),(0,0,0,0)); d=ImageDraw.Draw(im)
    mask=Image.new('L',(RW,RH),0); ImageDraw.Draw(mask).rounded_rectangle((0,0,RW-1,RH-1),14,fill=255)
    if wanted:                                                 # pulsimi kuq / blu
        ph=(t*2.2)%1.0; col=(210,30,30) if ph<0.5 else (30,70,230); a=0.32*abs(math.sin(math.pi*ph*2))
        tint=Image.new('RGBA',(RW,RH),col+(int(255*a),)); crop=Image.alpha_composite(crop,tint)
    im.paste(crop,(6,6),mask)
    cx,cy=6+RW//2,6+int(RH*0.7)
    blink=(int(t*6)%2==0)
    for i,(a,b,dist) in enumerate(T['police']):
        if a<=t<b:
            bx=cx+(18 if i%2 else -18); by=cy+dist
            if by<RH-4:
                c=(230,40,40,255) if (blink^(i%2==1)) else (40,90,255,255)
                d.ellipse((bx-9,by-9,bx+9,by+9),fill=c,outline=(255,255,255,255),width=2)
    d.polygon([(cx,cy-16),(cx+11,cy+12),(cx,cy+5),(cx-11,cy+12)],fill=(255,255,255,255),outline=K)
    d.rounded_rectangle((5,5,RW+6,RH+6),15,outline=(0,0,0,150),width=3)
    return im

N=int(round(T['duration']*FPS)); RE=W-50
for i in range(N):
    t=i/FPS; im=Image.new('RGBA',(W,H),(0,0,0,0))
    if T['hud_on']<=t<T['end']:
        L=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(L)
        n=T['stars'][0][1]
        for ts,s in T['stars']:
            if t>=ts: n=s
        show=True
        for b0,b1 in T['blink']:
            if b0<=t<b1: show=((t-b0)%0.5)<0.28
        for k in range(5):                                     # yjet
            sx=RE-28-k*62; sy=78; p=star(sx,sy,27); on=(4-k)<n
            if on and show: d.polygon(p,fill=(250,250,250,255)); d.line(p+[p[0]],fill=(0,0,0,200),width=3)
            else: d.polygon(p,fill=(0,0,0,90)); d.line(p+[p[0]],fill=(180,180,180,150),width=2)
        m=f"${T['money']:,}"; w=d.textlength(m,font=MON)        # paratë
        d.text((RE-w,128),m,font=MON,fill=(114,204,114,255),stroke_width=5,stroke_fill=K)
        wanted=n>0
        rd=radar(t,wanted); rx,ry=40,H-rd.size[1]-330; L.alpha_composite(rd,(rx,ry))
        by=ry+rd.size[1]+6; bw=rd.size[0]-12                    # shiritat
        d.rectangle((rx+6,by,rx+6+bw,by+16),fill=(0,0,0,150))
        d.rectangle((rx+9,by+3,rx+6+int(bw*0.5)-4,by+13),fill=(90,170,78,255))
        d.rectangle((rx+6+int(bw*0.5)+3,by+3,rx+6+int(bw*0.78),by+13),fill=(74,143,208,255))
        d.rectangle((rx+6+int(bw*0.78)+3,by+3,rx+6+bw-3,by+13),fill=(230,190,60,255))
        al=1.0
        f0,f1=T['fade']
        if t>=f0: al=max(0.0,1-(t-f0)/(f1-f0))
        if al<1: L.putalpha(L.getchannel('A').point(lambda v:int(v*al)))
        im=L
    im.save(f"{OUT}/hud_{i:04d}.png")
print(N)
