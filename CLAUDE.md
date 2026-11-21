# Master Prompter — baza për çdo projekt video me AI

Ky repo është "truri" i përbashkët i të gjitha projekteve video. Çdo video e re hapet si thread
i ri mbi këtë bazë. Rregullat këtu vlejnë gjithmonë; detajet teknike janë te skill-et.

Komunikimi me përdoruesin: **shqip**. Promptet për modelet: **gjithmonë anglisht**.

---

## Cili skill kur

| Situata | Skill |
|---|---|
| Vjen një brief i ri (reklamë, klient, markë, lokacion) | `cinematic-ai-video`: pyetjet, bota, plate-t, Elementet |
| Shkruhet një prompt për Seedance 2.5 | `seedance-clean`: struktura e blloqeve, FOV, prerjet |
| Film me histori, shumë skena, të njëjtët personazhe | `ai-narrative-film`: kontinuiteti, karta e karakterit, QC |
| Skenë me gjeografi (3+ shot-e, drejtim në ekran, shkallë) | `blender-blockout`: blockout → kamera → storyboard → prompt |
| "Shto SFX" / zë / tingull, ose projekti ka nevojë për to (propozoji vetë) | `tools/sfx/README.md`: Openverse, real-sfx, earshot |
| Një gjenerim doli keq | `cinematic-ai-video` §7 Kurthet + `ai-narrative-film` QC |

Kur një projekt kërkon më shumë se një skill, `cinematic-ai-video` vendos **rendin e punës**
dhe skill-i i modelit (p.sh. `seedance-clean`) vendos **formatin e promptit**.

---

## Rregullat e pandryshueshme

1. **Vendimet para prompteve.** Brief → pyetje në blloqe nga 2–3, jo prompt. Portë e hapur
   nuk mbyllet në heshtje: thuaj çfarë mungon dhe pse ka rëndësi.
2. **Shkruaj të dukshmen.** Numra, jo mbiemra: km/h, %, metra, FOV në gradë, Kelvin.
   Emocion përmes muskujve, jo etiketave.
3. **Vetëm pohore.** Shkruaj çfarë duhet të ndodhë, jo çfarë duhet shmangur.
4. **Një bllok drite i fiksuar** për gjithë projektin, i përsëritur fjalë për fjalë në çdo
   prompt. Ngjyra është lidhur me material + dritë + rol, jo listë.
5. **Referenca > përshkrim.** Kur ka imazh reference, përshkrimi me fjalë mbahet minimal.
   `@tag` vetëm në shot-in ku objekti është i pranishëm.
6. **Çdo prompt është i mbyllur në vetvete.** Pa "si më lart", pa numra skenash, pa
   personazhe që s'duhen në atë shot.
7. **Frame-first** për projekte me markë/lokacion: imazh → Element → image-to-video.
8. **Edito, mos rigjenero** kur një rezultat është 90% i mirë.
9. **Teksti, logoja, data dhe muzika vijnë në montim.** Promptet me `no music`.
10. **Prompt i plotë, gati për kopjim**, në code block, pa vendmbajtës.
11. **Kur del keq: shkaku konkret.** Nëse faji ishte një rresht i promptit, thuaj cili.
    Nëse diçka s'bëhet me modelin, thuaje **para** se të harxhohen kredite.
12. **Lock what you got:** nëse rezultati ndryshon nga prompti, por duket mirë, ai bëhet
    standardi i ri dhe blloku i dritës rishkruhet sipas tij.

---

## Konflikte të hapura mes skill-eve (pa vendim ende)

Skill-et vijnë nga projekte të ndryshme dhe në disa pika thonë të kundërtën. Derisa
përdoruesi të vendosë, **mos zgjidh në heshtje**. Në fillim të projektit pyet cilin drejtim
ndjekim dhe shënoje te `decisions.md` e projektit.

