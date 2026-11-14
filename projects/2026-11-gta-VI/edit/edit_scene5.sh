#!/usr/bin/env bash
# Montimi i skenës 5 (ura, natën): 5b varka mbërrin → 5a muri, heronjtë, Tommy → 5b kërcimi.
# Slow-motion me interpolim lëvizjeje (minterpolate) se gjenerimet dolën shumë të shpejta. Pa HUD (loja "ka mbaruar").
# Përdorim: bash edit_scene5.sh <5a_heronjte.mp4> <5b_varka.mp4> <folder_pune>
set -euo pipefail
X=$1; Y=$2; W=$3; mkdir -p $W; cd $W
ENC="-c:v libx264 -preset ${PRESET:-fast} -crf 16 -pix_fmt yuv420p -r 24"; AUD="-c:a pcm_s16le -ar 48000 -ac 2"
# seg <emri> <burimi> <nga> <deri> <shpejtësia> [filtër shtesë video]
seg(){ local VF="scale=720:1280,setsar=1${6:+,$6}"
  if [ "$5" != "1" ]; then VF="$VF,setpts=PTS/$5,minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1"; fi
  ffmpeg -v error -y -ss $3 -to $4 -i "$2" -vf "$VF" -af "aresample=48000,atempo=$5,afade=t=in:d=0.04" $ENC $AUD $1.mov; }
seg A "$Y" 0.00 2.00 0.75                       # varka del nga mangrovet
seg B "$X" 0.00 2.50 0.60                       # makinat bëhen mur
seg C "$X" 2.50 4.50 0.75                       # pesë heronjtë
seg D "$X" 4.50 8.06 1                          # Tommy: "Go. It's your game now."
seg E "$Y" 2.00 3.00 0.80 "scale=1008:1792,crop=720:1280:0:250"   # nga varka lart (pa objektin në qoshe)
seg F "$Y" 3.00 4.00 0.50                       # kërcimi
seg G "$Y" 4.00 7.00 0.80                       # Jason e nxjerr
seg H "$Y" 7.00 9.05 0.90                       # në varkë, ikin
printf "file '%s'\n" A.mov B.mov C.mov D.mov E.mov F.mov G.mov H.mov > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt $ENC $AUD cut.mov
ffmpeg -v error -y -i cut.mov -filter_complex "
[0:v]scale=1080:1920:flags=lanczos,eq=contrast=1.08:saturation=1.08,
curves=master='0/0.02 0.25/0.2 0.6/0.6 1/0.98',
colorbalance=rs=0.02:bs=0.04:rm=0.02:bm=0.03,split[a][b];
[b]curves=all='0/0 0.65/0 1/1',gblur=sigma=26[bl];
[a][bl]blend=all_mode=screen:all_opacity=0.28,vignette=angle=PI/4.5,noise=alls=7:allf=t+u,format=yuv420p[v];
[0:a]acompressor=threshold=-24dB:ratio=3:attack=8:release=180:makeup=4dB,loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -c:v libx264 -preset ${PRESET:-fast} -b:v 14M -maxrate 18M -bufsize 28M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart scene5_edit_v1.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 scene5_edit_v1.mp4
