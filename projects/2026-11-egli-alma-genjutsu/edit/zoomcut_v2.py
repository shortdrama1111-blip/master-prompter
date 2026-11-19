# Zoom-cut v2: montimi i veshjeve 2+3 nga NJË video 16 s (greybox v8 ose gjenerimi i prompt 28).
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
def real(z0=1.0,z1=1.0,cy=640):  return lambda u:(logz(z0,z1,u),360,cy,0)
def punch_end(cy=560):           return lambda u:(1.0 if u<0.88 else logz(1.0,1.3,(u-0.88)/0.12),360,cy,0)
def bounce(cy=640):              return lambda u:((logz(1.0,1.24,u/0.5) if u<0.5 else logz(1.24,1.06,(u-0.5)/0.5)),360,cy,0)
def crash_out(cy0=520,cy1=640):
    def f(u):
        z=logz(2.43,1.0,u); k=math.log(z)/math.log(2.43); return z,360,lerp(cy1,cy0,k),-5*k
    return f
def settle(z0=1.12,cy=640,roll=0): return lambda u:(1+(z0-1)*(1-ease_out(u)),360,cy,roll*(1-ease_out(u)))
# (start në burim, kohëzgjatja, lëvizja)
PLAN=[
 (0.20,1.80,punch_end(560)),      # O2 wide, ecën; punch-in në fund
 (2.30,0.21,bounce(450)),         # O2 fytyra: bounce
 (3.90,0.30,crash_out(520,640)),  # O2 trup i plotë: crash zoom out
 (4.20,0.70,settle(1.10)),        #   vazhdon, ngadalëson
 (5.10,1.40,real(1.06,1.0)),      # O2 këmbët
 (6.80,0.55,real(1.35,1.18)),     # O2 detaj beli: zoom out i lehtë
 (8.30,0.21,bounce(450)),         # O3 fytyra: bounce
 (9.90,0.30,crash_out(520,640)),  # O3 te kolona: crash zoom out
 (10.20,0.90,settle(1.12,640,-2)),#   vazhdon, ngadalëson
 (11.80,0.70,real(1.30,1.12)),    # O3 menga me dantella
 (13.05,1.50,real(1.0,1.0)),      # O3 3/4, kolonat
 (14.60,1.40,settle(1.25,600)),   # O3 wide, mbyllja
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
