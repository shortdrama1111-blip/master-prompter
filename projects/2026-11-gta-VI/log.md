# Log i gjenerimeve

| Data | Shot | Modeli | Rezultati | Problemi | Shkaku | Veprimi |
|---|---|---|---|---|---|---|
| 2026-11-14 | Sheet `@egli_kid` | model imazhi (përdoruesi) | ✅ | — | — | katror mbi fytyrën e qendrës |
| 2026-11-14 | Sheet `@egli_teen` | " | ✅ | kapela te paneli i shpinës duket me strehë përpara | — | pranohet |
| 2026-11-14 | Sheet `@egli_young` | " | ⚠️ | mjekër e plotë si te "tani", jo stubble 3-ditore; 22 dhe "tani" duken pothuajse njësoj | modeli ndoqi fort fytyrën e @image1 | propozim: edit "Change ONE thing: stubble" |
| 2026-11-14 | Sheet `@egli_now` | " | ✅ | — | — | — |
| 2026-11-14 | Sheet CJ, Tommy, Lucia, Michael, Jason | model imazhi (përdoruesi), me referencë fytyre | ✅ | — | — | katror mbi fytyrën e qendrës |
| 2026-11-14 | Sheet Franklin, Trevor | model imazhi, me referencë fytyre | ✅ | Trevor: tekst në qafë | detaj nga referenca | pranohet; në video mund të dalë i shtrembër |
| 2026-11-14 | Sheet car_86, truck_trevor, car_vi, car_now, airboat | model imazhi (përdoruesi) | ✅ | car_86 dhe car_vi kanë emblema të vogla marke (kali te kapaku, kali te grila) | modeli i shtoi nga forma e njohur | pranohen; në video mund të shfaqen; hiqen në montim nëse duken |
| 2026-11-14 | Sheet bike_franklin, dice_keys, car_92, car_michael | model imazhi (përdoruesi) | ✅ | lowrider-i doli 2 dyer (prompti: 4 dyer), sheet 4 panele | — | lock what you got. Imazhet s'u ruajtën në disk (vetëm në bisedë): skedarët te përdoruesi |
| 2026-11-14 | Plate loc_86 | model imazhi (tekst) | ✅ "spektakël" | tabela "HOTEL" të lexueshme | — | pranohet; në video mund të shtrembërohen |
| 2026-11-14 | Plate loc_92 | me foto ref | ✅ | makina të viteve '90 të parkuara | — | pranohen si dekor i epokës |
| 2026-11-14 | Plate loc_now_pch, loc_now_freeway | me foto ref | ✅ | — | — | tabelat bosh |
| 2026-11-14 | Plate loc_vi_aerial, loc_vi_deck, loc_dawn_deck | me foto ref + edit | ✅ | agimi u bë mbi kuvertën, jo aerial | — | aerial-i i agimit opsional (edit i loc_vi_aerial) |
| 2026-11-14 | Skena 1 v1 | Seedance 2.5 | 👎 | pa hook, pa histori | prompti: shot 1 pa ngjarje; lock "police far behind"; shot 3 statik | v2: hook me ngjarje në 0.0 s, ndjekje me konflikt, 7 prerje |
| 2026-11-14 | Skena 1 v3 | Seedance 2.5, 20 s | ⚠️ 60% | kupeja → makinë policie; brenda policisë duket mbrapsht; zari pa çelës; policia përpara në pasqyrë; drone me pozicione të tjera; prekje pa reagim | shih feedback | mbahen shot 1, 2, 8; rigjenerohet mesi (shot 3–7) si një bllok 11 s |
| 2026-11-14 | Skena 1 me blockout | Seedance 2.5 + @video1 blockout, 20 s | ✅ 90% | shot 2 (2.75–6.3 s) pa fëmijën; 18.4–20 s e zezë | rrahja e shot-it 2 pa pozicion kamere/plan të parë | patch 4 s për shot 2; e zeza e fundit pritet në montim |
| 2026-11-14 | Skena 1 final (blockout v2) | Seedance 2.5 + @video1 | ✅ aprovuar | drone nga lart pak jo-realist | — | mbulim në montim me grafikë wanted level |
| 2026-11-14 | Skena 3 (blockout v2) | Seedance 2.5 + @video1, 12 s | ⚠️ 50% | shih feedback: shot 4–8 | POV pa trup/automjet; "live stream of a bridge at night" → natë | patch-et A–E (4 s secili) |
| 2026-11-14 | Skena 4 (blockout v2) | Seedance 2.5 + @video1, 12 s | ✅ aprovuar | kabrioleti i errët në kurth; zari fuzzy | — | ngjyrim në montim |
| 2026-11-14 | Skena 3 patch A (Franklin) | Seedance 2.5, single-shot 4 s, pa blockout | ✅ | — | rreshti "his own forearms … gloved hands gripping both handlebar grips" + POSITIVE LOCK e zgjidhën motorin pa duar | në montim: ~1.9–3.7 s (afrimi + kalimi mes policëve) |
| 2026-11-14 | Skena 3 patch B (Trevor) | Seedance 2.5, 4 s | ✅ | arushi dhe Trevor nuk duken (vetëm parafango e kuqe) | kamera anash te qoshja e përparme mbulon push bar-in | goditja + rrotullimi lexohen shumë mirë; mbahet ~0.8–3.6 s |
| 2026-11-14 | Skena 3 patch C (konvoji) | Seedance 2.5, 4 s | 👎 | profil anash, xhami anësor, konvoji s'lexohet; flokët e Eglit dalin keq | modeli preferon fytyrën kur ka sheet personazhi + "driver turns his head" | C2: kamera te parakolpi i pasmë i kupesë, pa Eglin |
| 2026-11-14 | Skena 3 patch D (billbordet) | Seedance 2.5, 4 s | ✅ | billbordet si portale sipër rrugës, jo anash | — | dita ✓, ura brenda ekranit ✓, mbush kuadrin ✓ |
| 2026-11-14 | Montimi skena 3 v1 | ffmpeg: origjinali 0–5.958 + A 1.9–3.7 + B 0.8–3.6 + D 0–4.064 = 14.7 s | — | konvoji (C) mungon | përdoruesi s'do të rigjenerojë | HUD i ri `edit/hud_v.py` (radar drejtkëndësh që pulson kuq/blu, 5 yje të bardhë 2→3→4, paratë jeshile, shiritat), titulli LOS ANGELES 2013, riser drejt ekranit; render 70 s me preset fast |
| 2026-11-14 | Montimi skena 4 v1 + bashkimi 3→4 | ffmpeg | — | kabrioleti mbetet i errët te kurthi | ngjyrim selektiv s'u bë (rrezik për policinë/dritat) | `scenes_3-4_v1.mp4` 25.7 s; kalimi: ekrani → ura → drone, zoom 1.15→1.0 + shkrirje 0.6 s; HUD 4→5 yje, fiket me prozhektorin (10.0–10.6) |
| 2026-11-14 | Montimi 1–4 v1 | `edit/join_all.sh` (1-2 v3 + 3-4 v2) | — | — | — | `gta_scenes_1-4_v1.mp4` 61.9 s, 112 MB |
