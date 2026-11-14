#!/usr/bin/env bash
# Montimi i skenës 3 (LA sot). Përdorim: bash edit_scene3.sh <skena3.mp4> <patchA.mp4> <patchB.mp4> <patchD.mp4> <folder_pune>
set -euo pipefail
S3=$1; PA=$2; PB=$3; PD=$4; W=$5; HERE=$(cd "$(dirname "$0")" && pwd); mkdir -p $W; cd $W
ENC="-c:v libx264 -preset ${PRESET:-fast} -crf 16 -pix_fmt yuv420p -r 24"; AUD="-c:a pcm_s16le -ar 48000 -ac 2"
seg(){ D=$(echo "$4-$3" | bc); ffmpeg -v error -y -ss $3 -to $4 -i "$2" -vf "scale=720:1280,setsar=1" \
  -af "aresample=48000,afade=t=in:d=0.03,afade=t=out:st=$(echo "$D-0.04" | bc):d=0.04" $ENC $AUD $1.mov; }
seg A "$S3" 0.000 5.958        # PCH → pasqyra → helikopteri → Michael
seg B "$PA" 1.900 3.700        # Franklin mes policëve
seg C "$PB" 0.800 3.600        # Trevor godet
seg D "$PD" 0.000 4.064        # billbordet → ura brenda ekranit
printf "file '%s'\n" A.mov B.mov C.mov D.mov > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt $ENC $AUD cut.mov
[ -d hud ] || python3 $HERE/hud_v.py hud $HERE/timeline_scene3.json >/dev/null
# riser drejt ekranit (kalimi te skena 4)
ffmpeg -v error -y -f lavfi -i "anoisesrc=c=pink:r=48000:a=0.5:d=2.4" -af "highpass=f=400,lowpass=f=6000,volume='0.05+0.9*pow(t/2.4,3)':eval=frame,afade=t=out:st=2.25:d=0.15,aformat=channel_layouts=stereo" riser.wav
F1=/usr/share/fonts/opentype/inter/Inter-Light.otf; F2=/usr/share/fonts/opentype/inter/Inter-Regular.otf
AL="if(lt(t,0.50),0,if(lt(t,0.80),(t-0.50)/0.3,if(lt(t,1.75),1,if(lt(t,2.05),(2.05-t)/0.3,0))))"
ffmpeg -v error -y -i cut.mov -framerate 24 -i hud/hud_%04d.png -i riser.wav -filter_complex "
[0:v]scale=1080:1920:flags=lanczos,eq=contrast=1.06:saturation=1.03,
curves=master='0/0.01 0.25/0.22 0.6/0.62 1/0.98',
colorbalance=rs=-0.015:bs=0.03:rh=0.02:bh=-0.015,split[a][b];
[b]curves=all='0/0 0.75/0 1/1',gblur=sigma=22[bl];
[a][bl]blend=all_mode=screen:all_opacity=0.16,vignette=angle=PI/5,noise=alls=5:allf=t+u[g];
[g][1:v]overlay=0:0:eof_action=pass[s];
[s]drawtext=fontfile=$F1:text='L O S   A N G E L E S':fontsize=66:fontcolor=white:x=(w-text_w)/2:y=(h/2)-90:alpha='$AL',
drawtext=fontfile=$F2:text='2 0 1 3':fontsize=50:fontcolor=white:x=(w-text_w)/2:y=(h/2)+4:alpha='$AL',format=yuv420p[v];
[0:a]acompressor=threshold=-24dB:ratio=3:attack=8:release=180:makeup=4dB[o];
[2:a]adelay=12200|12200,volume=0.8[r];
[o][r]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -c:v libx264 -preset ${PRESET:-fast} -b:v 14M -maxrate 18M -bufsize 28M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart scene3_edit_v1.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 scene3_edit_v1.mp4
