# Skenari v2: "ATA MË SOLLËN DERI KËTU"

> **Logline:** Një djalë rritet brenda një ndjekjeje me policinë që zgjat katër epoka. Në çdo epokë,
> heronjtë e asaj kohe i bashkohen për ta mbrojtur. Kur policia i zë në kurth në një urë mbi kënetë,
> vijnë dy heronjtë e rinj për ta marrë. Ka vend vetëm për një, dhe të vjetrit qëndrojnë pas.

**Kohëzgjatja: 60 s** · **Formati: 9:16** (pret konfirmim) · **Modeli: Seedance 2.5** ·
**Muzika: në montim** (promptet me `no music`, me zhurmat e skenës) · **Pa dialog**

*(v1 "Të gjithë ishin unë" mbetet në historinë e git-it.)*

---

## 0. Kufiri i IP-së: si i sjellim personazhet pa i emërtuar
Heronjtë e lojërave **nuk mund të hyjnë me emër ose me fytyrën e tyre**. Fytyrat e tyre janë të aktorëve
realë, dhe modeli ose i bllokon, ose i shtrembëron. I sjellim si **arketipe**: veshja ikonike, makina, roli
dhe mënyra e lëvizjes, me **fytyra origjinale**. Kush ka luajtur i njeh menjëherë nga silueta. Kjo është
e njëjta gjë që bëjnë referencat, por pa rrezikun e bllokimit.

"Lufta me policinë" = ndjekje, bllokime me makina, rrëshqitje, kërcime. **Pa armë.** Sakrifica tregohet si
"ata qëndrojnë dhe ngrenë duart mes dritave të policisë", jo me dhunë.

---

## 1. Vendimet e regjisorit

**Pse 60 s.** Katër epoka × ~9 s = 36 s, plus 2 s hook dhe 22 s për kurthin, shpëtimin dhe ndarjen.
Shpëtimi dhe sakrifica janë zemra e filmit, ndaj marrin kohë që të ndihen. Struktura ka **3 sekuenca nga
20 s**, të prodhuara në **6 blloqe gjenerimi** (~10 s secili, çdo epokë me dritën e vet).

**Harku:**
| Faza | Koha | Ndjesia | Ndërtimi |
|---|---|---|---|
| Kujtimi | 0–20 s | nostalgji | Egli i vogël, heronjtë e parë, ngjyrat e ngrohta |
| Ngjitja | 20–40 s | adrenalinë | policia dhe konvoji rriten bashkë, prerjet shkurtohen |
| Kurthi | 40–46 s | rrezik | policia përpara dhe mbrapa, s'ka dalje |
| Shpëtimi + sakrifica | 46–60 s | drithërimë, mall | varka del nga këneta, të vjetrit bëjnë mur, Egli ikën dhe shikon pas |

**Katër pajisjet e regjisë:**
1. **"Wanted" që rritet, dhe miqtë që rriten bashkë me të.** Policia: 1 makinë → 2 → helikopter + 4 →
   kurth i plotë. Konvoji i heronjve: 1 → 2 → 5. *Sa më shumë policë, aq më shumë miq.*
2. **Rima e pasqyrës, që tani tregon kohën.** Çdo epokë hapet me sytë e Eglit në pasqyrë, por **sytë
   rriten**: fëmijë → adoleshent → i ri → sot. Shikuesi sheh një jetë të tërë në katër kuadro identike.
3. **Zari i kuq.** Te '86, heroi i parë e var zarin e kuq te pasqyra e tij. Zari udhëton në çdo makinë që
   ngas Egli. Në sakrificë, heroi i '86 ia hedh çelësat me zarin: "ik". I vetmi objekt i kuq në film (aksenti 10%).
4. **Egli kalon nga sedilja e pasagjerit te timoni.** '86: pasagjer. '92: sedilja e pasme. Sot: në timon,
   për herë të parë. VI: drejton konvojin. Në fund, pasagjer sërish, por i të rinjve. Rritja tregohet me vendin në makinë.

**Kalimet mes epokave:**
| Nga → te | Kalimi |
|---|---|
| Syri → '86 | push-in në syrin e fëmijës ku reflektohet neoni |
| '86 → '92 | errësira e tunelit |
| '92 → sot | **match cut** mbi kërcimin e lowrider-it: ngrihet në '92, ulet sot |
| sot → VI | push-in në ekranin e telefonit në panel, që transmeton live një urë me neon |
| kurthi → shpëtimi | errësirë: prozhektori i helikopterit fiket për 0.5 s, pastaj zhurma e varkës |

