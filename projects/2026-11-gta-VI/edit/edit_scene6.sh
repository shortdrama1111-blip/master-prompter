#!/usr/bin/env bash
# Montimi i skenës 6 (agimi): varka → ura nga larg → arrestimet (0.8x) → Tommy + BUSTED → Egli → zari → kujtimi → two-shot → drone + titujt.
# Përdorim: bash edit_scene6.sh <6a.mp4> <6b_lemuar.mp4> <folder_pune> <scratchpad_me_burimet>
set -euo pipefail
A=$1; B=$2; W=$3; SRC=$4; HERE=$(cd "$(dirname "$0")" && pwd); mkdir -p $W; cd $W
ENC="-c:v libx264 -preset ${PRESET:-fast} -crf 16 -pix_fmt yuv420p -r 24"; AUD="-c:a pcm_s16le -ar 48000 -ac 2"
fx(){ printf "%.3f" "$1"; }
seg(){ local D=$(fx $(echo "$4-$3" | bc)); ffmpeg -v error -y -ss $3 -to $4 -i "$2" -vf "scale=720:1280,setsar=1${5:+,$5}" \
  -af "aresample=48000,afade=t=in:d=0.04,afade=t=out:st=$(fx $(echo "$D-0.05" | bc)):d=0.05" $ENC $AUD $1.mov; }
slow(){ local D=$(fx $(echo "($4-$3)/$5" | bc -l)); ffmpeg -v error -y -ss $3 -to $4 -i "$2" -filter_complex \
  "[0:v]scale=720:1280,setsar=1,setpts=PTS/$5,minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1${6:+,$6}[v];[0:a]aresample=48000,atempo=$5,afade=t=in:d=0.04[a]" \
  -map "[v]" -map "[a]" -t $D $ENC $AUD $1.mov; }
