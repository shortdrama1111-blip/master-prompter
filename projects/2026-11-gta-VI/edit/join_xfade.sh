#!/usr/bin/env bash
# Bashkon dy pjesë me një kalim xfade (p.sh. fadeblack për kërcim kohe). Përdorim: bash join_xfade.sh <a.mp4> <b.mp4> <dalja.mp4> [transition=fadeblack] [kohëzgjatja=0.8]
set -euo pipefail
A=$1; B=$2; OUT=$3; TR=${4:-fadeblack}; XD=${5:-0.8}
DA=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$A"); OFF=$(printf "%.3f" $(echo "$DA-$XD" | bc))
ffmpeg -v error -y -i "$A" -i "$B" -filter_complex "[0:v]settb=AVTB,fps=24,format=yuv420p[a];[1:v]settb=AVTB,fps=24,format=yuv420p[b];[a][b]xfade=transition=$TR:duration=$XD:offset=$OFF[v];[0:a][1:a]acrossfade=d=$XD[x];[x]loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -c:v libx264 -preset ${PRESET:-fast} -b:v 12M -maxrate 16M -bufsize 24M -pix_fmt yuv420p -r 24 -c:a aac -b:a 256k -ar 48000 -movflags +faststart "$OUT"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
