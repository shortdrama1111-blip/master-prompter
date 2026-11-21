# Indrit Gjuzi, reklama e Krishtlindjeve: gjendja dhe çfarë mbetet

## Gjendja (11/21/2026)
Montazhi final v2, pa zë: `indrit-gjuzi_final_v2_silent.mp4` (18.0 s, 720×1280, prerjet në rrjetën 120 BPM).
Klipet e aprovuara janë te `approved-clips/`:

| Shot | Skedari | Pjesa në montazh | Si u bë |
|---|---|---|---|
| 1 Raftet-ashensor | shot1_shelves_v7.mp4 (v7, aprovuar 11/21) | 0–1.67 s | Animim 2D (`shot1/make_shot1.py`) mbi plate-in bosh + produktet si karta 3D nga Blender (`shot1/blender_cards.py`; mask/cond me Eevee). Versioni i vjetër Seedance: shot1_elevators_right-reversed.mp4 |
| 2 Konvejeri DreamDuo | shot2_conveyor.mp4 | 1.5–4.0 s | Nano Banana start frame + Seedance i2v |
| 3 Girlanda | shot3_garland.mp4 | 1.0–4.0 s | Seedance i2v (10 s) |
| 4 Rënia e dy kutive | shot4_tumble.mp4 | 0–3.75 s | Nano Banana edit + Seedance i2v |
| 5 DreamDuo në qese | shot5_bag_closer_v4.mp4 (v4, aprovuar 11/21) | 0.2–2.95 s | Kuadër më afër (refs/shot5-startframe-closer-v2.jpg). Kutia në Blender/Eevee me teksturë nga foto reale + kompozim me holdout (`shot5/box_blender.py`, `shot5/make_shot5.py`) |
| 6 "Gëzuar Festat xx" | shot6_tag.mp4 | 0–4.0 s | `shot6/make_shot6.py`: shkrim me dorë (Ink Free) mbi etiketën + afrim kamere |

## Feedback-u i klientit që mbetet për t'u zbatuar
1. ~~**Shot 1**~~: ✅ v7 aprovuar (shot1/shot1-v7.mp4). Montazhi final duhet ribërë me këtë klip.
2. ~~**Shot 3**~~: ✅ v7 në Blender me zinxhirë champagne-gold, lëvizja aprovuar (preview); renderi 1080×1920 → shot3/shot3-v7.mp4.
3. ~~**Shot 5**~~: ✅ v4 aprovuar (shot5/shot5-v4.mp4).

3b. **Shot 6**: teksti final "Happy Holidays" (në vend të "Gëzuar Festat xx").

## Pastaj
4. Muzika: ElevenLabs me promptin te `prompts/music-elevenlabs.md` (18 s, 120 BPM). SFX opsionale: rrotullat, whoosh + goditja e kutive, stilolapsi.
5. Montazhi final me muzikë; eksport 720×1280 dhe/ose 1080×1920.
6. Mbyllja sipas `CLAUDE.md`: mësimet → skill-et / `LESSONS.md`, merge në main.

## Mësimet kryesore (për mbylljen)
- Çdo shot nis me start frame (Nano Banana). Video pa imazh fillestar doli keq (Shot 4 v1).
- Drejtimet e lëvizjes lidhen me objektet/buzët e kuadrit, jo me "left/right" të përgjithshme, dhe çdo objekt që lëviz ka rreshtin e vet.
- Objektet që fshihen pas një tjetri (kthesat e spirales) zhduken → kuadri pritet që të mos ketë fshehje.
- "eases out" e ngadalëson dhe e ndal gjithë lëvizjen → "constant speed through the final frame".
- Rëniet me fizikë të saktë → Blender mbi plate statike, jo Seedance.
- Çdo objekt i një close-up-i duhet të duket që në shot-in e mëparshëm (etiketa te Shot 5).
- Seedance v2v nuk shton dot objekte të vogla mbi pjesë që lëvizin.
- Muzika e referencës (OUAI) ka licencë dhe nuk përdoret.
