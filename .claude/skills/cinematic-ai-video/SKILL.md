---
name: cinematic-ai-video
description: >
  Metoda e plotë për prodhim video kinematike me AI nga brief deri te montimi — vendimet
  para prompteve, referencat reale, plate-t, Elementet, dhe promptet shumë-shot me RULES
  dhe acting tasks. Përdore kur përdoruesi jep një brief për video reklame ose filmike me
  AI, kërkon prompt për një skenë kinematike, do të ndërtojë një botë vizuale me lokacion
  real, ose kur një gjenerim ka dështuar dhe duhet riparuar. Trigger: "video per klientin",
  "brief per reklame", "me bej 1 video", "prompt per skene", "pse doli keq".
---

# Prodhim video kinematike me AI

Sistemi për të kthyer një brief në video të përfunduar. Vlen për çdo brief: produkt,
lokacion, personazh, markë.

---

## PARIMI THEMELOR: VENDIMET PARA PROMPTEVE

Një prompt i shkruar para se bota të jetë e ngulitur duket produktiv, por ndërton mbi
vendime që s'janë marrë. Çdo ndryshim i vogël pas tij kërkon rishkrim të plotë.

Kur vjen një brief, **mos jep prompt**. Pyet.

Rendi i detyrueshëm:

```
Brief → Bota → Referencat → Plate-t → Elementet → Prompti → Gjenerimi → Montimi
```

---

## 1. BRIEFI → PYETJET

Pyetjet jepen në blloqe nga 2–3, jo të gjitha përnjëherë: përgjigja e një blloku
ndryshon çfarë ka kuptim të pyesësh në tjetrin.

**Portat që duhen mbyllur:**

| Porta | Pse ka rëndësi |
|---|---|
| Vendi | lokacion real i identifikueshëm kundrejt të përgjithshmit |
| Koha | natë / perëndim / ditë — ndryshon gjithë dritën |
| Formati | 9:16, 16:9, të dyja |
| Epoka | e sotmja, historike, apo mix |
| Subjekti | personazh apo vendi — vendos gjithçka më pas |
| Energjia | e qetë, festë, apo ngjitje |
| Markimi | ku shfaqet marka dhe në çfarë forme |

Nëse një portë mbetet e hapur, mos e zgjidh vetë në heshtje. Thuaj çfarë mungon dhe
pse ka rëndësi.

**Kur përdoruesi sjell një video referencë:** mos e kopjo. Nxirr atë që transferohet
(teknika e promptit, reçeta e dritës, struktura) dhe thuaj qartë çfarë nuk transferohet
(epoka, formati, konsistenca që kërkon Elemente).

---

## 2. REFERENCAT REALE

- **Lokacion bosh > lokacion i mbushur.** Foto pa njerëz dhe pa pajisje i lë modelit dy
  punë: ta bëjë natë dhe ta mbushë. Foto plot barriera e furgona kërkon rindërtim të
  ~80% të pikselëve, dhe aty humbet cilësia.
- Ngarko vetëm referencën përkatëse. Referenca të përziera → arkitekturë e përzier.
- Hiq shprehimisht: vinça, barriera, ekrane LED, reklama, mjete të parkuara, mobilje urbane.
- **Rreshti i detyrueshëm në çdo prompt:**
  `"reference defines architecture, geography and dressing ONLY — NOT a keyframe,
  sets no camera position; every shot builds its own viewpoint"`
  Pa të, i njëjti kënd ngjitet në të gjitha kuadrot.

---

## 3. PLATE-T (master frames)

**Frame-first gjithmonë:** imazh → Element → image-to-video. Kurrë text-to-video direkt
për projekt me markë ose lokacion.

- **4 variante** për çdo plate. Dështimet janë të rastësishme.
- Kontroll në 100%: dendësia, pozicioni i arkitekturës, ndonjë dritë moderne e mbetur.
- **Edito, mos rigjenero.** Kur një plate del 90% i mirë:
  `"Keep the supplied image exactly — same camera, framing, crowd, lighting, grade and
  grain. Change ONE thing only: X. Everything else untouched."`
- Ngjyrën mes plate-ve rregulloje me pass në Lightroom, jo me rigjenerim.

---

## 4. RREGULLI I DRITËS DHE NGJYRËS

