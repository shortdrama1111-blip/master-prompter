# Log i gjenerimeve

| Data | Shot | Modeli | Rezultati | Problemi | Shkaku | Veprimi |
|---|---|---|---|---|---|---|
| 2026-11-14 | analiza | ffmpeg | 4 look-e, 3 ndërrime wipe; frame-t 3.5/7.5/11.0/14.0s nxjerrë te `frames/` | — | — | pret konfirmimin e përdoruesit |
| 2026-11-14 | v2 take1 | Genjutsu (manual), prompt 04 v4 | `results/genjutsu-v2-take1.mp4`: lëvizja, 3 wipe-t, koha, drita ✓; teksti u hoq ✓; 4 veshjet në rendin e duhur ✓; mansheta me gur të zi duket te kyçi i majtë në 9.5s ✓ | (1) e zeza humbet në sfondin e natës; (2) fytyra në fund më e rrumbullakët/më e re se ref-et, buzëqeshja e thekson; (3) mansheta e djathtë del e thjeshtë | (1) zgjedhja e look-ut D, jo rresht i promptit; (2) ref-et e trupit me fytyrë ~140px, pa close-up si ref | v5 (blu në fund) + v6 (@Image6 close-up fytyre) |
| 2026-11-16 | v3 final | montazh (ffmpeg) | `results/egli-ashensor-final-v1-1080p.mp4`: upscale 1080p i përdoruesit + zë origjinal + grafika Monday–Thursday (Oranienbaum, e verdhë me kontur) | — | — | dorëzim te klienti; Seedance nga zero (07) mbetet opsion për realizëm |
| 2026-11-16 | sheet bazë v1 | image (manual, prompt 10 hapi 1) | `refs/v3/sheet-base-v1.jpg`; QC: sytë, vetullat, hunda, buzët, balluket përputhen me ref (~95%) | — | — | maskuar → `upload/10-sheet/sheet-base-masked.jpg` |
| 2026-11-16 | sheet bazë v2 | image (manual, prompt 10 hapi 1) | `refs/v3/sheet-base-v2.jpg`; QC: përputhje e fortë me ref, sfond më i çelët | — | — | maskuar → `upload/10-sheet/sheet-base-v2-masked.jpg` |
| 2026-11-16 | v3 nga zero take1 | Seedance 2.5 (manual), prompt 08 v3 | `results/seedance-08v3-take1.mp4`: figura, fytyra, veshjet, realizmi më mirë se Genjutsu (përdoruesi) | kamera statike frontale pa push-in; prerjet te 3.9/7.25/9.6s | pa video ref, Seedance zgjodhi vetë kamerën | v4: @video1 si ref kamere |
| 2026-11-16 | v3 nga zero take2 | Seedance 2.5, prompt 08 v4 (+@video1 kamerë) | `results/seedance-08v4-take1.mp4`: kamera dhe prerjet si te videoja 1 ✓ | pamja "AI", lëkurë e lëmuar si te Genjutsu | @video1 (rezultat Genjutsu) kaloi edhe pamjen, jo vetëm kamerën | v5 vetëm me prompt + propozim Blender grey-box si ref kamere |
| 2026-11-16 | v3 nga zero take3 | Seedance 2.5, prompt 08 v5 (kamera me fjalë, pa video) | `results/seedance-08v5-take1.mp4` — përdoruesi: "duket shumë më mirë"; prerjet te 4.04/6.79/9.13s | — | — | montazh: `results/egli-ashensor-final-v2-seedance.mp4` (kënga origjinale nga 0s + grafika Monday–Thursday) |
| 2026-11-17 | final v3 | montazh | `results/egli-ashensor-final-v3-script.mp4`: Pinyon Script e bardhë, me hije | — | — | dorëzuar |
| 2026-11-17 | final v4 | montazh | `results/egli-ashensor-final-v4-shein.mp4`: titull "SHEIN / 4 perfect / Autumn / looks 🍂" (Inter Display + Great Vibes, krem), 0.1–2.1s lart, pa ditë | — | — | dorëzuar |
| 2026-11-19 | sheet v4 (3 panele, profil) | image (manual, prompt 13) | `refs/v3/sheet-v4-3panel.jpg`: përpara ✓, profil me hapësirë para fytyrës ✓, topuzi dhe balluket ✓ | sfondi i profilit pak më i çelët; paneli i trupit më i ngushtë | — | maskuar → `upload/12-sheet/sheet-v4-3panel-masked.jpg` |

## 2026-11-19 — Outfit 3 me lëvizjen e references në montim (pa gjenerim të ri)
- `edit/zoomcut_v1.py` → `results/outfit3-zoomcut-v1.mp4` (4.25s): face A 11.80 bounce in/out (0.21s) → portik B 14.75 crash zoom out 2.43→1.0 + roll -5°→0 (0.30s) → detaj menge me dantella B 15.10 zoom 2.9→2.5 (0.25s) → portik wide ease-out 1.35→1.0 + roll -3°→0 (1.0s) → ura B 16.45 1.05→1.0 (2.5s). Motion blur 8 nën-frame.
- `results/firenze-v6-montage-v3.mp4` = montage v2 0–13.75 + outfit3-zoomcut-v1 (18.0s).

