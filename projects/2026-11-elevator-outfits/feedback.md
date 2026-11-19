# Feedback gjatë projektit

Shëno menjëherë, me fjalët e përdoruesit. 👍 pëlqen · 👎 s'pëlqen · 💡 zbulim · 🔧 rregull i ri

| Data | Lloji | Çfarë tha | Konteksti (shot / prompt / model) | Propozim: ku shkon |
|---|---|---|---|---|
| 2026-11-19 | 🔧 | "shoes u will suggest… i will share only the face… then we create the reference sheet, then we wear the girl, then we do the video" | rendi i punës: fytyrë → sheet → veshje → video | Nëse përsëritet: `cinematic-ai-video` §5 (rendi i Elementeve për projekte me veshje) |
| 2026-11-19 | 🔧 | "u dont generate i generate manually u just give prompt" | të gjitha hapat | konfirmon memorien ekzistuese: vetëm prompte |
| 2026-11-19 | 🔧 | "reference sheet i want face close, full body front and the logo close, 3 panels in 16:9" | character sheet, Banana Pro | `banana-pro-director`: sheet 3-panelësh me close-up të logos për projekte me produkt |
| 2026-11-19 | 🔧 | "will use this, do not reexplain how it looks like" | sheet v2: foto studio si referencë poze/sfondi; referencat zëvendësojnë përshkrimin | konfirmon CLAUDE.md rregulli 5 (referenca > përshkrim) |
| 2026-11-19 | 👎 | "it is in the right not in the left" | pozicioni i logos te sheet v1 ("wearer's right" lexohej majtas në kuadër) | (e kuptova gabim: "right" = e djathta e personit) |
| 2026-11-19 | 💡 | "will change to this" | fytyra e modeles ndryshon te `refs/face-model.jpg`; prompti v2 mbetet i njëjtë, sepse fytyra vjen vetëm nga referenca | — |
| 2026-11-19 | 👍 | "esht n t djatht ore si n t majt, esht mir logo aty ku duhet" | sheet v3: logoja në të djathtën e personit (majtas në kuadër) = e saktë; edit-i i logos anulohet. Sheet-i i zi = standardi | Pozicioni i produktit shkruhet nga ana e personit që e vesh |
| 2026-11-19 | 🔧 | "remove the face in each of these images in the center shot" | 3 kartat para Seedance: fytyra hiqet te paneli i mesit, mbetet vetëm te close-up | `ai-narrative-film` (kurthi i personazheve të dyfishuar): një fytyrë për referencë |
| 2026-11-19 | 👎 | "that thing at the hands moves like there are hands but they are open" | 04 v1: mëngët me zinxhir të hapur lëviznin si krahë | Kurthet (`cinematic-ai-video` §7): veshje me pjesë boshe → përshkruaj ndërtimin (bosh, i sheshtë, varet) + mos kërko lëvizje |
| 2026-11-19 | 🔧 | "i want 4 shots, one where she has the hoodie on" | 04 v2: 4 segmente, i katërti me kapuç të ngritur | — |
| 2026-11-19 | 👍 | (v2 pranuar pa vërejtje te mëngët/kapuçi) | 04 v2: blloku WARDROBE për mëngët boshe funksionoi | mëso: ndërtimi i veshjes në fjalë > referencë vetëm |
| 2026-11-19 | 🔧 | "she should be in the phone like chatting and typing" | 04 v3: chat/typing në vend të selfie-t | — |
| 2026-11-19 | 🔧 | "the elevator should have a full close and a full open" | 04 v3: cikël i plotë dere, prerja vetëm mbi derë të mbyllur e të palëvizur | `seedance-clean` CUTS: tranzicion me objekt kërkon kohë mbajtjeje para/pas HARD CUT |
| 2026-11-19 | 🔧 | "look this for her movements" (videoja referencë) | 04 v3: telefoni me dy duar poshtë gjoksit, trupi pothuajse i palëvizur, sytë lart-anash herë pas here | — |

| 👍 | "its better is 90%" | Seedance v3 (hf_20261119_181513) | Full door cycles, colours, hood-up finale and sleeves are all correct. This is now the standard (lock what you got). |
| 👎 | "in every shot she is typing and does almost the same movements, lets alternate" | Seedance v3, all 4 segments | One PHONE ACTION block for all segments → identical gesture. Each segment gets its own action. |
| 👍 | "scene 1,2,3 are perfect, use the last scene from the previous video for the one with the hoodie on" | Seedance v4 (hf_20261119_192123) seg 1–3 + v3 seg 4 | Alternating actions work. The v3 hood-up finale (typing → phone down → look to the lens) beats the v4 one. |
| 🔧 | "in one of the pics the arms need to be zipped and in the last one, the hoodie is bigger, look like this" | Montage A, blue seg + hood seg | Blue: sleeves zipped closed (as in the original product photo). Hood: large, deep, standing up off the head (refs/hood-sleeve-ref.jpg). Fix with V2V on each segment, not by regenerating everything. |
| 🔧 | "cant u give me one" | V2V fixes | Wants a single prompt instead of two separate edits. |
| 💡 | "doesnt it make sense to regenerate as an extend video just the shot with the zipped and the hoodie… use extend video functionality" | V2V fixes | Extend from the approved clip (0–10 s) instead of editing 19 s: fewer credits, the approved scenes stay untouched, the door tone stays continuous. |
| 💡 | "look what it is created maybe we should generate her outfit reference and use that" | Extend v1 | Agreed: the sheet has to show the exact garment state (zipped sleeves / big hood); text plus a crop do not override the sheet. |
| 🔧 | "it looks like it has two collars, the inner one up to the throat, then the hood over it" + "this applies to all the photos" | All sheets | Product: ribbed crew-neck collar + hood attached outside it, front edges crossing. Goes on all 3 colours. Refs: double-collar-crop.jpg, black-collar-detail.jpg |