Fiksohet një herë dhe përsëritet **fjalë për fjalë** në çdo plate dhe çdo prompt videoje.

- **Një temperaturë kryesore** (p.sh. 2700K praktike e ngrohtë), asnjë burim tjetër.
  Një llambë e bardhë ose blu e prish gjithë epokën.
- **Një ngjyrë e rezervuar** vetëm për personazhin kryesor ose elementin e markës.
  Kjo e bën një figurë të dallueshme mes mijëra vetash.
- **60:30:10** si numër, jo si përshkrim: dominanti / sfondi / aksenti.
- Qielli, të zezat, kokërriza, halacioni — njësoj kudo.
- **Ndërtesat reale marrin dekor minimal.** Nëse dekorohen shumë, videoja lexohet si
  reklamë e asaj godine, jo e markës.
- **Konsistenca është rregull, jo rast.** Ndriçohet në një kuadër → ndriçohet në të gjithë.

---

## 5. ELEMENTET

Pa Element, fytyra dhe veshja ndryshojnë çdo shot. Përshkrimi me fjalë nuk mjafton kurrë.

**Karta e karakterit:** sfond studio neutral gri, dritë e sheshtë 5000K, pa atmosferë.
Figura e plotë + close-up i fytyrës. Fytyra në figurën e plotë është shumë e vogël për
t'u mbajtur — close-up-i është i detyrueshëm.

Elemente të veçanta për: lokacionet, personazhet, prop-et kyçe, elementet e markës.

**Tag-et nuk funksionojnë të ngjitura si tekst** — futen nga lista e platformës ose me ID
direkt përmes API.

---

## 6. ANATOMIA E PROMPTIT

Blloqet në këtë rend, emrat në anglisht sepse hyjnë fjalë për fjalë:

```
Style          formati i filmit, optika, çfarë NUK duhet
Lighting       burimet praktike, temperaturat, drejtimi
Atmosphere     mjegull me shtresa në %, pluhur, tym, insekte
Color          60:30:10, aksenti i rezervuar, të zezat, kokërriza
Camera         kohëzgjatja, shot-et, shutter, fps, rregullat e kuadrimit
Skin           realizëm në nivel poresh
Acting         referencë te ACTING TASKS
Physics        pesha, inercia, pëlhurat
Escalation     si rritet energjia nga shot-i i parë te i fundit
RULES          të numëruara, HIGHEST PRIORITY te kritiket
Audio          gjithçka që dëgjohet; "no music" nëse muzika vjen në montim
Characters     secili me Elementin e vet
ACTING TASKS   motive / goal / obstacle / tactic + safety note
Scene          referencat si jo-keyframe + lista e shot-eve
SHOT N         FOV, lëvizje në km/h, timecode, veprimi
```

### Rregullat që e bëjnë të duket film

Këto futen në çdo prompt:

- **Kamera e mbajtur nga njeri:** float 2 cm, settle dhe micro-overshoot në fund të çdo
  lëvizjeje, një focus breath për shot. Lëvizja perfekte lexohet si AI.
- **Çdo prerje bie mbi lëvizje.** Lëvizja në fund të një shot-i vazhdon në hapjen e tjetrit.
- **Tri plane thellësie:** diçka brenda 4 m nga lentja, veprimi në mes, arkitektura mbrapa.
- **Një veprim i vetëm njerëzor i lexueshëm në çdo shot të gjerë.** "Turma valëzon" është
  tapet; dikush që ngre një fëmijë mbi supe është skenë.
- **Atmosfera me shtresa:** e hollë përpara, e dendur në mes, figurat e largëta pa kontrast.
- **Escalation:** energjia rritet nga shot-i i parë te i fundit.
- **Acting tasks, kurrë emocione.** Motiv / qëllim / pengesë / taktikë moment pas momenti,
  plus safety note: sy të gjallë, pulitje natyrale, kurrë shikim i ngrirë.
- **Mbi-specifiko aty ku modeli dështon.** Rregull kritik shkruhet në tri mënyra.
- **Vetëm pohore.** Kurrë "mos bëj X" — gjithmonë çfarë duhet të ndodhë.
- **Numra, jo mbiemra.** km/h, përqindje, metra, FOV në gradë.

