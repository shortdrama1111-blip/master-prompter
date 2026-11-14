#!/usr/bin/env bash
# Versioni final: B + mbyllja (prerë + zoom + slow) + tekst + muzikë. Nga folderi i projektit.
set -euo pipefail
R=renders; T=edit/tmpf; mkdir -p $T
ENC="-c:v libx264 -preset medium -crf 17 -pix_fmt yuv420p -r 24 -c:a aac -b:a 192k -ar 48000 -ac 2"
CX=350; CY=741; ZM=2.0          # qendra e logos në çantë dhe zoom-i final
# c1: 2.3–3.4 s e mbylljes, zoom që rritet butë 1.0 → 2.4 (smoothstep 0.3–1.1 s)
P="clip((in/24-0.3)/0.8\,0\,1)"
ffmpeg -v error -y -ss 2.3 -t 1.1 -i $R/closing-v1.mp4 -filter_complex \
 "[0:v]scale=2160:3840:flags=lanczos,zoompan=z='1+($ZM-1)*pow($P\,2)*(3-2*$P)':x='$CX*3-iw/zoom/2':y='$CY*3-ih/zoom/2':d=1:s=720x1280:fps=24,setsar=1[v];[0:a]afade=t=in:d=0.02[a]" \
 -map "[v]" -map "[a]" $ENC $T/c1.mp4
# c2: 3.4–5.0 s, zoom statik 2.0, ngadalësuar 1.6× (çanta lëkundet butë, jo kuadër i ngrirë)
W=$(python3 -c "print(int(720/$ZM)//2*2)"); H=$(python3 -c "print(int(1280/$ZM)//2*2)")
ffmpeg -v error -y -ss 3.4 -t 1.6 -i $R/closing-v1.mp4 -filter_complex \
 "[0:v]crop=$W:$H:$CX-$W/2:$CY-$H/2,scale=720:1280:flags=lanczos,setpts=1.6*PTS,setsar=1[v];[0:a]atempo=0.625,afade=t=out:st=2.3:d=0.25[a]" \
 -map "[v]" -map "[a]" $ENC $T/c2.mp4
printf "file '%s'\n" $(pwd)/edit/etos-cut-B.mp4 $(pwd)/$T/c1.mp4 $(pwd)/$T/c2.mp4 > $T/list.txt
ffmpeg -v error -y -f concat -safe 0 -i $T/list.txt $ENC $T/joined.mp4
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $T/joined.mp4)
B=$(ffprobe -v error -show_entries format=duration -of csv=p=0 edit/etos-cut-B.mp4)
TT=$(python3 -c "print(round($B+1.1,2))")          # teksti hyn kur zoom-i mbaron
MOFF=$(python3 -c "print(round($TT-25.0,2))")      # button-i i këngës (25.0 s) bie te teksti
MOFFMS=$(python3 -c "print(int($MOFF*1000))")
FB=/usr/share/fonts/opentype/inter/InterDisplay-SemiBold.otf
FL=/usr/share/fonts/opentype/inter/Inter-Light.otf
GOLD=0xD4B072
VF="drawtext=fontfile=$FB:text='BLACK FRIDAY':fontcolor=white:fontsize=46:x=(w-tw)/2:y=h*0.13:enable='between(t,0.15,1.7)':alpha='if(lt(t,0.4),(t-0.15)/0.25,if(gt(t,1.45),(1.7-t)/0.25,1))',"
VF+="drawtext=fontfile=$FB:text='BLACK FRIDAY':fontcolor=$GOLD:fontsize=78:x=(w-tw)/2:y=h*0.70:enable='gte(t,$TT)':alpha='min(1,(t-$TT)/0.3)',"
VF+="drawtext=fontfile=$FL:text='Ulje deri në 50%':expansion=none:fontcolor=white:fontsize=50:x=(w-tw)/2:y=h*0.70+105:enable='gte(t,$TT+0.35)':alpha='min(1,(t-$TT-0.35)/0.3)'"
ffmpeg -v error -y -i $T/joined.mp4 -i audio/music-velvet-bloom.wav -filter_complex \
 "[0:v]$VF[v];[0:a]volume=0.55[s];[1:a]adelay=${MOFFMS}|${MOFFMS},volume=0.9,afade=t=in:st=$MOFF:d=0.4[m];[s][m]amix=inputs=2:duration=first:normalize=0,afade=t=out:st=$(python3 -c "print(round($DUR-0.4,2))"):d=0.4,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
 -map "[v]" -map "[a]" $ENC edit/etos-FINAL.mp4
echo "final $(ffprobe -v error -show_entries format=duration -of csv=p=0 edit/etos-FINAL.mp4)s  tekst@$TT  muzika@$MOFF"
rm -rf $T
