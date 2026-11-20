"""Montage v3: clips + white-flash blend into the store + designed HUD PNG overlays + narrator/music mix."""
import subprocess, sys, os

D = "C:/Users/Desjon/Downloads/"
HERE = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
PNG = HERE + "/png/"
OUT = sys.argv[1]
NARR = D + "ElevenLabs_2026-11-20T00_33_28_eparaja_gen_s46_sim75_v4.mp3"
MUSIC = D + "Golden_Hour_Getaway_2026-11-20T003425.wav"
XF = 0.4  # white-flash blend 15b -> 16

clips = [  # file, in, out, crop16x9
    ("hf_20261119_220155_17633204-917e-41fd-86d4-7a1bc7af38a1.mp4", 0, 5.05, False),        # 14
    ("hf_20261119_220632_c021b1b7-8b6f-4c7a-abb3-f4524007bd26.mp4", 0, 5.05, False),        # 15
    ("hf_20261119_223001_40e6fbfe-478b-489e-91a8-dd66e23586c9.mp4", 0, 5.05, False),        # 15b
    ("hf_20261119_225727_e64ed23b-1347-4f97-8d4f-42dd367acd89 (1).mp4", 0.25, 15.0, False),  # 16 v3
    ("hf_20261119_225321_51b609b9-6afe-43b2-ba82-cac2fb382fdb.mp4", 0, 7.05, False),        # 18
    ("hf_20261119_230357_8aa691f0-930b-4260-be1c-f655990a4982.mp4", 0, 6.05, False),        # 19
    ("hf_20261119_231359_df0643ca-0d97-486b-8467-f29ae0f62599.mp4", 0, 6.05, False),        # 12 v4
    ("hf_20261120_002537_d788d546-ac4c-46a0-9095-4a0732e0fd7d.mp4", 0, 2.0, False),         # 21 v3 walk
    ("hf_20261120_002537_d788d546-ac4c-46a0-9095-4a0732e0fd7d.mp4", 5.4, 10.05, False),     # 21 v3 notes
    ("hf_20261119_233827_48fa4286-bdff-4487-bc77-c533f2f7cedf.mp4", 5.5, 13.7, True),       # 22
    ("hf_20261120_001229_54012be9-82dc-4a3e-9160-0ab17dd21042.mp4", 0, 10.05, False),       # 24 v3
]
durs = [b - a for _, a, b, _ in clips]
starts, t = [], 0.0
for i, d in enumerate(durs):
    if i == 3:
        t -= XF
    starts.append(t)
    t += d
TOTAL = t
S = starts
print("starts", [round(x, 2) for x in S], "total", round(TOTAL, 2))

tap, transfer, cash = S[4] + 2.6, S[6] + 1.2, S[8] + 1.6
mission, hud_end = S[10] + 1.6, S[10] + 6.5

# png, start, end, slide (px from right +, from left -), fade
ov = [
    ("hud_25000.png", 0.6, tap + 0.1, 0, 0.3),
    ("hud_16278.png", tap, transfer + 0.1, 0, 0.15),
    ("hud_14278.png", transfer, cash + 0.1, 0, 0.15),
    ("hud_12278.png", cash, hud_end, 0, 0.15),
    ("toast_pay.png", tap, tap + 3.2, 50, 0.22),
    ("toast_cashback.png", tap + 0.6, tap + 3.8, 50, 0.22),
    ("toast_sent.png", transfer, transfer + 3.2, 50, 0.22),
    ("toast_atm.png", cash, cash + 2.9, 50, 0.22),
    ("loc_blloku.png", 1.0, 4.6, -50, 0.3),
    ("loc_bulevardi.png", S[6] + 0.3, S[6] + 3.3, -50, 0.3),
    ("loc_stadiumi.png", S[7] + 0.2, S[7] + 3.2, -50, 0.3),
    ("mission.png", mission, mission + 3.8, 0, 0.35),
]

