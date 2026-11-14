#!/usr/bin/env bash
# Bashkon pjesët e montuara njëra pas tjetrës (prerje e fortë), zëri i bashkuar pa mbivendosje
# (crossfade-i i vjetër e nxirrte zërin 0.25 s para figurës → lipsync i prishur). Përdorim: bash join_all.sh <dalja.mp4> <pjesa1.mp4> <pjesa2.mp4> [...]
set -euo pipefail
OUT=$1; shift; N=$#; IN=""; V=""; i=0
for f in "$@"; do IN="$IN -i $f"; V="$V[$i:v]"; i=$((i+1)); done
AF=""; AL=""; i=0
for f in "$@"; do D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f"); AF="$AF[$i:a]afade=t=in:d=0.05,afade=t=out:st=$(printf "%.3f" $(echo "$D-0.05" | bc)):d=0.05[c$i];"; AL="$AL[c$i]"; i=$((i+1)); done
AF="${AF}${AL}concat=n=$N:v=0:a=1[a$((N-1))]"
ffmpeg -v error -y $IN -filter_complex "${V}concat=n=$N:v=1:a=0[v];$AF;[a$((N-1))]loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -c:v libx264 -preset ${PRESET:-fast} -b:v 14M -maxrate 18M -bufsize 28M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart "$OUT"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