---

## 2. Personazhet

### Egli, në katër mosha
Baza është **character sheet-i yt**. Unë të jap promptet e edit-it për çdo moshë.
| Versioni | Mosha (propozim) | Veshja | Ku ulet |
|---|---|---|---|
| `@egli_kid` | ~10 | bluzë pastel e madhe, shorte, atlete të bardha | pasagjer, '86 |
| `@egli_teen` | ~15 | bluzë e bardhë e madhe, xhinse të gjera, kapelë mbrapsht | sedilja e pasme, '92 |
| `@egli_young` | ~22 | këmishë-xhaketë ngjyrë rëre, bluzë e bardhë, syze të zeza | në timon, sot |
| `@egli_now` | mosha jote | xhaketë teknike e zezë, zinxhir argjendi | në timon, VI, pastaj në varkë |

### Heronjtë, si arketipe me fytyra origjinale
| Tag | Epoka | Arketipi (veshja + roli) | Mjeti |
|---|---|---|---|
| `@hero_86` | '86 | burrë ~35, flokë të zeza pas, **këmishë havajane bruz me palma**, zinxhir ari, xhinse të çelura | kupe sportive e bardhë, në formë pyke |
| `@hero_92` | '92 | burrë zezak ~25, flokë shumë të shkurtra, **kanotiere e bardhë**, xhinse blu të çelura | lowrider jeshil "candy", rrota ari |
| `@hero_v_suit` | sot | burrë ~45, flokë të thinjur pas, **kostum blu i errët, këmishë e bardhë e hapur** | sedan luksoz i zi |
| `@hero_v_young` | sot | burrë zezak ~25, **xhaketë bomber ulliri, bluzë e bardhë** | motor sportiv |
| `@hero_v_wild` | sot | burrë ~45, flokë të rralla, **bluzë e bardhë e njollosur**, sy të egër | pikap off-road i rrahur |
| `@duo_vi_her` | VI | grua latine ~30, flokë kaçurrela të errëta në bisht, **kanotiere e zezë, xhaketë xhins**, vathë ari rrethore | varkë me ajër (airboat) |
| `@duo_vi_him` | VI | burrë ~32, mjekër e shkurtër, krahë me tatuazhe, kapelë | në varkë, i jep dorën Eglit |

⚠️ Janë **11 karta karakteri** (4 Egli + 7 heronj). Është shumë punë, por pa to fytyrat ndryshojnë nga
shot-i në shot. Rregulli: `@tag` hyn vetëm në bllokun ku personazhi është i pranishëm.

---

## 3. Bota

| Epoka | Vendi | Drita (blloku i fiksuar) | Paleta 60:30:10 | Policia | Konvoji |
|---|---|---|---|---|---|
| **'86** | bulevard bregdetar, art-deco, palma, asfalt i lagur | natë, neon magenta majtas + cian djathtas | blu-natë · magenta/cian · zari | 1 makinë '80 | `@hero_86` (Egli pasagjer) |
| **'92** | lagje periferike, palma të larta, tela elektrikë | perëndim, diell 3200K, smog 30% | portokalli · kafe-ulliri · zari | 2 makina | lowrider + kupeja e bardhë |
| **sot** | rrugë malore mbi qytet, kodra të thata | mesditë 5600K, valë nxehtësie | bezhë · blu-qielli · zari | helikopter + 4 makina | + sedani, motori, pikapi |
| **VI** | urë e gjatë mbi kënetë, qytet LED në horizont | natë, LED vjollcë + bruz, prozhektor 6000K | vjollcë · bruz · zari | kurth: rreshta makinash përpara dhe mbrapa | të gjithë |
| **Agimi** | kanali i kënetës, ura mbrapa | drita e parë, horizont 3500K, hije 7000K, mjegull 40% | ar · blu-agimi · zari | dritat larg | varka + Egli |

---

## 4. SKENARI ME TIMECODE

**K** = kuadri/kamera · **V** = veprimi · **D** = drita · **Z** = zëri (Seedance; muzika në montim) · **Pse** = arsyeja

---

### SEKUENCA I: "KUJTIMI" · 0:00–0:20

