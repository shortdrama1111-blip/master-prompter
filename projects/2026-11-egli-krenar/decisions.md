# Vendimet e ngulitura

## Rruga e punës
- **Manuale** (2026-11-14): përdoruesi gjeneron, Claude dorëzon paketën e plotë në një mesazh
  (referencat e prera, rendi i ngarkimit, prompti).

## Personazhi: Krenar
- Fytyra, flokët, mjekra: si në fotot `references/IMG_88*.jpg` (konfirmuar).
- Veshja (konfirmuar 2026-11-15): triko blu e errët me qafë gjysmë të lartë, përparëse e bardhë
  doktori sipër, stetoskop i zi në qafë, pantallona të zeza, orë e zezë.
- Shtesë (2026-11-15): kartë identifikimi e bardhë në xhepin e gjoksit (ana e majtë e tij) me ikonë
  turkeze zemër-puls, pa shkrim (emri, nëse duhet, në montim).
- Ora: **dora e majtë**, byzylyk i hollë i artë në të djathtën (standard nga sheet-i v2, zëvendëson v1).
- Character sheet: paneli i pasmë ndërtohet nga Claude (mungon foto nga mbrapa; pamja nga pas
  pothuajse s'shihet në film).

## Koncepti
- Scripti mbetet baza. Shtesë: Krenari si "doktori i Meta-s": dëgjon telefonin/panelet me
  stetoskop (humor + paralelizëm). `ref-doctor-instagram.jpg` = referencë për gjestin, jo për ngjyrat.

## Stili
- Sipas scriptit: blu e errët, dritë e bardhë, theks turkez. Plate-t gjenerohen nga e para.

## Stetoskopi (konfirmuar)
- 01: stetoskopi mbi ekranin e telefonit → ngre sytë te kamera (hook).
- 03: stetoskopi mbi panelin e sigurisë, "kontroll", pastaj panel tjetër.
- 06: stetoskopi në qafë, tregon butonin = "diagnoza".

## Zëri dhe lip-sync
- Zëri dizajnohet në ElevenLabs (Voice Design), jo klon. Audio gjenerohet e para, për çdo skenë veç. Lip-sync shqip, "perfect". Hibrid: disa momente voice-over,
  pjesa tjetër lip-sync në kamerë.

## Audiot (Higgsfield media)
| Linja | Skedari | Media ID | Gjatësia |
|---|---|---|---|
| 01 | `audio/krenar-audio-1.mp3` (eleven_v4) | `ac6eb12d-4399-4000-bd4e-c5b5f1703633` | 4.52 s |
| 02 | `audio/krenar-audio-2.mp3` (eleven_v4) | `e0773c4e-4692-4bc6-bbfe-c3e09f905657` | 7.39 s |

Blloku A me audiot reale: 3.0 s pa fjalë + 4.5 s (01) + 0.3 s pauzë + 7.4 s (02) ≈ **15.5 s → gjenerim 16 s** (brief-i v1 ishte 13 s, përditësohet pas blockout-it v1).

## Finali
- Kuadri final qëndron i ngrirë 2 s, sipas scriptit (kërkesa e klientit ka përparësi; shih feedback.md).

## Blloku i dritës (fjalë për fjalë në çdo prompt), v2 sipas `look-ref-v1-user.jpg`
```
Lighting: one large soft cool-white key light at 5600K from the front, slightly above eye level and a little to the left, giving low-contrast, even light on his face and the white lab coat. The floating holographic panels glow turquoise and add a cyan edge light on his cheeks, beard and hands. The room behind him falls off into deep navy-blue darkness at 8% brightness, with medical equipment readable only as dark silhouettes. Blacks hold a deep navy tint, fine natural film grain, a soft halo around every glowing panel.
```
Status: në përdorim (përdoruesi vazhdoi pa kundërshtim, 2026-11-15).

## Ngjyra: 60:30:10, aksenti i rezervuar
- 60% navy e errët (sfondi, hijet) · 30% e bardhë (përparësja, drita kryesore) · 10% turkez = vetëm panelet.

## Elementet / referencat
| Tag | Çfarë është | Shënime |
|---|---|---|
| @krenar-doctor-v2 (aktiv) | `references/krenar-sheet-v2.jpg` · Higgsfield Element `7c3598f0-6cd0-4035-8ad8-e89eb3ca3561` | Sheet v2 me badge, nga fotot reale, fytyra e qendrës e mbuluar |
| kabineti (aktiv) | `references/kabinet-v3-user.jpg` | Ambienti i bllokut A, si @image1 (jo keyframe) |
| @krenar v1 (i vjetër) | `references/krenar-sheet-v1.jpg` | Sheet me 3 panele, fytyra e qendrës e mbuluar. Ora në dorën e djathtë: kjo është standardi tani |

## Konflikte të zgjidhura për këtë projekt (shih CLAUDE.md)
Përdoruesi: "të njëjtën ndjekim, e provojmë". I njëjti drejtim si te 2026-11-egli-SINDI-CAR:
- Video → `seedance-clean`: vetëm pohore, pa emra pajisjesh/filmi, take të gjata/extend.
- Imazhe → gjuhë fotografike pohore, pa bllok NEGATIVE.
Ky është projekti i dytë i provës për konfliktin.

## Kamera
- Dinamike: kënde qartë të ndryshme brenda çdo blloku, prerje mbi lëvizje, asnjë kuadër statik (përveç freeze-it final të kërkuar).

## Rruga e videos (2026-11-15)
- Reference-to-video në Seedance: @krenar v2 + plate i kabinetit bosh. Seedance zgjedh këndet brenda drejtimit të promptit. Pa kuadër fillestar.
