# Brief për chat-in me Blender: blockout i skenës 3 (v2)

```
You are building a grey-box BLOCKOUT animation in Blender for a vertical film. It is a placeholder that another AI video model will copy for camera angles, positions, movement and cut timing, so readability and exact timing matter more than detail. Build it with simple primitives (boxes, cylinders, capsules, planes), animate it, bind one camera per shot to timeline markers, and render it. Work in metres. Do every step below; where a value is given, use it exactly.

=== GLOBAL SETTINGS ===
- Resolution 720 x 1280 (vertical 9:16), 100%. Frame rate 24 fps. Frame range 1–288 (12.0 s).
- Render engine: Workbench. Lighting: Studio. Color: Object (every object shows its own Object Color). Shadows ON (helps read height and contact). Background: World colour light blue (#BFD9F2).
- Output: FFmpeg video, MPEG-4 container, H.264, file name blockout_scene3_v2.mp4.
- Cameras: one camera per shot, named CAM_01 … CAM_08. Add exactly ONE timeline marker at each shot start (frames 1, 37, 73, 109, 145, 181, 217, 253) and bind the matching camera to it (Marker > Bind Camera to Markers). No other markers anywhere, so there are no extra flash cuts.
- Sensor Fit: Auto, sensor 36 mm. Focal lengths are given per shot.

=== COLOUR KEY (Object Color, exact) ===
- Egli (the hero) person capsule: YELLOW #F2C200
- Egli's car: YELLOW box #F2C200 (a modern 2-door coupe, 4.5 x 1.9 x 1.2 m, with a darker glass band and an open interior so cameras can sit inside)
- Michael person capsule: NAVY #1E3A8A · Michael's sedan: NAVY box #1E3A8A (4.9 x 1.9 x 1.4 m)
- Franklin person capsule / arms: LIME #7CFC00 · Franklin's motorbike: LIME thin box #7CFC00 (2.3 x 0.9 x 1.2 m)
- Trevor's pickup truck: BROWN box #8B5A2B (5.0 x 2.0 x 1.8 m) with a push bar (brown cylinder across the front) and a small YELLOW-ORANGE cube 0.25 m strapped to the push bar (the teddy bear) #F0A030
- Tommy's coupe (convoy only): WHITE #FFFFFF (4.5 x 1.9 x 1.2 m)
- CJ's lowrider (convoy only): PURPLE #6A2C91 (5.2 x 2.0 x 1.3 m)
- Police cars: BLACK #111111 boxes (4.9 x 1.9 x 1.5 m), each with a thin white box on the roof (light bar)
- Police helicopter: DARK GREY #333333 (body 4 x 1.5 x 1.5 m + 2 thin rotor planes)
- The red die: RED sphere #C8102E, radius 0.035 m
- Interior mirror: BLACK flat box 0.26 x 0.02 x 0.08 m
- Roadside billboards: PURPLE #8E44AD panels 8 x 4.5 m on grey posts
- Environment: road dark grey #3A3A3A, lane lines white, concrete barriers light grey #BDBDBD, cliff sandstone #B79A6A, palms = thin brown cylinders 10 m + green sphere #3E7B3E, city skyline = grey boxes #8C8C8C

=== THE WORLD ===
SET A — Pacific Coast Highway (around the origin):
- A straight 6-lane road along the Y axis, x from -11 to +11, y from -60 to +120.
- A sandstone cliff on the +X side: a big sloped block from x=12 to x=30, 25 m high.
- A RAMP running down the cliff face: a 6 m wide inclined road from (x=8, y=46, z=4.0) down to (x=8, y=22, z=0), joining the highway. Low concrete parapet on its outer edge.
- 5 palms on top of the cliff, a traffic gantry (grey frame) across the road at y=40.

SET B — Freeway (far from Set A, along +Y):
- A straight 5-lane concrete freeway, x from -9 to +9 (lane centres at x = -7.2, -3.6, 0, 3.6, 7.2), y from 200 to 1400.
- Concrete barriers on both edges, dashed white lane lines.
- Two on-ramps joining from the right (+X) at y=300 and y=420, angled 15°.
- One overpass across the freeway at y=650.
- Skyline: 15 grey boxes 40–120 m tall at y=1500–1700.
- Billboards: 6 PURPLE panels on posts on the right shoulder at x=16, y = 700, 760, 820, 880, 940, 1000, faces turned toward the freeway, bottom edge 6 m high.

=== SHOTS (frames, camera, animation) ===

SHOT 1 · frames 1–36 · CAM_01 · 18 mm
- Camera on Set A road at (x=0, y=-2, z=0.5), looking toward +Y and slightly up (pitch +6°) so the ramp and cliff are in frame on the right.
- Egli's YELLOW car STARTS HIGH ON THE RAMP and COMES DOWN: f1 at (8, 44, 3.7) nose pointing down the ramp toward -Y; it drives down the ramp at 1.3 m/frame, reaches the bottom lip at (8, 22, 0) at f14, goes LIGHT over the lip (z rises +0.25 m between f14 and f17, lands at f18 with a 0.05 m bounce), then continues along the highway toward the camera, drifting from x=8 to x=2.5, passing the camera on its LEFT at f31 and leaving the frame by f36.
- The downward motion of the car is the key of this shot.

SHOT 2 · frames 37–72 · CAM_02 · 70 mm
- Egli's yellow car now drives on Set B at 25 m/s (1.04 m/frame) in lane x=0, starting at y=220.
- Inside the car: a YELLOW capsule (Egli, 1.75 m, seated) in the driver seat (left). CAM_02 is parented to the car, sitting in the passenger seat, looking forward-left and up at the interior MIRROR at the top centre of the windscreen.
- The RED die hangs 0.10 m below the mirror on a thin grey line, swinging ±10° (sine, period 1 s).
- On the mirror's face, place a small YELLOW ellipse (Egli's eyes in the mirror).
- Helicopter shadow: a black plane 6 x 3 m at 50% (or solid black) slides across the car's windscreen and roof from right to left between f55 and f65.

SHOT 3 · frames 73–108 · CAM_03 · 110 mm
- Camera on the police HELICOPTER, 60 m above the freeway and 40 m behind the yellow car, looking down at ~60°, following the car; add a light handheld shake (noise on rotation 0.3°).
- The yellow car continues in lane x=0. FOUR black police cars close in around it into a diamond: at f73 they are 25–35 m behind in lanes -3.6 / 0 / 3.6; by f108 they sit 8 m ahead, 8 m behind, and 4 m to the left and right of it.

SHOT 4 · frames 109–144 · CAM_04 · 28 mm
- Michael's NAVY sedan (navy capsule seated inside) comes from the on-ramp at y≈420, merges at f115 into lane x=3.6 directly in front of a black police car, then taps the brakes (decelerates from 1.1 to 0.8 m/frame f125–135). The police car brakes too and falls back 10 m.
- CAM_04 is parented to the sedan at its right side mirror (offset x+1.1, z 1.0), looking forward along the sedan's flank, so we see the sedan's side in the foreground and the police car being cut off.

SHOT 5 · frames 145–180 · CAM_05 · 18 mm
- Franklin's LIME bike, with a LIME capsule rider (two lime arm cylinders reaching to the handlebars in the camera's foreground), rides at 1.3 m/frame between two black police cars that drive side by side in lanes x=-3.6 and x=0 at 1.0 m/frame; the bike threads through the 0.5 m gaps between them from f150 to f170 and pulls ahead.
- CAM_05 parented to the bike's tank, 1.0 m high, looking forward.

SHOT 6 · frames 181–216 · CAM_06 · 18 mm
- Trevor's BROWN truck (teddy-bear cube on the push bar) drives at 1.2 m/frame.
- CAM_06 parented to the truck at the push bar, 0.8 m high, looking forward, the push bar and the teddy cube visible across the bottom of the frame.
- A black police car drives ahead in the same lane at 1.0 m/frame. At f190 the push bar hits the police car's REAR-LEFT corner; the police car rotates 90° to the right and slides off onto the right shoulder between f190 and f210, stopping against the barrier.
- Trevor (BROWN capsule) is not needed in frame.

SHOT 7 · frames 217–252 · CAM_07 · 40 mm
- Inside Egli's yellow car, CAM_07 sits in the back seat behind the yellow capsule's head, looking BACK through the rear window.
- Through the rear window, in a single line behind the yellow car in lane x=0, 10 m apart: NAVY sedan, LIME bike, BROWN truck, WHITE coupe, PURPLE lowrider. Far behind them (60 m+) a few black police cars.
- The yellow capsule's head turns 20° toward the rear between f230 and f240 (Egli looks at who follows him).

SHOT 8 · frames 253–288 · CAM_08 · 40 mm → push
- The yellow car passes the billboards. CAM_08 starts on the car's right side looking forward-right at the line of PURPLE billboards approaching; from f262 the camera leaves the car and pushes straight into one billboard (y=880) so that by f282 the purple panel fills the entire frame, and it stays fully purple until f288.

=== CHECKS BEFORE RENDERING ===
- Exactly 8 markers, at 1, 37, 73, 109, 145, 181, 217, 253, each bound to its camera.
- Shot 1: the yellow car visibly comes DOWN the ramp.
- Shots 2 and 7: the yellow capsule and the mirror/red die are visible.
- Every object uses the exact colour from the key; police cars are only BLACK.
- Render frames 1–288 to blockout_scene3_v2.mp4 and report the file path, plus a list of anything you could not build exactly.
```
