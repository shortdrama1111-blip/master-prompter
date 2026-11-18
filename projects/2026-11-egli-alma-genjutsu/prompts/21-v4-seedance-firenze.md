# v4 Firence — Seedance 2.5, 20 s, 9:16 — v1
Rruga: manuale (përdoruesi gjeneron; Claude NUK nis gjenerime). Raporti 9:16 dhe 20 s në UI.
Elementet: @model-firenze-1/-2/-3 (sheet-et e maskuara), @env-modele-1..4 (plate-t).
Hartimi me videon referencë (analysis-v4.md), 22.1 s → 20 s:
| Seg | Koha | Veshja | Lokacioni | Shot-i i ref |
|---|---|---|---|---|
| 1 | 0.0–2.0 | 1 pallto | env-2 Duomo | 1 ecja drejt kamerës |
| 2 | 2.0–3.4 | 1 | env-2 | 2–3 këmbët |
| 3 | 3.4–5.0 | 1 | env-2 | 4 anash |
| 4 | 5.0–6.8 | 1 | env-2 | 5 plan mesatar |
| 5 | 6.8–8.6 | 2 kuadrata | env-1 butikët | 7 plani i gjerë |
| 6 | 8.6–10.0 | 2 | env-1 | 8 më afër |
| 7 | 10.0–12.4 | 2 | env-1 | 9 profil te vitrina |
| 8 | 12.4–14.4 | 3 e zezë | env-3 portiku | 10 pozë te kolona |
| 9 | 14.4–17.0 | 3 | env-4 Arno | 11 ecja drejt kamerës |
| 10 | 17.0–20.0 | 3 | env-4 | 12 del nga kuadri, rruga bosh |
Kalimet light-leak të ref → në montim, mbi prerjet 6.8 dhe 12.4 (CLAUDE.md #9).

## Prompti
```
SCENE CONTEXT
A 20-second vertical street-style fashion film in the centre of Florence, Italy, in late-afternoon autumn light. One woman walks through four Florentine locations in three outfits: a narrow street with the cathedral dome, a boutique street of stone arches, a stone portico, and the Arno riverside with the Ponte Vecchio. Ten timed shots, each from a clearly different angle; the outfit and location change only at 6.8s and 12.4s.

ACTIVE REFERENCES
@model-firenze-1, @model-firenze-2 and @model-firenze-3 are the same woman in three outfits: late twenties, slim, brown curtain bangs with face-framing honey-blonde strands, hair gathered into a low bun at the nape, brown eyes, natural skin with fine freckles, thin gold hoop earrings. Her face is the large close-up panel of each reference; 100% matches the reference.
@env-modele-2: narrow street of ochre and cream palazzi with dark green shutters and grey stone paving, the terracotta cathedral dome at the end. 100% matches the reference.
@env-modele-1: boutique street, rusticated grey stone arches with warm-lit glass shop windows on the left, wide grey stone pavement. 100% matches the reference.
@env-modele-3: Renaissance portico, slender grey stone columns, white vaulted ceiling, piazza with ochre palazzi beyond. 100% matches the reference.
@env-modele-4: Arno riverside walkway, grey stone paving, low stone parapet on the right, the Ponte Vecchio and the hills beyond. 100% matches the reference.

LOCATION MAP
Every location is quiet and empty of other people. The low sun sits camera-left, behind thin high cloud; the upper facades glow warm gold and the street level lies in even soft light. The woman always walks on the stone paving at the centre of each location, the architecture of the reference framing her on both sides.

FIRST FRAME / BLOCKING
Frame one: @model-firenze-1 already in mid-stride in the centre of the @env-modele-2 street, 6 metres from the camera, walking straight toward the lens, the cathedral dome centred above her head at the far end of the street. She is in motion from the very first frame. Every shot opens with her already moving.

FORMAT MODE
Timed multishot, ten shots, hard cuts only at the stated seconds; cuts only at the specified points, the camera does not cut on its own.

OPTICS
Each shot keeps its stated FOV with no drift mid-segment. Clean rectilinear perspective, gentle natural falloff, soft background separation on the closer shots.

CAMERA
Handheld gimbal feel at chest height, smooth with a 1 cm natural float. The camera moves backward or alongside at her walking pace, about 4.5 km/h, keeping her the same size in frame through each moving shot. Focus stays on her face, or on her boots in the boot shot. Rich tonal latitude, soft highlight roll-off on the sunlit stone, natural skin tones.

ACTION
0.0s to 2.0s — @model-firenze-1 in @env-modele-2, wide shot, 47° FOV, camera at chest height, walking backward at 4.5 km/h. She walks straight toward the camera down the centre of the street with a confident runway walk, one foot crossing in front of the other, arms swinging loosely, the open coat swinging at her knees. The dome stays centred behind her.
2.0s HARD CUT
2.0s to 3.4s — @model-firenze-1 in @env-modele-2, low tracking shot, 29° FOV, camera 30 cm above the paving, moving sideways alongside her at 4.5 km/h. Profile view from the knee down: the brown leather midi skirt swaying, the brown pointed ankle boots striking the grey stone paving heel first, one step every 0.5 seconds.
3.4s HARD CUT
3.4s to 5.0s — @model-firenze-1 in @env-modele-2, medium-wide three-quarter shot, 63° FOV, camera tracking alongside on her right at 4.5 km/h. She walks past the ochre facades and green shutters, her gaze straight ahead down the street, the coat hem moving with each step.
5.0s HARD CUT
5.0s to 6.8s — @model-firenze-1 in @env-modele-2, medium shot from the waist up, 29° FOV, camera walking backward at her pace. She walks toward the lens, her right hand lifts and holds the coat lapel against her chest, her eyes lift to the lens for one beat, then slide off to the left.
6.8s HARD CUT
6.8s to 8.6s — @model-firenze-2 in @env-modele-1, wide shot, 47° FOV, camera at chest height on the pavement, walking backward at 4.5 km/h. She walks toward the camera along the stone arches, the warm-lit shop windows passing on the left, the brown leather bag on her left shoulder, the tall brown riding boots striding over the grey stone.
8.6s HARD CUT
8.6s to 10.0s — @model-firenze-2 in @env-modele-1, medium shot from the knees up, 29° FOV, camera tracking backward and slightly to her right. Her left hand rests on the bag strap, the plaid mini skirt moves with her stride, her chin is level, her eyes look ahead past the lens.
10.0s HARD CUT
10.0s to 12.4s — @model-firenze-2 in @env-modele-1, profile medium close-up, 29° FOV, camera on the street side moving in a slow arc of 20 degrees around her at 1 km/h. She slows in front of a lit shop window, turns her head toward the coats on the rails behind the glass, the window light warm on her cheek, her right hand lightly on the bag strap.
12.4s HARD CUT
12.4s to 14.4s — @model-firenze-3 in @env-modele-3, full-body shot, 47° FOV, low camera at hip height, locked off. She leans her left shoulder against the nearest stone column, left foot crossed over the right, both hands relaxed at her sides with the black lace cuffs falling over her wrists. She turns her face from the piazza toward the lens and holds a calm, closed-mouth half smile.
14.4s HARD CUT
14.4s to 17.0s — @model-firenze-3 in @env-modele-4, wide shot, 47° FOV, camera at chest height, walking backward at 4.5 km/h. She walks toward the camera along the riverside walkway, the stone parapet and the Arno on the right, the Ponte Vecchio behind her shoulder, the ecru wide-leg jeans moving with each stride.
17.0s HARD CUT
17.0s to 20.0s — @model-firenze-3 in @env-modele-4, wide shot, 47° FOV, camera locked off at chest height. She walks toward the camera and passes close to the lens on the right, leaving the frame at 18.6s; the camera holds on the empty sunlit walkway, the Ponte Vecchio and its reflection in the river, the water moving gently until 20.0s.

PERFORMANCE
Composed, self-assured model walk: shoulders back and relaxed, chin level, a steady gaze ahead, a soft closed mouth. Living eyes with warm catch-lights from the low sun, natural blinks, fine pore-level skin texture, the face-framing strands moving with every step.

PHYSICS
Natural weight transfer on every step; heels contact the stone with a small contact shadow. Fabric reacts to the stride: the wool coat swings with weight, the leather skirt holds its shape and creases at the knee, the plaid skirt bounces lightly, the wide jeans flow around the legs. Loose hair strands lift slightly in a light 5 km/h breeze. The river surface ripples gently.

LIGHTING
Soft late-afternoon autumn daylight at 4500 K, the sun low behind thin high cloud from camera-left, warm golden light on the upper stone facades, the street level in even soft light, gentle contrast, creamy highlights, soft warm-grey shadows, fine natural grain.

WARDROBE
@model-firenze-1: open long dark chocolate-brown wool coat, camel ribbed mock-neck knit, glossy brown leather midi pencil skirt with a side slit, brown pointed heeled ankle boots, gold hoop earrings.
@model-firenze-2: fitted cream ribbed long-sleeve knit with a scoop neck, brown and taupe plaid wool mini skirt with a brown belt, sheer dark tights, tall brown leather riding boots, small brown leather shoulder bag, gold watch.
@model-firenze-3: fitted black ribbed long-sleeve knit with black lace cuffs, ecru high-waisted wide-leg jeans, black leather belt with a silver buckle, dark brown suede clogs, gold hoop earrings.

AUDIO
Footsteps on stone and soft distant city ambience only, no music.

STYLE
Photoreal street-style fashion film shot on location, natural documentary realism, fine film grain, true-to-life fabric and stone texture.

OUTPUT SETTINGS
Vertical 9:16, 20 seconds, real-time speed in every shot.

POSITIVE LOCKS
The same woman with the same face, curtain bangs and low bun in all ten shots. Each outfit stays complete and unchanged within its shots: outfit one until 6.8s, outfit two from 6.8s to 12.4s, outfit three from 12.4s to 20.0s. Each location matches its reference. She is the only person in every frame. The warm late-afternoon light comes from camera-left in every shot. The image stays clean of any text, signage lettering or logo.
```
