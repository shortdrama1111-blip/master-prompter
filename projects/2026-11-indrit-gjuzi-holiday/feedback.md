# Feedback gjatë projektit

Shëno menjëherë, me fjalët e përdoruesit. 👍 pëlqen · 👎 s'pëlqen · 💡 zbulim · 🔧 rregull i ri

| Data | Lloji | Çfarë tha | Konteksti (shot / prompt / model) | Propozim: ku shkon |
|---|---|---|---|---|

- 🔧 "po per krishtlinte e" → fushatë Krishtlindjesh.
- 🔧 "e vendoshim n fund shkrimin ska problem pasi esht shot m vete": teksti i etiketës shtohet në montim.
- 🔧 "si te referenca": struktura ndjek referencën (girlanda + kutia që përmbyset).
- 🔧 "perdor seedance-clean": rregullat e `seedance-clean` për këtë projekt.
- 🔧 "ndoshta mund ti bejm dhe scene by scene nga 4s dhe i presim": 6 gjenerime nga 4 s, prerja në montim.
- 🔧 "me bej crop vetem pjeset e para dhe t vendosim seedance edit": edito, mos rigjenero; mban 0–2 s të v1.
- 🔧 "give me the reference video ... i want to place my products there": qasje v2v mbi klipet e referencës.

## Feedback nga klienti (Vasil AI, WhatsApp 11/19/2026, për raftet / Shot 1)
- 🔧 Sfond Mocha / Dark Taupe, ndriçim luksoz, rafte minimaliste.
- 🔧 Pjesa e brendshme e rafteve pak më e errët.
- 🔧 Drita LED të ngrohta, 3200K.
- 🔧 Rafte elegante ngjyrë champagne.
- 🔧 Dritë e butë përpara produkteve që të lexohen etiketat.
- 🔧 Kontrast i dukshëm mes shisheve të bardha dhe sfondit.
→ Zëvendëson botën velur pjeshkë-rozë. Blloku i dritës rishkruhet.
- 👎 "it created them with ouai label": v2v mbajti etiketat OUAI.
- 🔧 "m jep t krijoj foton e par t references me nano banana dhe e editojm": frame-first, Nano Banana edit mbi frame-in e parë të referencës.
- 👍 Start frame Nano Banana v2 (pa frame reference), mocha + champagne: "kjo ka dal shume mire" → refs/shot1-startframe.jpg.
- 💡 "dy ashensoret anesor te levizin poshte, ai i mesit lart": kolonat lëvizin si ashensorë në drejtime të kundërta, kamera e fiksuar.
- 👍 Shot 1 aprovuar: "okej duket mire" → shot1-v4_right-reversed.mp4 (kolona e djathtë e luajtur mbrapsht në montim).
- 👍 Start frame Shot 2 (Nano Banana v1) aprovuar → refs/shot2-startframe.jpg.
- 👍 Start frame Shot 3 (girlanda) aprovuar → refs/shot3-startframe.jpg.
- 👎 Shot 3 v1: "a vase disappear and then it stops".
- 💡 Shot 3: "they are not sliding": produktet duhet të rrëshqasin përgjatë spirales, si te referenca.
- 💡 Shot 3: "i want them to move in the air like from left to right": lëvizje organike në ajër, jo rrëshqitje lineare.
- 👍/👎 Shot 3 v4: "its good" por "they disappear" në fund dhe "not moving left and right in the air as i said swinging": lavjerrës para-mbrapa.
- 🔧 Shot 3: "they just have to get out of the camera not disappear", 10 s. Lëkundja nuk është më kusht.
- 👍 Shot 3 v6 aprovuar: "this was it, nice" → hf_20261121_000526_7857f566.
- 🔧 "duhet nje reference image first": çdo shot nis me start frame Nano Banana, pastaj video.
- 👍 Shot 4 frame v1 i mirë, por "the one is almost falling, i want the falling part to be after the video start": DreamDuo duhet drejt në frame-in e parë.
- 👍 Shot 4 start frame (edit v2, DreamDuo drejt) → refs/shot4-startframe.jpg.
- 🔧 Shot 4: kutia del nga kuadri poshtë që të lidhet me Shot 5 (match cut me kutinë që bie mbi kullë).
- 🔧 Shot 4: "e dua dhe raftin poshte, te vazhdoje i shkeputur dhe te bien nga te dyja": konvejeri i poshtëm mbetet me buzë më djathtas; bie nga një DreamDuo prej secilit.
- 👍 Shot 4 v3 aprovuar ("Po, Shot 5") → hf_20261121_170213_a078c252.
- 👍 Start frame Shot 5 (kulla e dhuratave) aprovuar → refs/shot5-startframe.jpg.
- 👍 Shot 5 v1 aprovuar ("Po, Shot 6") → hf_20261121_171453_d9872f4d.
- 🔧 Shot 6: "ska si te shfaqet out of nowhere, eshte gabim logjik": çdo objekt në një shot të mëvonshëm duhet të ekzistojë që në shot-in e mëparshëm. Etiketa shtohet te Shot 5 me edit.
- 🔧 "nuk e shtoi ribbonin, duhet me e rikriju 5 me ribbon, le te gjenerojme foton e bazes": rikrijim nga start frame me etiketë.
- 👎 Shot 5 v2: "zbret shume keq, dua qe te vije me mire zbritja".
- 💡 "shiko sa keq hidhet... mund ta bësh me Blender": rëniet e objekteve me fizikë → Blender + composite mbi plate, jo Seedance.
- 👍💡 Shot 5 Blender: "kjo eshte perfekte, ne mund te bejme te gjitha keshtu". Metoda: AI për botën (start frame), Blender për fizikën/animacionin mbi plate statike.
- 👍 Start frame Shot 6 (close-up etiketa) → refs/shot6-startframe.jpg.
- 💡 Shot 6: përdoruesi kërkoi test me "Gëzuar Festat", sa më afër referencës ("po te bej challenge").
- 🔧 Montazhi final: "mos harro ti shtosh dhe ndonje muzike" (ElevenLabs ose muzika e referencës pa SFX).

