# Vendimet e ngulitura

## Bota
- **Sfondi (2026-11-19, ndryshuar me kërkesë të klientit): mocha / dark taupe** për gjithë videon.
  Rafte minimaliste champagne, pjesa e brendshme e rafteve më e errët, LED të ngrohta 3200K, dritë e
  butë përpara që etiketat të lexohen, kontrast i qartë shishe krem / sfond kafe. E kuqja mbetet
  aksent te çanta dhe fjongot. Gjithçka rigjenerohet.
  - (i zëvendësuar) B, pjeshkë e ngrohtë, 2026-11-19.
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
  - **2026-11-19, mocha: të 6 shot-et ribëhen.** Shot 1 renderohet krejt në Blender me etiketa reale
    nga fotot (modeli s'riprodhon tekst). Shot-et 2–6: Seedance veç e veç, 4s secili, me
    `previz/solo/` dhe `prompts/v4_mocha_s2_s6.md`.
  - **Etiketat dhe logoja:** lexueshmëria vjen nga foto reale (Blender ose montim), plus packshot në fund.

- **2026-11-19, mbrëmje: shot-et 1–4 në Blender** me etiketa reale nga fotot (`blender/shot1..4_final.py`,
  montimi `renders/cut_s1-s4_v1.mp4`, 10.4s). **Shot-et 5–6: Seedance 2.5 extend** mbi këtë montim
  ("më e thjeshtë", përdoruesi), `prompts/v5_extend_s5_s6.md`. Rezervë: shot 5 në Blender (`shot5_final.py`, testi gati).

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
**v4 (2026-11-19, "lock what you got"):** i rishkruar sipas render-ave të aprovuar të Blender-it
(shot-et 1–4): mocha e butë, kapakë të bardhë, paketim në ngjyrën e vërtetë të printit, LED 3200K,
dritë e përparme neutrale. Zëvendëson v3.
```
Warm luxury studio light: slim 3200K LED strips glow warm gold along the edges of the set and wash softly down over the products; one large soft neutral-white front key from camera-left at 30° height evenly lights every product face so each label reads crisp; soft mocha-brown walls take a gentle warm spill and fall off into deeper brown shadow; champagne metal edges catch thin bright highlights. White caps read pure white and the peach and cream packaging keeps its true printed colour, standing out clearly against the soft mocha.
```
(i zëvendësuar) v3 mocha (2026-11-19, klienti). Zëvendëson v2 pjeshkë 4000K.
```
Warm luxury studio light at 3200K: slim warm LED strips hidden along the top inside edge of every shelf, opening and ledge wash softly down over the products; one large soft front key from camera-left at 30° height evenly lights every product face so each label reads crisp; mocha walls and the darker shelf interiors receive only gentle spill and fall off into deep warm shadow; champagne metal edges catch thin bright highlights. Cream bottles and white caps glow just below clipping, standing out clearly against the dark taupe.
```

## Ngjyra: 60:25:5:10, aksenti i rezervuar
- 60 mocha / dark taupe (sfondi, brendësia e rafteve) · 25 krem-bardhë (produktet, kutitë) · 5 champagne metalik (raftet, bordurat) · 10 e kuqe e çantës dhe fjongove (aksent i rezervuar)
- Kontrasti: produktet krem janë pjesa më e ndritshme e çdo kuadri; sfondi mbetet i errët.
- (i zëvendësuar) 60 pjeshkë / 25 krem / 5 ar / 10 e kuqe.

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
