# Blender blockout — Blloku A (v1)
Qëllimi: video blockout 9:16 që bëhet `@video1` te Seedance 2.5 (master i kamerës, prerjeve dhe bllokimit).
Pamja (fytyra, veshja, drita) vjen nga referencat, jo nga blockout-i.

## Teknike
- 1 Blender unit = 1 m. 24 fps. 13 s = frame 1–312. Render 1080×1920 (9:16), MP4 H.264.
- Render i thjeshtë (Workbench/EEVEE), ngjyra të sheshta, pa tekstura. Markera në çdo prerje (CUT1…CUT5).
- Një kamerë për shot (ose një kamerë me çelësa të kërcyer në frame-t e prerjes, pa interpolim mes shot-eve).

## Ngjyrat fikse
| Objekt | Ngjyra | Hex |
|---|---|---|
| Sfondi/muret e kabinetit | navy e errët | #0B1626 |
| Dyshemeja e kabinetit | gri e errët | #1E2329 |
| Pajisjet (siluete) | blu-gri | #2C3A4D |
| Figura: përparësja (trupi nga supet te gjunjët) | e bardhë | #F2F2F2 |
| Figura: koka + qafa | bezhë | #C99B7A |
| Figura: këmbët (pantallona) | e zezë | #111111 |
| Telefoni | e zezë me ekran turkez | #0E0E0E / #2EE6D6 emisiv |
| Panelet (të gjitha) | turkez emisiv, 60% opacitet | #2EE6D6 |
| Fijet e dritës | turkez emisiv | #2EE6D6 |
| Dyshemeja digjitale (nga frame 159) | navy shumë e errët, me reflektim | #050B14 |

## Skena
- Figura (njeri 1.80 m: kapsulë trupi + sferë koke, krahë si cilindra) në origjinë (0,0,0), me fytyrën nga −Y (drejt kamerës).
- Krahu i majtë i tij (ana +X) mban telefonin (0.07×0.15×0.01 m) në (0.12, −0.30, 1.25), ekrani i kthyer lart drejt fytyrës.
- Dora e djathtë (ana −X) pranë telefonit në (0.02, −0.32, 1.27), deri në frame 80.
- Kabineti: dysheme 6×6 m; mur mbrapa në y = +3.5; tavolinë ekzaminimi (1.9×0.7×0.75 m) në (1.6, 1.8); monitor në krah (0.5×0.35 m) në (−1.4, 3.3, 1.7); stendë IV (shtyllë 1.8 m) në (−2.0, 2.4); dollap me xham (1.0×0.45×1.9 m) në (0.6, 3.25).

## Animacioni i objekteve
- Frame 1–72: 3 panele të vogla (0.09×0.06 m) ngrihen nga ekrani i telefonit 0 → 0.10 m lart, të ndara 0.12 m nga njëri-tjetri.
- Frame 80–100: dora e djathtë ngjitet te veshi dhe zbret te gjoksi (heq kufjet).
- Frame 100–125: telefoni zbret 0.10 m.
- Frame 165–190: figura bën një hap përpara 0.6 m (y: 0 → −0.6).
- Frame 165–215: pajisjet e kabinetit dhe muret shpërbëhen (shkallë 1 → 0 me grimca të vogla që ngrihen 2 m, ose zhduken me dissolve); dyshemeja kalon në dyshemenë digjitale.
- Frame 175–220: 4 panele (0.60×0.40 m) dalin nga telefoni, rriten dhe vendosen në gjysmërreth me rreze 1.5 m rreth figurës, në lartësi 1.3–1.9 m, në kënde −60°, −20°, +20°, +60° nga boshti përpara.
- Frame 240–300: fije drite (cilindra 0.01 m) lidhin panelet njëri me tjetrin, me radhë.

## Kamerat dhe prerjet
| Shot | Frame | Lente | Kamera | Lëvizja |
|---|---|---|---|---|
| 1 MS | 1–48 | 50 mm | (0.25, −2.4, 1.45) → shikon (0.05, −0.2, 1.25) | dolly-in 0.55 m drejt duarve |
| 2 ECU | 49–72 | 135 mm | (0.10, −1.4, 0.95), poshtë telefonit, shikon ekranin | drift i lehtë 0.05 m |
| 3 MCU | 73–158 | 85 mm | (0, −2.2, 1.65) → shikon kokën (0, 0, 1.62) | pull-back 1.0 m |
| 4 WS | 159–230 | 35 mm | (−0.6, −3.6, 0.6) → shikon (0, −0.3, 1.1) | ndjek hapin, ngritje 0.2 m |
| 5 MS | 231–312 | 50 mm | hark 90° rreth figurës, rreze 2.6 m, nga përpara (−Y) në anën e tij të djathtë (−X), lartësi 1.4 m, shikon (0, −0.6, 1.35) | ~1.2 m/s, vazhdon deri në frame 312 |

Kamera e mbajtur në dorë: zhurmë e lehtë 1–2 cm në çdo shot.
