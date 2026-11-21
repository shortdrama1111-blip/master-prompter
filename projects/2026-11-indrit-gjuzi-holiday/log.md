# Log i gjenerimeve

| Data | Shot | Modeli | Rezultati | Problemi | Shkaku | Veprimi |
|---|---|---|---|---|---|---|

## Shot 1 v1: hf_20261120_214142_ba7dad4f (4.06 s)
- ✅ Muri me rafte velur, dritë nga brenda, kamera ngjitet; Mask/Conditioner në kolona të ndara (majtas/djathtas), nuk ngatërrohen; "INDRIT GJUZI" i lexueshëm te kutia.
- ⚠️ Vaji del portokalli-qelibar. Shkaku: rreshtat e promptit "golden oil" (COLOR GRADE) dhe "turning the oil amber" / "oil glows amber" (ACTION + LIGHTING). Produkti real duket transparent.
- ⚠️ Kutitë dalin bezhë-kafe, jo pjeshkë si referenca.
- ⚠️ Teksti i vogël në etiketa del i deformuar (pritej); rrjeti është i rregullt, jo me lartësi të ndryshme.
- ✂️ Përdoruesi zgjodhi pjesën e parë: crop 0–2 s → Downloads\shot1-v1_crop-0-2s.mp4; version 4 s me freeze-frame për Seedance edit → Downloads\shot1-v1_crop-0-2s_pad4s.mp4.
- 🎞️ Referenca e prerë në 6 klipe 4 s (freeze-frame në fund) → refs/reference-shots/ref-shot1..6.mp4; origjinali → refs/reference-full.mp4. Pjesa reale: s1 0–1.67, s2 0–2.97, s3 0–2.97, s4 0–2.63, s5 0–1.77, s6 0–3.86.

## V2V Shot 1 v1 (ref-shot1 + produktet)
- ❌ Produktet dolën me etiketën OUAI. Shkaku: @video1 u deklarua "master" për gjithçka, dhe logoja e madhe OUAI është pjesë e pikselëve të burimit. Prompti tha "products become Indrit Gjuzi products", por nuk e shkroi tekstin e ri të etiketës si veprim. Me forma krejt të ndryshme, v2v ruan identitetin e burimit.
- Gjithsesi, v2v mbi setin rozë të OUAI nuk vlen më pas feedback-ut të klientit (mocha). Rekomandimi: Shot 1 v2 mocha, gjeneruar nga e para.

## Shot 1 v4 i2v ashensorët (v1)
- ⚠️ Majtas poshtë ✅, mesi lart ✅, djathtas lart ❌. Shkaku: kolonat anësore u përshkruan bashkë në një fjali ("the left and right columns ... together", "in the side columns"). v2: secila kolonë në rreshtin e vet.
- Fix pa kredite: kolona e djathtë mund të kthehet mbrapsht në kohë (reverse) në montim, sepse lëvizja është konstante dhe produktet janë statike.
- ✂️ Fix pa kredite mbi hf_20261120_224159_368accdf: kolona e djathtë (x 468–720) u luajt mbrapsht dhe u vendos mbi origjinalin → Downloads\shot1-v4_right-reversed.mp4. Matje (0.5 s): majtas +98 px poshtë, mesi −95 px lart, djathtas +85 px poshtë. Prerja bie mbi kornizën champagne statike.

## Shot 2 i2v v1: hf_20261120_225438_366ed58b (4.06 s)
- ✅ Drejtimet e sakta (matje 1 s): konvejeri poshtë −91 px majtas, ai sipër +45 px djathtas. Bota mocha/champagne/LED vazhdon nga Shot 1. DreamDuo e dytë hyn nga e djathta si në prompt.
- ⚠️ Frame-i i parë nuk është identik me start frame-in (kamera pak më larg, 1 DreamDuo në fillim në vend të 2). Kutitë pjeshkë të vajit dalin pa tekst. Teksti i DreamDuo pak më i butë se në imazh.

