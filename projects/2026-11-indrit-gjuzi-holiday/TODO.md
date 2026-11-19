# TODO: shot-et 2 dhe 3 (Blender, etiketa reale)

Gjendja më 2026-11-19, ora 18:15:
- **Shot 1 v4:** i përfunduar, te `renders/shot1_final_v4.mp4`.
- **Shot 2 dhe shot 3:** skriptet janë gati, por nuk janë renderuar ende.

Pamja është e njëjtë me atë të shot-it 1 v4 dhe vjen nga `blender/final_common.py`. Produktet janë vetëm
ato të `refs/`.

## Rregulla para se të nisësh
- **Vetëm një render GPU në një kohë.** Dy render-a njëkohësisht e lënë GPU-në pa memorie
  (`Insufficient Memory`), dhe render-i ndalet në mes.
- Bëj gjithmonë më parë `test`, që renderon kuadrin e parë dhe të fundit. Shihi të dy kuadrot dhe vetëm
  pastaj nis `full`.
- Nëse një render ndalet, nise sërish me `RESUME=1` përpara komandës. Kuadrot që janë tashmë në disk
  nuk renderohen më.
- Komandat ekzekutohen nga folderi `projects/2026-11-indrit-gjuzi-holiday/blender/`.

## 1. Shot 2: spiralja me DreamDuo (3.0 s, 72 kuadro, ~45 min)
Gjendja: testi me 16 samples doli mirë. Printi real i DreamDuo lexohet dhe kolona e dhoma janë mocha.

```bash
cd projects/2026-11-indrit-gjuzi-holiday/blender
```
```bash
/Applications/Blender.app/Contents/MacOS/Blender -b --factory-startup --python shot2_final.py -- s2_test test
```
```bash
/Applications/Blender.app/Contents/MacOS/Blender -b --factory-startup --python shot2_final.py -- out_s2 full
```
```bash
ffmpeg -y -framerate 24 -i out_s2/f%04d.png -c:v libx264 -pix_fmt yuv420p -crf 16 -preset slow -movflags +faststart ../renders/shot2_final.mp4
```

Çfarë duhet kontrolluar në test:
- Në kuadrin e fundit, kutia e vajit mbetet në qendër dhe kutitë DreamDuo dalin pjesërisht nga kadri.
  Kjo është lëvizja e previz-it. Nëse s'të pëlqen, ndrysho `th = front - 1.4 + i * 0.42` te `shot2_final.py`.
- Kolona e dytë me shishet në sfond duhet të shihet e butë, jashtë fokusit.

## 2. Shot 3: kutitë e vajit të varura (3.0 s, 72 kuadro, ~45 min)
Gjendja: skripti është shkruar, por nuk është provuar ende. Nis patjetër me `test`.

```bash
/Applications/Blender.app/Contents/MacOS/Blender -b --factory-startup --python shot3_final.py -- s3_test test
```
```bash
/Applications/Blender.app/Contents/MacOS/Blender -b --factory-startup --python shot3_final.py -- out_s3 full
```
```bash
ffmpeg -y -framerate 24 -i out_s3/f%04d.png -c:v libx264 -pix_fmt yuv420p -crf 16 -preset slow -movflags +faststart ../renders/shot3_final.mp4
```

Çfarë duhet kontrolluar në test:
- Kutitë varen drejt dhe fjongot e kuqe satin prekin majën e kutisë.
- Tubi akrilik duhet të duket i qartë. Nëse del i zi ose i zbehtë, kjo vjen nga materiali `M_GLASS` te
  `final_common.py`.
- Sfondi duhet të jetë mocha. Nëse del shumë i errët, rrit energjinë e `WallGlow` te `shot3_final.py`.

## 3. Pas render-it
- Shëno rezultatin te `log.md` dhe bëj commit dhe push për MP4-at, pa kuadrot PNG.
- Konfirmo me përdoruesin vendimin që shot-et 2–3 të bëhen në Blender në vend të Seedance. Pastaj
  shkruaje te `decisions.md`.
- Shot-et 4–6 mbeten me Seedance (`prompts/v4_mocha_s2_s6.md`), ose bëhen edhe ato në Blender. Ky
  vendim mbetet i hapur.

## Parametra të rregullueshëm (env)
| Variabli | Default | Çfarë bën |
|---|---|---|
| `FINAL_SAMPLES` | 64 | cilësia; 16 mjafton për teste të shpejta |
| `FINAL_EXPOSURE` | -0.2 | ndriçimi i përgjithshëm |
| `FINAL_KEY` | 0.95,0.97,1.0 | ngjyra e dritës së përparme |
| `RESUME` | — | `1` = vazhdon një render që u ndal |
