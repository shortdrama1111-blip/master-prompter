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

## Struktura e një projekti

```
projects/YYYY-MM-emri/
├── brief.md        # briefi origjinal + përgjigjet e pyetjeve
├── decisions.md    # bota e ngulitur: blloku i dritës, paleta, Elementet, formati
├── prompts/        # një skedar për çdo shot/bllok, me versionet
└── log.md          # çfarë u gjenerua, çfarë doli keq, pse
```

Fillo nga `projects/_template/`.

---

## Rutina në fund të çdo projekti

1. Lexo `log.md` dhe nxirr mësimet: çfarë funksionoi, çfarë dështoi, shkaku.
2. Shtoji te `LESSONS.md` me datë dhe emrin e projektit.
3. Mësim i konfirmuar në **2+ projekte** → propozo ta kalojmë në skill-in përkatës ose këtu.
   Mësim që kundërshton një rregull ekzistues → ngrije si konflikt, mos e mbishkruaj.
4. Commit + merge në `main`. Pa merge, thread-i tjetër nuk e sheh mësimin.

`CLAUDE.md` mbahet i shkurtër. Detajet shkojnë te skill-et.