## Feedback nga klienti mbi montazhin final v2 (11/21)
- 🔧 Shot 1: klienti dha start frame të ri (raftet mocha, 3 kolona); kërkon ashensorët që lëvizin. → refs/shot1-client-frame-screenshot.jpg (screenshot, rezolucion i ulët).
- 👎 Shot 3: "keto si fjongo duken shume cheap, sikur jane ne garze etj" → zëvendësim i fjongove/fjongëve.
- 🔧 Shot 5: "pak me afer" → kuadër më i afërt i kullës.

## Shot 1 ribërje (11/21, pas montazhit v2)
- 🔧 Përdoruesi dha start frame-in e ri (768×1376) → refs/shot1-client-frame-v2.jpg: "une mendoj qe te jap nje start frame dhe ti te handlesh the rest sepse ngelen shume me te qarta se cfare produkte jane". Animimi bëhet pa gjenerim video, që produktet të mbeten të qarta.
- 🔧 "etiketat i ben shume me te mira ti?": etiketat duhet të jenë të lexueshme (në frame, teksti AI është i deformuar: "INORIT GJUZI", "NOURISHCHING").
- 🔧 "duhet qe te jete pak me afer shoti qe te lexohet qarte": kuadër më i afërt.
- 🔧 Shot 1: "shiko sa zgjat videoja e references ... e dua njësoj" → kohëzgjatja dhe shpejtësia si te ref-shot1: 1.67 s, lëvizje konstante; anësoret ~0.33 kat/s, mesi ~0.41 kat/s (matje: 120 px/s dhe 150 px/s në 720×1280, kati ~355 px).
- 🔧 Shot 1: zoom 1.35×, "dua të duken të tre kolonat dhe gjithashtu të lexohen mirë etiketat".
- 🔧 "mos me gjenero me me higgsfield ... do ti bej un manuale": Claude nuk gjeneron më vetë në Higgsfield. Jep promptin gati për kopjim; gjenerimet i bën përdoruesi me dorë. (Një gjenerim plate-i, job 500bae6c, ishte nisur para mesazhit.)
- 🔧 Shot 1 v5: "duhet pak me larg qe te duket tamam 3 kolonat sepse kolonat anesore nuk kan borderat anesore": kuadri duhet të përfshijë kornizat e jashtme të kolonave anësore. 1.35× ishte shumë afër.
- 👎 Shot 1 v6: "si m duket sikur nuk jan reale, sikur jan edited, se di ca mungon": produktet duken të ngjitura mbi plate.
- 💡 "blenderi me mcp lokalisht është më mirë": përdoruesi preferon Blender lokal me MCP (GPU, viewport live, skedari .blend te ai) në vend të bpy në cloud.
