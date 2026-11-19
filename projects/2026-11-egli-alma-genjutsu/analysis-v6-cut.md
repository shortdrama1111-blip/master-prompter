# Analiza e klipit të prerë (refs/v5/camera-ref-cut.mp4) — 27 frame, 30fps, 0.90s

Matje me OpenCV (ORB + estimateAffinePartial2D) frame pas frame. scale = sa zmadhohet subjekti nga një frame te tjetri.

| Frame | Shot | Çfarë ndodh | scale/frame |
|---|---|---|---|
| 0–2 | 1 medium close, gëzofi | zoom IN i shpejtë që frenon | 1.105 → 1.08 → 1.03 |
| 3–5 | 1 | kthehet në zoom OUT që përshpejton | 0.955 → 0.90 |
| 6–14 | 2 ajo e përkulur → trup i plotë | CRASH ZOOM OUT + roll ~+1°/frame | ~0.89 konstant (subjekti 100% → 41% në 0.27s) |
| 15–21 | 3 close ulur me dorë te fytyra | zoom out i lehtë | ~0.98 |
| 22–26 | 4 wide trup i plotë | zoom out i lehtë + roll -0.7° | 0.97–0.99 |

Mprehtësia (Laplacian) në shot 2 rritet 27 → 44 ndërsa zoom-i del: shenjë që zoom-i është digital
(crop nga 4K i keyframe-uar në montim), jo lente fizike.

## Mekanizmi
1. Zoom-out-i vazhdon përmes prerjeve (match on motion): shot 1 mbaron duke dalë me ~10%/frame,
   shot 2 fillon me të njëjtën shpejtësi. Prerja nuk ndihet, lexohet si një lëvizje e vetme.
2. Speed ramp në gjithë sekuencën: in i shpejtë → out shumë i shpejtë → out i ngadaltë (11% → 2%).
3. Shot-e 5–9 frame (0.17–0.30s), asnjë frame i palëvizur.
4. Roll i vogël 1° gjatë zoom-it + motion blur.
