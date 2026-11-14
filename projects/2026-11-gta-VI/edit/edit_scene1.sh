#!/usr/bin/env bash
# Montimi i skenës 1. Përdorim: bash edit_scene1.sh <video_burim.mp4> <folder_pune>
set -euo pipefail
SRC=$1; W=$2; mkdir -p $W; cd $W
HERE=$(cd "$(dirname "$0")" 2>/dev/null && pwd || echo .)
ENC="-c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -r 24"
AUD="-c:a pcm_s16le -ar 48000 -ac 2"

# 1. Segmentet (burimi → timeline). Droni shkurtohet në 2.0 s (pjesa më pak reale).
seg(){ ffmpeg -v error -y -ss $2 -to $3 -i "$SRC" -vf "setsar=1" $ENC $AUD $1.mov; }
seg A 0.00 2.29; seg B 2.29 4.21; seg C 4.21 6.21; seg D 6.21 8.71
seg E 8.71 11.21; seg F 11.21 12.71; seg G 13.10 15.10; seg H 15.25 17.05
blk(){ ffmpeg -v error -y -f lavfi -i color=black:s=720x1280:r=24:d=$2 -f lavfi -i anullsrc=r=48000:cl=stereo -t $2 $ENC $AUD $1.mov; }
blk K0 0.40; blk K9 0.90
printf "file '%s'\n" K0.mov A.mov B.mov C.mov D.mov E.mov F.mov G.mov H.mov K9.mov > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt $ENC $AUD cut.mov

# 2. Dizajni i zërit (i sintetizuar, pa kredite)
ffmpeg -v error -y -f lavfi -i "aevalsrc=0.05*sin(2*PI*60*t)+0.025*sin(2*PI*120*t)+0.004*sin(2*PI*15734*t):s=48000:d=2.69" \
  -f lavfi -i "anoisesrc=c=pink:r=48000:a=0.12:d=2.69" \
  -filter_complex "[1]highpass=f=500,lowpass=f=7000[r];[0][r]amix=2:normalize=0,afade=t=in:d=0.3,afade=t=out:st=2.4:d=0.29,aformat=channel_layouts=stereo" hum.wav
ffmpeg -v error -y -f lavfi -i "aevalsrc=(t/1.1)*0.12*sin(2*PI*(180*t+380*t*t)):s=48000:d=1.1" \
  -f lavfi -i "anoisesrc=c=white:r=48000:a=0.1:d=1.1" \
  -filter_complex "[1]bandpass=f=3000:w=2500,volume='t/1.1':eval=frame[n];[0][n]amix=2:normalize=0,afade=t=in:d=0.6,aformat=channel_layouts=stereo" riser.wav
ffmpeg -v error -y -f lavfi -i "aevalsrc=0.30*sin(2*PI*1400*t)*exp(-18*t)+0.14*sin(2*PI*2100*t)*exp(-26*t):s=48000:d=0.35" -af "aformat=channel_layouts=stereo" tick.wav
ffmpeg -v error -y -f lavfi -i "aevalsrc=0.95*sin(2*PI*(52-12*t)*t)*exp(-2.0*t):s=48000:d=2.2" \
  -f lavfi -i "anoisesrc=c=brown:r=48000:a=0.5:d=2.2" \
  -filter_complex "[1]lowpass=f=180,volume='exp(-6*t)':eval=frame[n];[0][n]amix=2:normalize=0,aformat=channel_layouts=stereo" boom.wav

# 3. Grade + grafika + titulli + miksimi
F1=/usr/share/fonts/opentype/inter/Inter-Light.otf; F2=/usr/share/fonts/opentype/inter/Inter-Regular.otf
AL="if(lt(t,4.80),0,if(lt(t,5.10),(t-4.80)/0.3,if(lt(t,6.15),1,if(lt(t,6.45),(6.45-t)/0.3,0))))"
B0="between(t,4.61,5.40)+between(t,14.30,16.70)*gte(mod(t-14.30,0.5),0.25)"
B3="between(t,11.90,14.30)+between(t,14.30,16.70)*lt(mod(t-14.30,0.5),0.25)"
ffmpeg -v error -y -i cut.mov -loop 1 -i stars_0.png -loop 1 -i stars_1.png -loop 1 -i stars_2.png -loop 1 -i stars_3.png \
  -i hum.wav -i riser.wav -i tick.wav -i tick.wav -i tick.wav -i boom.wav -filter_complex "
[0:v]scale=1080:1920:flags=lanczos,eq=contrast=1.07:saturation=1.06:brightness=-0.008,
curves=master='0/0.015 0.25/0.21 0.6/0.62 1/0.975',
colorbalance=rs=-0.02:bs=0.035:rh=0.025:bh=-0.02,split[a][b];
[b]curves=all='0/0 0.72/0 1/1',gblur=sigma=24[bl];
[a][bl]blend=all_mode=screen:all_opacity=0.22,vignette=angle=PI/5,noise=alls=6:allf=t+u,
fade=t=in:st=0.40:d=0.18[g];
[g][1:v]overlay=x=W-w-46:y=96:shortest=1:enable='$B0'[s0];
[s0][2:v]overlay=x=W-w-46:y=96:shortest=1:enable='between(t,5.40,8.20)'[s1];
[s1][3:v]overlay=x=W-w-46:y=96:shortest=1:enable='between(t,8.20,11.90)'[s2];
[s2][4:v]overlay=x=W-w-46:y=96:shortest=1:enable='$B3'[s3];
[s3]drawtext=fontfile=$F1:text='M I A M I':fontsize=74:fontcolor=white:x=72:y=h-360:alpha='$AL',
drawtext=fontfile=$F2:text='1 9 8 6':fontsize=50:fontcolor=white:x=76:y=h-268:alpha='$AL',
format=yuv420p[v];
[0:a]acompressor=threshold=-24dB:ratio=3:attack=8:release=180:makeup=6dB[o];
[5:a]adelay=0|0[h];[6:a]adelay=1590|1590[r];
[7:a]adelay=5400|5400[t1];[8:a]adelay=8200|8200[t2];[9:a]adelay=11900|11900[t3];
[10:a]adelay=16880|16880[bm];
[o][h][r][t1][t2][t3][bm]amix=inputs=7:normalize=0:duration=first,
loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -t 17.81 -c:v libx264 -preset slow -b:v 14M -maxrate 18M -bufsize 28M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart scene1_edit.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 scene1_edit.mp4
