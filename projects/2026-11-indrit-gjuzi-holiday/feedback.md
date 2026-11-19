# Feedback gjatë projektit

Shëno menjëherë, me fjalët e përdoruesit. 👍 pëlqen · 👎 s'pëlqen · 💡 zbulim · 🔧 rregull i ri

| Data | Lloji | Çfarë tha | Konteksti (shot / prompt / model) | Propozim: ku shkon |
|---|---|---|---|---|
| 2026-11-19 | 🔧 | "same vibe but to not feel copied, the movements and stuff can be the same, the product should be mine, and we will switch the background a little bit" | Brief, video referencë OUAI | decisions.md e projektit |
| 2026-11-19 | 💡 | Pipeline: Blender → render video → video + produkt + ambient si referenca te modeli AI | Brief | LESSONS.md nëse funksionon |
| 2026-11-19 | 👍 | Zgjodhi sfondin B: pjeshkë e ngrohtë, e kuqja vetëm aksent | Pyetja e sfondit (A krem-ari / B pjeshkë / C e kuqe) | decisions.md |
| 2026-11-19 | 👍 | Blender si blockout i thjeshtë ("mendoj se 1") | Pyetja e detajit të Blender-it | decisions.md; LESSONS.md nëse mjafton për modelin |
| 2026-11-19 | 👍 | Harta e produkteve për 6 shot-et: "duket mirë" | Propozimi i hartës | decisions.md |
| 2026-11-19 | 👍 | Gjatësia A: rreth 16s, si referenca | Pyetja 4 | decisions.md |
| 2026-11-19 | 👍 | Shkroi "5-4a", e lexova si 5A: një shot = një gjenerim | Pyetja 5 | decisions.md |
| 2026-11-19 | 🔧 | Dha metodën e vet për previz në Blender: grey-box pa GUI, vetëm kamera + blocking, ngarkohet si @video1 pranë referencave të produktit; lëvizje të buta e fizikisht të besueshme; 1 frame test për shot para renderit të plotë; asnjëherë video AI si @video1 | Previz për Seedance | skill (seedance-clean ose skill i ri previz) pas konfirmimit |
| 2026-11-19 | 💡 | Blender 5.2 i instaluar mjafton pa GUI: `blender.exe -b --factory-startup --python previz.py -- OUT test|full` — s'ka nevojë për `pip install bpy` as për serverin MCP | Previz lokal në Windows | LESSONS.md |
| 2026-11-19 | 🔧 | "pse s'më jep vetëm 1 video?" → "e tentojmë njëherë me 1 prompt" | Pas previz-it v2; ndarja në 6 shot-e i dukej e panevojshme | decisions.md; nëse funksionon, LESSONS.md: 1 gjenerim për reel 16s me 5 produkte |
| 2026-11-19 | 🔧 | "for the first shot one like elevator move up, the 2 others in the sides move down" | Shot 1 rafti, previz v3 | decisions.md (shot 1); previz.py |
| 2026-11-19 | 💡 | "pse për videon e parë e mbarove më shpejt?" — pritja e gjatë e renderit u vu re | Previz v3 me Cycles 23s/frame | LESSONS.md: në laptop pa GPU, previz me EEVEE |
| 2026-11-19 | 👍 | "now is better, I can see that is better, I really like it" | Gjenerimi v2 (prompt v2 + previz v3: kamera afër, softbox, DOF, rafti ashensor) | LESSONS.md: previz me dritë të butë + DOF + produkte të mëdha transferohet mirë |
