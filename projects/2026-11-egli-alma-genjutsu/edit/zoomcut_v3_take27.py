# Zoom-cut v3: montimi i veshjeve 2+3 mbi results/seedance-27-outfit2-3-take1.mp4 (prerjet e tij: 1.83 3.33 4.67 6.38 7.88 9.67 11.17 12.71 14.29).
# Shot-i 11.17–12.71 hiqet (njëra këmbë e xhinseve doli portokalli).
# Shpejtësitë nga analysis-v6-cut.md. Përdorimi: python3 zoomcut_v2.py BURIMI.mp4 DALJA.mp4
import cv2, numpy as np, math, subprocess, sys
SRC_PATH, OUT = sys.argv[1], sys.argv[2]
W,H,FPS,SUB = 720,1280,24,8
cap=cv2.VideoCapture(SRC_PATH); FR=[]; sfps=cap.get(cv2.CAP_PROP_FPS) or 24
while True:
    ok,f=cap.read()
    if not ok: break
    FR.append(cv2.resize(f,(W,H),interpolation=cv2.INTER_LANCZOS4))
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
PLAN=[
 (0.10,1.50,punch_end(580)),          # O2 wide, ecën drejt kamerës; punch-in në fund
 (1.90,1.30,real(1.06,1.0)),          # O2 këmbët (çizmet)
 (3.40,1.15,real(1.08,1.0)),          # O2 3/4 te vitrinat
 (4.75,0.21,bounce(420)),             # O2 plan mesatar: bounce te fytyra
 (4.96,0.30,crash_out(400,640,2.0)),  #   crash zoom out nga fytyra
 (5.26,0.90,settle(1.08)),            #   ngadalëson
 (6.45,1.35,real(1.12,1.0)),          # O2 profil te vitrina, zoom out → kalim
 (7.95,0.30,crash_out(720,640)),      # O3 portiku: crash zoom out (vazhdon lëvizjen)
 (8.25,1.30,settle(1.10)),            #   ngadalëson, ajo ecën
 (9.75,1.30,real(1.05,1.0)),          # O3 këmbët (xhinset, clogs)
 (12.80,0.21,bounce(660,300)),        # O3 menga me dantella: bounce
 (13.01,1.20,real(1.30,1.0,660,300)), #   zoom out i lehtë
 (14.35,1.65,settle(1.25,640)),       # O3 te kolona, mbyllja
]
def render(img,z,cx,cy,rot):
    hw,hh=W/2/z,H/2/z; cx=min(max(cx,hw),W-hw); cy=min(max(cy,hh),H-hh)
    M=cv2.getRotationMatrix2D((cx,cy),rot,z); M[0,2]+=W/2-cx; M[1,2]+=H/2-cy
    return cv2.warpAffine(img,M,(W,H),flags=cv2.INTER_LANCZOS4,borderMode=cv2.BORDER_REFLECT)
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
  '-c:v','libx264','-crf','16','-pix_fmt','yuv420p',OUT],stdin=subprocess.PIPE)
for st,dur,fn in PLAN:
    n=max(1,round(dur*FPS))
    for i in range(n):
        img=FR[min(round((st+i/FPS)*sfps),len(FR)-1)]
        acc=np.zeros((H,W,3),np.float32)
        for s in range(SUB):
            z,cx,cy,rot=fn(min((i+0.5*s/SUB)/n,1.0)); acc+=render(img,z,cx,cy,rot)
        p.stdin.write((acc/SUB).astype(np.uint8).tobytes())
p.stdin.close(); p.wait()
