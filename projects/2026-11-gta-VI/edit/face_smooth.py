# Lëmim i lëkurës vetëm në fytyrë (akne/puçrra): zbulim fytyre (Haar), maskë eliptike e butë,
# filtër bilateral (ruan skajet: sytë, mjekra, vetullat) + kokërr filmi e kthyer që të mos duket plastikë.
# Përdorim: python3 face_smooth.py <hyrja.mp4> <dalja.mp4> [forca 0–1, default 0.75]
import cv2, numpy as np, subprocess, sys, json
IN, OUT = sys.argv[1], sys.argv[2]; K = float(sys.argv[3]) if len(sys.argv) > 3 else 0.75
p = json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height,r_frame_rate','-of','json',IN]))['streams'][0]
W, H = p['width'], p['height']; FR = p['r_frame_rate']
dec = subprocess.Popen(['ffmpeg','-v','error','-i',IN,'-f','rawvideo','-pix_fmt','bgr24','-'], stdout=subprocess.PIPE)
enc = subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',FR,'-i','-','-i',IN,
    '-map','0:v','-map','1:a?','-c:v','libx264','-crf','15','-preset','fast','-pix_fmt','yuv420p','-c:a','copy',OUT], stdin=subprocess.PIPE)
cas = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
prof = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')
last, miss = [], 0; rng = np.random.default_rng(1)
while True:
    buf = dec.stdout.read(W*H*3)
    if len(buf) < W*H*3: break
    f = np.frombuffer(buf, np.uint8).reshape(H, W, 3).copy()
    g = cv2.equalizeHist(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY))
    ms = int(min(W, H) * 0.06)
    faces = list(cas.detectMultiScale(g, 1.1, 5, minSize=(ms, ms))) or list(prof.detectMultiScale(g, 1.1, 5, minSize=(ms, ms)))
    if faces: last, miss = faces, 0
    else:
        miss += 1
        if miss > 6: last = []
    if last:
        m = np.zeros((H, W), np.float32)
        for (x, y, w, h) in last:
            cv2.ellipse(m, (int(x+w/2), int(y+h*0.55)), (int(w*0.55), int(h*0.72)), 0, 0, 360, 1.0, -1)
        m = cv2.GaussianBlur(m, (0, 0), max(4, int(min(W, H)*0.02)))[..., None] * K
        s = cv2.bilateralFilter(f, 0, 38, max(5, min(W, H)//90))
        s = cv2.bilateralFilter(s, 0, 25, max(3, min(W, H)//150))
        grain = rng.normal(0, 2.2, (H, W, 1)).astype(np.float32)
        out = f.astype(np.float32)*(1-m) + (s.astype(np.float32)+grain)*m
        f = np.clip(out, 0, 255).astype(np.uint8)
    enc.stdin.write(f.tobytes())
enc.stdin.close(); enc.wait(); dec.wait()
print('ok')
