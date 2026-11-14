# Vendimet e ngulitura: gta VI

## Historia
Skenari v2 "Ata më sollën deri këtu", 60 s, **9:16** (vendim i regjisorit, përdoruesi: "zgjidh ti"). Plate-t e lokacioneve 16:9 si referenca. Shih `script.md`.

## Ndarja në skena (blloqe gjenerimi)
| Skena | Koha | Gjatësia | Përmbajtja |
|---|---|---|---|
| 1 | 0:00–0:10.5 | 10.5 s | Hook + Miami '86 (Egli 10 v.) |
| 2 | 0:10.5–0:20 | 9.5 s | LA '92 (Egli 15 v.) |
| 3 | 0:20–0:30 | 10 s | LA sot (Egli 22 v.) |
| 4 | 0:30–0:40 | 10 s | Florida VI, kurthi (Egli sot) |
| 5 | 0:40–0:50 | 10 s | Shpëtimi + sakrifica (frame-first) |
| 6 | 0:50–1:00 | 10 s | Ndarja në agim + aerial |
Çdo skenë = një epokë = një bllok drite. Errësirat (tuneli, prozhektori) janë pikat e bashkimit.

## Armët
Version A me armë (heronjtë mbajnë armë, pa qitje drejt njerëzve) → nëse modeli e bllokon/shtrembëron, version B pa armë.

## Blloqet e dritës (fjalë për fjalë në çdo prompt të epokës)
**'86:** `LIGHTING: Night, 1986. Magenta neon from the hotel facades on the left, cyan neon from the beach-side signs on the right at 8000K, warm 3200K sodium streetlamps every 25 m along the median. The asphalt is wet after rain and mirrors every light source in long vertical streaks. Deep navy sky, rich blacks, fine film grain.`

**'92:** `LIGHTING: Late golden hour, 1992. The sun sits 4° above the horizon at the far end of the street, 3200K, throwing shadows ten times longer than the objects that cast them. Warm smog haze at 30% density, palms and power lines in silhouette against an orange-to-peach sky, a soft horizontal lens flare, shadows lifted to warm brown.`

**Sot (v2, PCH):** `LIGHTING: Midday, present day. Hard sun high overhead at 5600K from camera right, short crisp shadows under every rock, post and palm, bleached sandstone cliff, heat shimmer rising from the asphalt over the first 30 m, deep clean blue sky with a few white clouds, high contrast, clean modern digital look.`

**VI (v2, ura mbi gji):** `LIGHTING: Night, present day. Purple-magenta and teal LED light from the city skyline across the bay, reflected in the water in long trembling streaks; cool white 6500K LED streetlights along the bridge every 30 m; humid air with low mist at 20% density hugging the water around the mangrove islands; deep violet-black sky; crisp modern digital look.`

**Agimi (v2):** `LIGHTING: First light, present day. The sun sits on the horizon just to the right of the skyline, 3500K gold on every surface that faces it, shadows cool blue 7000K, the streetlights switched off, the mist over the water at 40% density glowing gold, the sky graded from gold at the horizon to pale blue overhead.`
(Drejtimi "left/right" ndryshon sipas kuadrit në promptet e videos; temperaturat, dendësitë dhe paleta mbeten fjalë për fjalë.)

## Elementet / referencat
| Tag | Çfarë është | Statusi |
|---|---|---|
| `refs/egli-sheet-masked.png` | sheet-i origjinal i Eglit, fytyrat e vogla të mbuluara (katror 241,238,235) | ✅ |
| `@egli_kid` | `refs/egli_kid-sheet-masked.png` | ✅ v1 |
| `@egli_teen` | `refs/egli_teen-sheet-masked.png` | ✅ v1 |
| `@egli_young` | `refs/egli_young-sheet-masked.png` | ✅ v1 (mjekra e plotë pranohet nga përdoruesi) |
| `@egli_now` | `refs/egli_now-sheet-masked.png` | ✅ v1 |
| CJ · Tommy · Lucia · Michael · Jason | `refs/<emri>-sheet-masked.png` | ✅ v1 |
| Franklin · Trevor | `refs/<emri>-sheet-masked.png` | ✅ v1 |
| car_86 · truck_trevor · car_vi · car_now · airboat | `refs/<emri>-sheet.jpg` | ✅ v1 |
| car_92 (lowrider 2 dyer) · car_michael · bike_franklin · dice_keys | te përdoruesi (s'janë në repo) | ✅ v1 |
| lokacionet ×5, mjetet ×6, çelësi me zar | | në pritje |

## Konflikte të zgjidhura për këtë projekt (shih CLAUDE.md)
Propozim (si te SINDI-CAR, pret konfirmim): video → `seedance-clean` (vetëm pohore, pa emra pajisjesh,
blloqe ~10 s); imazhe → gjuhë fotografike pohore, pa bllok NEGATIVE.

## Kush është kush (në bisedë me emra, në prompte vetëm tag-et)
| Tag në prompt | Në bisedë |
|---|---|
| `@hero_86` | Tommy (Vice City) |
| `@hero_92` | CJ (San Andreas) |
| `@hero_v_suit` | Michael (GTA V) |
| `@hero_v_young` | Franklin (GTA V) |
| `@hero_v_wild` | Trevor (GTA V) |
| `@duo_vi_her` | Lucia (GTA VI) |
| `@duo_vi_him` | Jason (GTA VI) |

## Lokacioni GTA V (v2)
Pacific Coast Highway te California Incline (Santa Monica) → autostrada. Zëvendëson rrugën malore. Plate-t me foto reference.

## Lokacioni GTA VI (v2)
Ura me hark mbi gji me ishuj mangrove, qyteti në horizont (sipas trailerit; analog real Rickenbacker Causeway). Zëvendëson kënetën. Plate: aerial natën, mbi urë natën, aerial në agim (edit).
Vice City dhe San Andreas: plate-t gati te përdoruesi.
