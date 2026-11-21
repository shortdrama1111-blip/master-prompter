# Vendimet

## Mjeti
- **Pa model AI.** Videoja është motion graphic me shumë tekst; modelet e videos e shtrembërojnë
  tekstin (ë, %, rreshtat e drejtuar). Render me kod: HTML + Playwright (frame pas frame) → ffmpeg.
  Burimi është te `render/`.
- Remotion / HyperFrames do të funksiononin njësoj (janë po HTML/React → video), por nuk ishin të nevojshëm.

## Formati
- 1080×1920, 24 fps, 9 s, H.264, audio e heshtur (muzika/zëri në montim).

## Pamja (nga referenca D.Franklin)
- Sfond krem #e7e0cf me kokërriza; fatura #2a2a29 me teh të grisur lart, palosje horizontale.
- Teksti krem #ebe4d2.
- Logo CLASS Beauty House (nga PNG 225 px, e kthyer krem) lart, në qendër.
- Titulli BLACK FRIDAY: matricë pikash 5×7 me pika të rrumbullakëta, të vizatuara me canvas.
- Tabela: SHËRBIMI / OFERTA (shqip), font Space Mono.
- Rreshtat (renditja e briefit): Makeup −30%, pastaj 5 shërbimet me −50%.
- Fundi: INSTAGRAM  @class_beauty_house

## Lëvizja
- Fatura ngjitet nga y=1560 në y=96 për 3.0 s (easeOutQuart), me hapa të vegjël si printer
  termik gjatë lëvizjes; pastaj qëndron deri në 9 s.
