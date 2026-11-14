#!/usr/bin/env bash
# Montimi i skenës 5 (v4): varka (0.6x, zë i ri) → WH parkimi → WH heronjtë dalin → Tommy → kërcimi (5b) → Jason → në varkë.
# Përdorim: bash edit_scene5.sh <5a.mp4> <5b.mp4> <varka_slow.mp4> <WH.mp4> <folder_pune>
set -euo pipefail
X=$1; Y=$2; BOAT=$3; WH=$4; W=$5; mkdir -p $W; cd $W
ENC="-c:v libx264 -preset ${PRESET:-fast} -crf 16 -pix_fmt yuv420p -r 24"; AUD="-c:a pcm_s16le -ar 48000 -ac 2"
seg(){ ffmpeg -v error -y -ss $3 -to $4 -i "$2" -vf "scale=720:1280,setsar=1" -af "aresample=48000,afade=t=in:d=0.03,afade=t=out:st=$(printf "%.3f" $(echo "$4-$3-0.04" | bc)):d=0.04" $ENC $AUD $1.mov; }
# A · varka: zëri i Seedance ulet dhe pastrohet; mbi të një helikë e sintetizuar që afrohet + spërkatje uji
ffmpeg -v error -y -f lavfi -i "aevalsrc='0.5*(sin(2*PI*46*t)+0.6*sin(2*PI*92*t)+0.35*sin(2*PI*138*t)+0.2*sin(2*PI*184*t))*(0.35+0.65*t/3.21)':s=48000:d=3.21" \
  -f lavfi -i "anoisesrc=c=brown:r=48000:a=0.6:d=3.21" -f lavfi -i "anoisesrc=c=pink:r=48000:a=0.35:d=3.21" -filter_complex "
[0]lowpass=f=900,tremolo=f=23:d=0.25[e];[1]lowpass=f=400,volume='0.3+0.7*t/3.21':eval=frame[r];
[2]highpass=f=1800,lowpass=f=9000,volume='if(gt(t,1.6),0.9*min((t-1.6)/0.4,1),0.05)':eval=frame[s];
[e][r][s]amix=inputs=3:normalize=0,acompressor=threshold=-14dB:ratio=3,aformat=channel_layouts=stereo" boat_sfx.wav
ffmpeg -v error -y -i "$BOAT" -i boat_sfx.wav -filter_complex "[0:v]scale=720:1280,setsar=1[v];[0:a]aresample=48000,lowpass=f=3000,volume=0.3[o];[o][1:a]amix=inputs=2:normalize=0,afade=t=in:d=0.3[a]" -map "[v]" -map "[a]" -t 3.21 $ENC $AUD A.mov
seg B "$WH" 0.00 4.10                           # parkimi
seg C "$WH" 4.125 10.08                         # heronjtë dalin një nga një → rreshti
seg D "$X" 4.50 8.06                            # Tommy + zari
ffmpeg -v error -y -ss 2.00 -to 3.00 -i "$Y" -vf "scale=1008:1792,crop=720:1280:0:250,setsar=1" -af "aresample=48000,afade=t=in:d=0.03" $ENC $AUD E1.mov
seg E2 "$Y" 3.00 4.00                           # kërcimi
seg F "$Y" 4.00 7.00                            # Jason e nxjerr
seg G "$Y" 7.00 9.05                            # në varkë, ikin
printf "file '%s'\n" A.mov B.mov C.mov D.mov E1.mov E2.mov F.mov G.mov > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt $ENC $AUD cut.mov
ffmpeg -v error -y -i cut.mov -filter_complex "
[0:v]scale=1080:1920:flags=lanczos,eq=contrast=1.08:saturation=1.08,
curves=master='0/0.02 0.25/0.2 0.6/0.6 1/0.98',
colorbalance=rs=0.02:bs=0.04:rm=0.02:bm=0.03,split[a][b];
[b]curves=all='0/0 0.65/0 1/1',gblur=sigma=26[bl];
[a][bl]blend=all_mode=screen:all_opacity=0.28,vignette=angle=PI/4.5,noise=alls=7:allf=t+u,format=yuv420p[v];
[0:a]highpass=f=35,acompressor=threshold=-24dB:ratio=3:attack=8:release=180:makeup=4dB,alimiter=limit=0.89,loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -c:v libx264 -preset ${PRESET:-fast} -b:v 14M -maxrate 18M -bufsize 28M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart scene5_edit_v4.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 scene5_edit_v4.mp4
