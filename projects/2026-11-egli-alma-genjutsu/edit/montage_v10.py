# Montage v10 (nga v9): ritmi i references (analysis-v7-ramps.md). Pa ndalesa, prerje mbi lëvizje, pa frame të dyfishta.
# Burimi P32 interpolohet me optical flow në 72 fps (ffmpeg minterpolate) para ramp-it; blur = mesatare e 2 frame-ve.
import cv2, numpy as np, subprocess, sys
OUT=sys.argv[1]; P32_72=sys.argv[2]; W,H,FPS=720,1280,24
def load(p):
    cap=cv2.VideoCapture(p); fr=[]; fps=cap.get(cv2.CAP_PROP_FPS)
    while True:
        ok,f=cap.read()
        if not ok: break
        fr.append(cv2.resize(f,(W,H),interpolation=cv2.INTER_AREA))
    return fr,fps
SRC={k:load(v) for k,v in {'V2':'results/firenze-v5-montage-v2.mp4','T27':'results/seedance-27-outfit2-3-take1.mp4',
     'B':'results/seedance-v5-greybox-take1.mp4','P':P32_72,'Q':'results/seedance-33-continuous-take1.mp4'}.items()}
def ramp(segs):
    out=[]
    for a,b,v0,v1 in segs:
        s=a
        while s<b-1e-6:
            v=v0+(v1-v0)*(s-a)/(b-a); ds=v/FPS; out.append((s,ds)); s+=ds
    return out
def real(a,b): return [(a+i/FPS,1/FPS) for i in range(round((b-a)*FPS))]
# v10: pjesët më të mira të take 32 + 33; kalimi 2→3 me wipe-in natyral të kolonës (take 33, 7.9–9.3).
PLAN=[
 ('V2', real(0.00,1.75)+real(3.875,5.33)+real(5.42,8.11)),   # veshja 1
 ('Q',  ramp([(0.20,1.20,1.4,1.4),(1.20,2.60,1.4,1.8)])),    # veshja 2: kapësja e çantës → kamera ngjitet te fytyra
 ('P',  ramp([(1.95,2.30,1.5,3),(2.30,2.60,3,6),(2.60,3.80,6,6),(3.80,4.05,6,2.5)])),  # tërheqje te muri
 ('P',  ramp([(4.45,4.80,1.5,1.5)])),                        #   poza te muri
 ('P',  ramp([(6.25,6.50,4,6),(6.50,7.30,6,6),(7.30,7.70,6,1.5),(7.70,8.10,1.5,1.2)])),  # afrim → e përkulur
 ('Q',  ramp([(6.55,7.85,1.1,1.1)])),                        #   ulur në shkallë, dora te flokët
 ('Q',  ramp([(7.85,8.25,1.1,2.0),(8.25,9.05,2.5,2.5),(9.05,9.40,2.0,1.1)])),  # WIPE me kolonën → veshja 3
 ('Q',  ramp([(9.40,11.20,1.1,1.1)])),                       # veshja 3: shpina, shikim mbi sup, dantella te kolona
 ('T27',real(12.90,13.70)),                                  #   menga me dantella
 ('P',  ramp([(9.20,9.60,1.3,1.5),(9.60,10.20,2.5,3),(10.20,10.50,3,6),(10.50,11.40,6,6),(11.40,11.70,6,2.5)])),
 ('P',  ramp([(12.00,12.35,1.5,1.5)])),                      #   te kolona
 ('P',  ramp([(13.45,13.70,4,6),(13.70,14.90,6,6),(14.90,15.30,6,1.5),(15.30,16.00,1.5,1.0)])),  # afrim → ulur, mbyllja
]
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
  '-c:v','libx264','-crf','16','-pix_fmt','yuv420p',OUT],stdin=subprocess.PIPE)
for src,frames in PLAN:
    FR,sf=SRC[src]
    for s,ds in frames:
        i0=min(round(s*sf),len(FR)-1)
        if src=='P' and ds*sf>2.5:   # lëvizje e shpejtë: mesatare e 2 frame-ve të interpoluara
            img=(FR[i0].astype(np.float32)+FR[min(i0+1,len(FR)-1)].astype(np.float32))/2
        else: img=FR[i0]
        p.stdin.write(np.asarray(img).astype(np.uint8).tobytes())
p.stdin.close(); p.wait()
