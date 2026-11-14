#!/usr/bin/env bash
# Muzika e filmit mbi montimin e plotë + kartë e zezë në fund me titullin (që akordi i fundit të tingëllojë).
# Muzika vendoset në 4 copa, të sinkronizuara me ngjarjet e filmit:
#   A  muzika 0.96–61.0  → filmi 0.00   (prerja e saj në heshtje bie kur fiket prozhektori, filmi 60.04)
#   B  muzika 62.0–84.8  → filmi 62.25  (skena 5)
#   C  muzika 84.8–98.0  → filmi 85.99  (agimi; mbaron kur nis kujtimi)
#   D  muzika 99.6–112   → filmi TM     (rritja finale nis me kujtimin: kujtimi pa zhurma, vetëm muzikë)
# Ulje: nën temat e lojës (14.5–36.0), nën megafonin (55.3–57.8), nën Tommy-n (76.6–79.8).
# Përdorim: bash mix_score.sh <filmi.mp4> <muzika.wav> <dalja.mp4> <TM> <TME>
set -euo pipefail
F=$1; M=$2; OUT=$3; TM=$4; TME=$5; END=4.4; O=${OFFSET:-0}
DF=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$F"); DT=$(printf "%.3f" $(echo "$DF+$END" | bc))
MS(){ python3 -c "print(int(round($1*1000)))"; }
F1=/usr/share/fonts/opentype/inter/Inter-Light.otf
# Dritaret (në kohën e filmit final, pas +1.0 s të skenës 1):
#   TEMAT e lojës (mission passed VC + SA): zhurmat/temat lart, muzika poshtë
#   DIALOGU (radio e policisë, Tommy '86, CJ, megafoni, Tommy te ura): zëri lart, muzika poshtë
TH="between(t,14.6,23.2)+between(t,27.3,37.0)"
DL="between(t,6.5,11.7)+between(t,21.9,24.0)+between(t,55.3+$O,57.8+$O)+between(t,76.6+$O,79.8+$O)"
VOL="${MV:-0.95}*if(gt($TH,0),0.18,if(gt($DL,0),0.22,1))"
FXV="if(gt($TH,0),0.95,if(gt($DL,0),0.95,${FXB:-0.4}))"
ffmpeg -v error -y -i "$F" -i "$M" -filter_complex "
[0:v]fade=t=out:st=$(printf "%.3f" $(echo "$DF-1.0" | bc)):d=1.0,tpad=stop_mode=add:stop_duration=$END:color=black,drawtext=fontfile=$F1:text='They brought me here.':fontsize=64:fontcolor=white:x=(w-text_w)/2:y=h*0.20:enable='gte(t,$DF-1.0)':alpha='if(lt(t,$DT-1.2),1,max(0,($DT-t)/1.2))',format=yuv420p[v];
[1:a]aresample=48000,asplit=4[m1][m2][m3][m4];
[m1]atrim=$(python3 -c "print(max(0,0.96-$O))"):61.0,asetpts=PTS-STARTPTS,afade=t=in:d=1.5,afade=t=out:st=$(echo "59.7+$O" | bc):d=0.3[a];
[m2]atrim=62.0:84.8,asetpts=PTS-STARTPTS,afade=t=in:d=0.8,afade=t=out:st=21.8:d=1.0,adelay=$(MS 62.25+$O)|$(MS 62.25+$O)[b];
[m3]atrim=84.8:98.0,asetpts=PTS-STARTPTS,afade=t=in:d=1.0,afade=t=out:st=12.9:d=0.3,adelay=$(MS 85.99+$O)|$(MS 85.99+$O)[c];
[m4]atrim=99.6:112.0,asetpts=PTS-STARTPTS,afade=t=in:d=0.4,adelay=$(MS $TM)|$(MS $TM)[d];
[a][b][c][d]amix=inputs=4:normalize=0:duration=longest,volume='$VOL':eval=frame,apad=whole_dur=$DT[mus];
[0:a]volume='$FXV':eval=frame,apad=whole_dur=$DT[fx];
[fx][mus]amix=inputs=2:normalize=0:duration=longest,atrim=0:$DT,alimiter=limit=0.89,loudnorm=I=-14:TP=-1.5:LRA=11[aout]" \
  -map "[v]" -map "[aout]" -t $DT -c:v libx264 -preset ${PRESET:-fast} -b:v 12M -maxrate 16M -bufsize 24M -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -movflags +faststart "$OUT"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
