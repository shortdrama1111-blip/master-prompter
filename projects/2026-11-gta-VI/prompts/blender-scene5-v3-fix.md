# Brief për chat-in me Blender: rregullimet e skenës 5 (v3)

Problemi i v2: te shot-i 2 heronjtë qëndrojnë në këmbë te parmaku (rreth 25 kopje të përsëritura),
pastaj te shot-i 3 vijnë me makina. Rendi logjik (gabim i skenarit tim): ata janë në makina pas
kurthit të skenës 4, prandaj **fillimisht ngrenë murin me makina, pastaj dalin dhe qëndrojnë**.
Shot-et 1, 4, 5, 6, 7 mbeten si në v2.

```
Update the existing Scene 5 blockout v2 (720x1280, 24 fps, 16 s, frames 1–384). Keep the camera, objects and animation of every shot exactly as they are EXCEPT the two shots between 2.0 s and 6.5 s (frames 49–156), which are rebuilt below in a NEW ORDER. Keep every other marker and cut where it is.
Colour key (Object Color, Workbench Solid): Egli YELLOW #F2C200, Tommy AQUAMARINE #3FE0D0, CJ PURPLE #8A2BE2, Michael NAVY #1E3A8A, Franklin LIME #7CFC00, Trevor BROWN #8B5A2B, Lucia HOT PINK #FF4FA3, Jason OLIVE #808000. Hero vehicles: Tommy WHITE coupe, CJ PURPLE lowrider, Michael NAVY sedan, Franklin LIME bike, Trevor BROWN pickup, Egli YELLOW convertible. Police cars BLACK, officers DARK GREY.

THE STORY OF THESE TWO SHOTS: after the trap, the heroes are still INSIDE their vehicles. First they swing their vehicles sideways into a wall between the police and Egli; only then do they step out and stand in front of the wall. Nobody is on foot before the wall exists.

0) DELETE all the duplicated hero capsules standing along the railing in the old 2–4 s shot. In the whole file there must be exactly ONE capsule per hero.

1) NEW SHOT 2 · frames 49–108 (2.0–4.5 s) · the old HIGH wide camera (6 m above the deck), moved to this slot
- At frame 49 the five hero vehicles are stopped in the convoy lane behind the YELLOW convertible, each hero capsule SEATED inside its own vehicle (on the bike: Franklin seated on it).
- Frames 55–100: one after another (8 frames apart: white, purple, navy, brown, lime bike last), each vehicle swings 90° sideways and slides into place, forming ONE continuous wall across both lanes, between the BLACK police wall (ahead) and the YELLOW convertible + YELLOW Egli (behind the wall, near the railing).
- Egli (YELLOW) is standing next to his convertible near the railing, watching.

2) NEW SHOT 3 · frames 109–156 (4.5–6.5 s) · the old SLOW SIDEWAYS DOLLY, now at chest height (1.5 m) on the POLICE side of the wall, 3 m in front of the heroes, moving left to right
- Frames 109–125: the five heroes open their doors (simple door boxes rotating 70°) and step out IN FRONT of the wall, toward the police.
- By frame 130 they stand in one row, 1.2 m apart, in this order from left to right: AQUAMARINE Tommy, PURPLE CJ, NAVY Michael, LIME Franklin, BROWN Trevor, facing the camera / the police, the wall of their vehicles behind them.
- Each holds a small BLACK pistol box LOW at the side of the leg, pointing at the ground.
- Frames 135–148: every head turns 60° over the shoulder toward the railing and the water (they look back at the airboat), then back.
- Frames 148–156: Tommy's head dips 10° and comes back (a nod).
- The dolly moves slowly enough that all five are in frame during frames 130–156. No colour appears twice in this shot.

Check: exactly one capsule per hero in the whole file; the vehicles are in the wall BEFORE anyone stands in front of it; existing markers unchanged. Render to blockout_scene5_v3.mp4 and report anything you could not build exactly.
```