### SUBJECT RULE — kur videoja duhet të tregojë vendin

Nëse një shot duhet të tregojë ambientin, **hiq çdo Element karakteri nga ai shot** dhe shto:

```
SUBJECT RULE — HIGHEST PRIORITY: there is NO main character in this film. No face is ever
closer than fifteen metres from the lens, no individual is featured, tracked or favoured,
and the camera never pushes toward or lingers on any person. The subject of every frame
is the PLACE.
```

Pa këtë, modeli e tërheq kamerën te fytyra dhe ambienti humbet.

---

## 7. KURTHET

| Simptomë | Shkaku | Zgjidhja |
|---|---|---|
| Kamera mbyllet te fytyra në kuadrot e gjera | Element karakteri në atë shot | Hiqe Elementin + SUBJECT RULE |
| Turma del tapet kokash | "asnjë boshllëk, guri i padukshëm" | Dendësi që bie drejt skajeve, guri i dukshëm anash |
| Telat e dritave duken të prera | "kryqëzohen nga X drejt jashtë" | Vija paralele, të ankoruara në të dy skajet |
| Shkrimi kursiv del i shtrembër | Modeli nuk e riprodhon dot | Panel bosh + logo në montim |
| Videoja duket reklamë e lokacionit | Godina e dekoruar si skenë | Godinat vetëm kontur drite |
| Ngjyra ndryshon mes kuadrove | Plate-t veç e veç | Rregull i vetëm drite + pass ngjyre |
| Sfondi ngrin me video reference | Videoja burim ka sfond statik | Lëvizjen e sfondit si shot i veçantë image-to-video |

---

## 8. STRUKTURA, KOHËZGJATJA, MONTIMI

- Kufiri i gjenerimit e vendos strukturën. Blloqe brenda kufirit, bashkim në montim —
  një shot i keq kërkon rigjenerim të një blloku, jo të gjithë videos.
- Prerja mes blloqeve bie aty ku ndryshon skena, jo aty ku mbaron koha.
- Video vertikale promocionale: **20–30 sekonda.** Nën 15 nuk mban histori, mbi 30 bie
  shikueshmëria.
- Harku që funksionon: **vendi → mbërritja → shfaqja.**
- Teksti, data dhe logoja gjithmonë në montim. Për tekst mbi kuadër, kërko që prompti të
  lërë zonë të zezë të sheshtë pa teksturë.
- Korniza e fundit ngrihet 1–2 sekonda nëse mbi të vjen tekst.
- Muzika zgjidhet pas montimit; prompti shkruhet me `no music`.

### Montimi (i testuar, pëlqyer nga përdoruesi)
- **Dy versione:** A = segmentet të plota njëri pas tjetrit; B = me prerje. Përdoruesi zgjedh.
- **Segmente nga një kënd i fiksuar:** pri momentet e dobëta (gabime fizike, produkt i deformuar)
  dhe jep **punch-in 1.2–1.8×** në copat që mbeten. Copa e fundit e një segmenti kthehet te
  kuadri i gjerë, që lidhja me segmentin tjetër të jetë e padukshme.
- **Ritmi i produkteve në reel:** ~2 s për produkt.
- **Muzika:** gjenerohet me gjatësinë e montimit dhe zhvendoset që "button"-i i fundit të bjerë
  mbi kuadrin e mbylljes; tingujt e videos ~-5 dB nën muzikë; final -14 LUFS.
- **Mbyllje që s'e mbush kuadrin:** zoom i butë (smoothstep) mbi objektin + slow 1.5–1.6× në
  pjesën e mbajtur. Kurrë freeze-frame.
- Skriptet: `tools/montage/` (`edit.sh`, `final.sh`, `grade.py`).

---

## 9. SI TË SILLESH

- Brief → pyetje, jo prompt.
- Prompt i plotë, gati për kopjim. Pa vendmbajtës.
- Kur del keq: shkaku konkret, jo "le ta provojmë përsëri". Nëse faji ishte një rresht i
  promptit tënd, thuaje cili.
- Kur diçka nuk bëhet dot me modelin, thuaje para se të harxhohen kredite, jo pas tri provave.
- Numëro kuadrot para se të shtosh. Kur mjaftojnë, thuaje.
