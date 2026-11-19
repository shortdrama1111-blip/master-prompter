# Shënime: "The Workflow" (Arcads, GPT Image 2.6 + Seedance 2.5, video "Vice City")

Burimi: artifact publik claude.ai i dërguar nga përdoruesi (2026-11-19). Përmbledhje me fjalët e mia, vetëm pjesët për promptet e videos.

## Çfarë bëjnë ata
- Një charsheet për çdo personazh (ballë, profil, shpinë + 2 close-up), një tag për çdo sheet (`@image1`, `@image2`).
- Prompti i Seedance ka blloqe fikse: hapja e identitetit → vendi + drita → pamja e personazhit → **veprime me timestamp** (0-2s, 2-5s...), një veprim për bllok, me fjalët e sakta që thuhen → `Camera` → `Behavior` → `Style` → `Audio` (me "No music") → `Voices` → `Important`.
- Kaos në sfond në të njëjtin shot, kamera e ndjek: kjo është "stop scroll".
- Extend: thuaj ku shkon kamera nga frame-i i fundit, përndryshe Seedance kthehet te fillimi.
- Maks 2 imazhe referencë për extend, përndryshe përzihen fytyrat.
- Tag-u përsëritet në çdo veprim, jo vetëm një herë.
- Rreshti `Voices`: mosha, theksi, qëndrimi, i njëjti fjalë për fjalë në çdo extend.
- Rreshti `Behavior`: personazhi s'pozon, s'buzëqesh si model.
- Energjia "e çmendur" përshkruhet me sy, buzëqeshje, të qeshur, jo me "crazy".
- Moderim: ndaje promptin në dysh për të gjetur rreshtin që e shkakton (s'harxhon kredite).

## Ku na shërben (epara GTA)
| Ide | Përdorimi te ne |
|---|---|
| Timestamp për veprimet | ✅ çdo shot Seedance: 0-2s / 2-5s me një veprim të dukshëm për bllok |
| Tag-u në çdo veprim | ✅ `@Djali-GTA-Plastik` në çdo bllok kohe ku shfaqet |
| "Përdore vetëm për fytyrën/trupin, jo sfondin gri ose layout-in e sheet-it" | ✅ zgjidh rrezikun e rrobave/sfondit të studios që rrjedhin nga charsheet-i |
| Extend: ku shkon kamera nga frame-i i fundit | ✅ për kalimet dyqan → rrugë → makinë |
| Maks 2 referenca | ✅ p.sh. djali + karta te tap-i; plate-i si frame i parë |
| Behavior line | ✅ "relaxed, confident, never poses" përkthyer në muskuj (rregulli 2) |
| Voices | ⚠️ te ne zëri është narrator shqip në montim → Seedance vetëm SFX/ambient, `no music` |
| Kamera handheld e dridhur | ⚠️ te GTA ne kemi kamera loje (follow cam, bonnet cam, slow-mo) — handheld vetëm për momente "realiteti" |
| Style "photoreal, never a game render" | ❌ e kundërta e briefit tonë (personazh plastik GTA); por plate-et tona dolën foto-reale → shih feedback |

## Konflikt me rregullat tona (pa vendim)
- Ata përdorin shumë negative ("never smooth", "no logos", "never a game render"). CLAUDE.md rregulli 3: vetëm pohore. Është i njëjti konflikt i hapur te tabela (`seedance-clean` vs `ai-narrative-film`).
- Ata përdorin "35mm footage, film grain": emër pajisjeje/filmi, që `seedance-clean` e ndalon.
