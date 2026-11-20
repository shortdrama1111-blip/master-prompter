"""Mix narrator (one-shot ElevenLabs take, cut into lines) + music + clip SFX onto montage v1."""
import subprocess, sys

D = "C:/Users/Desjon/Downloads/"
VIDEO = D + "epara_montim_v1.mp4"
NARR = D + "ElevenLabs_2026-11-20T00_33_28_eparaja_gen_s46_sim75_v4.mp3"
MUSIC = D + "Golden_Hour_Getaway_2026-11-20T003425.wav"
OUT = sys.argv[1]
TOTAL = 74.2

# (start, end in narration take) -> start in montage
lines = [
    (0.00, 3.75, 0.60),    # Tirana... Qyteti ku secili ka nje plan.
    (4.60, 9.70, 5.60),    # Plani im? ... asnje yll ne koke.
    (10.95, 13.95, 17.00), # Mos u nxito...
    (14.85, 16.60, 26.75), # Po... keto po.
    (17.40, 22.50, 30.40), # Pa kesh, pa stres... mbrapsht.
    (22.90, 24.95, 39.40), # Te vjetrat? Histori e mbyllur.
    (25.35, 29.20, 43.60), # Arbit i kisha nje borxh...
    (29.60, 32.40, 49.40), # Por disa pune...
    (32.90, 39.45, 53.00), # Xhaxhi... / Gështenja të nxehta...
    (40.20, 43.15, 65.75), # Misioni u krye. Pa asnje yll.
    (43.80, 45.87, 72.05), # Me mire se para.
]

f = []
for i, (a, b, at) in enumerate(lines):
    ms = int(at * 1000)
    f.append(f"[1:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:d=0.04,afade=t=out:st={b-a-0.06:.2f}:d=0.06,adelay={ms}|{ms}[n{i}]")
f.append("".join(f"[n{i}]" for i in range(len(lines))) + f"amix=inputs={len(lines)}:normalize=0,volume=1.6,apad,atrim=0:{TOTAL}[voice]")
f.append("[voice]asplit=2[vmix][vkey]")
f.append(f"[2:a]aresample=48000,atrim=0:{TOTAL},afade=t=out:st={TOTAL-1.5}:d=1.5,volume=0.55[mus]")
f.append("[mus][vkey]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[musd]")
f.append(f"[0:a]aresample=48000,volume=0.40[sfx]")
f.append("[vmix][musd][sfx]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[mix]")

fs = OUT + ".filter.txt"
open(fs, "w", encoding="utf-8").write(";\n".join(f))
args = ["ffmpeg", "-v", "error", "-y", "-i", VIDEO, "-i", NARR, "-i", MUSIC,
        "-/filter_complex", fs, "-map", "0:v", "-map", "[mix]", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k",
        "-ar", "48000", "-shortest", OUT]
r = subprocess.run(args, capture_output=True, text=True)
print(r.returncode, r.stderr[-2000:])
