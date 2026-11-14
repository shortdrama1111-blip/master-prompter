# Log i gjenerimeve

| Data | Shot | Modeli | Rezultati | Problemi | Shkaku | Veprimi |
|---|---|---|---|---|---|---|
| 2026-11-13 | Character sheet v4 | Higgsfield Soul | ✅ i zgjedhur nga përdoruesi | bluza doli me volan; syzet mbi kokë edhe te paneli front | modeli interpretoi "off-shoulder" si volan | Lock what you got; maska gri mbi fytyrën e qendrës |
| 2026-11-13 | Plate v2 | image (përdoruesi) | 🟡 | 16:9 sërish; nuancë e verdhë në hije; mbështetësja gjysmë e ngritur, bllok në mes të ndenjëses | raporti në UI; drita e reflektuar nga lëkura | pass ngjyre `tools/grade.py` → `refs/plate-v2-graded.png` |
| 2026-11-13 | Plate v3 | image (përdoruesi) | 🟡 | 9:16 ✅, mbështetësja e mbyllur ✅, drita neutrale ✅; shpinoret e përparme (korniza e ref) mungojnë, kamera më afër (~63°) | edit-i e riformatoi kuadrin | në pritje: lock apo edit zoom-out |
| 2026-11-13 | Plate final | image (përdoruesi, edit zoom-out) | ✅ | — | — | ngulitur si @image1 |
| 2026-11-13 | Akti 1 seated v1 | Nano Banana Pro | ✅ 👍 | syzet mbi kokë (sipas promptit); tekst i vogël i shtrembër te çantat ("PERFUNERY", Kérastase) | modeli s’e riprodhon tekstin e vogël | edit vetëm për syzet; teksti → vendim i përdoruesit |
| 2026-11-13 | Akti 1 v1 | Seedance 2.5 | ✅ (përdoruesi e mban) | HARD CUT-et u injoruan → take i vazhdueshëm; në ~1.5 s ajo qëndron në këmbë brenda kabinës; te 5.5–8 s shishja del e vogël/portokalli, jo Eight & Bob | modeli preferon vazhdimësinë me kamerë të fiksuar; parfumi pa sheet → forma humbet kur është larg | prerjet në montim; akti 2 si take i vazhdueshëm; sheet parfumi |
| 2026-11-13 | Akti 2 v1 (extend) | Seedance 2.5 | ✅ "perfect" | — | take i vazhdueshëm + @video1 si master funksionoi | ngulitur; extend për aktin 3 |
| 2026-11-14 | Akti 3 v1 (extend, 7 shot-e) | Seedance 2.5 | ✅ | doli 10 s (jo 12); fondatina vetëm 0.6 s; shot-i i fundit i gjerë 0.4 s | gjatësia e gjenerimit 10 s | ngrirje 2 s e kuadrit të fundit në montim |
| 2026-11-14 | Montimi A (30.0 s) + B (27.2 s) | ffmpeg `tools/edit.sh` | ✅ | aktet 1–2 nga një kënd i vetëm | — | B: prerje + punch-in 1.2–1.8×; insert-e I1–I3 të propozuara |
| 2026-11-14 | Muzika "Velvet Bloom" | ElevenLabs Music | ✅ | 26 s, mbaron te 25.0 s (button + reverb) ndërsa videoja finale ~30 s | prompti kërkoi 26 s para mbylljes | muzika fillon te ~3.2 s që button-i të bjerë kur çanta mbulon kuadrin |
| 2026-11-14 | Mbyllja v1 | Seedance 2.5 | 🟡 përdoruesi: "i dont really like this" | 0–2.2 s statike; çanta nuk mbuloi gjithë kuadrin (duar lart, sedilje anash), logoja në mes jo lart | modeli e ndali çantën te ~85% e kuadrit | montim: prerë nga 2.3 s, zoom i butë 1→2.0 mbi logon, 3.4–5 s slow 1.6×; tekst Inter |
| 2026-11-14 | FINAL v1 (28.9 s) | ffmpeg `tools/final.sh` | ✅ | — | — | hook "BLACK FRIDAY" 0.15–1.7 s; tekst final @26.3 s; muzika nga 1.3 s, button-i bie te teksti; -14 LUFS |

## Kostoja (lexuar nga transaksionet Higgsfield, 2026-11-14; dritarja e projektit 13.11 22:21 → 14.11 00:45 UTC)
| Çfarë | Model | Gjenerime | Kredite |
|---|---|---|---|
| Akti 1, 2, 3, mbyllja (përputhen me emrat e skedarëve hf_…) | Seedance 2.5 Flash | 4 | 0 |
| Imazhe (plate, sheet-e, start frame) | Nano Banana Pro | 8 të regjistruara | 16 |
| Character sheet | Soul | — (asnjë transaksion në dritare) | 0 |
| **Totali i projektit** | | | **16** |
Në të njëjtën dritare, jashtë pipeline-it tonë: Wan 3.0 Prime Video ×15 = 438, MiniMax H3 = 24, Gemini Omni Flash 1.2 = 22.5 (gjithsej 484.5) — për t'u konfirmuar nga përdoruesi.
ElevenLabs: connector-i kërkon rilidhje me leje shtesë → kostoja e muzikës s'u lexua.
Bilanci Higgsfield pas projektit: 5782.1 kredite (plan Ultra).
