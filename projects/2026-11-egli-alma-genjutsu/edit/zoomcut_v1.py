# Outfit 3: rindertim i levizjes se references (analysis-v6-cut.md) ne montim.
# Zoom/roll digital me motion blur (8 nen-frame, shutter 180°), 24fps, 720x1280.
import cv2, numpy as np, math, subprocess, sys
A='results/sheet-v3-test-video.mp4'; B='results/seedance-v5-greybox-take1.mp4'
W,H,FPS,SUB=720,1280,24,8
def load(path):
    cap=cv2.VideoCapture(path); fr=[]
    while True:
        ok,f=cap.read()
        if not ok: break
        fr.append(f)
    return fr
SRC={'A':load(A),'B':load(B)}
def lerp(a,b,u): return a+(b-a)*u
def logz(z0,z1,u): return math.exp(lerp(math.log(z0),math.log(z1),u))
# cdo shot: (burim, start_s, kohezgjatja, funksion(u)->(z,cx,cy,rot))
def s1(u):  # bounce: in deri 1.24 ne gjysme, pastaj out ne 1.06
    z = logz(1.0,1.24,u/0.5) if u<0.5 else logz(1.24,1.06,(u-0.5)/0.5)
    return z,360,560,0
def s2(u):  # crash zoom out 2.43 -> 1.0, ~11%/frame @30fps, roll -5 -> 0
    z=logz(2.43,1.0,u); k=math.log(z)/math.log(2.43)
    return z,360,lerp(640,560,k),-5*k
def s3(u):  # detaj menge me dantella, zoom out i lehte 2%/frame
    return logz(2.9,2.5,u),265,765,0
def s4(u):  # wide, zoom out me ease-out 1.35 -> 1.0, roll -3 -> 0
    z=1+0.35*(1-u)**3; return z,360,lerp(600,640,u),-3*(z-1)/0.35
def s5(u):  # ura, vazhdon ngadale
    return lerp(1.05,1.0,u),360,640,0
SHOTS=[('A',11.80,0.21,s1),('B',14.75,0.30,s2),('B',15.10,0.25,s3),('B',15.40,1.00,s4),('B',16.45,2.50,s5)]
def render(img,z,cx,cy,rot):
    M=cv2.getRotationMatrix2D((cx,cy),rot,z)
    M[0,2]+=W/2-cx; M[1,2]+=H/2-cy
    return cv2.warpAffine(img,M,(W,H),flags=cv2.INTER_LANCZOS4,borderMode=cv2.BORDER_REFLECT)
def clamp(z,cx,cy):
    hw,hh=W/2/z,H/2/z
    return min(max(cx,hw),W-hw),min(max(cy,hh),H-hh)
out=sys.argv[1]
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
  '-c:v','libx264','-crf','16','-pix_fmt','yuv420p',out],stdin=subprocess.PIPE)
for src,st,dur,fn in SHOTS:
    n=round(dur*FPS); fr=SRC[src]
    for i in range(n):
        img=fr[min(round(st*FPS)+i,len(fr)-1)]
        acc=np.zeros((H,W,3),np.float32)
        for s in range(SUB):
            u=min((i+0.5*s/SUB)/n,1.0)
            z,cx,cy,rot=fn(u); cx,cy=clamp(z,cx,cy)
            acc+=render(img,z,cx,cy,rot)
        p.stdin.write((acc/SUB).astype(np.uint8).tobytes())
p.stdin.close(); p.wait()
