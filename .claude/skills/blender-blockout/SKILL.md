---
name: blender-blockout
description: >
  Blockout 3D në Blender (përmes Blender MCP) → kamera reale për çdo shot → storyboard nga renderat →
  gjuha e kamerës për Seedance ose një model imazhi. Përdore kur një skenë ka gjeografi që modeli e
  prish (përmasa, drejtim në ekran, kush ku qëndron), kur ka 3+ shot-e në të njëjtin hapësirë, ose kur
  përdoruesi thotë "blockout", "storyboard", "previz", "Blender", "vendos kamerat", "busull".
---

# Blender Blockout → Storyboard → Prompt

Modelet video/imazh janë të forta në **pamje**, të dobëta në **logjikë hapësinore**: ndryshojnë
përmasat, kthejnë drejtimin në ekran, lëvizin njerëzit. Një blockout me kuti gri e zgjidh këtë:
çdo gjë ka përmasën reale, vendin real, drejtimin real, dhe çdo kamerë është një thjerrëz reale
në një pozicion real. **Storyboard-i është blockout-i i fotografuar.**

**Blockout-i është burimi i së vërtetës për vendosjen.** Pamja vjen nga referencat; hapësira vjen
nga blockout-i.

Burimi: "Nexus Blender Storyboard Workflow" (Theo Dudley / Nexus, tetor 2025), përshtatur për këtë repo.

---

## Kur ia vlen (dhe kur jo)

| Po | Jo |
|---|---|
| 3+ shot-e në të njëjtën hapësirë, me prerje mes tyre | Një oner i vetëm pa gjeografi të ndërlikuar |
| Objekte gjigante vs njerëz (shkalla prishet lehtë) | Product shot në studio të zbrazët |
| Drejtimi në ekran ka rëndësi (ndjekje, sulm, takim) | B-roll freestyle |
| Disa personazhe që ndërrojnë vend gjatë skenës | Talking-head |

---

## Ku ruhen skedarët

```
projects/YYYY-MM-emri/
├── blockout/        # emri_v001.blend, emri_v002.blend ... asnjëherë mbishkrim
└── storyboard/
    ├── v1/          # renderat e shot-eve (1A.png, 1B.png ...) + faqet (page_01.png ...)
    └── v2/
```

Çdo ndryshim = version i ri. Ruaj me `bpy.ops.wm.save_as_mainfile(filepath=..., copy=False)` në
një emër të ri, kurrë në të njëjtin.

---

## HAPI 0 — Kontrollo lidhjen

Para çdo gjëje: verifiko që Blender është hapur dhe MCP-ja përgjigjet (p.sh.
`get_objects_summary`). Inspekto skenën ekzistuese para se të fshish ose ndryshosh diçka;
mos fshi objektet e përdoruesit pa pyetur.

---

## HAPI 1 — Skena në shkallë reale

Kuti gri mjaftojnë. Ka rëndësi vetëm **përmasa, pozicioni, drejtimi**.

- **Njësitë:** metra, Z lart.
- **Orientimi i fiksuar, një herë për gjithë projektin:**
  - jashtë → busull: **+X = Lindje (E), +Y = Veri (N)**;
  - brenda → mure me emër ("muri i dritares", "muri i derës").
- **Fleta e shkallës** (shkruaje te `decisions.md`): njerëz, mobilje, mjete, rekuizita, arkitekturë.
  Kontrolloji krah për krah në një pamje të gjerë. Nëse duket gabim në blockout, do dalë gabim në
  çdo gjenerim.
- **Njerëzit si stand-in:** cilindër/kapsulë me ngjyrë, në lartësinë reale, **një ngjyrë për
  personazh**, me një shenjë (kon/kuti e vogël) që tregon nga sheh fytyra. Pa figura me poza:
  performanca vjen nga modeli.
- **Sfondi i lexueshëm:** çdo drejtim i busullës ka diçka të njohur (mur, dritare, mal, hënë), që
  të dihet gjithmonë nga sheh kamera. Këto bëhen blloku `COMPASS` te prompti.
- **Lëvizja:** animo vetëm atë që lëviz, në rrugë të thjeshta, me shpejtësi reale (km/h → m/frame).
  Tymi, zjarri, grimcat nuk futen: përshkruhen te prompti.
- **Shënimi i paraqitjes** (layout note), në gjuhë të thjeshtë: "tavolina në qendër; ajo ulur nga
  ana e dritares, sheh nga dera; ai në këmbë te banaku".

---

## HAPI 2 — Kamerat

- **Një kamerë për shot**, me emër: `CAM_01_WIDE`, `CAM_02_CU_HER`. Një **timeline marker** në fillim
  të çdo shot-i, i lidhur me kamerën (`marker.camera = cam`), që playback-u të presë si montazh.
