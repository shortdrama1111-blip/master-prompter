# Skena 3 · patch-et (shtesa të veçanta, 9:16, 4 s secila)

Analiza e rezultatit `hf_20261114_190001` (12 s, prerjet 1.5/3/4.5/5.96/7.42/9/10.42):

| Shot | Koha | Gjykimi | Çfarë është gabim |
|---|---|---|---|
| 1 PCH, zbritja | 0–1.5 | ✅ mbahet | kupeja e vogël dhe larg; zbritja lexohet pak, por funksionon |
| 2 pasqyra + zari | 1.5–3 | ✅ mbahet | — |
| 3 helikopteri, diamanti | 3–4.5 | ✅ mbahet | 7 makina policie në vend të 4, numri "24" dy herë: s'bie në sy |
| 4 Michael | 4.5–6 | ⚠️ mbahet si "mbërritja" | kamera është te krahu i një makine të errët (lexohet si kupeja e Eglit); Michael vjen anash e përshëndet, **asnjë makinë policie**: s'ka prerje para policisë |
| 5 Franklin | 6–7.5 | 👎 patch A | **motori pa duar**: timoni lëviz vetë, s'ka kalorës |
| 6 Trevor | 7.5–9 | 👎 patch B | **arushi rri mbi një parmak druri të kuq**, kamera statike: lexohet si arush në gardh që sheh policinë të rrotullohet vetë; pa pikap, pa goditje |
| 7 konvoji | 9–10.5 | 👎 patch C | xhami anësor, jo i pasmë; sfondi kthehet te shkëmbi i PCH (ishim në autostradë); konvoji jo i plotë (motori + 2 makina; mungojnë kupeja e bardhë, lowrider-i, pikapi) |
| 8 billbordet | 10.5–12 | 👎 patch D | **natë** në mes të ndjekjes së mesditës; billbordet mbi qytet, jo pranë autostradës; ekranet tregojnë rrugë me policë, jo urën |
| 4b opsional | — | patch E | Michael pret policinë (veprimi që mungon te shot 4) |

**Shkaku** (rregulli 11): shot 5 dhe 6 ishin POV të montuara në automjet; me blockout-in modeli
mori pozicionin e kamerës, por jo trupin/automjetin që e mban: POV pa duar = motor bosh, POV
me arushin = arush në gardh. Patch-et B dhe D ndryshojnë këndin në ekster, ku automjeti
lexohet i plotë. Shot 8: rreshti "a live stream of a long bridge at night" e tërhoqi gjithë
kuadrin në natë.

Montimi: 0–6.0 nga origjinali → A (1.5 s) → B (1.5–2 s) → C (1.5 s) → D (1.5–2 s, deri te
ekrani vjollcë i plotë) → kalim te skena 4. E opsionale: futet pas shot-it 4 (1.2 s).

---

## Patch A · Franklin, motori me duar · 4 s

**Rendi:** `@image1` franklin-sheet-masked.png · `@image2` sheet-i i motorit jeshil · `@image3` loc_now_freeway.jpg

