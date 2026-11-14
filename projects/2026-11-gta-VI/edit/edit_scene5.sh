#!/usr/bin/env bash
# Montimi i skenës 5 (v2): varka (0.6x, zëri normal) → fundi i murit → H → Tommy → J → Jason → në varkë.
# H dhe J: nëse skedari mungon ("-"), vendoset ekran i zi me etiketë (vend për gjenerimin).
# Përdorim: bash edit_scene5.sh <5a.mp4> <5b.mp4> <varka_slow.mp4> <H.mp4|-> <J.mp4|-> <folder_pune>
set -euo pipefail
X=$1; Y=$2; BOAT=$3; H=$4; J=$5; W=$6; mkdir -p $W; cd $W
ENC="-c:v libx264 -preset ${PRESET:-fast} -crf 16 -pix_fmt yuv420p -r 24"; AUD="-c:a pcm_s16le -ar 48000 -ac 2"
FT=/usr/share/fonts/opentype/inter/Inter-Regular.otf
seg(){ ffmpeg -v error -y -ss $3 -to $4 -i "$2" -vf "scale=720:1280,setsar=1" -af "aresample=48000,afade=t=in:d=0.03" $ENC $AUD $1.mov; }
hold(){ ffmpeg -v error -y -f lavfi -i color=black:s=720x1280:r=24:d=$2 -f lavfi -i anullsrc=r=48000:cl=stereo -t $2 \
  -vf "drawtext=fontfile=$FT:text='$3':fontsize=34:fontcolor=white@0.85:x=(w-text_w)/2:y=(h-text_h)/2" $ENC $AUD $1.mov; }
seg A "$BOAT" 0 3.21                            # varka (0.6x)
seg B "$X" 1.60 2.45                            # muri mbyllet
if [ "$H" = "-" ]; then hold C 5.0 'H  ·  heronjte dalin (5 s)'; else seg C "$H" 0 5.0; fi
seg D "$X" 4.50 8.06                            # Tommy + zari
if [ "$J" = "-" ]; then hold E 3.5 'J  ·  kercimi ne uje (3.5 s)'; else seg E "$J" 1.0 4.5; fi
seg F "$Y" 4.00 7.00                            # Jason e nxjerr
seg G "$Y" 7.00 9.05                            # në varkë, ikin
printf "file '%s'\n" A.mov B.mov C.mov D.mov E.mov F.mov G.mov > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt $ENC $AUD cut.mov
ffmpeg -v error -y -i cut.mov -filter_complex "
[0:v]scale=1080:1920:flags=lanczos,eq=contrast=1.08:saturation=1.08,
curves=master='0/0.02 0.25/0.2 0.6/0.6 1/0.98',
colorbalance=rs=0.02:bs=0.04:rm=0.02:bm=0.03,split[a][b];
[b]curves=all='0/0 0.65/0 1/1',gblur=sigma=26[bl];
[a][bl]blend=all_mode=screen:all_opacity=0.28,vignette=angle=PI/4.5,noise=alls=7:allf=t+u,format=yuv420p[v];
[0:a]acompressor=threshold=-24dB:ratio=3:attack=8:release=180:makeup=4dB,loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -c:v libx264 -preset ${PRESET:-fast} -b:v 14M -maxrate 18M -bufsize 28M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart scene5_edit_v2.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 scene5_edit_v2.mp4