## 2026-11-19 — Seedance prompt 27 (veshjet 2+3, 16 s, pa video ref)
- `results/seedance-27-outfit2-3-take1.mp4`: prerjet 1.83 3.33 4.67 6.38 7.88 9.67 11.17 12.71 14.29. Fytyra dhe veshjet shumë mirë.
- Defekt: 11.17–12.71 (3/4 te kolonat) njëra këmbë e xhinseve portokalli + bluza kafe. Shkaku i mundshëm: rreshti "the warm stripes of light from between the columns sliding across her black knit". Hiqet në montim.
- Defekt i vogël: te vitrina (6.4–7.9) kapëse e zezë në vend të topuzit.
- `edit/zoomcut_v3_take27.py` → `results/outfit2-3-zoomcut-v3.mp4` (12.67 s).

## 2026-11-19 — Montage v4 (struktura e klientit)
- Përdoruesi: ngjyrat mbeten (klientit i pëlqejnë); problem vetëm kalimet (zoom-blur, split-screen) dhe veshja 2 që s'dukej.
- `edit/montage_v4.py` → `results/firenze-v7-montage-v4.mp4` (21.5 s): veshja 1 = montage v2 0–8.11; veshja 2 = take 27 (7.6 s: wide, çizmet, 3/4, mesatar, vitrina); veshja 3 = take 27 portiku (wide, xhinset, menga, kolona). Kalimet e veshjeve: crash zoom out 0.3 s. Kohë reale kudo tjetër, pa ndryshim ngjyrash.

## 2026-11-19 — Take 31 (poza, 16 s) + montage v6
- `results/seedance-31-poses-take1.mp4`: 6 poza të pastra. Veshja 2: te muri 0.2–2.3, përballë 3.3–6.4, përkulur 7.3–8.15. Veshja 3: te kolona 8.3–9.6, krahu lart 11.9–12.9, ulur 14.6–16.0. Prerja te 8.21.
- `edit/montage_v6.py` → `results/firenze-v8-montage-v6.mp4` (18.8 s): trick-u i references mbi pozat (bounce afër → crash zoom out → close → i plotë).

## 2026-11-19 — Take 32 (lëvizje reale) + montage v7 (speed ramp)
- `results/seedance-32-realmoves-take1.mp4`: kamera tërhiqet/afrohet vërtet, pozat ndryshojnë gjatë lëvizjes. Prerja te 8.375. Veshja 2: close 0–2.4, tërheqje 2.4–4.0, wide 4.0–6.2, afrim poshtë 6.2–7.6, përkulur 7.6–8.37. Veshja 3: close me mëngën te nofulla 8.4–10.3, tërheqje 10.3–11.8, te kolona 11.8–13.6, afrim + ulur 13.6–15.3, ulur 15.3–16.
- `edit/montage_v7.py` → `results/firenze-v9-montage-v7.mp4` (21.8 s): pa crop/zoom digital; speed ramp 1×→6× në lëvizje me mesatare frame-sh (shutter 180°).

## 2026-11-19 — Montage v9 + take 33
- `results/firenze-v11-montage-v9.mp4` (12.8 s): ritmi i references mbi take 32 (pozat ~0.25 s, prerje mbi lëvizje, P32 i interpoluar në 72 fps).
- `results/seedance-33-continuous-take1.mp4`: kapësja e çantës 0–1.2, ngjitja te fytyra 1.2–2.75, ulet 2.75–3.75, WIPE nga shtylla 3.75–4.25, ulur në shkallë 4.25–7.9, WIPE nga kolona 8.0–9.1, shpina + shikim mbi sup me dantellën te kolona 9.25–11.25, te kolona 11.5–12.75, ulur 13–16.
- `edit/montage_v10.py` → `results/firenze-v12-montage-v10.mp4` (15.75 s): veshja 1 (v2) → çanta + ngjitja te fytyra (33) → ramp-et e 32 → ulur në shkallë (33) → WIPE me kolonën (33) → shpina/dantella (33) → menga (27) → ramp-et e 32 deri te ulur.
- `edit/montage_v11_client_v1.py` → `results/CLIENT-V1-firenze.mp4` (15.7 s): si v10, por veshja 3 pas wipe-it pa speed ramp: shpina/dantella (33 9.4–10.9) → menga (27 12.85–14.2) → te kolona (27 14.35–16.0).
- `results/CLIENT-V2-reel-origjinal-kalimet-fix.mp4` (16.75 s): video e parë (sheet-v3-test-video) me hequr vetëm zoom-blur (4.62–4.79) dhe split-screen + flash (6.38–6.92). Përdoruesi: V2 më vonë, pasi të mbyllim V1.

## 2026-11-19 — Take 34 (veshja 3) + CLIENT-V1 i ri
- `results/seedance-34-outfit3-take1.mp4` (10 s): rrotullim 0–3.5, beli/xhepi 3.5–5.0, menga 5.0–6.29, clogs 6.29–8.0, te kolona 8.0–10.05.
- `results/CLIENT-V1-firenze.mp4` (19.6 s): veshja 2 me rripin e rikthyer; veshja 3 = wipe me kolonën (33) → 5 shot-et e take 34. Profili i pallto-s te veshja 1 (~1.8 s) pret prompt 35.