```
SCENE CONTEXT
Los Angeles today, hard midday sun, on a wide concrete freeway. A young man on a green touring motorbike threads at speed between two black-and-white police cruisers and pulls ahead. Vertical 9:16, live-action, photoreal, one continuous shot.

ACTIVE REFERENCES
@image1: the rider, twenty-five, olive bomber jacket, white t-shirt, black riding gloves. Face and wardrobe 100% match the reference.
@image2: the touring cruiser motorbike in gloss green with a batwing fairing and saddlebags. 100% matches the reference.
@image3: the freeway: concrete lanes, barriers, overpasses, blank green gantry signs, the downtown skyline ahead. Reference defines architecture, geography and dressing ONLY — not a keyframe.

THE POLICE
Modern black-and-white police sedans with blazing red and blue LED light bars, driving forward in the same direction as the bike.

OPTICS
Wide 100° field of view from the rider's point of view, deep focus.

CAMERA
Mounted just above the bike's fuel tank at the rider's chest height, looking forward down the freeway, moving with the bike, leaning with it.

ACTION
The rider's own forearms in olive bomber sleeves reach into the bottom of the frame from both sides, his black-gloved hands gripping both handlebar grips; the gloss green tank and fairing fill the lower third. Two police cruisers drive side by side ahead at 110 km/h; the bike closes at 140 km/h, his right hand twists the throttle, the bike leans left then right and slips through the 0.5 m gap between the two cruisers, their side mirrors flashing past on both edges of the frame, and pulls ahead onto the open lane.

PERFORMANCE
His gloved fingers tighten on the grips, the knuckles bunch under the leather, a quick small correction of the bars as the gap closes.

PHYSICS
Real weight: the bike leans and corrects, the fairing vibrates, wind tugs at the bomber sleeves, heat shimmer bends the distance, the cruisers rock slightly on their suspension.

LIGHTING
LIGHTING: Midday, present day. Hard sun high overhead at 5600K from camera right, short crisp shadows under every rock, post and palm, bleached sandstone cliff, heat shimmer rising from the asphalt over the first 30 m, deep clean blue sky with a few white clouds, high contrast, clean modern digital look.

AUDIO
No music. The bike's engine roaring up, wind roar, two sirens Dopplering past on both sides.

STYLE
Photorealistic live-action film footage, present-day Los Angeles at midday, crisp colour, fine grain, cinematic contrast.

OUTPUT SETTINGS
Vertical 9:16, real-time speed, 24 fps motion cadence, 4 seconds.

POSITIVE LOCKS
Both gloved hands stay on the handlebar grips for the whole shot. The bike is gloss green. The cruisers drive forward in the same direction as the bike.
```

---

## Patch B · Trevor e godet policinë · 4 s

**Rendi:** `@image1` trevor-sheet-masked.png · `@image2` truck_trevor-sheet.jpg · `@image3` loc_now_freeway.jpg

```
SCENE CONTEXT
Los Angeles today, hard midday sun, on a wide concrete freeway. A wild man in a faded red pickup with a teddy bear strapped to its push bar rams the rear corner of a police cruiser, which spins away onto the dirt shoulder. Vertical 9:16, live-action, photoreal, one continuous shot.

ACTIVE REFERENCES
@image1: the driver, forty-five, thinning hair, wild eyes, stained white t-shirt. Face 100% matches the reference.
@image2: the faded red 1960s off-road pickup with a rusty push bar, a worn yellow teddy bear strapped to the centre of the push bar with rope, and a roll bar with four round lamps. 100% matches the reference.
@image3: the freeway: concrete lanes, barriers, overpasses, blank green gantry signs, the downtown skyline ahead. Reference defines architecture, geography and dressing ONLY — not a keyframe.

THE POLICE
A modern black-and-white police sedan with a blazing red and blue LED light bar.

OPTICS
35 mm equivalent, 63° field of view, low, the road surface sharp in the foreground.

CAMERA
Low tracking shot 0.6 m above the asphalt, travelling alongside at the pickup's front-left corner, 4 m away, looking back at three-quarters toward its nose, moving at the same speed as the pickup.

ACTION
0.0s to 1.5s — The red pickup charges at 120 km/h, the worn yellow teddy bear bouncing on its rope against the rusty push bar, the driver hunched at the wheel behind the windscreen with a manic grin; ahead of it, in the same lane, the police cruiser at 100 km/h.
1.5s to 2.5s — The push bar hits the cruiser's rear-left corner with a hard metal crunch; the cruiser's tail snaps to the right.
2.5s to 4.0s — The cruiser spins a full 180° across the lane and slides backwards onto the dirt shoulder in a thick cloud of tan dust; the pickup roars on past the camera, the teddy bear swinging.

PERFORMANCE
The driver: eyes wide, mouth open in a laugh at the impact, head thrown back.

PHYSICS
Real weight: the pickup's nose dips at impact then rises, the cruiser's rear bumper crumples, glass shards and dust spray, the cruiser's spin has real inertia, the teddy bear's rope snaps tight.

LIGHTING
LIGHTING: Midday, present day. Hard sun high overhead at 5600K from camera right, short crisp shadows under every rock, post and palm, bleached sandstone cliff, heat shimmer rising from the asphalt over the first 30 m, deep clean blue sky with a few white clouds, high contrast, clean modern digital look.

AUDIO
No music. The pickup's engine roar, a metal crunch, tyres screeching, a wild laugh, the siren dropping away.

STYLE
Photorealistic live-action film footage, present-day Los Angeles at midday, crisp colour, fine grain, cinematic contrast.

OUTPUT SETTINGS
Vertical 9:16, real-time speed, 24 fps motion cadence, 4 seconds.

POSITIVE LOCKS
The teddy bear is strapped to the moving pickup's push bar for the whole shot. The pickup is faded red. The pickup and the cruiser drive forward in the same direction until the impact.
```

