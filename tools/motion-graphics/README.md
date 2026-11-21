# Motion graphics me kod (HyperFrames + Remotion), për tekstin, logon, numrat dhe kartat e fundit

Regjistruar më 2026-11-21. Burimi: ultra-skills.com, "Claude Code Animation Prompts" (30 prompte).
Faqja i ngarkon promptet me JavaScript, ndaj përdoruesi i ngjiti në chat. Këtu ruhen ato që na hyjnë në punë.

**Ku hyn te metoda jonë:** rregulli 9 (teksti, logoja, data dhe muzika vijnë në montim). Seedance bën
botën dhe personazhet; këto bëjnë shtresën grafike: karta e fundit, "−50%", numërues, njoftime porosish,
logo e animuar. Nuk zëvendësojnë Seedance.

**Propozo vetë** kur një projekt ka: ofertë ose çmim në ekran, numër që rritet, logo në fund, ose një
objekt "produkt" që del më mirë i pastër me kod (si fatura e Black Friday te `clever-faraday`).

## Dy rrugë: HyperFrames (kryesore) dhe Remotion (për efekte të veçanta)

**HyperFrames** (open source nga HeyGen, `hyperframes-kit/`) është rruga kryesore. Animacioni bëhet si faqe web
(`index.html`), Chrome bën foto çdo frame dhe ffmpeg i bashkon. Kjo është e njëjta mënyrë që përdorëm me dorë
te fatura e Black Friday. Kit-i (Damiano Caudullo) ka 15 prompte të testuara, 4 stile, fontet (OFL, falas edhe
për klientë) dhe 9 SFX UI. Promptet më të vlefshme për ne:

| Prompti | Na shërben për |
|---|---|
| **11** Grafika mbi videon tonë | Videoja nga Seedance/montimi mbetet e paprekur. Whisper e transkripton dhe çdo grafikë (numërues, checklist, krahasim) nis te fjala e saktë. Për reklama me voiceover si Krenar ose epara |
| **14** Eksport transparent (ProRes 4444) | Kartë ose tekst mbi footage në çdo program montimi |
| **08** Video vetëm me tekst | Hook ose reel pa footage |
| **09** Video produkti | Lansim produkti, kartë fundi me CTA |
| **13** SFX | Me `hyperframes-kit/sfx/`, ose me `tools/sfx/` (real-sfx e njeh HyperFrames direkt) |
| **04–07** Stilet: Kinetic Type, Liquid Glass, Editorial Grain, Pop Bold | Blloku STYLE nën promptin. **Ngjyrat dhe fontet merren nga `decisions.md` e projektit**, stili jep vetëm lëvizjen |

Kujdes te **15** (spec ad për çdo markë): merr maskotën dhe asetet nga faqet e markës. E përdorim vetëm për
marka që janë klientët tanë dhe na i kanë dhënë asetet.

Përgatitja një herë për kompjuter: Prompti 01 (Node 22+, FFmpeg, whisper-cpp, `npx hyperframes skills`).
Para çdo projekti: kopjo `hyperframes-kit/fonts/` (dhe `sfx/` nëse duhet) në folderin e projektit.
Kit-i origjinal kishte edhe `clip.mp4` (18 s, burrë i gjeneruar me AI) dhe screenshot-e prove: s'u ruajtën.

**Remotion** (`prompts.md`) mbetet për efektet 3D që HyperFrames s'i ka gati: fatura, paratë, njoftimet,
kalendari, logo nga pluhuri.

## Pse funksionojnë

E njëjta filozofi si rregulli 2 ("numra, jo mbiemra"): çdo prompt fikson stack-un, paletën me hex,
lëvizjen e kamerës dhe **frame-in e saktë** të çdo ngjarjeje. Kjo e bën renderin deterministik
(pa `Math.random`, pa orë) dhe na jep një listë ngjarjesh me kohë të sakta, që `real-sfx`
e merr direkt për SFX (`tools/sfx/`).

