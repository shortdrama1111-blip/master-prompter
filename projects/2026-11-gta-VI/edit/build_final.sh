#!/usr/bin/env bash
# Rindërton filmin final nga skena 1 deri te muzika, pastaj versionin me kokërr sipas epokës.
# Përdorim: bash build_final.sh <scratchpad>
set -euo pipefail
S=$1; HERE=$(cd "$(dirname "$0")" && pwd); cd $HERE
P1=$S/p1s1/v.mp4 bash edit_scene1.sh $S/s1c/v.mp4 $S/ed1 >/dev/null
bash edit_scene1_v2.sh $S/ed1 >/dev/null
bash join_1_2.sh $S/ed1/scene1_edit_v2.mp4 $S/ed2/scene2_edit_v1.mp4 $S/scenes_1-2_v4.mp4 >/dev/null
bash join_2_3_switch.sh $S/scenes_1-2_v4.mp4 $S/s3/v.mp4 $S/scenes_3-4_v4.mp4 $S/gta_scenes_1-4_v5.mp4 >/dev/null
bash join_all.sh $S/gta_scenes_1-5_v5.mp4 $S/gta_scenes_1-4_v5.mp4 $S/ed5d/scene5_edit_v4.mp4 >/dev/null
bash join_dawn.sh $S/gta_scenes_1-5_v5.mp4 $S/ed6/scene6_edit_v3.mp4 $S/gta_full_v4_nomusic.mp4 1.5 >/dev/null
D15=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $S/gta_scenes_1-5_v5.mp4); S6=$(python3 -c "print($D15-1.5)")
P=$(for f in S01 S02 S03 S04 S05 S06; do ffprobe -v error -show_entries format=duration -of csv=p=0 $S/ed6/$f.mov; done | paste -sd+ | bc)
Q=$(for f in M1 M2 M3 M4 M5 M6 M7; do ffprobe -v error -show_entries format=duration -of csv=p=0 $S/ed6/$f.mov; done | paste -sd+ | bc)
TM=$(python3 -c "print(round($S6+$P,3))"); TME=$(python3 -c "print(round($S6+$P+$Q,3))")
D12=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $S/scenes_1-2_v4.mp4)
echo "TM=$TM TME=$TME D12=$D12 D15=$D15 S6=$S6"
OFFSET=1.0 bash mix_score.sh $S/gta_full_v4_nomusic.mp4 audio/score_v1.wav $S/GTA_They_Brought_Me_Here_FINAL.mp4 $TM $TME
# versioni me kokërr: 1986 → C, 1992 → A, 2013–2026 → E, agimi → A, kujtimi → D, karta e zezë pa kokërr
F=$S/GTA_They_Brought_Me_Here_FINAL.mp4; DF=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $F)
B1=18.15; B2=$(python3 -c "print(round($D12-0.4,3))"); B3=$S6; B4=$TM; B5=$TME; B6=$(python3 -c "print(round($DF-4.4,3))")
GA="noise=c0s=9:c0f=t+u:c1s=3:c1f=t:c2s=3:c2f=t"
GC="split[x][y];[y]curves=all='0/0 0.88/0 1/1',gblur=sigma=14,colorchannelmixer=rr=1:gg=0.35:bb=0.2[h];[x][h]blend=all_mode=screen:all_opacity=0.16,noise=c0s=13:c0f=t+u:c1s=4:c1f=t:c2s=4:c2f=t"
GD="eq=saturation=0.8:contrast=0.92:brightness=0.03,colorbalance=rs=0.06:bs=-0.05,gblur=sigma=1,noise=c0s=28:c0f=t+u:c1s=10:c1f=t:c2s=10:c2f=t,vignette=angle=PI/3.5"
GE="noise=c0s=12:c0f=t+u,unsharp=3:3:0.3"
ffmpeg -v error -y -i $F -filter_complex "
[0:v]split=7[v1][v2][v3][v4][v5][v6][v7];
[v1]trim=0:$B1,setpts=PTS-STARTPTS,$GC[g1];
[v2]trim=$B1:$B2,setpts=PTS-STARTPTS,$GA[g2];
[v3]trim=$B2:$B3,setpts=PTS-STARTPTS,$GE[g3];
[v4]trim=$B3:$B4,setpts=PTS-STARTPTS,$GA[g4];
[v5]trim=$B4:$B5,setpts=PTS-STARTPTS,$GD[g5];
[v6]trim=$B5:$B6,setpts=PTS-STARTPTS,$GA[g6];
[v7]trim=$B6,setpts=PTS-STARTPTS[g7];
[g1][g2][g3][g4][g5][g6][g7]concat=n=7:v=1:a=0,format=yuv420p[v]" -map "[v]" -map 0:a -c:v libx264 -preset ${PRESET:-fast} -b:v 12M -maxrate 16M -bufsize 24M -pix_fmt yuv420p -r 24 -c:a copy -movflags +faststart $S/GTA_They_Brought_Me_Here_FINAL_grain.mp4
for f in FINAL FINAL_grain; do ffmpeg -v error -y -i $S/GTA_They_Brought_Me_Here_$f.mp4 -c:v libx264 -preset fast -b:v 6M -maxrate 8M -bufsize 12M -pix_fmt yuv420p -c:a copy -movflags +faststart $S/GTA_${f}_preview.mp4; done
echo BUILT