---

## Patch C · Pas tij, konvoji i plotë · 4 s

**Rendi:** `@image1` egli_young-sheet-masked.png · `@image2` sheet-i i sedanit gri · `@image3` sheet-i i motorit jeshil · `@image4` truck_trevor-sheet.jpg · `@image5` car_86-sheet.jpg · `@image6` sheet-i i lowrider-it · `@image7` loc_now_freeway.jpg

```
SCENE CONTEXT
Los Angeles today, hard midday sun, on a wide concrete freeway. A young man driving a matte-black sports coupe looks back and sees his heroes following him in a single line. Vertical 9:16, live-action, photoreal, one continuous shot.

ACTIVE REFERENCES
@image1: the driver, twenty-two, short dark hair, short beard, sand-beige overshirt over a white t-shirt, black sunglasses. Face 100% matches the reference.
@image2 @image3 @image4 @image5 @image6: the convoy behind him, in this order from nearest to farthest: the graphite-grey sport saloon, the green touring motorbike, the faded red pickup with a teddy bear on its push bar, the white 1980s wedge coupe, the candy-green lowrider with gold wire wheels. Each 100% matches its reference.
@image7: the freeway: concrete lanes, barriers, overpasses, blank green gantry signs. Reference defines architecture, geography and dressing ONLY — not a keyframe.

OPTICS
40 mm equivalent, 54° field of view, focus on the convoy through the glass, the driver's head soft in the foreground.

CAMERA
Inside the coupe on the back seat, centred, looking straight back through the rear window; the camera moves with the car, a slight road vibration.

ACTION
The rear window fills the upper two thirds of the frame; the driver's head and right shoulder sit in the lower left foreground. Through the glass, on the straight sunlit freeway receding behind, the five vehicles drive in one lane in a single line 10 m apart, all following him at the same speed; far behind them, 80 m back, a few red and blue police lights. At 1.5s the driver turns his head over his right shoulder toward the rear window and holds there.

PERFORMANCE
The driver: his jaw loosens, his lips part, a slow breath out through the nose, then the corner of his mouth lifts.

PHYSICS
Real weight: the convoy's vehicles rock gently on their suspensions, heat shimmer bends the road behind them, the coupe's cabin vibrates.

LIGHTING
LIGHTING: Midday, present day. Hard sun high overhead at 5600K from camera right, short crisp shadows under every rock, post and palm, bleached sandstone cliff, heat shimmer rising from the asphalt over the first 30 m, deep clean blue sky with a few white clouds, high contrast, clean modern digital look.

AUDIO
No music. Engines in harmony behind the glass, wind, a distant siren.

STYLE
Photorealistic live-action film footage, present-day Los Angeles at midday, crisp colour, fine grain, cinematic contrast.

OUTPUT SETTINGS
Vertical 9:16, real-time speed, 24 fps motion cadence, 4 seconds.

POSITIVE LOCKS
All five vehicles are visible through the rear window for the whole shot, in the stated order, driving toward the camera behind the coupe. The road behind is the freeway.
```

---

## Patch D · Billbordet ditën, ura në ekran · 4 s

**Rendi:** `@image1` loc_now_freeway.jpg · `@image2` loc_vi_aerial.jpg (përmbajtja e ekraneve)