#### G1: Hook + '86 · 0:00–0:10.5
`[REF: @egli_kid]` `[REF: @hero_86]` `[REF: @loc_86]` `[REF: @car_86]` `[REF: @dice_keys]`

**SHOT 1 · 0:00–0:02 · HOOK: syri i fëmijës**
- **K:** ECU i syrit të një fëmije 10-vjeçar, FOV 12°, push-in 0.5 km/h.
- **V:** errësirë. Në 0.3 s ndizet drita blu e një televizori të vjetër. Në bebëzë reflektohen palma dhe neon
  rozë në lëvizje. Pulit një herë, në 1.6 s.
- **Z:** zukatja e televizorit që ndizet, pastaj një motor V8 që afrohet.
- **Pse:** një botë e tërë brenda syrit të një fëmije. Në 2 s shikuesi kupton "kjo është fëmijëria ime".

**SHOT 2 · 0:02–0:03.5 · RIMA #1: pasqyra, sytë e fëmijës**
- **K:** CU i pasqyrës së brendshme, FOV 29°, dridhje dore 2 cm.
- **V:** sytë e Eglit 10-vjeçar, që mezi arrijnë lart sa të shohin në pasqyrë. Një dorë burri (unaza ari)
  var **zarin e kuq** te pasqyra. Në xhamin e pasmë, larg, ndizet **një** makinë policie.
- **D:** shirita neoni magenta/cian rrëshqasin mbi fytyrë.
- **Pse:** zari lind këtu, nga dora e heroit të parë. Policia e parë.

**SHOT 3 · 0:03.5–0:06.5 · Heroi i parë**
- **K:** MS frontal përmes xhamit të përparmë, kamera ecën para makinës me 60 km/h, FOV 47°.
- **V:** `@hero_86` në timon, këmisha havajane bruz valon në erë, krahu jashtë dritares. Kthen kokën nga
  fëmija dhe i shkel syrin. Egli i vogël buzëqesh me gjithë fytyrën, me dhëmbët e përparmë të dukshëm.
- **D:** neon nga të dy anët, asfalt i lagur.
- **Pse:** marrëdhënia në 3 s: heroi e mbron fëmijën. Këtu fillon gjithçka.

**SHOT 4 · 0:06.5–0:08.5 · Bulevardi**
- **K:** WS i ulët 40 cm mbi asfalt, tracking paralel me 70 km/h, FOV 84°.
- **V:** kupeja e bardhë kalon mes hoteleve art-deco dhe palmave. Makina e policisë del nga një rrugicë mbrapa.
- **Z:** Doppler, spërkatje uji, sirena '80.

**SHOT 5 · 0:08.5–0:10.5 · Tuneli**
- **K:** WS nga mbrapa, ndjek me 80 km/h, FOV 63°.
- **V:** kupeja zhytet në tunel. Kuadri **i zi i plotë** në 10.0–10.5 s.
- **Pse:** pika e bashkimit me bllokun tjetër, dhe kalimi i viteve.

#### G2: '92 · 0:10.5–0:20
`[REF: @egli_teen]` `[REF: @hero_92]` `[REF: @hero_86]` `[REF: @loc_92]` `[REF: @car_92]` `[REF: @car_86]` `[REF: @dice_keys]`

**SHOT 6 · 0:10.5–0:12 · Dalja**
- **K:** WS nga brenda tunelit drejt daljes, FOV 63°.
- **V:** nga errësira del lowrider-i jeshil drejt diellit portokalli, me kupenë e bardhë pas tij.
- **D:** diell 3200K në kamerë, flare, smog 30%.
- **Pse:** shpërthimi i ngjyrës = epokë e re. Kupeja e bardhë mbrapa = heroi i parë është ende këtu.

**SHOT 7 · 0:12–0:13.5 · RIMA #2: sytë 15-vjeçarë**
- **K:** identik me Shot 2.
- **V:** sytë e Eglit adoleshent nga sedilja e pasme, nën strehën e kapelës. Zari lëkundet, tani te pasqyra e
  lowrider-it. Mbrapa: **dy** makina policie.
- **Pse:** sytë u rritën, policia u dyfishua.

