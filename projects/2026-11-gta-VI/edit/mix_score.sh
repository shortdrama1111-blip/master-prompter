#!/usr/bin/env bash
# Muzika e filmit mbi montimin e plotë + kartë e zezë në fund me titullin (që akordi i fundit të tingëllojë).
# Muzika vendoset në 4 copa, të sinkronizuara me ngjarjet e filmit:
#   A  muzika 0.96–61.0  → filmi 0.00   (prerja e saj në heshtje bie kur fiket prozhektori, filmi 60.04)
#   B  muzika 62.0–84.8  → filmi 62.25  (skena 5)
#   C  muzika 84.8–98.0  → filmi 85.99  (agimi; mbaron kur nis kujtimi)
#   —  kujtimi pa zë                     (filmi TM–TME)
#   D  muzika 99.6–112   → filmi TME    (two-shot, drone, karta e zezë)
# Ulje: nën temat e lojës (14.5–36.0), nën megafonin (55.3–57.8), nën Tommy-n (76.6–79.8).
# Përdorim: bash mix_score.sh <filmi.mp4> <muzika.wav> <dalja.mp4> <TM> <TME>
set -euo pipefail
F=$1; M=$2; OUT=$3; TM=$4; TME=$5; END=4.4
DF=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$F"); DT=$(printf "%.3f" $(echo "$DF+$END" | bc))
MS(){ python3 -c "print(int(round($1*1000)))"; }
F1=/usr/share/fonts/opentype/inter/Inter-Light.otf
VOL="0.45*if(between(t,14.5,36.0),0.18,1)*if(between(t,55.3,57.8),0.45,1)*if(between(t,76.6,79.8),0.3,1)"
ffmpeg -v error -y -i "$F" -i "$M" -filter_complex "
[0:v]tpad=stop_mode=add:stop_duration=$END:color=black,drawtext=fontfile=$F1:text='They brought me here.':fontsize=64:fontcolor=white:x=(w-text_w)/2:y=h*0.20:enable='gte(t,$DF)':alpha='if(lt(t,$DT-1.2),1,max(0,($DT-t)/1.2))',format=yuv420p[v];
[1:a]aresample=48000,asplit=4[m1][m2][m3][m4];
[m1]atrim=0.96:61.0,asetpts=PTS-STARTPTS,afade=t=in:d=1.5,afade=t=out:st=59.7:d=0.3[a];
[m2]atrim=62.0:84.8,asetpts=PTS-STARTPTS,afade=t=in:d=0.8,afade=t=out:st=21.8:d=1.0,adelay=$(MS 62.25)|$(MS 62.25)[b];
[m3]atrim=84.8:98.0,asetpts=PTS-STARTPTS,afade=t=in:d=1.0,afade=t=out:st=12.9:d=0.3,adelay=$(MS 85.99)|$(MS 85.99)[c];
[m4]atrim=99.6:112.0,asetpts=PTS-STARTPTS,afade=t=in:d=0.4,adelay=$(MS $TME)|$(MS $TME)[d];
[a][b][c][d]amix=inputs=4:normalize=0:duration=longest,volume='$VOL':eval=frame,volume='if(between(t,$TM,$TME),0,1)':eval=frame,apad=whole_dur=$DT[mus];
[0:a]apad=whole_dur=$DT[fx];
[fx][mus]amix=inputs=2:normalize=0:duration=longest,atrim=0:$DT,alimiter=limit=0.89,loudnorm=I=-14:TP=-1.5:LRA=11[aout]" \
  -map "[v]" -map "[aout]" -t $DT -c:v libx264 -preset ${PRESET:-fast} -b:v 12M -maxrate 16M -bufsize 24M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart "$OUT"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