## Shot 3 i2v v1: hf_20261120_230800_200ef55b
- ❌ Produktet zhduken/ndërrohen gjatë rrotullimit; lëvizja bie nga 16 në 2 (matje energjie), ndalon nga ~3 s. Frame-i i parë më i largët se start frame-i.
- Shkaku: rrotullimi i spirales me ~20 objekte që kalojnë para njëri-tjetrit + rreshti "eases out with inertia". v2: spiralja e fiksuar, lëviz kamera me shpejtësi konstante.
- Shot 3 i2v v2 (hf_20261120_231521_bca73d33): lëvizja konstante deri në fund ✅ (energjia 9→14), kamera zbret. 👎 "they are not sliding": përdoruesi do që produktet të rrëshqasin përgjatë spirales. → v3.
- Shot 3 i2v v3 (hf_20261120_233223_82d38abc, 10 s): produktet rrëshqasin, por LART në vend të poshtë; lëvizja bie në ~1.5 s e fundit. 👎 "moving really linear". → v4: lëkundje në ajër majtas→djathtas, valë e shkallëzuar.
- Shot 3 i2v v4 (hf_20261120_234336_8b4870cf, 10 s): 👍 "its good", por produktet udhëtojnë përgjatë tubit dhe zhduken te kthesa djathtas; nuk lëkunden majtas-djathtas. → v5 lavjerrës.
- Shot 3 i2v v5 (hf_20261120_235609_4ff9d187): produktet zhduken, nuk lëkunden. Përdoruesi: lëkundja s'ka problem, por duhet të dalin nga kuadri, jo të zhduken. → v6 10 s me start frame të prerë (kthesat jashtë kuadrit).
- ✅ Shot 3 v6 (hf_20261121_000526_7857f566, 10 s): aprovuar. Start frame i prerë = zgjidhja për zhdukjen te kthesat.
- ❌ Shot 4 video pa start frame (hf_20261121_160305_5ab13af5, 10 s): ngjyrë portokalli, shishet shtrirë, asnjë kuti nuk bie, rrëmujë. Përdoruesi: "ngjan shume keq, duhet reference image first". Konfirmim: frame-first për çdo shot.
- Shot 4 i2v v1 (hf_20261121_165221_fca6e808, 5 s): konvejeri lëvizi majtas→djathtas (kundër promptit); DreamDuo ra nga ana e djathtë/përpara, jo nga buza e rrumbullakët majtas, dhe u ul mbi konvejerin poshtë djathtas. 👎 "bie tek ana tjeter, dua te bjere poshte qe ta lidhim me pjesen e kutive poshte".

## Shot 4 i2v v3: hf_20261121_170213_a078c252 (5 s)
- ✅ Të dy DreamDuo bien nga buzët e rrumbullakëta majtas dhe dalin nga kuadri poshtë: e sipërmja ~0.7–1.9 s, e poshtmja ~3.0–3.8 s. Konvejerët lëvizin drejt buzëve si në prompt. Kamera rrëshqet pak djathtas (jo plotësisht e fiksuar). Kutitë mbeten të ngurta.
- Pikat e prerjes për match cut me Shot 5: ~1.9 s ose ~3.8 s.

## Montazh i përafërt Shot 1–4 → Downloads\indrit-gjuzi_roughcut_shots1-4.mp4 (11.3 s, pa zë)
- Shot 1 0–2.0 s | Shot 2 1.5–4.0 s | Shot 3 1.0–4.0 s | Shot 4 0–3.8 s

## Shot 5 i2v v1: hf_20261121_171453_d9872f4d (5 s)
- ✅ DreamDuo hyn nga lart (~0.6 s), bie dhe futet brenda qeses së kuqe (~2.2 s), titulli "DreamDuo" duket mbi buzë; kamera afrohet. Rënia më e ngadaltë se plani (~1.6 s në vend të 0.6 s). Logo e qeses e lexueshme.
- Shot 5 v2v edit (etiketa): ❌ nuk u shtua. → Nano Banana edit i start frame-it + i2v v2.
- Shot 5 i2v v2 (hf_20261121_172818_0a9bd5e1): etiketa e pranishme gjatë gjithë kohës ✅; rënia e ngadaltë, diagonale, kutia zhytet në qese, kamera zmadhon jashtë ❌. → v3.

## Shot 5 i2v v3 (hf_20261121_173340_7cd5e642): ❌ kutia shfaqet vetëm pas ~2 s, noton ngadalë, nuk ulet. Seedance nuk e bën dot rënien e pastër. Përdoruesi: "mund ta bësh me Blender".
## Shot 5 Blender v2 → blender/shot5-blender-v2.mp4 (kopje te Downloads), 3 s, 24 fps
- Plate: frame-i i parë i v2 me etiketë (720×1280). Kamera ortografike (1 njësi = 100 px). Kutia: kub 1.32×0.45×1.88 me fytyrën e përparme nga DreamDuo-ja në plate (e njëjta dritë), materiale emission, view transform Standard.
- Holdout mbi pjesën e përparme të qeses (px x205–470, y459–680), që kutia të futet pas buzës.
- Animim me fizikë: hyn nga lart me v0 = 3 u/s, g = 52.3 u/s² (1 njësi ≈ 18.75 cm), rënie 0.42 s, goditje te frame 16, kërcim 2 cm + 0.5 cm, anim 14°→0 dhe rrotullim 8°→0, lëkundje e vogël pas goditjes. Motion blur.
- Hije e butë te buza (gradient) nga frame 17. Skedari: blender/IG_shot5.blend (skena IG_Shot5).