**SHOT 8 · 0:13.5–0:17 · Bllokimi i parë**
- **K:** WS nga lart 4 m, kamera tërhiqet para konvojit me 40 km/h, FOV 63°.
- **V:** `@hero_92` në timon, krahu i majtë jashtë. Ngre dy gishta nga pasqyra drejt kupesë së bardhë mbrapa.
  Kupeja e bardhë ngadalëson dhe kthehet tërthor në rrugë. Dy makinat e policisë frenojnë me tym nga gomat.
  Egli adoleshent kthehet në sedilje dhe shikon nga xhami i pasmë.
- **Z:** gomat, sirenat që priten shkurt.
- **Pse:** heronjtë fillojnë ta mbrojnë. Bllokimi me makinë është lufta jonë, pa armë.

**SHOT 9 · 0:17–0:20 · Kërcimi**
- **K:** WS anësor i ulët 30 cm, FOV 84°.
- **V:** `@hero_92` shtyp hidraulikën dhe lowrider-i ngre pjesën e përparme 60 cm. **HARD MATCH CUT në pikun e kërcimit.**
- **Z:** fërshëllima e hidraulikës.

---

### SEKUENCA II: "NGJITJA" · 0:20–0:40

#### G3: sot · 0:20–0:30
`[REF: @egli_young]` `[REF: @hero_v_suit]` `[REF: @hero_v_young]` `[REF: @hero_v_wild]` `[REF: @loc_now]` `[REF: @car_now]` `[REF: @dice_keys]`

**SHOT 10 · 0:20–0:21.5 · Ulja**
- **K:** WS anësor, i njëjti drejtim lëvizjeje si Shot 9, FOV 84°.
- **V:** kupeja e zezë mat bie nga kreshta me të katër rrotat në ajër dhe ulet me 90 km/h. Pluhur.
- **D:** mesditë 5600K, valë nxehtësie.
- **Pse:** ulja i përgjigjet ngritjes. Drita e bardhë thyen ngrohtësinë e kujtimit: jemi në të tashmen.

**SHOT 11 · 0:21.5–0:23 · RIMA #3: sytë 22-vjeçarë, në timon**
- **K:** identik me Shot 2, por tani nga sedilja e pasagjerit drejt shoferit.
- **V:** sytë e Eglit të ri pas syzeve të zeza, **në timon për herë të parë**. Zari lëkundet. Hija e
  helikopterit kalon mbi makinë.
- **Pse:** fëmija që ishte pasagjer tani ngas vetë.

**SHOT 12 · 0:23–0:27 · Konvoji i ri**
- **K:** EWS nga drone 25 m, ndjek konvojin në kthesat e kodrës, FOV 84°.
- **V:** katër makina policie afrohen. Nga një rrugë anësore del sedani i zi i `@hero_v_suit` dhe zë rreshtin
  pas Eglit. Motori sportiv i `@hero_v_young` kalon mes dy makinave policie me 120 km/h. Pikapi i rrahur i
  `@hero_v_wild` del nga pluhuri jashtë rrugës dhe e shtyn një makinë policie anash, që rrotullohet në bar
  të thatë (pa përplasje me njerëz).
- **Z:** rotori, motorët, kërcitja e metalit.
- **Pse:** konvoji bëhet ushtri. Çdo hero vjen me stilin e vet: elegant, i shpejtë, i çmendur.

**SHOT 13 · 0:27–0:30 · Në ekran**
- **K:** CU i telefonit në mbajtësen e panelit, push-in 3 km/h, FOV 47° → 29°.
- **V:** telefoni transmeton live një urë mbi kënetë natën, me neon vjollcë dhe dritat e policisë që presin.
  Kamera shtyhet derisa ekrani bëhet kuadri.
- **Z:** zhurmat e mesditës zbehen dhe dalin sirenat e natës e insektet e kënetës.
- **Pse:** në 9:16 ekrani = kuadri. Epoka e social media-s lind nga ekrani, dhe tregon kurthin që i pret.

#### G4: VI, kurthi · 0:30–0:40
`[REF: @egli_now]` `[REF: @hero_86]` `[REF: @hero_92]` `[REF: @hero_v_suit]` `[REF: @hero_v_young]` `[REF: @hero_v_wild]` `[REF: @loc_vi]` `[REF: @car_vi]` `[REF: @dice_keys]`

**SHOT 14 · 0:30–0:32 · Ura**
- **K:** EWS nga drone 30 m, ndjek me 100 km/h, FOV 84°.
- **V:** kabrioleti vjollcë i Eglit **prin**, pas tij në rresht kupeja e bardhë, lowrider-i, sedani, motori,
  pikapi. Mbrapa, një lumë dritash kuq-blu.
