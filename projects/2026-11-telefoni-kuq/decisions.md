# Vendimet e ngulitura

## Blloku i dritës (fjalë për fjalë në çdo prompt)
```
```

## Ngjyra: 60:30:10, aksenti i rezervuar

## Elementet / referencat
| Tag | Çfarë është | Shënime |
|---|---|---|

## Konflikte të zgjidhura për këtë projekt (shih CLAUDE.md)

## Audio (2026-11-20)
- Zëri i karakterit: ElevenLabs Eleven v3, shqip. Ajo thotë vetëm replika të shkurtra ("Po.", "Natyrisht.").
- Audio i saj i jepet Seedance si referencë: mp4 9:16 me ekran të zi + audio.
- Pyetjet = voiceover (zë tjetër, në telefon), shtohen në montim.
- "In Arabic too?" → "Edhe në anglisht?"

## Karakteri (2026-11-20) — I NGULUR
refs/wardrobe-sheet-locked.jpg: blazer i zi double-breasted me kopsa ari (doli i gjatë deri mes kofshës, mbahet — "lock what you got"), bluzë fildishi me pussy-bow, leggings të zeza, pumps lustrafine, vathë perle, orë ari.

## Grain / look
- Prompt: drita + ngjyra (blloku i dritës).
- Montim: film grain, halation, vinjeta — njësoj mbi të gjitha shot-et.

## Blloku i dritës — I NGULUR (2026-11-20, "okay")
```
Warm tungsten light at 3200K from frosted wall sconces and a soft overhead source, low contrast, blacks lifted to a faded charcoal, cream highlights rolling off gently with a soft glow around bright edges, muted palette of cream walls, oxblood red lacquer and antique gold.
```

## Referencat për Seedance
| Tag | Skedari |
|---|---|
| @image1 | refs/wardrobe-sheet-pa-fytyre.jpg (fytyrat e rreshtit poshtë të mbuluara) |
| @image2 | refs/plate-v1.jpg |
| @image3 | refs/telefoni-v1.jpg |
| @video1 | audio/black-genA-10s.mp4 ose audio/black-genB-15s.mp4 (vetëm zëri i saj) |

## Ndarja e gjenerimeve (max 20 s për gjenerim)
- A: 10 s, shot-et 1–8 (timeline 0.0–10.0) — "Po" te 5.85 dhe 7.6
- B: 15 s, shot-et 9–12 (timeline 9.6–24.6) — "Natyrisht" 0.9, "E pakrahasueshme" 3.9, CTA 9.0
- Shot 1 pa emrin e markës për momentin (pret klipin).

## Konflikte të zgjidhura
- Formati i promptit: seedance-clean (pa emra pajisjesh, vetëm pohore, stil i shpërndarë).

## Skripti v2 (2026-11-20) — ajo përgjigjet në çdo shot
Aura. / Strategji? → Po. / Rrjete sociale? → E menaxhova. / Përmbajtje? → E kemi. / Produksion? → Edhe këtë. / AI? → Po. / Influencerë? → Po. / Reklama me pagesë? → Gati. / Edhe në anglisht? → Natyrisht. / Po cilësia? → E pakrahasueshme. / Pra… pa ju, humbas klientë. → qesh / Na kontaktoni për të parë punën tonë.
Promptet 04/05 v1 dhe black-genA/B janë të vjetra — rindërtohen pas audios së re.

## Ambienti v2 — 2026-11-21 (ZËVENDËSON zyrën vintage dhe bllokun e dritës 3200K)
- Gjithë videoja kalon në ambientin e ri; A rigjenerohet (promptet dhe audioja e A mbeten).
- Referencat: refs/env-v2/1–4.jpg. Banak çeliku i lakuar, mur i bardhë, hark me dritë blu në vend të pasqyrës ovale.
- Telefoni i kuq me disk (refs/telefoni-v1.jpg) mbetet i vetmi aksent i ngopur.
- Grade "ulli" (look-ref.sh) s'vlen më për këtë dritë; grain-i (grain-ref.sh) mbetet.

### Blloku i dritës v2 — fjalë për fjalë në çdo prompt (pret plate v2 për t'u ngulur)
```
Daylight at 5600K: hard afternoon sun entering from a tall window outside frame right at a 30° downward angle, casting crisp window-frame shadows and soft leaf shadows across the white wall and floor; the shade side filled by bright bounce from the white plaster to 1.5 stops under; whites held clean with a faint cool blue tint in the shade; muted palette of white plaster, brushed steel and pale grey, with the red telephone as the only saturated colour.
```
