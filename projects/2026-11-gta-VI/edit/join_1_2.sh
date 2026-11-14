#!/usr/bin/env bash
# Bashkon skenën 1 + 2 me kalim "drita e fenerëve": fenerët e kupesë mbushin kuadrin → e bardhë →
# tuneli i 1992. Përdorim: bash join_1_2.sh <scene1_edit.mp4> <scene2_edit.mp4> <out.mp4>
set -euo pipefail
S1=$1; S2=$2; OUT=$3; HERE=$(cd "$(dirname "$0")" && pwd); MP1=${MP1:-14.67}; MP2=${MP2:-13.90}; T1=17.15; XD=0.7; OFF=$(python3 -c "print($T1-$XD)")
WH=$(mktemp -d)
ffmpeg -v error -y -f lavfi -i "anoisesrc=c=white:r=48000:a=0.35:d=1.4" \
  -af "bandpass=f=1800:w=3000,volume='min(1,t/0.9)*if(lt(t,0.95),1,exp(-6*(t-0.95)))':eval=frame,afade=t=in:d=0.3,aformat=channel_layouts=stereo" $WH/whoosh.wav
ffmpeg -v error -y -i "$S1" -i "$S2" -i $WH/whoosh.wav -i $HERE/audio/mission_passed_vc.mp3 -i $HERE/audio/mission_passed_sa.mp3 -filter_complex "
[0:v]trim=0:$T1,setpts=PTS-STARTPTS,eq=brightness='if(gt(t,$T1-0.5),(t-($T1-0.5))*0.9,0)':eval=frame[v1];
[1:v]setpts=PTS-STARTPTS[v2];
[v1][v2]xfade=transition=fadewhite:duration=$XD:offset=$OFF,format=yuv420p[v];
[0:a]atrim=0:$T1,asetpts=PTS-STARTPTS[a1];[1:a]asetpts=PTS-STARTPTS[a2];
[a1][a2]acrossfade=d=$XD[ax];
[2:a]adelay=$(python3 -c "print(int(($T1-1.05)*1000))")|$(python3 -c "print(int(($T1-1.05)*1000))"),volume=0.8[w];
[ax][w]amix=inputs=2:normalize=0:duration=first,asplit=2[sc][mainA];
[3:a]aresample=48000,atrim=0:8.40,afade=t=out:st=7.9:d=0.5,adelay=$(python3 -c "print(int($MP1*1000))")|$(python3 -c "print(int($MP1*1000))")[m1];
[4:a]aresample=48000,adelay=$(python3 -c "print(int(($OFF+$MP2)*1000))")|$(python3 -c "print(int(($OFF+$MP2)*1000))")[m2];
[m1][m2]amix=inputs=2:normalize=0,volume=0.85[mus];
[mus][sc]sidechaincompress=threshold=0.06:ratio=4:attack=20:release=300[duck];
[mainA][duck]amix=inputs=2:normalize=0:duration=first,afade=t=out:st=$(python3 -c "print(round($T1-$XD+16.56-1.0,2))"):d=1.0,loudnorm=I=-14:TP=-1.5:LRA=9[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -preset slow -b:v 14M -maxrate 18M -bufsize 28M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart "$OUT"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
