# Brief: Indrit Gjuzi Haircare, reklamë festash

## Briefi origjinal
Përdoruesi (2026-11-19): "I need to make for these products. My idea is: create the Blender,
then add the Blender video and the product and the env to recreate it. I want it to be the
same vibe but to not feel copied. The movements and stuff can be the same, the product should
be mine, and we will switch the background a little bit."

**Video referencë:** reklama festash OUAI (Instagram), 15.9s, 9:16, 720×1280, 30fps.
Kontakt-sheet: `refs/original-contact-sheet.jpg`. Skedari origjinal: te Downloads e përdoruesit
(nuk futet në repo).

### Struktura e referencës (6 shot-e)
| # | Koha | Çfarë ndodh |
|---|---|---|
| 1 | 0–2s | Raft me kuti të ndriçuara nga brenda, me produkte; kamera ngjitet vertikalisht |
| 2 | 2–5s | Rripa transportues spiralë mbi kolona rozë kadife; kuti dhuratash lëvizin |
| 3 | 5–8s | Tub transparent i lakuar, stolira-kuti të varura që lëkunden |
| 4 | 8–10s | Rrip transportues diagonal me kuti dhe stolira |
| 5 | 10–12s | Pirg kutish dhuratash me fjongo + çanta |
| 6 | 12–16s | Close-up çantë, kartë me shkrim dore "Jingle all the …" |

### Çfarë transferohet / çfarë jo
- **Transferohet:** lëvizjet e kamerës, ritmi, struktura e 6 shot-eve, ndjesia e butë studioje.
- **Nuk transferohet:** paleta rozë-kadife, forma e saktë e setit, marka OUAI, teksti i kartës.

### Produktet (refs/)
| Skedari | Produkti |
|---|---|
| `peptide-mask.jpg` | Leave-In Peptide Mask 150ml, shishe bezhë-pjeshkë, kapak i bardhë |
| `leave-in-conditioner.jpg` | Nourishing Leave-In Conditioner 150ml, e njëjta formë |
| `hair-oil-with-box.jpg` | Nourishing Hair Oil 40ml, xham transparent, kapak i zi + kuti bezhë |
| `dreamduo-box.jpg` | Kuti DreamDuo Limited Edition (mask + conditioner), valë pjeshkë/ari |
| `holiday-bag-red.jpg` | Çanta festash e kuqe me ilustrime, dorezë satin e bardhë |

### Pipeline (ideja e përdoruesit)
Blender (lëvizja + kamera + set) → render video → video + foto produkti + ambienti si referenca
në modelin AI → videoja finale.

## Portat
| Porta | Përgjigja |
|---|---|
| Vendi | set studioje abstrakt, sfondi pjeshkë e ngrohtë |
| Koha | dritë studioje, e butë |
| Formati | 9:16, rreth 16s, 6 shot-e |
| Epoka | e sotmja |
| Subjekti | produktet, pa njerëz |
| Energjia | festive e qetë, si referenca |
| Markimi | produktet reale + çanta e kuqe; teksti/logo në montim |
| Modeli (Seedance 2.5 / Kling / tjetër) | Seedance 2.5 me video referencë, një gjenerim për shot |
