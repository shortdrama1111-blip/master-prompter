# Generates the printer feed motion (motion.js, used by index.html) and the matching
# thermal-printer sound (printer.wav) from one timeline, so picture and sound stay in sync.
import numpy as np, wave, json, sys

TOTAL = 10.0          # seconds of video
START, END = 1720.0, 96.0  # receipt top y (px, 1080x1920 frame)
V_RUN = 400.0         # px/s while the motor runs
T0 = 0.20             # first movement
rng = np.random.default_rng(4)

# --- motion: bursts of feed separated by short head pauses, quick stop at the end
dt = 1 / 1000
t = np.arange(0, TOTAL, dt)
v = np.zeros_like(t)
pos = START
cur = T0
segments = []
while True:
    run = rng.uniform(0.32, 0.62)
    segments.append((cur, cur + run))
    cur += run + rng.uniform(0.07, 0.16)
    if (cur - T0) * V_RUN * 0.8 > (START - END) * 1.2:
        break
y = np.full_like(t, START)
dist = 0.0
for i, ti in enumerate(t):
    running = any(a <= ti < b for a, b in segments)
    if running and dist < START - END:
        # tiny speed wobble of the motor
        sp = V_RUN * (1 + 0.04 * np.sin(ti * 37.0))
        remaining = START - END - dist
        if remaining < 60:  # last 60 px: settle
            sp *= max(0.25, remaining / 60)
        dist = min(START - END, dist + sp * dt)
        v[i] = sp
    y[i] = START - dist
t_end = t[np.argmax(y <= END + 1e-6)]
print('print ends at', round(float(t_end), 2), 's')

FPS = 24
frames = [round(float(np.interp(f / FPS, t, y)), 2) for f in range(int(TOTAL * FPS))]
open('motion.js', 'w').write('window.MOTION=' + json.dumps(frames) + ';')

# --- sound
SR = 48000
ts = np.arange(0, TOTAL, 1 / SR)
vs = np.interp(ts, t, v)
run = (vs > 1).astype(float)
# smooth on/off envelope (4 ms)
k = np.ones(int(0.004 * SR)) / int(0.004 * SR)
env = np.convolve(run, k, 'same')

# stepper: one micro-step every 0.38 px -> ~1 kHz step rate
step_px = 0.38
phase = np.cumsum(vs / step_px / SR)
steps = np.diff(np.floor(phase), prepend=0) > 0
imp = steps.astype(float) * (0.8 + 0.4 * rng.random(len(ts)))
kt = np.arange(int(0.004 * SR)) / SR
click = np.exp(-kt * 1400) * (np.sin(2 * np.pi * 2900 * kt) + 0.6 * np.sin(2 * np.pi * 5200 * kt))
stepper = np.convolve(imp, click)[:len(ts)]

def band(x, lo, hi):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    X[(f < lo) | (f > hi)] = 0
    return np.fft.irfft(X, len(x))

# thermal head: buzzy noise pulsed at the dot-line rate
noise = band(rng.standard_normal(len(ts)), 1500, 7000)
line_rate = vs / 3.0  # one dot-line every 3 px
lphase = np.cumsum(line_rate / SR)
gate = 0.55 + 0.45 * (np.sin(2 * np.pi * lphase) > 0.2)
head = noise * gate
# motor body
motor = band(rng.standard_normal(len(ts)), 120, 600) * 1.6 + 0.25 * np.sin(2 * np.pi * 180 * ts)

sig = env * (0.55 * stepper / np.abs(stepper).max() + 0.22 * head / np.abs(head).max()
             + 0.20 * motor / np.abs(motor).max())
# start/stop clicks at each segment edge
edges = np.flatnonzero(np.abs(np.diff(run)) > 0)
ck = np.exp(-np.arange(int(0.012 * SR)) / SR * 500) * band(rng.standard_normal(int(0.012 * SR)), 300, 4000)
ck /= np.abs(ck).max()
for e in edges:
    n = min(len(ck), len(sig) - e)
    sig[e:e + n] += 0.35 * ck[:n]
# small room
ir = rng.standard_normal(int(0.09 * SR)) * np.exp(-np.arange(int(0.09 * SR)) / SR * 45)
ir[0] = 1 / 0.06
sig = np.fft.irfft(np.fft.rfft(sig, len(sig) + len(ir)) * np.fft.rfft(ir, len(sig) + len(ir)))[:len(ts)]
sig = sig / np.abs(sig).max() * 10 ** (-3 / 20)
stereo = np.stack([sig, np.roll(sig, 12)], 1)
pcm = (stereo * 32767).astype('<i2')
with wave.open('printer.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
