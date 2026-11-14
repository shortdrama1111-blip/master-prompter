#!/usr/bin/env bash
# Montimi i skenës 4 (Florida sot, natën). Përdorim: bash edit_scene4.sh <skena4.mp4> <folder_pune>
set -euo pipefail
S4=$1; W=$2; HERE=$(cd "$(dirname "$0")" && pwd); mkdir -p $W; cd $W
[ -d hud ] || python3 $HERE/hud_v.py hud $HERE/timeline_scene4.json >/dev/null
F1=/usr/share/fonts/opentype/inter/Inter-Light.otf; F2=/usr/share/fonts/opentype/inter/Inter-Regular.otf
AL="if(lt(t,0.50),0,if(lt(t,0.80),(t-0.50)/0.3,if(lt(t,1.75),1,if(lt(t,2.05),(2.05-t)/0.3,0))))"
ffmpeg -v error -y -i "$S4" -framerate 24 -i hud/hud_%04d.png -filter_complex "
[0:v]scale=1080:1920:flags=lanczos,eq=contrast=1.08:saturation=1.08,
curves=master='0/0.02 0.25/0.2 0.6/0.6 1/0.98',
colorbalance=rs=0.02:bs=0.04:rm=0.02:bm=0.03,split[a][b];
[b]curves=all='0/0 0.65/0 1/1',gblur=sigma=26[bl];
[a][bl]blend=all_mode=screen:all_opacity=0.28,vignette=angle=PI/4.5,noise=alls=7:allf=t+u[g];
[g][1:v]overlay=0:0:eof_action=pass[s];
[s]drawtext=fontfile=$F1:text='M I A M I':fontsize=66:fontcolor=white:x=(w-text_w)/2:y=(h/2)-90:alpha='$AL',
drawtext=fontfile=$F2:text='2 0 2 6':fontsize=50:fontcolor=white:x=(w-text_w)/2:y=(h/2)+4:alpha='$AL',format=yuv420p[v];
[0:a]aresample=48000,acompressor=threshold=-24dB:ratio=3:attack=8:release=180:makeup=4dB,loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -c:v libx264 -preset ${PRESET:-fast} -b:v 14M -maxrate 18M -bufsize 28M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart scene4_edit_v1.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 scene4_edit_v1.mp4