## Kërkesat

- Node 20+ dhe ffmpeg (në cloud: node 22, ffmpeg 6.1, Chromium i instaluar).
- 3D (prompt 1–14): `@remotion/three` + React Three Fiber, render me `--gl=angle`.
- Bojë, të dhëna, UI (15–30): vetëm CSS dhe SVG, më të lehta.
- Të gjitha: 1080×1920, 30 fps, 2–3 s. Për 16:9 ndrysho kompozimin në 1920×1080.
- Pritu 1–2 raunde rregullimesh versionesh herën e parë.

## Si përdoret

1. Folder bosh brenda projektit (p.sh. `projects/<emri>/motion/<efekti>/`).
2. Merr promptin nga `prompts.md`, zëvendëso `[kllapat]` me tekstin, paletën dhe numrat e projektit.
   **Paleta vjen nga `decisions.md` e projektit**, jo nga prompti.
3. Ndërto, shiko preview-n, ndrysho një gjë për raund ("fillo rrugën te frame 20").
4. Render → montim me `tools/montage`. Pastaj SFX me `tools/sfx` nëse duhet.

## Zgjedhja jonë (sipas projekteve që kemi bërë)

| # | Efekti | Na shërben për | Shembull nga projektet tona |
|---|---|---|---|
| 13 | Receipt: fatura printohet, griset, ngrihet drejt lentes | Ofertë, çmim, Black Friday | per-class-black-friday (e bëmë me dorë) |
| 12 | Money stack: para bien, numëruesi rritet | Cashback, kursime, totale | epara GTA ("cashback 8.90 L") |
| 27 | Lock-screen notifications: porositë grumbullohen | E-commerce, "sa shitje sot" | Inspired by Love, SINDI-CAR |
| 24 | Day counter: kalendari 30 ditë | Kurse, sfida, oferta me afat | egli-krenar (kursi Meta) |
| 28 | Type slam: fjalë të mëdha që përplasen | Hook në 2 s të para, kartë fundi | SINDI-CAR ("BLACK FRIDAY") |
| 29 | Particle word: pluhuri bëhet fjalë ose logo | Logo në fund pa e gjeneruar me AI | çdo reklamë me markë |
| 11 | Turntable: produkt që rrotullohet me specifikime | Produkt i vetëm me 3 karakteristika | — |
| 22 | Stat chart: vija çan kufirin e grafikut | Rezultate, rritje | egli-krenar |
| 25 | Split-flap: tabela e nisjeve shkruan fjalinë | Titull, ofertë, "NOW BOARDING" | — |
| 26 | Before/after slider | Rebranding, faqe e re | — |

Të tjerat (1–10, 14–21, 23, 29–30) janë më shumë për tech/SaaS: hartë, orë e çmontuar, qytet GitHub,
glob, hologram, vrimë e zezë, hartë konture, siluetë neoni, laptop, rrugë izometrike, ajsberg,
gazetë, poster zviceran, blueprint, letra në tavolinë, doodle, bojë kineze, kolaps doodle, agent swarm,
terminal → faqe. Teksti i plotë: `prompts.md` ka 13, 12, 27, 24, 28, 29; për të tjerat ri-ngjite nga faqja.

## Rregullat tona mbi to

- Paleta, fonti dhe ngjyra-aksent merren nga `decisions.md` e projektit, që grafika të lidhet me videon.
- Asnjë numër, datë ose çmim i shpikur: vetëm ato që jep klienti (prompti e thotë vetë: "demo").
- Dorëzo dy versione kur ka zë: pa zë dhe me SFX (`tools/sfx`).

## Regjistri i përdorimit

Në mbylljen e çdo projekti kontrollo: nëse s'është përdorur në **3 projektet e fundit**, thuaja përdoruesit.

| Data | Projekti | Efekti | Për çfarë |
|---|---|---|---|
| 2026-11-21 | — | — | Vetëm regjistrim, pa test ende |