```
SCENE CONTEXT
Los Angeles today, hard midday sun. Beside a wide concrete freeway, a line of tall roadside digital billboards all show the same live stream: a long bridge over a bay at night under purple and teal neon. The camera pushes into one screen until it fills the frame. Vertical 9:16, live-action, photoreal, one continuous shot.

ACTIVE REFERENCES
@image1: the freeway: concrete lanes, barriers, overpasses, blank green gantry signs, palms, the downtown skyline ahead. Reference defines architecture, geography and dressing ONLY — not a keyframe.
@image2: the image shown on every billboard screen: the long bridge over the dark bay at night, mangrove islands, the neon skyline in purple and teal, a line of red and blue police lights waiting at the top of the bridge.

OPTICS
40 mm equivalent, 54° field of view, deep focus.

CAMERA
0.0s to 1.0s — From a car's right side at window height, travelling at 100 km/h along the freeway, looking forward-right at the line of six billboards on the right shoulder.
1.0s to 4.0s — The camera leaves the car and pushes in a straight line into the fourth billboard, accelerating, until the glowing screen fills the entire frame by 3.5s and keeps pushing into the image of the bridge.

ACTION
Six billboards 8 m wide on steel posts in the bright sun, their LED screens glowing purple and teal, brighter than the daylight around them, all showing the same night bridge with the police lights; traffic and police lights streak past in the foreground in the first second.

PHYSICS
The screen's LED pixel grid becomes visible as the camera gets close, then dissolves into the image; heat shimmer over the asphalt.

LIGHTING
LIGHTING: Midday, present day. Hard sun high overhead at 5600K from camera right, short crisp shadows under every rock, post and palm, bleached sandstone cliff, heat shimmer rising from the asphalt over the first 30 m, deep clean blue sky with a few white clouds, high contrast, clean modern digital look.
The billboard screens glow purple and teal, brighter than the daylight around them.

AUDIO
No music. Freeway rush fading, then the tinny audio of the live stream: sirens and night insects.

STYLE
Photorealistic live-action film footage, present-day Los Angeles at midday, crisp colour, fine grain, cinematic contrast.

OUTPUT SETTINGS
Vertical 9:16, real-time speed, 24 fps motion cadence, 4 seconds.

POSITIVE LOCKS
The world around the billboards is bright midday with a blue sky. The night exists only inside the screens. The last frame is the night bridge image filling the whole frame.
```

---

## Patch E (opsional) · Michael pret policinë · 4 s

**Rendi:** `@image1` michael-sheet-masked.png · `@image2` sheet-i i sedanit gri · `@image3` loc_now_freeway.jpg

```
SCENE CONTEXT
Los Angeles today, hard midday sun, on a wide concrete freeway. A calm man in a navy suit slides his graphite-grey sedan in front of a police cruiser and taps the brakes; the cruiser brakes hard and falls back. Vertical 9:16, live-action, photoreal, one continuous shot.

ACTIVE REFERENCES
@image1: the driver, forty-six, dark hair combed back, navy suit, open white shirt. Face 100% matches the reference.
@image2: the modern four-door sport saloon in graphite-grey metallic with a black honeycomb grille. 100% matches the reference.
@image3: the freeway: concrete lanes, barriers, overpasses, blank green gantry signs, the downtown skyline ahead. Reference defines architecture, geography and dressing ONLY — not a keyframe.

THE POLICE
A modern black-and-white police sedan with a blazing red and blue LED light bar and a push bar.

OPTICS
28 mm equivalent, 75° field of view, deep focus.

CAMERA
Tracking from the next lane at 1.2 m height, level with the grey sedan's rear door, 5 m away, moving at the same speed, looking forward at three-quarters so both the sedan and the cruiser ahead of it on the right are in frame.

ACTION
0.0s to 1.5s — The grey sedan drives at 120 km/h, the man in the navy suit at the wheel visible through the side window, one hand on the wheel; the police cruiser is in the lane to its right, 6 m ahead.
1.5s to 2.5s — The sedan accelerates, overtakes the cruiser and swings across into its lane, directly in front of its push bar with 3 m between them.
2.5s to 4.0s — The sedan's brake lights flash red twice; the cruiser's nose dives under hard braking, tyres smoke, and it falls back 10 m; the sedan pulls away.

PERFORMANCE
The man: bored, precise, a slow glance at his side mirror, no expression.

PHYSICS
Real weight: the sedan's body rolls as it changes lanes, the cruiser's nose dives and its rear lifts under braking, a puff of tyre smoke.

LIGHTING
LIGHTING: Midday, present day. Hard sun high overhead at 5600K from camera right, short crisp shadows under every rock, post and palm, bleached sandstone cliff, heat shimmer rising from the asphalt over the first 30 m, deep clean blue sky with a few white clouds, high contrast, clean modern digital look.

AUDIO
No music. Engine roar, a brake squeal from the cruiser, the siren dropping back.

STYLE
Photorealistic live-action film footage, present-day Los Angeles at midday, crisp colour, fine grain, cinematic contrast.

OUTPUT SETTINGS
Vertical 9:16, real-time speed, 24 fps motion cadence, 4 seconds.

POSITIVE LOCKS
The sedan is graphite grey. Both vehicles drive forward in the same direction. The cruiser ends up behind the sedan.
```

