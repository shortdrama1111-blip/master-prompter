# Vendimet e ngulitura

## Bota
- **Sfondi (2026-11-19): B, pjeshkë e ngrohtë.** E kuqja e çantës është aksent, vetëm te fjongot
  dhe te shot-i i fundit. Butësia e referencës mbetet, kurse rozëja-kadife e OUAI zëvendësohet.
- **Blender (2026-11-19): blockout i thjeshtë.** Forma, kamera, lëvizja dhe materiale bazë.
  Pamjen finale e jep modeli AI.

- **Gjatësia (2026-11-19): A, rreth 16s, 6 shot-e**, me ritmin e referencës.
- **Modeli (2026-11-19): Seedance 2.5 me video referencë** (videoja e Blender-it për lëvizjen,
  fotot e produkteve për pamjen).
  - 2026-11-19: fillimisht 5A, një gjenerim për shot.
  - **2026-11-19, ndryshuar: provë me 1 prompt për gjithë videon** (`previz/previz_v2_full.mp4` si
    @video1). Nëse dështon, kthehemi te 6 gjenerime me `previz/s1..s6.mp4`.
  - **2026-11-19, pas v2: hibrid.** Shot-et 2, 4, 5 nga gjenerimi v2 (i pëlqyer). Shot-et 1, 3, 6
    rigjenerohen veç e veç (4s secili, `previz/solo/`, `prompts/v3_solo_s1_s3_s6.md`), sepse 1 prompt
    nuk i mbajti kohët e prerjeve në dy prova.
  - Shot 3: stolirat varen me fjongo të kuqe satin, që aksenti i kuq të shfaqet në mes të videos.

## Harta e shot-eve (2026-11-19, e pranuar)
| # | Shot-i | Produkti |
|---|---|---|
| 1 | Raft me kuti të ndriçuara; kolonat si ashensor (mesi lart, anët poshtë), kamera e fiksuar | Peptide Mask, Leave-In Conditioner, Hair Oil |
| 2 | Rripa transportues spiralë | Kutia DreamDuo |
| 3 | Stolira-kuti të varura nga tub i lakuar | Kuti të vogla bezhë (si kutia e vajit) |
| 4 | Rrip diagonal | Hair Oil + DreamDuo |
| 5 | Pirg dhuratash | Kuti dhuratash + çanta e kuqe |
| 6 | Close-up çanta me kartë | Çanta e kuqe; teksti i kartës në montim |

## Blloku i dritës (fjalë për fjalë në çdo prompt)
v2 (2026-11-19). Te v1 drita doli e sheshtë, prandaj u shtuan rim light dhe bloom.
```
Soft warm studio light: one large diffused key from camera-left at 45° height, 4000K, wrapping gently around bottles and boxes with soft contact shadows; a warm 3500K rim from behind camera-right outlines every product edge with a thin glowing line; warm peach bounce fill from the set at 30% of the key; the shelf cubbies glow evenly from behind at 3500K with a gentle bloom. White caps and the cream tag sit just below clipping, glass and gold catch one long soft highlight.
```

## Ngjyra: 60:25:5:10, aksenti i rezervuar
- 60 pjeshkë (seti) · 25 krem-bezhë (produktet, rripat) · 5 ar i butë metalik (bordura, fije) · 10 e kuqe e çantës (aksent i rezervuar)
- v2: u shtua ari, sepse te v1 produktet bezhë humbnin mbi sfondin pjeshkë.

## Elementet / referencat
| Tag | Çfarë është | Shënime |
|---|---|---|
| — | `refs/peptide-mask.jpg` | |
| — | `refs/leave-in-conditioner.jpg` | |
| — | `refs/hair-oil-with-box.jpg` | |
| — | `refs/dreamduo-box.jpg` | |
| — | `refs/holiday-bag-red.jpg` | aksenti i kuq |

## Konflikte të zgjidhura për këtë projekt (shih CLAUDE.md)
Modeli është Seedance 2.5, ndaj ndiqet `seedance-clean` (2026-11-19):
- Emra pajisjesh/filmi: asnjëherë.
- Bllok NEGATIVE: jo, vetëm pohore.
- Stili: i shpërndarë, jo në krye.
- Gjatësia e shot-it: një shot i referencës për çdo gjenerim (rreth 2–4s).
- Kamera: e motivuar, ndjek lëvizjen e Blender-it.
