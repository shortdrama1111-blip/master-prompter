#!/usr/bin/env bash
# Montimi i skenës 2 (LA 1992). Përdorim: bash edit_scene2.sh <skena2.mp4> <extend.mp4> <folder_pune>
set -euo pipefail
S2=$1; EX=$2; W=$3; HERE=$(cd "$(dirname "$0")" && pwd); mkdir -p $W; cd $W
ENC="-c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -r 24"; AUD="-c:a pcm_s16le -ar 48000 -ac 2"
seg(){ ffmpeg -v error -y -ss $3 -to $4 -i "$2" -vf "scale=720:1280,setsar=1" -af "aresample=48000" $ENC $AUD $1.mov; }
seg A "$S2" 0.00 10.00          # tuneli → djali te xhami i pasmë
seg B "$EX" 2.75 4.79           # drifti nga ajri
seg C "$EX" 4.79 7.20           # tri të shtëna në qiell
seg D1 "$S2" 10.00 11.25        # hidraulika ngrihet
seg D2 "$S2" 11.55 12.06        # maja e kërcimit (pa shiritin e zi)
ffmpeg -v error -y -f lavfi -i color=black:s=720x1280:r=24:d=0.40 -f lavfi -i anullsrc=r=48000:cl=stereo -t 0.40 $ENC $AUD K9.mov
printf "file '%s'\n" A.mov B.mov C.mov D1.mov D2.mov K9.mov > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt $ENC $AUD cut.mov
python3 $HERE/hud_sa.py hud $HERE/timeline_scene2.json >/dev/null
# xhingël "mission passed" (i sintetizuar, ton bronzi)
ffmpeg -v error -y -f lavfi -i "aevalsrc='0.16*(sin(2*PI*440*t)+0.5*sin(2*PI*880*t)+0.33*sin(2*PI*1320*t))*between(t,0,0.16)*exp(-6*t)+0.16*(sin(2*PI*554*(t-0.16))+0.5*sin(2*PI*1108*(t-0.16))+0.33*sin(2*PI*1662*(t-0.16)))*between(t,0.16,0.32)*exp(-6*(t-0.16))+0.16*(sin(2*PI*659*(t-0.32))+0.5*sin(2*PI*1318*(t-0.32))+0.33*sin(2*PI*1977*(t-0.32)))*between(t,0.32,0.5)*exp(-6*(t-0.32))+0.2*(sin(2*PI*880*(t-0.5))+0.5*sin(2*PI*1760*(t-0.5))+0.33*sin(2*PI*2640*(t-0.5)))*gte(t,0.5)*exp(-2.4*(t-0.5))':s=48000:d=1.8" \
  -af "lowpass=f=5000,aecho=0.8:0.6:80|160:0.3|0.18,aformat=channel_layouts=stereo" jingle.wav
ffmpeg -v error -y -f lavfi -i "aevalsrc=0.95*sin(2*PI*(52-12*t)*t)*exp(-2.0*t):s=48000:d=2.2" -f lavfi -i "anoisesrc=c=brown:r=48000:a=0.5:d=2.2" \
  -filter_complex "[1]lowpass=f=180,volume='exp(-6*t)':eval=frame[n];[0][n]amix=2:normalize=0,aformat=channel_layouts=stereo" boom.wav
F1=/usr/share/fonts/opentype/inter/Inter-Light.otf; F2=/usr/share/fonts/opentype/inter/Inter-Regular.otf
AL="if(lt(t,0.50),0,if(lt(t,0.80),(t-0.50)/0.3,if(lt(t,1.75),1,if(lt(t,2.05),(2.05-t)/0.3,0))))"
ffmpeg -v error -y -i cut.mov -framerate 24 -i hud/hud_%04d.png -i jingle.wav -i boom.wav -filter_complex "
[0:v]scale=1080:1920:flags=lanczos,eq=contrast=1.07:saturation=1.04:brightness=-0.008,
curves=master='0/0.015 0.25/0.21 0.6/0.62 1/0.975',
colorbalance=rs=-0.02:bs=0.035:rh=0.025:bh=-0.02,split[a][b];
[b]curves=all='0/0 0.72/0 1/1',gblur=sigma=24[bl];
[a][bl]blend=all_mode=screen:all_opacity=0.20,vignette=angle=PI/5,noise=alls=6:allf=t+u[g];
[g][1:v]overlay=0:0:eof_action=pass[s];
[s]drawtext=fontfile=$F1:text='L O S   A N G E L E S':fontsize=66:fontcolor=white:x=(w-text_w)/2:y=(h/2)-90:alpha='$AL',
drawtext=fontfile=$F2:text='1 9 9 2':fontsize=50:fontcolor=white:x=(w-text_w)/2:y=(h/2)+4:alpha='$AL',format=yuv420p[v];
[0:a]acompressor=threshold=-24dB:ratio=3:attack=8:release=180:makeup=5dB[o];
[2:a]adelay=13900|13900,volume=1.4[j];[3:a]adelay=16160|16160[bm];
[o][j][bm]amix=inputs=3:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -t 16.56 -c:v libx264 -preset slow -b:v 14M -maxrate 18M -bufsize 28M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart scene2_edit_v1.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 scene2_edit_v1.mp4
