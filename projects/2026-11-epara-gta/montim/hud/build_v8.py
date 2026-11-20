"""Montage v8 (18 v3 vertical card, sped up 1.5x): 15 v3 one-take, tighter trims, bench starts on lacing, animated radar, designed HUD, narrator + music.

usage: python build_v6.py OUT.mp4 RADAR_FRAMES_DIR
"""
import subprocess, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import radar_anim

D = "C:/Users/Desjon/Downloads/"
HERE = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
PNG = HERE + "/png/"
OUT, RDIR = sys.argv[1], sys.argv[2]
NARR = D + "ElevenLabs_2026-11-20T00_33_28_eparaja_gen_s46_sim75_v4.mp3"
END_LINE = D + "ElevenLabs_2026-11-20T01_00_05_eparaja_gen_s46_sim75_v4.mp3"
MUSIC = D + "Golden_Hour_Getaway_2026-11-20T003425.wav"
XF = 0.4     # white flash: street -> store interior
HOLD = 1.5   # hold the logo at the end

# name, file, in, out, crop16x9
clips = [
    ("14",  "hf_20261119_220155_17633204-917e-41fd-86d4-7a1bc7af38a1.mp4", 0.0, 4.0, False),
    ("15",  "hf_20261120_010848_cefab0c6-b40f-4e49-b254-c5e687ca73e5.mp4", 0.3, 7.8, False),
    ("16a", "hf_20261119_225727_e64ed23b-1347-4f97-8d4f-42dd367acd89 (1).mp4", 2.0, 8.84, False),
    ("16b", "hf_20261119_225727_e64ed23b-1347-4f97-8d4f-42dd367acd89 (1).mp4", 10.6, 15.0, False),
    ("18",  "epara_18v3_x1.5.mp4", 0.0, 3.37, False),
    ("19",  "hf_20261119_230357_8aa691f0-930b-4260-be1c-f655990a4982.mp4", 0.4, 5.4, False),
    ("12",  "hf_20261119_231359_df0643ca-0d97-486b-8467-f29ae0f62599.mp4", 0.3, 5.6, False),
    ("21",  "hf_20261120_002537_d788d546-ac4c-46a0-9095-4a0732e0fd7d.mp4", 0.0, 10.05, False),
    ("22",  "hf_20261119_233827_48fa4286-bdff-4487-bc77-c533f2f7cedf.mp4", 6.0, 13.7, True),
    ("24",  "hf_20261120_001229_54012be9-82dc-4a3e-9160-0ab17dd21042.mp4", 0.0, 10.05, False),
]
XF_INTO = "16a"  # white-flash blend into this clip from the previous one

S, t = {}, 0.0
for name, f, a, b, _ in clips:
    if name == XF_INTO:
        t -= XF
    S[name] = t
    t += b - a
TOTAL = t + HOLD
print({k: round(v, 2) for k, v in S.items()}, "total", round(TOTAL, 2))

tap = S["18"] + 1.65
transfer = S["12"] + 0.9
cash = S["21"] + 7.0
mission = S["24"] + 1.6
hud_end = S["24"] + 6.5

ov = [  # png, start, end, slide px, fade
    ("hud_25000.png", 0.6, tap + 0.1, 0, 0.3),
    ("hud_16278.png", tap, transfer + 0.1, 0, 0.15),
    ("hud_14278.png", transfer, cash + 0.1, 0, 0.15),
    ("hud_12278.png", cash, hud_end, 0, 0.15),
    ("toast_pay.png", tap, tap + 3.2, 50, 0.22),
    ("toast_cashback.png", tap + 0.6, tap + 3.8, 50, 0.22),
    ("toast_sent.png", transfer, transfer + 3.2, 50, 0.22),
    ("toast_atm.png", cash, cash + 2.9, 50, 0.22),
    ("loc_blloku.png", 0.8, 3.8, 50, 0.3),
    ("loc_bulevardi.png", S["12"] + 0.3, S["12"] + 3.3, 50, 0.3),
    ("loc_stadiumi.png", S["21"] + 0.2, S["21"] + 3.2, 50, 0.3),
    ("mission.png", mission, mission + 3.8, 0, 0.35),
]