# kujtimi: ngjyrë e ngrohtë e zbehur, pak blur, vinjetë; zëri i ulët
MEM="eq=saturation=0.55:brightness=0.03:contrast=0.92,colorbalance=rs=0.08:gs=0.03:bs=-0.06,gblur=sigma=1.2,vignette=angle=PI/3.5"
seg S01 "$B" 0.00 1.95                                  # varka, kthen kokën
seg S02 "$A" 0.30 2.48                                  # ura nga larg në agim
slow S03 "$A" 2.52 6.56 0.8 "eq=saturation=0.3:contrast=1.05"   # arrestimet, gri si ekrani "busted" i lojës
seg S04 "$A" 6.62 9.40                                  # Tommy, i fundit
seg S05 "$B" 1.98 3.44                                  # Egli nga afër
seg S06 "$B" 3.48 4.94                                  # zari në pëllëmbë
seg M1 "$SRC/s1c/v.mp4" 9.80 10.30 "$MEM"               # Tommy varet zarin (1986)
seg M2 "$SRC/s2/v.mp4" 4.40 4.85 "$MEM"                 # CJ (1992)
seg M3 "$SRC/s3/v.mp4" 4.70 5.15 "$MEM"                 # Michael
seg M4 "$SRC/pA/v.mp4" 2.10 2.55 "$MEM"                 # Franklin
seg M5 "$SRC/p1/v.mp4" 1.70 2.15 "$MEM"                 # Trevor
seg M6 "$SRC/s4/v.mp4" 0.30 0.75 "$MEM"                 # konvoji mbi urë
seg M7 "$SRC/s5/x1.mp4" 6.80 7.40 "$MEM"                # Tommy ia jep zarin
seg S07 "$B" 4.98 6.52                                  # two-shot
seg S08 "$B" 6.56 12.05                                 # drone
printf "file '%s'\n" S01.mov S02.mov S03.mov S04.mov S05.mov S06.mov M1.mov M2.mov M3.mov M4.mov M5.mov M6.mov M7.mov S07.mov S08.mov > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt $ENC $AUD cut.mov
T=$(ffprobe -v error -show_entries format=duration -of csv=p=0 cut.mov)
# kohët në montim, nga kohëzgjatjet reale të copave
DUR=$(for f in S01 S02 S03 S04 S05 S06 M1 M2 M3 M4 M5 M6 M7 S07 S08; do ffprobe -v error -show_entries format=duration -of csv=p=0 $f.mov; done | tr '\n' ',')
t(){ python3 -c "d=[$DUR];print(round(sum(d[:$1]),3))"; }
TB=$(t 2); TM=$(t 6); TS=$(t 14)
# zëri: jehona e kujtimeve + një ton i mbajtur (akord i butë) nga zari deri në fund
ffmpeg -v error -y -f lavfi -i "aevalsrc='0.06*(sin(2*PI*220*t)+0.8*sin(2*PI*261.63*t)+0.7*sin(2*PI*329.63*t)+0.4*sin(2*PI*440*t))*min(t/2,1)*if(gt(t,$(echo "$T-$(t 5)-1.5" | bc)),max(0,($T-$(t 5)-t)/1.5),1)':s=48000:d=$(echo "$T-$(t 5)" | bc)" -af "lowpass=f=2500,aecho=0.8:0.7:120|240:0.3|0.2,aformat=channel_layouts=stereo" pad.wav
ffmpeg -v error -y -ss 9.8 -to 11.2 -i $SRC/s1c/v.mp4 -vn -af "aresample=48000,highpass=f=200,aecho=0.8:0.6:180|360:0.4|0.25,volume=0.7,aformat=channel_layouts=stereo" e1.wav
ffmpeg -v error -y -ss 6.6 -to 8.06 -i $SRC/s5/x1.mp4 -vn -af "aresample=48000,highpass=f=200,aecho=0.8:0.6:180|360:0.4|0.25,volume=0.7,aformat=channel_layouts=stereo" e2.wav
FT=$HERE/fonts/TitanOne-Regular.ttf; F1=/usr/share/fonts/opentype/inter/Inter-Light.otf
MS(){ python3 -c "print(int(round($1*1000)))"; }
ffmpeg -v error -y -i cut.mov -i pad.wav -i e1.wav -i e2.wav -filter_complex "
[0:v]scale=1080:1920:flags=lanczos,eq=contrast=1.06:saturation=1.05,curves=master='0/0.02 0.3/0.28 0.7/0.72 1/0.98',
colorbalance=rh=0.03:bh=-0.03:rs=-0.01:bs=0.03,split[a][b];[b]curves=all='0/0 0.7/0 1/1',gblur=sigma=26[bl];
[a][bl]blend=all_mode=screen:all_opacity=0.22,vignette=angle=PI/4.5,noise=alls=6:allf=t+u[g];
[g]drawtext=fontfile=$FT:text='busted':fontsize=230:fontcolor=0xC81E1E:borderw=10:bordercolor=black:x=(w-text_w)/2:y=(h-text_h)/2-120:alpha='if(lt(t,$TB),0,if(lt(t,$TB+0.15),(t-$TB)/0.15,if(lt(t,$(t 3)-0.25),1,max(0,($(t 3)-t)/0.25))))',
drawtext=fontfile=$F1:text='1 9 8 6   ·   1 9 9 2   ·   2 0 1 3   ·   2 0 2 6':fontsize=40:fontcolor=white:x=(w-text_w)/2:y=h*0.20:alpha='if(lt(t,$TS+0.4),0,if(lt(t,$TS+0.8),(t-$TS-0.4)/0.4,if(lt(t,$TS+2.2),1,max(0,($TS+2.6-t)/0.4))))',
drawtext=fontfile=$F1:text='They brought me here.':fontsize=64:fontcolor=white:x=(w-text_w)/2:y=h*0.20:alpha='if(lt(t,$TS+2.8),0,if(lt(t,$TS+3.4),(t-$TS-2.8)/0.6,1))',format=yuv420p[v];
[0:a]highpass=f=35,acompressor=threshold=-24dB:ratio=3:attack=8:release=180:makeup=3dB[o];
[1:a]adelay=$(MS $(t 5))|$(MS $(t 5)),volume=0.9[p];[2:a]adelay=$(MS $TM)|$(MS $TM)[x];[3:a]adelay=$(MS "$TM+2.6")|$(MS "$TM+2.6")[y];
[o][p][x][y]amix=inputs=4:normalize=0:duration=first,alimiter=limit=0.89,loudnorm=I=-14:TP=-1.5:LRA=9[aout]" \
  -map "[v]" -map "[aout]" -c:v libx264 -preset ${PRESET:-fast} -b:v 14M -maxrate 18M -bufsize 28M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart scene6_edit_v1.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 scene6_edit_v1.mp4