## Shot 6 v2 → shot6/shot6-v2.mp4 (kopje te Downloads), 4 s, 24 fps — pa gjenerim
- Plate: refs/shot6-startframe.jpg (1116x2000). Skripti shot6/make_shot6.py: "Gëzuar / Festat / xx" me Ink Free, rrotulluar -27.6° sipas etiketës, shfaqje shkronjë pas shkronje (0.45–3.4 s, ease brenda çdo shkronje, majë stilolapsi e butë 10 px), boja si shumëzim mbi letër (ruhet tekstura). Afrim kamere 1.0→0.80 drejt etiketës, ease.
- v1: teksti dilte jashtë etiketës → v2: font 112/72, qendra (560,1385).

## Montazhi final v2 (pa zë) → indrit-gjuzi_final_v2_silent.mp4, 18.0 s
- S1 0–2.0 | S2 1.5–4.0 | S3 1.0–4.0 | S4 0–3.75 | S5 Blender 0.2–2.95 | S6 0–4.0. Prerjet në rrjetë 120 BPM.

## Shot 1 v5 (animim 2D mbi frame-in e klientit), 11/21
- Gjeometria e frame-it (768×1376): shtyllat champagne x≈0, 250, 506, 760. Raftet: L y≈127/483/845/1229, M y≈208/555/921/1306 (mesi i zhvendosur ~80 px), R y≈131/488/856/1189. Kati ≈ 360 px.
- Plate pa produkte, Nano Banana Pro 4K: job 500bae6c-a219-4f7a-bf3e-8688e748b019 (nisur automatikisht; pas kësaj, gjenerimet i bën përdoruesi me dorë).
- Plate pa produkte, i marrë nga përdoruesi → refs/shot1-plate-empty.webp (1116×2000). Buzët e rafteve me hap identik 559 px në të tria kolonat (L 107, M 219, R 115 + k·559), kështu që përsëritja s'ka qepje të dukshme.
- ✅ Shot 1 v5 → shot1/shot1-v5.mp4 (1080×1920, 30 fps, 2.0 s; në montim 1.67 s). Skripti shot1/make_shot1.py: kolonat zhvendosen si shirita (anësoret poshtë 0.33 kat/s, mesi lart 0.41 kat/s), shtyllat champagne statike, zoom 1.35×, motion blur me 4 nën-frame. Produktet janë foto reale nga refs/ (etiketa të sakta), ngjyrosur me raportin klient/foto për çdo kanal, me hije kontakti + hije të butë mbi mur. Vaji: xham transparent (sfondi × transmetim) + vija të bardha anësore.
- ⚠️ Etiketa e vajit lexohet, por është e butë: foto burimore e shishes ka vetëm 122 px gjerësi (refs/image1-hair-oil.jpg). Duhet foto me rezolucion më të lartë.
- ✅ Shot 1 v6 → shot1/shot1-v6.mp4: zoom 1.0 mbi një "botë" më të gjerë (plate + 40 px anash): kornizat e jashtme champagne u plotësuan me teksturën e shtyllës së brendshme (24 px), sfond i errët (34,24,19) anash me hije të butë. Plate-i u zgjat vertikalisht me hapin 559 px që të mbushet 9:16. Produktet u rritën (vaji 340, kutia 405, maska/conditioner-i 450 px në plate), që etiketat të mbeten të lexueshme.
- Shot 1 v7 (në punë): produktet si objekte 3D në Blender (bpy 5.0.1 në cloud, CPU) → shot1/blender_cards.py → karta RGBA shot1/assets/card_*.png (produkt + dritë LED 3200K + dritë përpara 7500K + reflektim nga muret anësore + kapje hijesh). Xhami i vajit del real. Mbetet: vija horizontale te shishet mask/cond (zhurmë te profili i rrezes) dhe ngjyra krem del pak gri.
- Shot 1 v7, ndalur për kalim lokal: blender_cards.py tani pastron profilin e rrezes (mediane 31 rreshta + buzë të rrumbullakosura, 260 unaza) që të hiqen vijat horizontale; teksturat mask/cond u ngrohën (×1.0/0.965/0.92). Kartat mask/cond duhen renderuar sërish me këtë version. Mbetet: lidhja e kartave te make_shot1.py (zëvendëson produktet 2D) dhe renderi i v7.
- Për ta nisur lokalisht: Blender 5.x → `blender -b -P shot1/blender_cards.py -- mask cond` (ose python me bpy). Variablat KEY/LED/KEYK/SPP/PXU ndryshojnë dritën dhe cilësinë.