lines = [  # (in, out) of the one-shot take -> montage start
    (0.00, 3.75, 0.60),
    (4.60, 9.70, S["15"] + 0.5),
    (10.95, 13.95, S["16a"] + XF + 0.3),
    (14.85, 16.60, S["16b"] + 1.0),
    (17.40, 22.50, S["18"] + 0.0),
    (22.90, 24.95, S["19"] + 2.6),
    (25.35, 29.20, S["12"] + 0.2),
    (29.60, 32.40, S["21"] + 0.1),
    (32.90, 39.45, S["21"] + 7.6),
    (40.20, 43.15, mission),
]
end_at = S["24"] + 7.6

ev = dict(walk_start=S["15"] + 2.2, store_enter=S["15"] + 7.0, exit_store=S["19"] + 0.2,
          green=S["12"] + 4.2, atm_walk=S["21"], cart_walk=S["21"] + 8.4, s2=S["12"], s3=S["21"])
print("radar frames", radar_anim.render(ev, hud_end, RDIR))

args = ["ffmpeg", "-v", "error", "-y"]
for _, f, *_ in clips:
    args += ["-i", D + f]
n = len(clips)
args += ["-i", NARR, "-i", MUSIC, "-i", END_LINE]
NI, MI, EI = n, n + 1, n + 2
OI = n + 3
for png, a, b, *_ in ov:
    args += ["-loop", "1", "-framerate", "24", "-t", f"{b - a:.3f}", "-i", PNG + png]
RI = OI + len(ov)
args += ["-framerate", "24", "-i", RDIR + "/radar_%05d.png"]

g = []
for i, (name, f, a, b, crop) in enumerate(clips):
    v = f"[{i}:v]trim={a}:{b},setpts=PTS-STARTPTS"
    if crop:
        v += ",crop=405:720,scale=720:1280:flags=lanczos"
    g.append(v + f",fps=24,format=yuv420p,setsar=1[v{i}]")
    g.append(f"[{i}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=48000[a{i}]")
xi = [c[0] for c in clips].index(XF_INTO)
pd = clips[xi - 1][3] - clips[xi - 1][2]
g.append(f"[v{xi-1}][v{xi}]xfade=transition=fadewhite:duration={XF}:offset={pd - XF:.3f}[vx]")
g.append(f"[a{xi-1}][a{xi}]acrossfade=d={XF}[ax]")
seq = [(f"[v{i}]", f"[a{i}]") for i in range(xi - 1)] + [("[vx]", "[ax]")] + [(f"[v{i}]", f"[a{i}]") for i in range(xi + 1, n)]
g.append("".join(v + a for v, a in seq) + f"concat=n={len(seq)}:v=1:a=1[base0][sfx00]")
g.append(f"[base0]tpad=stop_mode=clone:stop_duration={HOLD}[base]")
g.append(f"[sfx00]apad=pad_dur={HOLD}[sfx0]")

cur = "base"
for k, (png, a, b, slide, fd) in enumerate(ov):
    dur = b - a
    g.append(f"[{OI + k}:v]format=rgba,fade=t=in:st=0:d={fd}:alpha=1,fade=t=out:st={dur - fd:.3f}:d={fd}:alpha=1,"
             f"setpts=PTS-STARTPTS+{a:.3f}/TB[o{k}]")
    x = "0" if slide == 0 else f"'if(lt(t-{a:.3f},{fd}),{slide}*(1-(t-{a:.3f})/{fd}),0)'"
    g.append(f"[{cur}][o{k}]overlay=x={x}:y=0:eof_action=pass:format=auto[c{k}]")
    cur = f"c{k}"
g.append(f"[{RI}:v]format=rgba[rad]")
g.append(f"[{cur}][rad]overlay=x={34 - radar_anim.PAD}:y={1280 - 40 - radar_anim.D - radar_anim.PAD}:eof_action=pass:format=auto,format=yuv420p[vout]")

for i, (a, b, at) in enumerate(lines):
    ms = int(at * 1000)
    g.append(f"[{NI}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:d=0.04,"
             f"afade=t=out:st={b - a - 0.06:.2f}:d=0.06,adelay={ms}|{ms}[n{i}]")
g.append(f"[{EI}:a]aresample=48000,adelay={int(end_at*1000)}|{int(end_at*1000)}[nend]")
g.append("".join(f"[n{i}]" for i in range(len(lines))) + "[nend]" +
         f"amix=inputs={len(lines) + 1}:normalize=0,volume=1.6,apad,atrim=0:{TOTAL:.3f}[voice]")
g.append("[voice]asplit=2[vmix][vkey]")
g.append(f"[{MI}:a]aresample=48000,atrim=0:{TOTAL:.3f},afade=t=out:st={TOTAL - 2.0:.3f}:d=2.0,volume=0.55[mus]")
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
