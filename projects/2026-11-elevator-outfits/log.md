# Log i gjenerimeve

| Data | Shot | Modeli | Rezultati | Problemi | Shkaku | Veprimi |
|---|---|---|---|---|---|---|
| 2026-11-19 | 04 v1 (3 segmente) | Seedance 2.5 | ngjyrat, dera, fytyra, kamera OK | mëngët e hapura sillen si krahë/flatra | prompti kërkonte lëkundje mëngësh dhe ngritje krahësh; askund s'thuhej që paneli është bosh dhe i sheshtë | v2: bllok WARDROBE + PHYSICS për panelet boshe, pa ngritje krahësh |
| 2026-11-19 | 04 v2 (4 segmente, 20 s) | Seedance 2.5 | mëngët dhe kapuçi OK | dera s'mbyllet e plotë, prerja kërcen te dera e mbyllur | mbyllja 0.55 s + HARD CUT në të njëjtin moment, pa kohë dere të mbyllur | v3: 1.0 s hapje/mbyllje + 0.2 s derë e mbyllur e palëvizur në të dy anët e prerjes |

## Seedance v3 → hf_20261119_181513 (20.05 s)
- ✅ Doors fully open and fully close, cuts on closed doors. Colours in the right order. Hood-up in seg 4. Sleeves hang flat.
- ❌ Same typing gesture in all 4 segments. Cause: the shared "PHONE ACTION, in every segment" block.
- ❌ Seg 3 (blue): boots came out black instead of cream-white. Fix: separate lock in POSITIVE LOCKS.
- → v4: only ACTION/PERFORMANCE/AUDIO/LOCKS change; everything else identical to v3.

## Seedance v4 → hf_20261119_192123 (20.06 s)
- ✅ Seg 1–3 perfect according to the user: typing / reflection with hand on hip / phone call, cream boots in blue.
- Seg 4 (hood): replaced with v3's seg 4.
- ⚠️ Grade: the v4 doors are dark (Y≈53 on closed doors), the v3 doors bright (Y≈117).

## Montage A → montage/elevator-v4-v3-cut-A.mp4 (19.34 s, not in git)
- v4 frames 0–360 (0–15.04 s, ends on closed doors) + v3 from frame 378 (15.75 s, 3 bright closed frames, then the doors open).
- Hard cut on the closed doors; v4 audio up to 15.04, v3 audio after, with 0.05 s fades.
- The door brightness jumps at the cut; it reads as a "new floor". If it bothers the user: grade v3 seg 4 to v4's tone, or v4 to v3.

## Extend v1 → hf_20261119_200522 (19.07 s)
- ✅ Seg 1–2 kept, the blue call and the black finale are there, cream boots.
- ❌ Blue: sleeves still open. Cause: @image1 = sheet-blue-noface shows the sleeves open; the sheet beats the text and the sleeve crop.
- ❌ Hood: slightly bigger but close to the head. Cause: sheet-black has the hood down; the shape came from text plus a reference with a different face.
- ❌ Seg 4: the face drifts and the doors turn bright again (like v3).
- → New sheets: blue zipped, black with a big hood (prompts/06).

## Sheet D2 (black, collar) → refs/sheet-black-collar-v1.jpg
- ✅ Centre panel: the double collar is right, the face is consistent.
- ❌ Left panel: no crew-neck collar (only the hood V). ❌ Right panel: a neckline close-up instead of the logo.
- Cause: "change the neckline" with no panel named; the collar crop got copied as a panel. Fix: v3 panel locks (D3).
- ⚠️ Centre logo reads "VIVANUS". The right panel gets restored from the original sheet.
