#!/usr/bin/env bash
# Kalimi 2 → 3 si "ndërrimi i personazhit" i lojës së 2013: kamera ngrihet/zhytet me blur dhe ngjyra shuhet,
# pamja satelitore e LA-së mbi kupenë e zezë (nga helikopteri), pastaj zhytje te skena 3 me 3 goditje zëri.
# Përdorim: bash join_2_3_switch.sh <skenat_1-2.mp4> <skena3_burim_raw.mp4> <skenat_3-4.mp4> <dalja.mp4>
set -euo pipefail
A=$1; R=$2; B=$3; OUT=$4; WD=$(mktemp -d)
E=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$A"); E=$(echo "$E-0.40" | bc)   # pa të zezën e fundit
S=$(echo "$E-0.60" | bc); X=0.60; Y=0.50
ffmpeg -v error -y -f lavfi -i "anoisesrc=c=pink:r=48000:a=0.7:d=1.3" -af "highpass=f=250,lowpass=f=5000,volume='if(lt(t,0.6),pow(t/0.6,2),exp(-5*(t-0.6)))':eval=frame,aformat=channel_layouts=stereo" $WD/wh.wav
ffmpeg -v error -y -f lavfi -i "aevalsrc=0.9*sin(2*PI*(70-30*t)*t)*exp(-14*t):s=48000:d=0.35" -af "aformat=channel_layouts=stereo" $WD/th.wav
MS(){ echo "$1*1000/1" | bc; }
ffmpeg -v error -y -i "$A" -i "$R" -i "$B" -i $WD/wh.wav -i $WD/th.wav -i $WD/th.wav -i $WD/th.wav -filter_complex "
[0:v]split[a][at];[a]trim=0:$S,setpts=PTS-STARTPTS,format=yuv420p[v0];
[at]trim=$S:$E,setpts=PTS-STARTPTS,scale=w='2*trunc(540*(1+0.5*pow(t/$X,2)))':h='2*trunc(960*(1+0.5*pow(t/$X,2)))':eval=frame,crop=1080:1920,split[p][q];
[q]gblur=sigma=26[qb];[p][qb]blend=all_expr='A*(1-min(T/$X,1))+B*min(T/$X,1)',eq=saturation='1-0.75*min(t/$X,1)':brightness='0.06*min(t/$X,1)':eval=frame,format=yuv420p[v1];
[1:v]trim=3.0:3.6,setpts=PTS-STARTPTS,scale=1080:1920,scale=w='2*trunc(540*(1.0+0.35*t/0.6))':h='2*trunc(960*(1.0+0.35*t/0.6))':eval=frame,crop=1080:1920,eq=saturation=0.25:contrast=1.1,colorbalance=bs=0.08:bm=0.05,gblur=sigma=3,format=yuv420p[v2];
[2:v]split[b][bt];[bt]trim=0:$Y,setpts=PTS-STARTPTS,scale=w='2*trunc(540*(1.25-0.25*sin(PI/2*min(t/$Y,1))))':h='2*trunc(960*(1.25-0.25*sin(PI/2*min(t/$Y,1))))':eval=frame,crop=1080:1920,split[m][n];
[n]gblur=sigma=22[nb];[m][nb]blend=all_expr='A*min(T/$Y,1)+B*(1-min(T/$Y,1))',eq=saturation='0.25+0.75*min(t/$Y,1)':eval=frame,format=yuv420p[v3];
[b]trim=$Y,setpts=PTS-STARTPTS,format=yuv420p[v4];
[v0][v1][v2][v3][v4]concat=n=5:v=1:a=0,setsar=1[v];
[0:a]atrim=0:$E,asetpts=PTS-STARTPTS,afade=t=out:st=$(echo "$E-0.5" | bc):d=0.5[a0];
anullsrc=r=48000:cl=stereo,atrim=0:0.6[sil];
[2:a]asetpts=PTS-STARTPTS,afade=t=in:d=0.3[a2];
[a0][sil][a2]concat=n=3:v=0:a=1[ac];
[3:a]adelay=$(MS $S)|$(MS $S),volume=0.8[w];
[4:a]adelay=$(MS $E)|$(MS $E)[t1];[5:a]adelay=$(MS "$E+0.3")|$(MS "$E+0.3")[t2];[6:a]adelay=$(MS "$E+0.6")|$(MS "$E+0.6"),volume=1.2[t3];
[ac][w][t1][t2][t3]amix=inputs=5:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -c:v libx264 -preset ${PRESET:-fast} -b:v 14M -maxrate 18M -bufsize 28M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart "$OUT"
rm -rf $WD; ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
