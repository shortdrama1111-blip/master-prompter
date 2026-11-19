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
| 2026-11-19 | 👍 | "Po, bëji": pranoi hibridin (v2 + rigjenerim i shot-eve 1, 3, 6 veç e veç) | Pas krahasimit të v2 | decisions.md; LESSONS.md: 1 prompt me 5+ prerje s'mban kohët |
| 2026-11-19 | 🔧 | "I want that to be readable that are my products and none else" | Shot 1 v3: etiketat e shpikura nga modeli | CLAUDE.md / skill: etiketat e markës s'lihen te modeli, vijnë nga foto reale (Blender ose montim) |
| 2026-11-19 | 🔧 | Klienti (WhatsApp, 15:41): "sfond Mocha / Dark Taupe, me ndriçim luksoz dhe rafte minimaliste; pjesa e brendshme e rafteve pak më e errët; drita LED të ngrohta 3200K; rafte champagne; ndriçim i butë përpara produkteve që të lexohen etiketat; kontrast i dukshëm mes shisheve të bardha dhe sfondit" | Pas shot-it 1 v3 (pjeshkë/krem); kundërshton vendimin B (pjeshkë) dhe bllokun e dritës 4000K | decisions.md pasi të konfirmohet shtrirja (vetëm rafti apo gjithë videoja) |
| 2026-11-19 | 🔧 | "duhet ta ribëjmë të gjithën" — mocha vlen për gjithë videon | Pas kërkesës së klientit | decisions.md (u përditësua) |
| 2026-11-19 | 🔧 | "ndalo, nuk ia vlen, do ta provoj nga PC im Mac" | Renderi i shot-it 1 në laptopin Windows (~3 min/frame) | — (vazhdon në Mac) |
| 2026-11-19 | 👎 | "sepse në fillim janë disa që janë të errëta" | Shot 1 final, test në Mac (f0000): shishet e vajit 40ml dalin cilindra të zinj, jo xham i qartë si `refs/hair-oil-with-box.jpg`; kutia e vajit gjysmë e bardhë | shot1_final.py; LESSONS.md: xhami transmission në EEVEE mbi sfond të errët del i zi → alpha-glass |
| 2026-11-19 | 🔧 | "kujdes që produktet të jenë vetëm produktet që unë kam vendos si referenca" | Para renderit të plotë të shot-it 1 | CLAUDE.md / cinematic-ai-video: çdo produkt në render kontrollohet 1:1 me `refs/` para renderit të plotë |
| 2026-11-19 | 👎 | "nuk duket si xham i qartë të them të drejtën, mund ta përpunosh dhe pak" | Shot 1 v2: vaji 40ml me xham alpha-blend (pa thyerje drite, pa shkëlqim buzësh) | shot1_final.py; LESSONS.md: xhami kërkon thyerje + reflekse buzësh, jo vetëm transparencë |
| 2026-11-19 | 👍 | "ok me cycles 64 samples" | Shot 1 render i plotë: Cycles GPU (M2 Pro) për xhamin e vajit, ~35s/frame në vend të EEVEE ~4s | decisions.md (shot 1); LESSONS.md: xhami i qartë → Cycles, EEVEE mjafton për materiale opake |
| 2026-11-19 | 👍👎 | "mirë duket, por janë si shumë të bardha bro" | Shot 1 final v3 (Cycles): produktet dalin më të zbehta/të bardha se fotot reale (kutia pjeshkë → krem, mëngët bezhë → të bardha) | shot1_final.py; blloku i dritës: "glow just below clipping" e tepron → produktet në ngjyrën e fotos |
| 2026-11-19 | 🔧 | Ridërgoi mesazhin e klientit (mocha "kafe e butë", brendësia më e errët, LED 3200K, champagne, etiketa të lexueshme, "kontrast mes shisheve të bardha dhe sfondit") + "po nise A" | Pas korrigjimit B: sfondi doli çokollatë e ngopur, shiritat LED të bardhë, shishet krem | Render A: produktet në ngjyrën e fotos (kapak i bardhë, mëngë bezhë), mocha më e butë, LED të ngrohta të dukshme |
| 2026-11-19 | 🔧 | "a mund të vazhdosh vetë me pjesën e dytë dhe të tretën... do largohem pak nga kompjuteri dhe dua ta lë ndezur të punosh" | Pas shot-it 1 v4. Seedance s'mund ta përdor vetë, ndaj shot-et 2 dhe 3 bëhen në Blender me etiketa reale, si shot 1 | decisions.md: shot-et 2–3 kalojnë nga Seedance në Blender (për t'u konfirmuar nga përdoruesi) |
