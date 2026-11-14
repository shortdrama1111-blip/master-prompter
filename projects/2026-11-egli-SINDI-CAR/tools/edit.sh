#!/usr/bin/env bash
# Montimi egli-SINDI-CAR. Përdorim: bash tools/edit.sh  (nga folderi i projektit)
set -euo pipefail
R=renders; T=edit/tmp; mkdir -p $T edit
ENC="-c:v libx264 -preset medium -crf 17 -pix_fmt yuv420p -r 24 -c:a aac -b:a 192k -ar 48000 -ac 2"

# seg <out> <src> <start> <end> <zoom> <cx> <cy> [speed]   (cx,cy = qendra e crop-it në 720x1280; speed 1.0 = normal)
SP12=${SP12:-1.25}   # shpejtësia e akteve 1–2 (klienti: "pak më shpejt")
SP3=${SP3:-1.0}      # shpejtësia e aktit 3
seg () {
  local out=$1 src=$2 ss=$3 to=$4 z=$5 cx=$6 cy=$7 sp=${8:-1.0}
  local d; d=$(python3 -c "print(round($to-$ss,3))")
  local vf="scale=720:1280"
  if [ "$z" != "1" ]; then
    vf="crop=trunc(720/$z/2)*2:trunc(1280/$z/2)*2:max(0\,min(720-720/$z\,$cx-360/$z)):max(0\,min(1280-1280/$z\,$cy-640/$z)),scale=720:1280:flags=lanczos"
  fi
  local od; od=$(python3 -c "print(round($d/$sp,3))")
  ffmpeg -v error -y -ss $ss -t $d -i $src -vf "$vf,setpts=PTS/$sp,setsar=1" \
    -af "atempo=$sp,afade=t=in:d=0.02,afade=t=out:st=$(python3 -c "print(max(0,round($od-0.03,3)))"):d=0.03" $ENC $T/$out.mp4
}

# ---------- VERSIONI A: i plotë, pa prerje (aktet njëri pas tjetrit) ----------
seg A1 $R/act1-v1.mp4 0 10.08 1 0 0
seg A2 $R/act2-v1.mp4 0.04 10.0 1 0 0
seg A3 $R/act3-v1.mp4 0 10.0 1 0 0
printf "file '%s'\n" A1.mp4 A2.mp4 A3.mp4 > $T/listA.txt
ffmpeg -v error -y -f concat -safe 0 -i $T/listA.txt $ENC edit/etos-full-A.mp4

# ---------- VERSIONI B: me prerje + punch-in ----------
# Akti 1
seg b01 $R/act1-v1.mp4 0.40 1.40 1   0   0 $SP12      # dera hapet, çantat hyjnë
seg b02 $R/act1-v1.mp4 2.00 3.10 1.2 360 600 $SP12    # ulet (kapërcen momentin në këmbë)
seg b03 $R/act1-v1.mp4 3.15 4.80 1.6 360 560 $SP12    # zgjidh fjongon
seg b04 $R/act1-v1.mp4 5.00 5.90 1.4 360 600 $SP12    # dora në çantë
seg b05 $R/act1-v1.mp4 8.00 10.08 1  0   0 $SP12      # shishja drejt kamerës (kapërcen shishen e gabuar 6–8 s)
# Akti 2
seg b06 $R/act2-v1.mp4 0.50 2.60 1.6 360 480 $SP12    # spërkat kyçin
seg b07 $R/act2-v1.mp4 3.00 4.80 1.8 360 420 $SP12    # nuhat kyçin
seg b08 $R/act2-v1.mp4 5.20 6.80 1.6 360 450 $SP12    # spërkat qafën
seg b09 $R/act2-v1.mp4 7.20 9.00 1.5 360 480 $SP12    # blush
seg b10 $R/act2-v1.mp4 9.00 10.00 1 0 0 $SP12         # kthim në të gjerë (lidhet me aktin 3)
# Akti 3 (i ka prerjet vetë), pa kuadër të ngrirë
seg b11 $R/act3-v1.mp4 0 10.0 1 0 0 $SP3
# (kuadri i ngrirë 2 s u hoq me kërkesë të përdoruesit)
printf "file '%s'\n" b01.mp4 b02.mp4 b03.mp4 b04.mp4 b05.mp4 b06.mp4 b07.mp4 b08.mp4 b09.mp4 b10.mp4 b11.mp4 > $T/listB.txt
ffmpeg -v error -y -f concat -safe 0 -i $T/listB.txt $ENC edit/etos-cut-B.mp4
for f in edit/etos-full-A.mp4 edit/etos-cut-B.mp4; do echo "$f $(ffprobe -v error -show_entries format=duration -of csv=p=0 $f)s"; done