# narrator lines: (in, out of the one-shot take, start in montage); last line removed
d16 = -(XF + 0.25)
lines = [
    (0.00, 3.75, 0.60), (4.60, 9.70, 5.60), (10.95, 13.95, 17.00 + d16), (14.85, 16.60, 26.75 + d16),
    (17.40, 22.50, 30.40 + d16), (22.90, 24.95, 39.40 + d16), (25.35, 29.20, 43.60 + d16),
    (29.60, 32.40, 49.40 + d16), (32.90, 39.45, 53.00 + d16), (40.20, 43.15, 65.75 + d16),
]

args = ["ffmpeg", "-v", "error", "-y"]
for f, *_ in clips:
    args += ["-i", D + f]
n = len(clips)
args += ["-i", NARR, "-i", MUSIC]
NI, MI = n, n + 1
for png, a, b, *_ in ov:
    args += ["-loop", "1", "-framerate", "24", "-t", f"{b - a:.3f}", "-i", PNG + png]
OI = n + 2

g = []
for i, (f, a, b, crop) in enumerate(clips):
    v = f"[{i}:v]trim={a}:{b},setpts=PTS-STARTPTS"
    if crop:
        v += ",crop=405:720,scale=720:1280:flags=lanczos"
    g.append(v + f",fps=24,format=yuv420p,setsar=1[v{i}]")
    g.append(f"[{i}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=48000[a{i}]")
g.append(f"[v2][v3]xfade=transition=fadewhite:duration={XF}:offset={durs[2]-XF:.3f}[v23]")
g.append(f"[a2][a3]acrossfade=d={XF}[a23]")
seq_v = ["[v0]", "[v1]", "[v23]"] + [f"[v{i}]" for i in range(4, n)]
seq_a = ["[a0]", "[a1]", "[a23]"] + [f"[a{i}]" for i in range(4, n)]
g.append("".join(x + y for x, y in zip(seq_v, seq_a)) + f"concat=n={len(seq_v)}:v=1:a=1[base][sfx0]")

cur = "base"
for k, (png, a, b, slide, fd) in enumerate(ov):
    dur = b - a
    g.append(f"[{OI + k}:v]format=rgba,fade=t=in:st=0:d={fd}:alpha=1,fade=t=out:st={dur - fd:.3f}:d={fd}:alpha=1,"
             f"setpts=PTS-STARTPTS+{a:.3f}/TB[o{k}]")
    x = "0" if slide == 0 else f"'if(lt(t-{a:.3f},{fd}),{slide}*(1-(t-{a:.3f})/{fd}),0)'"
    g.append(f"[{cur}][o{k}]overlay=x={x}:y=0:eof_action=pass:format=auto[c{k}]")
    cur = f"c{k}"
g.append(f"[{cur}]format=yuv420p[vout]")

for i, (a, b, at) in enumerate(lines):
    ms = int(at * 1000)
    g.append(f"[{NI}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:d=0.04,"
             f"afade=t=out:st={b - a - 0.06:.2f}:d=0.06,adelay={ms}|{ms}[n{i}]")
g.append("".join(f"[n{i}]" for i in range(len(lines))) +
         f"amix=inputs={len(lines)}:normalize=0,volume=1.6,apad,atrim=0:{TOTAL:.3f}[voice]")
g.append("[voice]asplit=2[vmix][vkey]")
g.append(f"[{MI}:a]aresample=48000,atrim=0:{TOTAL:.3f},afade=t=out:st={TOTAL - 1.5:.3f}:d=1.5,volume=0.55[mus]")
g.append("[mus][vkey]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[musd]")
g.append("[sfx0]volume=0.40[sfx]")
g.append("[vmix][musd][sfx]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[aout]")

fs = OUT + ".filter.txt"
open(fs, "w", encoding="utf-8").write(";\n".join(g))
args += ["-/filter_complex", fs, "-map", "[vout]", "-map", "[aout]", "-c:v", "libx264", "-crf", "17",
         "-preset", "medium", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-t", f"{TOTAL:.3f}", OUT]
r = subprocess.run(args, capture_output=True, text=True)
os.remove(fs)
print(r.returncode, r.stderr[-2500:])