- **D:** LED vjollcë/magenta në ujë, prozhektori i helikopterit mbi konvoj.
- **Pse:** imazhi i gjithë historisë: të gjitha epokat në një rresht, me Eglin përpara.

**SHOT 15 · 0:32–0:33.5 · RIMA #4: sytë e sotëm**
- **K:** identik me Shot 2.
- **V:** sytë e Eglit sot, në fytyrë drita e telefonit. Zari lëkundet. Në xhamin e pasmë: gjithë konvoji,
  dhe pas tyre kuq-blu nga skaji në skaj.
- **Pse:** rima e fundit, kuadri më i mbushur, me të gjithë që i ka mbrapa.

**SHOT 16 · 0:33.5–0:35.5 · Publiku**
- **K:** MS, kamera e fiksuar te parmaku, FOV 63°.
- **V:** tre të rinj filmojnë me telefona vertikal ndërsa konvoji kalon me 100 km/h. Flokët u lëvizin nga
  ajri, njëri ngre grushtin dhe bërtet nga gëzimi.
- **Pse:** epoka VI: ndjekja është show live.

**SHOT 17 · 0:35.5–0:38 · Kurthi**
- **K:** WS frontal i ulët, FOV 47°.
- **V:** në fund të urës, një mur makinash policie tërthor me drita të ndezura. Kabrioleti frenon dhe
  rrëshqet 90°, ndalon 15 m para tyre. Mbrapa konvojit mbyllet një mur i dytë. Konvoji ndalon. Kurth.
- **Z:** gomat, sirenat në maksimum.

**SHOT 18 · 0:38–0:40 · S'ka dalje**
- **K:** CU i Eglit, FOV 18°, kamera e fiksuar.
- **V:** Egli shikon majtas, djathtas, mbrapa. Nofulla shtrëngohet. Prozhektori i bie drejt në fytyrë, pastaj
  **fiket** dhe kuadri bëhet i zi në 39.5–40 s. Nga errësira dëgjohet një zhurmë e fortë helike në ajër që afrohet nga këneta.
- **Pse:** kulmi i rrezikut. Zhurma në errësirë është premtimi i shpëtimit, para se ta shohim.

---

### SEKUENCA III: "SHPËTIMI" · 0:40–1:00

#### G5: Shpëtimi dhe sakrifica · 0:40–0:50
`[REF: @egli_now]` `[REF: @duo_vi_her]` `[REF: @duo_vi_him]` `[REF: @hero_86]` `[REF: @hero_92]` `[REF: @hero_v_suit]` `[REF: @hero_v_young]` `[REF: @hero_v_wild]` `[REF: @loc_vi]` `[REF: @airboat]` `[REF: @dice_keys]`

> ⚠️ Ky është blloku më i rëndë: 8 personazhe në 10 s. **Frame-first:** fillimisht gjenerojmë një imazh me
> heronjtë e vjetër në rresht te makinat, dhe pastaj e animojmë. Nëse Seedance i ngatërron, e ndajmë në dy blloqe 5-sekondësh.

**SHOT 19 · 0:40–0:42.5 · Varka**
- **K:** WS nga niveli i ujit, pranë një shtylle të urës, FOV 84°.
- **V:** nga errësira e kënetës del një **airboat** me 70 km/h, me helikën e madhe që ngre mjegull uji. Kthehet
  anash poshtë urës dhe ndalon pranë parmakut. `@duo_vi_her` në timon me flokët në erë. `@duo_vi_him` qëndron
  në këmbë dhe ngre dorën drejt Eglit lart te parmaku.
- **D:** dritat e policisë nga lart, në ujë LED vjollcë, në varkë një dritë e bardhë e vogël.
- **Pse:** heronjtë e rinj nuk vijnë në rrugë, por nga këneta. Vijnë nga një botë e re.

**SHOT 20 · 0:42.5–0:45 · Vendimi**
- **K:** MS i heronjve të vjetër në rresht, FOV 47°, dolly anësor i ngadaltë 2 km/h.
- **V:** heronjtë e '86, '92 dhe sot shikojnë varkën, pastaj njëri-tjetrin. `@hero_86` bën me kokë një herë.
  Pa fjalë, secili kthehet te makina e vet.
