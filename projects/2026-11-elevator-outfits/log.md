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
