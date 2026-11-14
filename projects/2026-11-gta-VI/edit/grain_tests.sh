#!/usr/bin/env bash
# Prova të kokrrës së filmit: 5 pamje × 2 shot-e, me etiketë, në një video krahasimi.
# Përdorim: bash grain_tests.sh <shot1.mp4> <nga> <shot2.mp4> <nga> <folder> 
set -euo pipefail
A=$1; TA=$2; B=$3; TB=$4; W=$5; mkdir -p $W; cd $W
FT=/usr/share/fonts/opentype/inter/Inter-Regular.otf
ENC="-c:v libx264 -preset fast -crf 14 -pix_fmt yuv420p -r 24 -an"
declare -A L; declare -A G
L[0]="ORIGJINALI";                  G[0]="null"
L[1]="A - 35mm i holle (dite)";      G[1]="noise=c0s=9:c0f=t+u:c1s=3:c1f=t:c2s=3:c2f=t,curves=master='0/0.03 0.5/0.5 1/0.97'"
L[2]="B - 16mm i trashe";            G[2]="crop=iw-8:ih-8:4+2*sin(n*1.7):4+2*cos(n*1.3),scale=1080:1920,gblur=sigma=0.6,noise=c0s=20:c0f=t+u:c1s=8:c1f=t:c2s=8:c2f=t,vignette=angle=PI/4"
L[3]="C - 500T nate (halation)";     G[3]="split[a][b];[b]curves=all='0/0 0.75/0 1/1',gblur=sigma=18,colorchannelmixer=rr=1:gg=0.25:bb=0.1[h];[a][h]blend=all_mode=screen:all_opacity=0.45,noise=c0s=13:c0f=t+u:c1s=4:c1f=t:c2s=4:c2f=t"
L[4]="D - Super 8 (kujtim)";         G[4]="crop=iw-12:ih-12:6+3*sin(n*2.3):6+3*cos(n*1.9),scale=1080:1920,eq=saturation=0.8:contrast=0.92:brightness=0.03,colorbalance=rs=0.06:bs=-0.05,gblur=sigma=1,noise=c0s=28:c0f=t+u:c1s=10:c1f=t:c2s=10:c2f=t,vignette=angle=PI/3.5"
L[5]="E - kokerr organike vetem drite"; G[5]="noise=c0s=12:c0f=t+u,unsharp=3:3:0.3"
i=0
for SRC in "$A:$TA" "$B:$TB"; do F=${SRC%%:*}; T=${SRC##*:}
  for k in 0 1 2 3 4 5; do
    ffmpeg -v error -y -ss $T -t 2.5 -i "$F" -filter_complex "[0:v]scale=1080:1920:flags=lanczos,${G[$k]},drawtext=fontfile=$FT:text='${L[$k]}':fontsize=44:fontcolor=white:box=1:boxcolor=black@0.55:boxborderw=14:x=(w-text_w)/2:y=h-220[v]" -map "[v]" $ENC c_${i}_$k.mp4
  done; i=$((i+1)); done
ls c_*.mp4 | sort -V | sed "s/.*/file '&'/" > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt -c:v libx264 -preset fast -b:v 14M -pix_fmt yuv420p -movflags +faststart grain_tests.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 grain_tests.mp4
