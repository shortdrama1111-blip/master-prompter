#!/usr/bin/env bash
# Bashkon pjesët e montuara njëra pas tjetrës (prerje e fortë; pjesa e parë mbaron në të zezë),
# me crossfade të shkurtër zëri. Përdorim: bash join_all.sh <dalja.mp4> <pjesa1.mp4> <pjesa2.mp4> [...]
set -euo pipefail
OUT=$1; shift; N=$#; IN=""; V=""; i=0
for f in "$@"; do IN="$IN -i $f"; V="$V[$i:v]"; i=$((i+1)); done
AF="[0:a]anull[a0]"; for ((k=1;k<N;k++)); do AF="$AF;[a$((k-1))][$k:a]acrossfade=d=0.25:c1=tri:c2=tri[a$k]"; done
ffmpeg -v error -y $IN -filter_complex "${V}concat=n=$N:v=1:a=0[v];$AF;[a$((N-1))]loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -c:v libx264 -preset ${PRESET:-fast} -b:v 14M -maxrate 18M -bufsize 28M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart "$OUT"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
