# Feedback gjatë projektit

Shëno menjëherë, me fjalët e përdoruesit. 👍 pëlqen · 👎 s'pëlqen · 💡 zbulim · 🔧 rregull i ri

| Data | Lloji | Çfarë tha | Konteksti (shot / prompt / model) | Propozim: ku shkon |
|---|---|---|---|---|
| 2026-11-21 | 👍 | "po me pëlqejnë sugjerimet e tua" (LENS: një editim jo zinxhir; NEVER → pohore) | Integrimi i LENS në skill-e | Tashmë te `cinematic-ai-video` §3 + `seedance-clean` |
| 2026-11-21 | 🔧 | "bëj diçka shumë të bukur dhe wow", 20 s në një gjenerim, me storyboard | Hapja e projektit | Liri krijuese kur përdoruesi e jep shprehimisht |
| 2026-11-21 | 👍 | "është perfekt, më pëlqen shumë" | Storyboard v1 (2 faqe) + prompti 20 s v1, para gjenerimit | Metoda blockout → storyboard → prompt funksionon për përdoruesin; konfirmo pas gjenerimit |
| 2026-11-21 | 💡 | Pyeti nëse 3 veglat SFX (Openverse, real-sfx, earshot) na duhen "në përgjithësi, gjatë gjithë kohës", sepse repo përdoret për çdo projekt dhe do ta trajnojë me shijen e vet | Vlerësim veglash, jo shot specifik. Rekomandimi: real-sfx = po (shtresë opsionale pas gjenerimit, kur zëri i Seedance del i dobët); Openverse/Freesound = vetëm burim tingujsh CC0; earshot = jo për skena kinematike (tinguj të sintetizuar) | Në mbyllje: hap opsional "SFX në post" te `cinematic-ai-video`; rregulli i licencës (vetëm CC0 për reklama klientësh) te `CLAUDE.md` ose skill. Konfirmo pas provës së parë reale |
| 2026-11-21 | 💡 | "shiko te gjitha branchet dhe cfar kam krijuar sepse mendoj se na duhen" | Kontroll i të gjitha branch-eve: SFX u kërkua në 3 projekte (printer te per-class-black-friday, zile telefoni te telefoni-kuq, ndjekje/megafon/mission passed te gta-VI); montimi bëhet nga Claude me ffmpeg (`tools/montage`). Rekomandimi u ndryshua: veglat SFX duhen | Në mbyllje: hap "SFX" te `cinematic-ai-video` + `tools/` (real-sfx për tinguj realë, earshot për tinguj mekanikë/UI, Openverse CC0 si burim); rregulli "dy versione: pa zë / me SFX" dhe niveli ~−16 dB peak nga per-class-black-friday |
