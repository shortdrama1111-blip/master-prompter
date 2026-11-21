"""SFX i stilolapsit per Shot 6, i sinkronizuar me shfaqjen e shkronjave te shot6/make_shot6.py.

Sinteze (pa gjenerim): zhurme e filtruar 1.4-6 kHz (ferkimi i majes ne leter), e moduluar me
shpejtesine e vijes (me e forte ne mes te cdo shkronje, qetesi e shkurter mes shkronjave),
mikro-dridhje 25-45 Hz per teksturen e letres, nje "tak" i lehte kur maja prek letren ne fillim te rreshtit.

python audio/make_pen_sfx.py  -> audio/sfx-pen-writing.wav (48 kHz stereo, 18 s, ne kohen e montazhit)
"""
import os, wave
import numpy as np
from PIL import ImageFont, Image, ImageDraw

P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SR, DUR = 48000, 18.0
SHOT6_START = 14.0                     # Shot 6 fillon ne 14.0 s te montazhit
FONT = "C:/Windows/Fonts/Inkfree.ttf"
LINES = [("Happy", 104), ("Holidays", 104)]          # si te make_shot6.py
T0, LINE_DUR, GAP = 0.45, [1.0, 1.3], 0.18
rng = np.random.default_rng(3)


def bandpass(x, lo, hi):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    g = np.exp(-0.5 * (np.log(np.maximum(f, 1) / np.sqrt(lo * hi)) / (np.log(hi / lo) / 2.6)) ** 2)
    return np.fft.irfft(X * g, len(x))


n = int(SR * DUR)
t = np.arange(n) / SR
noise = bandpass(rng.standard_normal(n), 1400, 6000)
noise /= np.abs(noise).max()
env = np.zeros(n)
taps = np.zeros(n)
d = ImageDraw.Draw(Image.new('L', (10, 10)))
tl = T0
for (text, size), dur in zip(LINES, LINE_DUR):
    font = ImageFont.truetype(FONT, size)
    xs = [d.textlength(text[:i + 1], font=font) for i in range(len(text))]
    w = np.diff([0] + xs); w = w / w.sum()
    a = tl
    for k, wk in enumerate(w):
        b = a + wk * dur
        i0, i1 = int((SHOT6_START + a) * SR), int((SHOT6_START + b) * SR)
        p = np.linspace(0, 1, i1 - i0)
        # shpejtesia e majes brenda shkronjes: derivati i ease (smoothstep) -> 6p(1-p), plus goditje te vogla
        speed = 6 * p * (1 - p)
        strokes = 0.65 + 0.35 * np.abs(np.sin(np.pi * p * rng.integers(2, 4)))
        env[i0:i1] = np.maximum(env[i0:i1], speed * strokes * rng.uniform(0.8, 1.0))
        a = b
    # tak ne fillim te rreshtit
    it = int((SHOT6_START + tl) * SR)
    m = int(0.012 * SR)
    taps[it:it + m] += rng.standard_normal(m) * np.exp(-np.arange(m) / (0.0025 * SR))
    tl += dur + GAP
# zbutje e zarfit (5 ms) dhe mikro-dridhje e letres
k = int(0.005 * SR); env = np.convolve(env, np.ones(k) / k, 'same')
grain = 0.75 + 0.25 * np.sin(2 * np.pi * (25 + 20 * rng.random()) * t + rng.random() * 6) * (0.5 + 0.5 * rng.random(n))
sig = noise * env * grain + bandpass(taps, 800, 5000) * 0.6
sig /= np.abs(sig).max()
sig *= 10 ** (-6 / 20)                 # -6 dBFS kulm; niveli final vendoset ne montazh
st = np.stack([sig * 0.95, sig], 1)    # pak me djathtas, si etiketa ne kuader
out = os.path.join(P, 'audio', 'sfx-pen-writing.wav')
with wave.open(out, 'wb') as wf:
    wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR)
    wf.writeframes((np.clip(st, -1, 1) * 32767).astype('<i2').tobytes())
print(out)
