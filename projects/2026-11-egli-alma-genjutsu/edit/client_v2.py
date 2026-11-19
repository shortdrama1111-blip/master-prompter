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
SRC={k:load(v) for k,v in {'V2':'results/firenze-v5-montage-v2.mp4','A':'results/sheet-v3-test-video.mp4','T27':'results/seedance-27-outfit2-3-take1.mp4',
     'B':'results/seedance-v5-greybox-take1.mp4','P':P32_72,'Q':'results/seedance-33-continuous-take1.mp4','R':'results/seedance-34-outfit3-take1.mp4','PR':'results/seedance-35-profiles-take1.mp4','RT':sys.argv[3]}.items()}
def ramp(segs):
    out=[]
    for a,b,v0,v1 in segs:
        s=a
        while s<b-1e-6:
            v=v0+(v1-v0)*(s-a)/(b-a); ds=v/FPS; out.append((s,ds)); s+=ds
    return out
def real(a,b): return [(a+i/FPS,1/FPS) for i in range(round((b-a)*FPS))]
# v11 = V1 për klienten: veshja 3 pas wipe-it nga take 34 (pa speed ramp); rripi rikthyer te veshja 2.
# v10: pjesët më të mira të take 32 + 33; kalimi 2→3 me wipe-in natyral të kolonës (take 33, 7.9–9.3).
# CLIENT V2: reel-i i parë (sheet-v3-test-video) me komentet e klientes: pa zoom-blur, pa split-screen,
# profilet e rigjeneruara (prompt 35), veshja me kuadrata e zgjatur me materialin ekzistues.
PLAN=[
 ('A',  real(0.00,3.875)),                                   # veshja 1: Duomo, këmbët
 ('PR', real(0.40,1.20)),                                    #   profili i ri (pallto)
 ('A',  real(4.79,6.38)),                                    #   plan mesatar (pa zoom-blur, pa split)
 ('A',  real(6.92,9.00)),                                    # veshja 2: kuadratat (close + kryqëzimi)
 ('B',  real(10.20,11.50)),                                  #   duart te rripi
 ('T27',real(3.40,4.60)),                                    #   3/4 te vitrinat
 ('T27',real(4.75,6.30)),                                    #   plan mesatar, shikim te lentja
 ('PR', real(4.50,6.90)),                                    # veshja 3: profili i ri te Arno
 ('A',  real(11.40,16.95)),                                  #   pjesa tjetër e origjinalit, pa daljen nga kuadri
 ('T27',real(12.85,14.20)),                                  #   portiku: menga me dantella
 ('T27',real(14.35,16.00)),                                  #   portiku: e mbështetur te kolona, mbyllja
]
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
  '-c:v','libx264','-crf','16','-pix_fmt','yuv420p',OUT],stdin=subprocess.PIPE)
for src,frames in PLAN:
    FR,sf=SRC[src]
    for s,ds in frames:
        i0=min(round(s*sf),len(FR)-1)
        if src in ('P','RT') and ds*sf>2.5:   # lëvizje e shpejtë: mesatare e 2 frame-ve të interpoluara
            img=(FR[i0].astype(np.float32)+FR[min(i0+1,len(FR)-1)].astype(np.float32))/2
        else: img=FR[i0]
        p.stdin.write(np.asarray(img).astype(np.uint8).tobytes())
p.stdin.close(); p.wait()
