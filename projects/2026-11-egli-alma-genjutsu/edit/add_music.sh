#!/bin/bash
# Muzika nga videoja e klientes (refs/v4/reference-video-v4.mp4, 0–17.86 s, ~108 bpm, takti ~2.23 s).
# Për video më të gjata: 0–15.83 s, pastaj loop i pastër nga takti 9.14 s (crossfade 0.08 s), fade-out 1.5 s, loudnorm -14 LUFS.
# Përdorimi: edit/add_music.sh VIDEO DALJA
set -e
V="$1"; O="$2"; R=refs/v4/reference-video-v4.mp4
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
FO=$(python3 -c "print(max(0,$D-1.5))")
ffmpeg -v error -y -i "$V" -i "$R" -filter_complex \
"[1:a]atrim=0:15.83,asetpts=PTS-STARTPTS[a1];[1:a]atrim=9.14:17.86,asetpts=PTS-STARTPTS[a2];[a1][a2]acrossfade=d=0.08:c1=tri:c2=tri,atrim=0:$D,afade=t=out:st=$FO:d=1.5,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
-map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest "$O"