- **Për çdo kamerë shëno:** madhësia e shot-it, **FOV në gradë** (nga tabela FOV e `seedance-clean`:
  107/84/63/47/29/18/12/8), drejtimi sipas busullës (CAM FACING: N/NE/E...), lartësia në metra,
  këndi, distanca nga subjekti, lëvizja (static / push in / dolly / pan / handheld).
- **FOV në Blender:** `cam.data.sensor_width = 36`, `cam.data.lens_unit = 'FOV'`,
  `cam.data.angle = radians(FOV)`. I njëjti numër shkon te prompti, që board-i dhe teksti të
  përputhen.
- **Raporti:** vendos rezolucionin e daljes sipas formatit final (16:9 → 1920×1080; 9:16 →
  1080×1920; 2.39:1 → 2048×858) dhe kompono brenda tij.
- **Rregulli 180°:** lëvizja e vazhdueshme rrjedh në një drejtim në gjithë sekuencën.
- **Kontrollo çdo kamerë:** a është besnike ndaj skenës, a ka kuptim pranë shot-eve të tjera, a është
  e komponuar mirë? Rregulloje para se të vazhdosh.
- **Previz (opsional):** render Workbench i shpejtë i gjithë sekuencës për të parë prerjet dhe ritmin.

---

## HAPI 3 — Renderat dhe faqet e storyboard-it

- **2–4 frame për shot**, me shkronja sipas radhës (1A, 1B, 1C): fillimi, momenti kyç, fundi.
  **Vetëm nga kamerat reale të shot-eve**: asnjë kënd i shpikur për board-in.
- **Render:** Workbench (flat/solid, me ngjyrat e objekteve) mjafton. Ruaj te `storyboard/vN/`.
- **Kurth i provuar:** kur marker-at janë të lidhur me kamera, `scene.camera = cam` **injorohet**,
  sepse marker-i e zgjedh kamerën sipas frame-it. Për çdo render bëj `scene.frame_set(frame_i_shotit)`
  dhe kontrollo `scene.camera.name` para `render.render(write_still=True)`. Përndryshe të gjitha
  renderat dalin nga e njëjta kamerë.
- **Stand-in-i ka "hundë":** një kub i bardhë i vogël para kokës, që në çdo render të shihet nga sheh
  personazhi (frame left / frame right). Pa të, një cilindër duket i njëjtë nga çdo anë.
- **Faqet** (landscape 3300×2550, ose më e vogël për provë):
  - faqja 1 hapet me **shënimin e paraqitjes**;
  - çdo shot: **titulli**, **rreshti i kamerës** (facing, FOV, lartësia, lëvizja), **frame-t me
    shkronjë** me një rresht përshkrim poshtë secilit, dhe **shënimi brenda kuadrit** (ku qëndron
    çdo gjë siç shihet nga kamera, majtas/djathtas nga kamera);
  - **footer:** çelësi i ngjyrave të stand-in-eve + "çdo numër i ri shot-i = prerje".
- Faqet mund të montohen me Pillow ose me compositing në Blender; çdo mënyrë që del si PNG.

---

## HAPI 4 — Gjuha e kamerës në prompt

**Për Seedance (video):** bashkëngjit faqet e storyboard-it si referenca dhe për çdo shot shkruaj
nga board-i, pa shpikur:

```
SHOT 1: [EMRI] (CAM FACING: N) (PANELS 1 TO 3)
Size: [shot size]. Placement: [kush ku në kuadër, majtas/djathtas nga kamera]. Angle: [lartësia + këndi].
Lens: [FOV]°, about [X] meters away. Mount: [static / handheld / dolly + lëvizja]. Focus: [subjekti].
```

Shto blloqet `COMPASS` dhe `STORYBOARD` sipas `seedance-clean` → "SPATIAL LOCK".

**Për model imazhi (frame-first, Element):** një render i vetëm si referencë kompozimi + gjuha e
kamerës poshtë tij (FOV, lartësia, drejtimi, kuadri, çfarë ku qëndron), pastaj referencat për pamjen.

---

## Checklist

- [ ] Lidhja me Blender e verifikuar, skena ekzistuese e inspektuar
- [ ] Orientimi i fiksuar (busull ose mure me emër) dhe i shkruar te `decisions.md`
- [ ] Gjithçka në përmasë reale, e kontrolluar krah për krah
- [ ] Njerëzit si stand-in me ngjyrë, në lartësi reale, me shenjë drejtimi
- [ ] Një kamerë me emër për shot: FOV°, facing, lartësi, lëvizje + marker
- [ ] Drejtimi në ekran konsistent; çdo kamerë e kontrolluar
- [ ] Frame-t me shkronjë, vetëm nga kamerat reale
- [ ] Faqet: shënimi i paraqitjes, rreshtat e kamerës, përshkrimet, shënimet në kuadër, çelësi
- [ ] Gjuha e kamerës e shkruar nën çdo board → prompt
- [ ] Çdo gjë e ruajtur si version i ri
