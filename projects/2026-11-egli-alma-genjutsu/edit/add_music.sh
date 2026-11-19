#!/bin/bash
# Muzika: "Timeless" (versioni i plotë mp3 i përdoruesit) — videoja e klientes përdor këtë këngë nga 105.876 s,
# e ngadalësuar 0.90× (slowed, me pitch më të ulët), gjetur me korrelacion valësh (corr 0.63).
# Këtu: e njëjta pikë nisjeje dhe e njëjta shpejtësi, kënga vazhdon natyrshëm pa loop; fade-out 1.5 s; loudnorm -14 LUFS.
# Përdorimi: edit/add_music.sh VIDEO DALJA SONG.mp3
set -e
V="$1"; O="$2"; M="$3"; SR=$(ffprobe -v error -select_streams a -show_entries stream=sample_rate -of csv=p=0 "$M")
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
FO=$(python3 -c "print(max(0,$D-1.5))")
ffmpeg -v error -y -i "$V" -ss 105.876 -i "$M" -filter_complex \
"[1:a]asetrate=$SR*0.9,aresample=44100,atrim=0:$D,asetpts=PTS-STARTPTS,afade=t=out:st=$FO:d=1.5,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
-map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest "$O"
