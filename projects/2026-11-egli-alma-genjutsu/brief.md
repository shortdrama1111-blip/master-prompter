# Brief

## Briefi origjinal
Projekt "egli-alma-genjutsu". Përdoruesi jep një video referencë me një vajzë (Alma) dhe disa
imazhe me veshje. Vajza në video ndërron veshjet me ato të referencave; gjithçka tjetër mbetet
e njëjtë: fytyra, identiteti, lëvizja, kamera, sfondi dhe drita.

Dorëzimet:
1. **Imazhet**: një frame për çdo veshje, me Almën që e ka veshur, i nxjerrë nga videoja
   (frame-first, edit mbi frame-in origjinal).
2. **Prompti final për Genjutsu** (Higgsfield), gati për copy-paste: V2V sipas
   `seedance-clean` §INPUT VIDEO — `@video1` master, ndryshon vetëm veshja.

Rregull bazë: identiteti i Almës i paprekur. Ndryshon VETËM veshja.

## Ndryshim drejtimi (2026-11-14)
Përdoruesi: Alma zëvendësohet me një vajzë të re (`refs/char-ref-1.jpg`, + 4–5 ref të tjera që do dërgojë).
Fytyra e saj duhet të jetë 100% e njëjtë. Rrjedha: character sheet → 4 frame me 4 veshjet → Genjutsu.
Nga videoja ruhen: lëvizja, kamera, kohët, ndërrimet wipe, sfondi, drita.

## Portat
| Porta | Përgjigja |
|---|---|
| Videoja referencë (kohëzgjatja, formati) | në pritje |
| Sa veshje | në pritje |
| Si ndërrohen (për prerje / në ritëm / në lëvizje) | në pritje |
| Formati dhe gjatësia e daljes | në pritje |
| Rruga: MCP (Claude gjeneron) apo manuale | në pritje |
| Modeli | Genjutsu (Higgsfield) për videon; model editimi imazhi për frame-t |
