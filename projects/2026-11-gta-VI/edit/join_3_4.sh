#!/usr/bin/env bash
# Bashkimi 3 → 4, "zoom-through": kamera përshpejton brenda ekranit të billbordit (zoom 1→3x me motion blur
# dhe ndriçim), prerje e fortë, skena 4 hapet nga 1.35x në 1.0 (ease-out) me blic 3 frame. Dimensione çift
# (pa vija jeshile në skaje). Përdorim: bash join_3_4.sh <skena3_edit.mp4> <skena4_edit.mp4> <dalja.mp4> [cut=14.05]
set -euo pipefail
A=$1; B=$2; OUT=$3; C=${4:-14.05}; Z=0.40; C0=$(echo "$C-$Z" | bc); WD=$(mktemp -d)
ffmpeg -v error -y -f lavfi -i "anoisesrc=c=pink:r=48000:a=0.6:d=0.9" -af "highpass=f=300,lowpass=f=7000,volume='if(lt(t,0.4),pow(t/0.4,2),exp(-6*(t-0.4)))':eval=frame,aformat=channel_layouts=stereo" $WD/whoosh.wav
ffmpeg -v error -y -i "$A" -i "$B" -i $WD/whoosh.wav -filter_complex "
[0:v]trim=0:$C0,setpts=PTS-STARTPTS,format=yuv420p[a1];
[0:v]trim=$C0:$C,setpts=PTS-STARTPTS,scale=w='2*trunc(540*(1+2.0*pow(t/$Z,2)))':h='2*trunc(960*(1+2.0*pow(t/$Z,2)))':eval=frame,crop=1080:1920,tmix=frames=3,eq=brightness='0.22*pow(t/$Z,3)':eval=frame,format=yuv420p[a2];
[1:v]trim=0:0.45,setpts=PTS-STARTPTS,scale=w='2*trunc(540*(1.35-0.35*sin(PI/2*min(t/0.45,1))))':h='2*trunc(960*(1.35-0.35*sin(PI/2*min(t/0.45,1))))':eval=frame,crop=1080:1920,eq=brightness='0.22*max(0,1-t/0.125)':eval=frame,format=yuv420p[b1];
[1:v]trim=0.45,setpts=PTS-STARTPTS,format=yuv420p[b2];
[a1][a2][b1][b2]concat=n=4:v=1:a=0,setsar=1[v];
[0:a]atrim=0:$C,asetpts=PTS-STARTPTS[x];[1:a]asetpts=PTS-STARTPTS[y];
[x]afade=t=out:st=$(printf "%.3f" $(echo "$C-0.06" | bc)):d=0.06[x2];[y]afade=t=in:d=0.06[y2];[x2][y2]concat=n=2:v=0:a=1[xy];[2:a]adelay=$(echo "($C0-0.05)*1000/1" | bc)|$(echo "($C0-0.05)*1000/1" | bc),volume=0.7[w];
[xy][w]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -c:v libx264 -preset ${PRESET:-fast} -b:v 14M -maxrate 18M -bufsize 28M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart "$OUT"
rm -rf $WD; ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
