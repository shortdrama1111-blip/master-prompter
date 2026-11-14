#!/usr/bin/env bash
# Varianti vetëm-zë i mix_score.sh: nxjerr miksin si WAV, që të vendoset mbi videon ekzistuese pa e ri-enkoduar.
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
MS(){ python3 -c "print(int(round(($1)*1000)))"; }
F1=/usr/share/fonts/opentype/inter/Inter-Light.otf
# Dritaret (në kohën e filmit final, pas +1.0 s të skenës 1):
#   TEMAT e lojës (mission passed VC + SA): zhurmat/temat lart, muzika poshtë
#   DIALOGU (radio e policisë, Tommy '86, CJ, megafoni, Tommy te ura): zëri lart, muzika poshtë
# Automatizim i butë (rampa R s në hyrje/dalje të çdo dritareje, jo me "thikë"), kohët në filmin final.
#   tema e lojës: muzika 0.18 · dialogu: muzika 0.15 · ndjekja: zhurmat pak më lart
EXPR=$(python3 - "$O" <<'PY'
import sys
O=float(sys.argv[1]); R=0.8
def k(a,b): return f"clip(min((t-({a-R}))/{R},(({b+R})-t)/{R}),0,1)"
TH=[(14.6,23.2),(27.3,37.0)]
DL=[(6.5,11.7),(21.9,24.0),(55.0+O,59.2+O),(76.6+O,79.8+O)]
CH=[(36.5+O,59.2+O)]
mus="0.95"+"".join(f"*(1-{1-0.18}*{k(a,b)})" for a,b in TH)+"".join(f"*(1-{1-0.15}*{k(a,b)})" for a,b in DL)
fx="min(1,0.25"+"".join(f"+0.7*{k(a,b)}" for a,b in TH+DL)+"".join(f"+0.15*{k(a,b)}" for a,b in CH)+")"
print(mus); print(fx)
PY
)
VOL=$(echo "$EXPR" | sed -n 1p); FXV=$(echo "$EXPR" | sed -n 2p)
ffmpeg -v error -y -i "$F" -i "$M" -filter_complex "

[1:a]aresample=48000,equalizer=f=2500:t=q:w=1:g=3,equalizer=f=900:t=q:w=1:g=2,asplit=4[m1][m2][m3][m4];
[m1]atrim=$(python3 -c "print(max(0,0.96-$O))"):61.0,asetpts=PTS-STARTPTS,afade=t=in:d=1.5,afade=t=out:st=$(echo "58.8+$O" | bc):d=1.2[a];
[m2]atrim=62.0:84.8,asetpts=PTS-STARTPTS,afade=t=in:d=2.0,afade=t=out:st=20.8:d=2.0,adelay=$(MS 62.25+$O)|$(MS 62.25+$O)[b];
[m3]atrim=84.8:98.0,asetpts=PTS-STARTPTS,afade=t=in:d=2.0,afade=t=out:st=11.7:d=1.5,adelay=$(MS 85.99+$O)|$(MS 85.99+$O)[c];
[m4]atrim=99.6:112.0,asetpts=PTS-STARTPTS,afade=t=in:d=1.5,adelay=$(MS $TM)|$(MS $TM)[d];
[a][b][c][d]amix=inputs=4:normalize=0:duration=longest,volume='$VOL':eval=frame,apad=whole_dur=$DT[mus];
[0:a]volume='$FXV':eval=frame,apad=whole_dur=$DT[fx];
[fx][mus]amix=inputs=2:normalize=0:duration=longest,atrim=0:$DT,acompressor=threshold=-24dB:ratio=3:attack=25:release=350:makeup=5dB,alimiter=limit=0.89,loudnorm=I=-14:TP=-1.5:LRA=8[aout]" \
  -map "[aout]" -t $DT -c:a pcm_s16le "$OUT"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
