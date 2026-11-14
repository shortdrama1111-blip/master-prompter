#!/usr/bin/env bash
# Vetëm miksi i muzikës + kokrra + previews (pa rindërtuar skenat). Përdorim: bash final_mix.sh <scratchpad>
set -euo pipefail
S=$1; cd $(dirname "$0")
D15=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $S/gta_scenes_1-5_v5.mp4); S6=$(python3 -c "print($D15-1.5)")
P=$(for f in S01 S02 S03 S04 S05 S06; do ffprobe -v error -show_entries format=duration -of csv=p=0 $S/ed6/$f.mov; done | paste -sd+ | bc)
Q=$(for f in M1 M2 M3 M4 M5 M6 M7; do ffprobe -v error -show_entries format=duration -of csv=p=0 $S/ed6/$f.mov; done | paste -sd+ | bc)
TM=$(python3 -c "print(round($S6+$P,3))"); TME=$(python3 -c "print(round($S6+$P+$Q,3))")
OFFSET=1.0 bash mix_score.sh $S/gta_full_v4_nomusic.mp4 audio/score_v1.wav $S/GTA_They_Brought_Me_Here_FINAL.mp4 $TM $TME
bash grain_pass.sh $S
