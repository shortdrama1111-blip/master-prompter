#!/usr/bin/env bash
# Kalimi nata → agimi (5 → 6): shkrirje e gjatë mes dy shot-eve në varkë, me një dritë të artë (screen) që
# ngrihet dhe bie në mes të kalimit, si dielli që lind. Zëri: crossfade me të njëjtën kohëzgjatje (pa zhvendosje).
# Përdorim: bash join_dawn.sh <a.mp4> <b.mp4> <dalja.mp4> [XD=1.5]
set -euo pipefail
A=$1; B=$2; OUT=$3; XD=${4:-1.5}
DA=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$A"); OFF=$(printf "%.3f" $(echo "$DA-$XD" | bc))
ffmpeg -v error -y -i "$A" -i "$B" -filter_complex "
[0:v]settb=AVTB,fps=24,format=yuv420p,split[a0][a1];[1:v]settb=AVTB,fps=24,format=yuv420p,split[b0][b1];
[a0]trim=0:$OFF,setpts=PTS-STARTPTS[p1];
[a1]trim=$OFF,setpts=PTS-STARTPTS[at];[b0]trim=0:$XD,setpts=PTS-STARTPTS[bh];
[at][bh]xfade=transition=fade:duration=$XD:offset=0,format=gbrp[x];
color=c=0xFFB050:s=1080x1920:r=24:d=$XD,format=gbrp[g];
[x][g]blend=all_expr='A+(B-A*B/255)*0.65*max(0,1-abs(T-$XD/2)/($XD/2))',format=yuv420p[p2];
[b1]trim=$XD,setpts=PTS-STARTPTS[p3];
[p1][p2][p3]concat=n=3:v=1:a=0[v];
[0:a][1:a]acrossfade=d=$XD[ax];[ax]loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -c:v libx264 -preset ${PRESET:-fast} -b:v 12M -maxrate 16M -bufsize 24M -pix_fmt yuv420p -r 24 -c:a aac -b:a 256k -ar 48000 -movflags +faststart "$OUT"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
