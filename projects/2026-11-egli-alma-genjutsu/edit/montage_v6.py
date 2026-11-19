# Montage v6 (bazuar te v4): struktura e klientit; veshja 1 nga montage v2, 2+3 nga take 27. Burimi i vjetër: zoom-cut v3 (prerjet e tij: 1.83 3.33 4.67 6.38 7.88 9.67 11.17 12.71 14.29).
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
SRC={'P31':load('results/seedance-31-poses-take1.mp4'),'B':load('results/seedance-v5-greybox-take1.mp4'),'V2':load('results/firenze-v5-montage-v2.mp4'),'T27':load('results/seedance-27-outfit2-3-take1.mp4')}
def lerp(a,b,u): return a+(b-a)*u
def logz(z0,z1,u): return math.exp(lerp(math.log(z0),math.log(z1),u))
def ease_out(u): return 1-(1-u)**3
# çdo funksion: u∈[0,1] -> (zoom, cx, cy, roll°); cx,cy në pikselë të burimit
def real(z0=1.0,z1=1.0,cy=640,cx=360):  return lambda u:(logz(z0,z1,u),cx,cy,0)
def punch_end(cy=560):           return lambda u:(1.0 if u<0.88 else logz(1.0,1.3,(u-0.88)/0.12),360,cy,0)
def bounce(cy=640,cx=360,base=1.0): return lambda u:(base*(logz(1.0,1.24,u/0.5) if u<0.5 else logz(1.24,1.06,(u-0.5)/0.5)),cx,cy,0)
def crash_out(cy0=520,cy1=640,z0=2.43,cx0=360):
    def f(u):
        z=logz(z0,1.0,u); k=math.log(z)/math.log(z0); return z,lerp(360,cx0,k),lerp(cy1,cy0,k),-5*k
    return f
def settle(z0=1.12,cy=640,roll=0,cx=360): return lambda u:(1+(z0-1)*(1-ease_out(u)),cx,cy,roll*(1-ease_out(u)))
# (start në burim, kohëzgjatja, lëvizja)
# Struktura e videos së klientit (refs/v4/reference-video-v4.mp4), kohë reale; zoom vetëm te kalimet e veshjeve.
# v6: veshjet 2 dhe 3 me trick-un e references mbi pozat e take 31 (bounce afër → crash zoom out → close → i plotë).
PLAN=[
 ('V2',0.00,8.11,real()),                     # veshja 1: montage v2
 ('T27',0.10,0.30,crash_out(560,640)),        # kalim → veshja 2
 ('T27',0.40,1.00,real()),                    # wide, ecën drejt kamerës
 ('B',10.20,1.50,real()),                     # duart te rripi
 ('P31',3.50,0.21,bounce(340,348,2.2)),       # poza 2 (përballë): bounce te fytyra
 ('P31',0.80,0.30,crash_out(500,640,2.43,408)),# poza 1 (te muri): crash zoom out
 ('P31',1.10,0.60,settle(1.08,640,0,400)),    #   ngadalëson
 ('P31',7.40,0.55,real(1.8,1.55,460,350)),    # poza 3 (përkulur): afër, zoom out
 ('P31',4.40,0.80,settle(1.15,640,0,350)),    # poza 2 trup i plotë
 ('B',12.95,1.40,real()),                     # profil te vitrina
 ('T27',12.80,0.21,bounce(660,300)),          # veshja 3: menga me dantella, bounce
 ('T27',13.01,1.20,real(1.30,1.0,660,300)),   #   zoom out
 ('P31',8.60,0.21,bounce(340,377,2.2)),       # poza 1 (te kolona): bounce te fytyra
 ('P31',12.05,0.30,crash_out(450,640,2.43,320)),# poza 2 (krahu lart): crash zoom out
 ('P31',12.35,0.55,settle(1.08,640,0,330)),   #   ngadalëson
 ('P31',14.70,0.55,real(1.8,1.55,690,360)),   # poza 3 (ulur): afër, zoom out
 ('P31',15.00,1.05,settle(1.2,700,0,360)),    #   trup i plotë, mbyllja
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
