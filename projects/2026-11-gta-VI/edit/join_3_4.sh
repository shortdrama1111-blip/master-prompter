#!/usr/bin/env bash
# Bashkimi 3 → 4: kamera hyn në ekranin e billbordit; ura brenda ekranit bëhet drone-i i skenës 4
# (skena 4 nis e zmadhuar 1.15x dhe zbret në 1.0 ndërsa shkrihet mbi fundin e skenës 3).
# Përdorim: bash join_3_4.sh <skena3_edit.mp4> <skena4_edit.mp4> <dalja.mp4>
set -euo pipefail
A=$1; B=$2; OUT=$3
DA=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$A"); XD=0.6; OFF=$(echo "$DA-$XD" | bc)
ffmpeg -v error -y -i "$A" -i "$B" -filter_complex "
[0:v]settb=AVTB,fps=24,format=yuv420p[a];
[1:v]scale=w='1080*(1.15-0.15*min(t/1.0,1))':h=-2:eval=frame:flags=bicubic,crop=1080:1920,settb=AVTB,fps=24,format=yuv420p[b];
[a][b]xfade=transition=fade:duration=$XD:offset=$OFF[v];
[0:a][1:a]acrossfade=d=$XD:c1=tri:c2=tri,loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -c:v libx264 -preset ${PRESET:-fast} -b:v 14M -maxrate 18M -bufsize 28M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart "$OUT"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
