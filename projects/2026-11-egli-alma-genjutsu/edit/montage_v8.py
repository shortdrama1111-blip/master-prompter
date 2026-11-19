# Montage v8 (nga v7): pa crop/zoom digital. Lëvizjet e kamerës janë reale (take 32); montimi bën vetëm speed ramp
# (1× në poza, deri 6× në lëvizje) me mjegullim kohor real (mesatare e frame-ve brenda shutter 180°).
import cv2, numpy as np, subprocess, sys, math
OUT=sys.argv[1]; W,H,FPS=720,1280,24
def load(p):
    cap=cv2.VideoCapture(p); fr=[]
    while True:
        ok,f=cap.read()
        if not ok: break
        fr.append(cv2.resize(f,(W,H),interpolation=cv2.INTER_AREA))
    return fr
SRC={k:load(v) for k,v in {'V2':'results/firenze-v5-montage-v2.mp4','T27':'results/seedance-27-outfit2-3-take1.mp4',
     'B':'results/seedance-v5-greybox-take1.mp4','P32':'results/seedance-32-realmoves-take1.mp4'}.items()}
def ramp(segs):
    """segs: (src_a, src_b, v0, v1) – shpejtësia ndryshon linearisht brenda segmentit. Kthen listë (t_src, dt_src) për çdo frame dalës."""
    out=[]
    for a,b,v0,v1 in segs:
        s=a
        while s<b-1e-6:
            v=v0+(v1-v0)*(s-a)/(b-a); ds=v/FPS
            out.append((s,ds)); s+=ds
    return out
def real(a,b): return [(a+i/FPS,1/FPS) for i in range(round((b-a)*FPS))]
def mv(a,b,peak=6,acc=0.3,vin=1.3): return [(a,a+acc,vin,peak),(a+acc,b-acc,peak,peak),(b-acc,b,peak,1)]
# v8: hequr këmbët anash te veshja 1 (1.75–3.875) dhe frame-i i zi (5.33); hequr profili te vitrina te veshja 2;
# pozat para ramp-it më të shkurtra (~0.5 s) dhe me shpejtësi 1.3× që lëvizja të nisë menjëherë.
PLAN=[
 ('V2', real(0.00,1.75)+real(3.875,5.33)+real(5.42,8.11)),  # veshja 1
 ('T27',real(0.40,1.40)),                                   # veshja 2: wide, ecën
 ('B',  real(10.20,11.70)),                                 #   duart te rripi
 ('P32',ramp([(1.60,2.30,1,1.3)]+mv(2.30,4.10)+[(4.10,4.60,1,1.3),(5.80,6.10,1.3,1.3)]+mv(6.10,7.70)+[(7.70,8.35,1,1)])),
 ('T27',real(12.80,14.00)),                                 # veshja 3: menga me dantella
 ('P32',ramp([(8.90,9.60,1,1.3),(9.60,10.20,1.5,2.5)]+mv(10.20,11.80,vin=2.5)+[(11.80,12.40,1,1.3),(13.10,13.40,1.3,1.3)]+mv(13.40,15.30)+[(15.30,16.00,1,1)])),
]
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
  '-c:v','libx264','-crf','16','-pix_fmt','yuv420p',OUT],stdin=subprocess.PIPE)
for src,frames in PLAN:
    FR=SRC[src]
    for s,ds in frames:
        i0=min(round(s*24),len(FR)-1); n=max(1,round(ds*24*0.5))   # shutter 180°
        img=sum(FR[min(i0+k,len(FR)-1)].astype(np.float32) for k in range(n))/n
        p.stdin.write(img.astype(np.uint8).tobytes())
p.stdin.close(); p.wait()
