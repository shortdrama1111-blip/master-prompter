#!/usr/bin/env bash
# Skena 1 v2: si v1 + HUD i viteve '80 (ora, paratë, jeta, 2 yje, arma, minimapa) + "mission passed".
# Kërkon cut.mov, hum.wav, riser.wav, tick.wav, boom.wav nga edit_scene1.sh në <folder_pune>.
set -euo pipefail
W=$1; HERE=$(cd "$(dirname "$0")" && pwd); cd $W
python3 $HERE/hud_vc.py hud $HERE/timeline_scene1.json >/dev/null
# xhingël "mission passed" i sintetizuar (jo muzika e lojës)
ffmpeg -v error -y -f lavfi -i "aevalsrc='0.22*(sin(2*PI*523*t)+0.3*sin(2*PI*1569*t))*between(t,0,0.14)*exp(-8*t)+0.22*(sin(2*PI*659*(t-0.12))+0.3*sin(2*PI*1977*(t-0.12)))*between(t,0.12,0.26)*exp(-8*(t-0.12))+0.22*(sin(2*PI*784*(t-0.24))+0.3*sin(2*PI*2352*(t-0.24)))*between(t,0.24,0.40)*exp(-8*(t-0.24))+0.26*(sin(2*PI*1046*(t-0.40))+0.25*sin(2*PI*3138*(t-0.40)))*gte(t,0.40)*exp(-2.6*(t-0.40))':s=48000:d=1.6" \
  -af "aecho=0.8:0.6:90|180:0.35|0.2,aformat=channel_layouts=stereo" jingle.wav
F1=/usr/share/fonts/opentype/inter/Inter-Light.otf; F2=/usr/share/fonts/opentype/inter/Inter-Regular.otf
AL="if(lt(t,4.80),0,if(lt(t,5.10),(t-4.80)/0.3,if(lt(t,6.15),1,if(lt(t,6.45),(6.45-t)/0.3,0))))"
ffmpeg -v error -y -i cut.mov -framerate 24 -i hud/hud_%04d.png \
  -i hum.wav -i riser.wav -i tick.wav -i tick.wav -i $HERE/audio/mission_passed_vc.mp3 -i boom.wav -filter_complex "
[0:v]scale=1080:1920:flags=lanczos,eq=contrast=1.07:saturation=1.06:brightness=-0.008,
curves=master='0/0.015 0.25/0.21 0.6/0.62 1/0.975',
colorbalance=rs=-0.02:bs=0.035:rh=0.025:bh=-0.02,split[a][b];
[b]curves=all='0/0 0.72/0 1/1',gblur=sigma=24[bl];
[a][bl]blend=all_mode=screen:all_opacity=0.22,vignette=angle=PI/5,noise=alls=6:allf=t+u,
fade=t=in:st=0.40:d=0.18[g];
[g][1:v]overlay=0:0:eof_action=pass[s];
[s]drawtext=fontfile=$F1:text='M I A M I':fontsize=74:fontcolor=white:x=(w-text_w)/2:y=(h/2)-90:alpha='$AL',
drawtext=fontfile=$F2:text='1 9 8 6':fontsize=50:fontcolor=white:x=(w-text_w)/2:y=(h/2)+4:alpha='$AL',format=yuv420p[v];
[0:a]acompressor=threshold=-24dB:ratio=3:attack=8:release=180:makeup=6dB[o];
[2:a]adelay=0|0[h];[3:a]adelay=1590|1590[r];
[4:a]adelay=5450|5450[t1];[5:a]adelay=8200|8200[t2];
[6:a]aresample=48000,atrim=0:2.55,afade=t=out:st=2.05:d=0.5,adelay=14670|14670,volume=${JV:-0.9}[j];[7:a]adelay=17160|17160[bm];
[o][h][r][t1][t2][j][bm]amix=inputs=7:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -t 17.81 -c:v libx264 -preset ${PRESET:-medium} -b:v 14M -maxrate 18M -bufsize 28M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart scene1_edit_v2.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 scene1_edit_v2.mp4
