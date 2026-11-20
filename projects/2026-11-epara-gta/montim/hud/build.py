import subprocess, sys, os

D = "C:/Users/Desjon/Downloads/"
S = "C:/Users/Desjon/AppData/Local/Temp/claude/729be58a07cccf18/7c8f4f84-3aa7-466e-9f3b-303eae627606/scratchpad/hud/"
OUT = sys.argv[1]

# (file, start, end, crop16x9)
clips = [
    ("hf_20261119_220155_17633204-917e-41fd-86d4-7a1bc7af38a1.mp4", 0, 5.05, False),   # 14
    ("hf_20261119_220632_c021b1b7-8b6f-4c7a-abb3-f4524007bd26.mp4", 0, 5.05, False),   # 15
    ("hf_20261119_223001_40e6fbfe-478b-489e-91a8-dd66e23586c9.mp4", 0, 5.05, False),   # 15b
    ("hf_20261119_225727_e64ed23b-1347-4f97-8d4f-42dd367acd89 (1).mp4", 0, 15.0, False),  # 16 v3
    ("hf_20261119_225321_51b609b9-6afe-43b2-ba82-cac2fb382fdb.mp4", 0, 7.05, False),   # 18
    ("hf_20261119_230357_8aa691f0-930b-4260-be1c-f655990a4982.mp4", 0, 6.05, False),   # 19
    ("hf_20261119_231359_df0643ca-0d97-486b-8467-f29ae0f62599.mp4", 0, 6.05, False),   # 12 v4
    ("hf_20261120_002537_d788d546-ac4c-46a0-9095-4a0732e0fd7d.mp4", 0, 2.0, False),    # 21 v3 walk
    ("hf_20261120_002537_d788d546-ac4c-46a0-9095-4a0732e0fd7d.mp4", 5.4, 10.05, False),# 21 v3 notes -> vendor
    ("hf_20261119_233827_48fa4286-bdff-4487-bc77-c533f2f7cedf.mp4", 5.5, 13.7, True),  # 22 (16:9 crop)
    ("hf_20261120_001229_54012be9-82dc-4a3e-9160-0ab17dd21042.mp4", 0, 10.05, False),  # 24 v3
]

args = ["ffmpeg", "-v", "error", "-y"]
for f, *_ in clips:
    args += ["-i", D + f]

parts, t = [], 0.0
starts = []
for i, (f, a, b, crop) in enumerate(clips):
    starts.append(t)
    v = f"[{i}:v]trim={a}:{b},setpts=PTS-STARTPTS"
    if crop:
        v += ",crop=405:720,scale=720:1280:flags=lanczos"
    v += f",fps=24,format=yuv420p,setsar=1[v{i}]"
    au = f"[{i}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=48000[a{i}]"
    parts += [v, au]
    t += b - a
total = t
print("starts", [round(s, 2) for s in starts], "total", round(total, 2))

cat = "".join(f"[v{i}][a{i}]" for i in range(len(clips))) + f"concat=n={len(clips)}:v=1:a=1[cv][ca]"
parts.append(cat)

F = "C\\:/Windows/Fonts/"
def tf(name):
    return (S + name).replace(":", "\\:")

def dt(txt, font, size, color, x, y, a, b, border=4, extra=""):
    return (f"drawtext=fontfile='{F}{font}':textfile='{tf(txt)}':fontsize={size}:fontcolor={color}"
            f":borderw={border}:bordercolor=black@0.85:x={x}:y={y}:enable='between(t,{a:.2f},{b:.2f})'{extra}")

T = starts
tap = T[4] + 2.6          # card touches terminal in 18
transfer = T[6] + 1.2     # double tap in 12
cash = T[8] + 1.6         # notes out of slot in 21
mission = T[10] + 1.6
hud_end = T[10] + 6.5     # before sky -> logo

R = "w-tw-40"
f = []
f.append(dt("b1.txt", "bahnschrift.ttf", 54, "white", R, 70, 0.6, tap))
f.append(dt("b2.txt", "bahnschrift.ttf", 54, "white", R, 70, tap, transfer))
f.append(dt("b3.txt", "bahnschrift.ttf", 54, "white", R, 70, transfer, cash))
f.append(dt("b4.txt", "bahnschrift.ttf", 54, "white", R, 70, cash, hud_end))
f.append(dt("stars.txt", "seguisym.ttf", 40, "white", R, 138, 0.6, hud_end, border=3))
f.append(dt("m1.txt", "bahnschrift.ttf", 46, "0xFF4D4D", R, 190, tap, tap + 2.6))
f.append(dt("c1.txt", "bahnschrift.ttf", 42, "0x5CFF7A", R, 245, tap + 0.6, tap + 3.6))
f.append(dt("t1.txt", "bahnschrift.ttf", 42, "0x5CFF7A", R, 190, transfer, transfer + 3.0))
f.append(dt("m2.txt", "bahnschrift.ttf", 46, "0xFF4D4D", R, 190, cash, cash + 2.6))
f.append(dt("l1.txt", "seguibli.ttf", 50, "white", 50, "h-200", 1.0, 4.6))
f.append(dt("l2.txt", "seguibli.ttf", 50, "white", 50, "h-200", T[6] + 0.3, T[6] + 3.3))
f.append(dt("l3.txt", "seguibli.ttf", 50, "white", 50, "h-200", T[7] + 0.2, T[7] + 3.2))
f.append(dt("mp.txt", "seguibli.ttf", 74, "0xFFC93C", "(w-tw)/2", "h*0.40", mission, mission + 3.6, border=6,
            extra=f":alpha='if(lt(t,{mission:.2f}+0.3),(t-{mission:.2f})/0.3,1)'"))
f.append(dt("rp.txt", "seguibli.ttf", 56, "white", "(w-tw)/2", "h*0.40+95", mission + 0.4, mission + 3.6, border=5))
parts.append("[cv]" + ",".join(f) + "[ov]")

fs = S + "filter.txt"
open(fs, "w", encoding="utf-8").write(";\n".join(parts))
args += ["-/filter_complex", fs, "-map", "[ov]", "-map", "[ca]",
         "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", OUT]
r = subprocess.run(args, capture_output=True, text=True)
print(r.returncode, r.stderr[-3000:])