## Shot 1 v7 → shot1/shot1-v7.mp4 (lokal, 11/21)
- Kompjuteri lokal ka vetëm Intel UHD: Cycles punon me CPU (~1–2 min për kartë). Kartat mask/cond u renderuan me **Eevee** (`ENGINE=EEVEE`, 17 s për të dyja); box/oil mbeten kartat Cycles të mëparshme.
- Vijat horizontale te mask/cond vinin nga **tekstura** (piksele të zeza/të përsëritura anash), jo nga gjeometria. → `shot1/make_tex.py` rindërton teksturat nga fotot origjinale: çdo rresht shtrihet mbi gjerësinë e profilit të zbutur (pa 2 px buzë). Profili: mediane 31 + zbutje bilaterale (tol 2.5 px), heq dridhjen 0.5 px te kapakët dhe ruan shkallën kapak/trup.
- Eevee s'ka shadow catcher → muri/rafti fshihen nga kamera dhe hija (mur + kontakt) shtohet në 2D te `make_shot1.py` (`SHADOW_2D`).
- `make_shot1.py`: produktet tani janë kartat 3D (`--2d` = v6). Etiketat lexohen qartë; mask/cond dalin pak më të ftohta/gri se kutia.

## Shot 3 v7 (Blender, Eevee) → shot3/shot3-v7-preview.mp4 (540×960, 4 s), 11/21
- Plate: refs/shot3-plate-empty.jpg (Nano Banana edit nga përdoruesi, vetëm muri + kolona), si plan emission i hartuar në kuadrin e kamerës. Skripti: shot3/make_shot3.py (përdor gjeometrinë e produkteve nga shot1/blender_cards.py).
- Spirale akrilike R 27 cm, hap 46 cm, tub 3 cm; kamera 1.6 m, VFOV 32°. 56 produkte çdo 18 cm, rrëshqasin poshtë me 0.12 m/s konstante dhe dalin nga kuadri (pa modulo). Varëse: grep unazë + zinxhir 5 cm champagne-gold. Lëkundja: lavjerrës i simuluar (2.5–6°, shuarje 0.35) + rrotullim i lehtë rreth fijes.
- v1 i still-it: Glass/Transmission në Eevee del i zi (s'thyen plate-in) → xham = transparent + glossy sipas fresnel. Dritat ishin 4× shumë (produktet të djegura) → key 60, LED 45, fill 18. VFOV 45° → 32° që produktet të lexohen.
- Renderi: ~7 s/frame në gjysmë rezolucioni (14 min për 120 frame) në Intel UHD.

## Shot 5 v4 (kuadri më afër) → shot5/shot5-v4.mp4 (1080×1920, 24 fps, 3 s), 11/21
- Plate: refs/shot5-startframe-closer-v2.jpg (1116×2000; logo "INDRIT GJUZI" e korrigjuar nga përdoruesi pasi v1 kishte "INORIT GJUZI").
- Kutia: Blender/Eevee (shot5/box_blender.py), kamera ortografike 1 u = 100 px. Faqja përpara nga foto reale refs/dreamduo-v2.jpg, e drejtuar me perspektivë dhe me dritën e kutisë së plate-it (raport low-pass σ70) → shot5/assets/dreamduo_front.png. Shkrimet te shishet tani janë të saktat (te plate-i ishin të deformuara nga AI).
- Fizika: g reale (qesja 513 px ≈ 32 cm → 157 u/s²), v0 3 u/s, goditje te frame 12.5, kërcime 2 cm + 0.5 cm, anim 14°→0 dhe rrotullim 8°→0, lëkundje e shuar pas goditjes. Kutia 280×385 px, 42% e saj poshtë buzës.
- Kompozimi (shot5/make_shot5.py): holdout i qeses (poligoni i buzës + fjongoja mbi buzë), hije te buza mbi kutinë pas goditjes (0.55, σ 26 px), dridhje kamere 4 px që shuhet për ~0.25 s.

## Shot 6 v3 → shot6/shot6-v3.mp4 (720×1280, 24 fps, 4 s), 11/21
- Teksti final "Happy Holidays" (feedback i përdoruesit), Ink Free 104, dy rreshta, shkruhet 0.45–3.1 s; e njëjta plate dhe afrim kamere si v2.
- ⚠️ Kontinuiteti: plate-i i Shot 6 është nga kuadri i vjetër i Shot 5; kutia DreamDuo lart-majtas është ajo e AI-së, ndërsa te Shot 5 v4 kutia vjen nga foto reale.
