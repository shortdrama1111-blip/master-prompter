# Montage v4: struktura e klientit; veshja 1 nga montage v2, 2+3 nga take 27. Burimi i vjetër: zoom-cut v3 (prerjet e tij: 1.83 3.33 4.67 6.38 7.88 9.67 11.17 12.71 14.29).
# Shot-i 11.17–12.71 hiqet (njëra këmbë e xhinseve doli portokalli).
# Shpejtësitë nga analysis-v6-cut.md. Përdorimi: python3 zoomcut_v2.py BURIMI.mp4 DALJA.mp4
import cv2, numpy as np, math, subprocess, sys
OUT = sys.argv[1]
W,H,FPS,SUB = 720,1280,24,8
def load(path):
    cap=cv2.VideoCapture(path); fr=[]
    while True:
        ok,f=cap.read()
        if not ok: break
        fr.append(cv2.resize(f,(W,H),interpolation=cv2.INTER_LANCZOS4))
    return fr, cap.get(cv2.CAP_PROP_FPS) or 24
SRC={'B':load('results/seedance-v5-greybox-take1.mp4'),'V2':load('results/firenze-v5-montage-v2.mp4'),'T27':load('results/seedance-27-outfit2-3-take1.mp4')}
def lerp(a,b,u): return a+(b-a)*u
def logz(z0,z1,u): return math.exp(lerp(math.log(z0),math.log(z1),u))
def ease_out(u): return 1-(1-u)**3
# çdo funksion: u∈[0,1] -> (zoom, cx, cy, roll°); cx,cy në pikselë të burimit
def real(z0=1.0,z1=1.0,cy=640,cx=360):  return lambda u:(logz(z0,z1,u),cx,cy,0)
def punch_end(cy=560):           return lambda u:(1.0 if u<0.88 else logz(1.0,1.3,(u-0.88)/0.12),360,cy,0)
def bounce(cy=640,cx=360):       return lambda u:((logz(1.0,1.24,u/0.5) if u<0.5 else logz(1.24,1.06,(u-0.5)/0.5)),cx,cy,0)
def crash_out(cy0=520,cy1=640,z0=2.43,cx0=360):
    def f(u):
        z=logz(z0,1.0,u); k=math.log(z)/math.log(z0); return z,lerp(360,cx0,k),lerp(cy1,cy0,k),-5*k
    return f
def settle(z0=1.12,cy=640,roll=0): return lambda u:(1+(z0-1)*(1-ease_out(u)),360,cy,roll*(1-ease_out(u)))
# (start në burim, kohëzgjatja, lëvizja)
# Struktura e videos së klientit (refs/v4/reference-video-v4.mp4), kohë reale; zoom vetëm te kalimet e veshjeve.
PLAN=[
 ('V2',0.00,8.11,real()),               # veshja 1: montage v2 (e pëlqyer)
 ('T27',0.10,0.30,crash_out(560,640)),  # kalim → veshja 2: crash zoom out
 ('T27',0.40,1.00,real()),              # wide, i vetmi plan që ecën drejt kamerës (veshja e plotë)
 ('B',10.20,1.50,real()),               # detaj: duart te rripi dhe fundi me kuadrata
 ('T27',4.80,1.40,real()),              # plan mesatar, shikim te lentja
 ('T27',3.45,1.00,real()),              # 3/4 trupi i plotë te vitrinat
 ('B',12.95,1.50,real()),               # profil i afërt te vitrina
 ('T27',7.95,0.30,crash_out(700,640)),  # kalim → veshja 3: crash zoom out
 ('T27',8.25,1.35,real()),              # wide në portik
 ('T27',9.75,1.35,real()),              # xhinset, clogs
 ('T27',12.80,1.40,real()),             # menga me dantella
 ('T27',14.35,1.65,real()),             # te kolona, mbyllja
]
def render(img,z,cx,cy,rot):
    hw,hh=W/2/z,H/2/z; cx=min(max(cx,hw),W-hw); cy=min(max(cy,hh),H-hh)
    M=cv2.getRotationMatrix2D((cx,cy),rot,z); M[0,2]+=W/2-cx; M[1,2]+=H/2-cy
    return cv2.warpAffine(img,M,(W,H),flags=cv2.INTER_LANCZOS4,borderMode=cv2.BORDER_REFLECT)
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
  '-c:v','libx264','-crf','16','-pix_fmt','yuv420p',OUT],stdin=subprocess.PIPE)
for src,st,dur,fn in PLAN:
    FR,sfps=SRC[src]; n=max(1,round(dur*FPS))
    for i in range(n):
        img=FR[min(round((st+i/FPS)*sfps),len(FR)-1)]
        acc=np.zeros((H,W,3),np.float32)
        for s in range(SUB):
            z,cx,cy,rot=fn(min((i+0.5*s/SUB)/n,1.0)); acc+=render(img,z,cx,cy,rot)
        p.stdin.write((acc/SUB).astype(np.uint8).tobytes())
p.stdin.close(); p.wait()