---

## Patch C2 · Konvoji pa Eglin, nga parakolpi i pasmë · 4 s

**Rendi:** `@image1` car_now-sheet.jpg · `@image2` sedani gri · `@image3` motori jeshil · `@image4` truck_trevor-sheet.jpg · `@image5` car_86-sheet.jpg · `@image6` lowrider-i · `@image7` loc_now_freeway.jpg

```
SCENE CONTEXT
Los Angeles today, hard midday sun, on a wide concrete freeway. Behind a matte-black sports coupe, five vehicles follow it in a single line like an escort: a grey saloon, a green motorbike, a red pickup with a teddy bear, a white 1980s coupe and a green lowrider; far behind them, the police. Vertical 9:16, live-action, photoreal, one continuous shot.

ACTIVE REFERENCES
@image1: the matte-black modern two-door sports coupe, satin black paint, graphite wheels. 100% matches the reference.
@image2 @image3 @image4 @image5 @image6: the convoy, in this order from nearest to farthest: the graphite-grey sport saloon, the green touring motorbike, the faded red pickup with a worn yellow teddy bear strapped to its push bar, the white 1980s wedge coupe, the candy-green lowrider with gold wire wheels. Each 100% matches its reference.
@image7: the freeway: concrete lanes, barriers, overpasses, blank green gantry signs, palms. Reference defines architecture, geography and dressing ONLY — not a keyframe.

OPTICS
35 mm equivalent, 63° field of view, deep focus from the coupe's bodywork to the far end of the convoy.

CAMERA
Mounted low on the coupe's rear bumper, 0.5 m above the asphalt, looking straight back down the freeway, moving with the coupe at 120 km/h, a slight road vibration; a slow rise from 0.5 m to 1.5 m over the 4 seconds.

ACTION
The satin-black rear deck, spoiler edge and one red tail light of the coupe run across the bottom of the frame. Behind it, in the same lane, the five vehicles follow in a single line 10 m apart at the same speed, each one sharp and readable: the grey saloon nearest, its honeycomb grille filling a third of the frame, then the green motorbike leaning slightly, then the red pickup with the teddy bear on its push bar, then the white wedge coupe, then the green lowrider. 80 m behind them, a row of police cruisers with red and blue light bars, falling back.

PHYSICS
Real weight: the convoy's vehicles rock gently on their suspensions, the bike's rider shifts his weight, heat shimmer bends the road between the vehicles, the coupe's bodywork vibrates.

LIGHTING
LIGHTING: Midday, present day. Hard sun high overhead at 5600K from camera right, short crisp shadows under every rock, post and palm, bleached sandstone cliff, heat shimmer rising from the asphalt over the first 30 m, deep clean blue sky with a few white clouds, high contrast, clean modern digital look.

AUDIO
No music. Five engines in harmony, wind roar, sirens falling away far behind.

STYLE
Photorealistic live-action film footage, present-day Los Angeles at midday, crisp colour, fine grain, cinematic contrast.

OUTPUT SETTINGS
Vertical 9:16, real-time speed, 24 fps motion cadence, 4 seconds.

POSITIVE LOCKS
All five vehicles are visible in one line for the whole shot, in the stated order, driving toward the camera. The police stay far behind the convoy.
```