| Tema | `seedance-clean` | `cinematic-ai-video` | `ai-narrative-film` |
|---|---|---|---|
| Emra pajisjesh/filmi | asnjëherë | — | po (`Kodak Vision3 500T`) |
| Bllok NEGATIVE | jo, vetëm pohore | vetëm pohore, por Style përmban "çfarë NUK" | po, si rrjetë sigurie |
| Stili në krye | jo, i shpërndarë | `Style` blloku i parë | film stock pas referencave |
| Gjatësia e shot-it | deri në 30s, oner | blloqe brenda kufirit | 4s / 8s, shot-e të shkurtra |
| Kamera | e motivuar, sipas skenës | handheld float 2 cm | "nuk lëviz" duhet thënë fort |

Hipoteza ime (për t'u konfirmuar): dallimet varen nga **modeli**. Seedance 2.5 punon mirë me
pohore dhe take të gjata; modelet image/Kling kanë nevojë për negative dhe shot-e të shkurtra.
Nëse konfirmohet, rregulli shkon te skill-i i modelit përkatës.

---

## Procesi: main → thread/branch për çdo video → merge

`main` është baza. Aty jetojnë vetëm rregullat, skill-et dhe mësimet e konfirmuara.
Çdo video e re = **një thread i ri = një branch i veçantë**. Modeli kryesor: Seedance 2.5
(mund të ndryshojë sipas projektit).

### 1. Hapja e projektit (në thread-in e ri)
- Krijo `projects/YYYY-MM-emri/` nga `projects/_template/`.
- Plotëso `brief.md` sipas portave. Pyet për konfliktet e hapura dhe shkruaji te `decisions.md`.

### 2. Gjatë punës: kap çdo feedback menjëherë
Sa herë që përdoruesi thotë se diçka i pëlqen, nuk i pëlqen, ose zbulon diçka të re,
shënoje **menjëherë** te `projects/<emri>/feedback.md`, pa pritur fundin. Shënimi përmban:
- çfarë tha, sa më afër fjalëve të tij;
- kontekstin (shot-i, prompti, modeli);
- llojin: 👍 pëlqen / 👎 s'pëlqen / 💡 zbulim / 🔧 rregull i ri.

Bëj commit dhe push në branch-in e projektit pas çdo shënimi ose grupi shënimesh. Container-i
mund të zhduket, kurse branch-i mbetet. Gjatë projektit **mos prek** `CLAUDE.md`, `LESSONS.md`
dhe skill-et: gjithçka qëndron te folderi i projektit.

### 3. Mbyllja: kur përdoruesi thotë "kam mbaruar"
1. **Përmbledh** te biseda çfarë ke kuptuar: çfarë i pëlqeu, çfarë jo, zbulimet, dhe ku
   propozon ta çosh secilën (`CLAUDE.md` / skill-i X / `LESSONS.md`).
2. **Pyet** nëse ka vërejtje ose feedback që s'i ka thënë ende. Prit përgjigjen.
3. Pas konfirmimit, **përditëso skedarët** sipas këtij rregulli:
   - Preferencë e qartë ose rregull që përdoruesi e thotë si të prerë → `CLAUDE.md` ose skill-i
     i modelit.
   - Teknikë specifike për një model → skill-i përkatës (p.sh. `seedance-clean`).
   - Mësim nga një projekt i vetëm, ende i pakonfirmuar → `LESSONS.md`. Kur konfirmohet në
     2+ projekte, propozo ta ngresh në skill.
   - Kundërshton një rregull ekzistues → mos e mbishkruaj në heshtje, pyet.
   - Zgjidh një konflikt të hapur → hiqe nga tabela dhe vendose rregullin te vendi i duhur.
4. **Merge në `main`**: rebase mbi `main`-in më të fundit, merge, push. Folderi i projektit
   shkon edhe ai në `main` si arkivë.
5. Thuaj shkurt çfarë ndryshoi te secili skedar.

`CLAUDE.md` mbahet i shkurtër. Detajet shkojnë te skill-et.

### Struktura e një projekti

```
projects/YYYY-MM-emri/
├── brief.md        # briefi origjinal + përgjigjet e pyetjeve
├── decisions.md    # bota e ngulitur: blloku i dritës, paleta, Elementet, formati
├── feedback.md     # pëlqen / s'pëlqen / zbulime, të kapura gjatë punës
├── prompts/        # një skedar për çdo shot/bllok, me versionet
└── log.md          # çfarë u gjenerua, çfarë doli keq, pse
```