- **Pse:** varka ka vend vetëm për një. Vendimi merret me sy, pa dialog.

**SHOT 21 · 0:45–0:47.5 · Muri**
- **K:** WS i lartë 6 m, FOV 63°.
- **V:** makinat e heronjve rrotullohen tërthor dhe formojnë një mur të vetëm mes policisë dhe Eglit.
  Heronjtë dalin dhe qëndrojnë para makinave, me shpinën nga Egli, përballë dritave.
- **Pse:** sakrifica. Ata e mbrojnë me trupin e tyre, ashtu si e kanë mbrojtur gjithë jetën.

**SHOT 22 · 0:47.5–0:50 · Çelësat**
- **K:** MS, `@hero_86` kthehet nga kamera, FOV 29°.
- **V:** heroi i '86 ia hedh Eglit çelësat me zarin e kuq me një hark të butë. Egli i kap me një dorë, kalon
  parmakun dhe hidhet në varkë. `@duo_vi_him` e kap për krahu.
- **Pse:** stafeta. Zari që ia dha kur ishte fëmijë, tani ia kthen.

#### G6: Ndarja në agim · 0:50–1:00
`[REF: @egli_now]` `[REF: @duo_vi_her]` `[REF: @duo_vi_him]` `[REF: @hero_86]` `[REF: @airboat]` `[REF: @loc_dawn]` `[REF: @dice_keys]`

**SHOT 23 · 0:50–0:53 · Shikimi pas**
- **K:** MCU i Eglit në varkë, kamera përballë tij, FOV 29°. Ura mbrapa tij, jashtë fokusit.
- **V:** varka largohet me 60 km/h. Egli kthen kokën pas. Në urë, heronjtë e vjetër qëndrojnë para makinave,
  të rrethuar nga dritat kuq-blu, me duart lart. `@hero_86` ngre dy gishta në ballë si përshëndetje.
  Gryka e Eglit lëviz kur gëlltit një herë.
- **D:** horizonti fillon të zbardhë, 3500K, dritat e policisë zbehen në mjegull.
- **Z:** helika e varkës, sirenat që largohen. (Muzika: momenti më i ndjerë.)
- **Pse:** kjo është skena që mbetet në mendje. Ata e sollën deri këtu.

**SHOT 24 · 0:53–0:55.5 · Zari**
- **K:** ECU i dorës, FOV 12°, slow-motion i lehtë.
- **V:** Egli hap grushtin. Zari i kuq në pëllëmbë, i ndriçuar nga rrezja e parë e diellit.
- **Pse:** aksenti i kuq i ndërtuar në 55 s merr kuptim: luaj sërish, për ta.

**SHOT 25 · 0:55.5–1:00 · Aerial-i**
- **K:** drone fillon 5 m mbi varkë dhe ngjitet vertikalisht me 15 km/h deri në 80 m. FOV 84°.
- **V:** Egli kthehet përpara. `@duo_vi_her` i hedh një vështrim dhe vë syzet. Varka çan kënetën e artë me
  një gjurmë në formë V. Ura dhe dritat mbeten të vogla mbrapa. **40% e sipërme e kuadrit** = qiell agimi për
  tekstin. Kamera **vazhdon të ngjitet deri në fund**, pa ngrirje.
- **Z:** helika, zogjtë e kënetës.

**TEKST NË MONTIM (propozim):** `1986 · 1992 · 2013 · 2026` → `Ata më sollën deri këtu.` / `They brought me here.`

---

## 5. Ritmi dhe muzika
- **Prerje mesatare:** 2.5 s (I) → 1.8 s (II) → 2.5 s (III, merr frymë për emocionin).
- **Muzika (propozim):** synthwave '80 → G-funk '92 → trap → **heshtje në 0:39.5** → hyrja e varkës mbi një
  bas të thellë → finale emocionale synth + orkestër. Tempo bazë 96 BPM.

## 6. Plani i prodhimit (asgjë e gjeneruar ende)
1. Edit-et e moshave nga sheet-i yt (×4).
2. Kartat e heronjve (×7), sipas hard rule #13.
3. Plate-t e lokacioneve (×5) dhe product sheet-et (6 mjete + çelësi me zar).
4. Imazhi start për G5.
5. Video G1 → G6.
6. Montimi, muzika, teksti.
