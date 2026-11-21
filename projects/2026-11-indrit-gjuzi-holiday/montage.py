"""Montazhi final v3: klipet e aprovuara + muzika, prerjet ne rrjeten 120 BPM (1 beat = 0.5 s).

python montage.py            -> indrit-gjuzi_final_v3.mp4 (1080x1920, 24 fps, me muzike)
python montage.py --silent   -> indrit-gjuzi_final_v3_silent.mp4
"""
import os, sys, subprocess

P = os.path.dirname(os.path.abspath(__file__))
A = lambda f: os.path.join(P, 'approved-clips', f)
W, H, FPS = 1080, 1920, 24

# (skedari, fillimi ne burim, kohezgjatja); fillimet ne montazh: 0, 2, 4.5, 7.5, 11.25, 14, fund 18
CLIPS = [
    (A('shot1_shelves_v7.mp4'),          0.0, 2.0),
    (A('shot2_conveyor.mp4'),            1.5, 2.5),
    (A('shot3_garland_v7.mp4'),          0.5, 3.0),
    (A('shot4_tumble.mp4'),              0.0, 3.75),
    (A('shot5_bag_closer_v4.mp4'),       0.1, 2.75),   # goditja ne 11.67 s, me zilen e muzikes
    (A('shot6_happy_holidays_v3.mp4'),   0.0, 4.0),
]
MUSIC = os.path.join(P, 'audio', 'music-winter-glow.wav')

silent = '--silent' in sys.argv
cmd = ['ffmpeg', '-v', 'error', '-y']
for f, _, _ in CLIPS:
    cmd += ['-i', f]
if not silent:
    cmd += ['-i', MUSIC]
parts = []
for i, (_, ss, d) in enumerate(CLIPS):
    parts.append(f'[{i}:v]trim=start={ss}:duration={d},setpts=PTS-STARTPTS,fps={FPS},'
                 f'scale={W}:{H}:flags=lanczos,setsar=1[v{i}]')
parts.append(''.join(f'[v{i}]' for i in range(len(CLIPS))) + f'concat=n={len(CLIPS)}:v=1:a=0[v]')
total = sum(d for _, _, d in CLIPS)
maps = ['-map', '[v]']
if not silent:
    parts.append(f'[{len(CLIPS)}:a]atrim=0:{total},apad=whole_dur={total},afade=t=out:st={total - 0.4}:d=0.4[a]')
    maps += ['-map', '[a]', '-c:a', 'aac', '-b:a', '256k']
out = os.path.join(P, 'indrit-gjuzi_final_v3_silent.mp4' if silent else 'indrit-gjuzi_final_v3.mp4')
cmd += ['-filter_complex', ';'.join(parts)] + maps + ['-c:v', 'libx264', '-crf', '16', '-preset', 'slow',
                                                      '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-t', str(total), out]
subprocess.run(cmd, check=True)
print(out, total, 's')
