# Log i gjenerimeve

| Data | Shot | Modeli | Rezultati | Problemi | Shkaku | Veprimi |
|---|---|---|---|---|---|---|
| 2026-11-14 | analiza | ffmpeg | 4 look-e, 3 ndërrime wipe; frame-t 3.5/7.5/11.0/14.0s nxjerrë te `frames/` | — | — | pret konfirmimin e përdoruesit |
| 2026-11-14 | v2 take1 | Genjutsu (manual), prompt 04 v4 | `results/genjutsu-v2-take1.mp4`: lëvizja, 3 wipe-t, koha, drita ✓; teksti u hoq ✓; 4 veshjet në rendin e duhur ✓; mansheta me gur të zi duket te kyçi i majtë në 9.5s ✓ | (1) e zeza humbet në sfondin e natës; (2) fytyra në fund më e rrumbullakët/më e re se ref-et, buzëqeshja e thekson; (3) mansheta e djathtë del e thjeshtë | (1) zgjedhja e look-ut D, jo rresht i promptit; (2) ref-et e trupit me fytyrë ~140px, pa close-up si ref | v5 (blu në fund) + v6 (@Image6 close-up fytyre) |
| 2026-11-16 | v3 final | montazh (ffmpeg) | `results/egli-ashensor-final-v1-1080p.mp4`: upscale 1080p i përdoruesit + zë origjinal + grafika Monday–Thursday (Oranienbaum, e verdhë me kontur) | — | — | dorëzim te klienti; Seedance nga zero (07) mbetet opsion për realizëm |
| 2026-11-16 | sheet bazë v1 | image (manual, prompt 10 hapi 1) | `refs/v3/sheet-base-v1.jpg`; QC: sytë, vetullat, hunda, buzët, balluket përputhen me ref (~95%) | — | — | maskuar → `upload/10-sheet/sheet-base-masked.jpg` |
| 2026-11-16 | sheet bazë v2 | image (manual, prompt 10 hapi 1) | `refs/v3/sheet-base-v2.jpg`; QC: përputhje e fortë me ref, sfond më i çelët | — | — | maskuar → `upload/10-sheet/sheet-base-v2-masked.jpg` |
