# Promptet e zgjedhura (nga ultra-skills.com, ngjitur nga përdoruesi 2026-11-21)

Ngjiti në Claude Code në një folder bosh. Zëvendëso `[kllapat]` dhe paletën me ato të projektit.
Shared setup: Remotion, vetëm `useCurrentFrame`, `interpolate`, `spring`; seeded random (mulberry32),
asnjëherë `Math.random` ose `Date`. Node 20+ dhe ffmpeg. 3D: `@remotion/three` + R3F, `--gl=angle`.

---

## 13 · Receipt

```
Create a new Remotion project in this folder (TypeScript, 1080x1920, 30 fps, 60 frames, composition id "Receipt"). Use @remotion/three with React Three Fiber, three and @react-three/drei (Environment, ContactShadows), plus a monospace font from @remotion/google-fonts. Drive every animation from useCurrentFrame, interpolate and spring only. Render with --gl=angle.

LOOK: a dark warm tabletop in low light with a small black thermal printer at the top of the frame, its one amber light blinking. Paper feeds out toward the camera in short mechanical steps, each step leaving a printed line. The paper ends with a bold total. Then it jerks, tears on the serrated edge, lifts off the table leaving its shadow behind, and tilts up toward the lens with the total pin sharp while the printer falls out of focus.

PALETTE: stage #1c100a, #100906, #070403; table #1a120e; printer body #070403, printer edge #251913; LED #ffc24b; key light #ff6a2a; paper #fffdf8; print ink #17130f, secondary print #5e554b; total underline #e5432d; shadow #050100.

BUILD (all in code): a low warm key light from the upper left and a low-intensity studio Environment over a table that falls off to the stage colour. Printer: a small rounded box at y 340-620 with bevels, a slot, a serrated tear bar and one small LED that blinks on each step. Receipt: a 660-wide plane with a very slight curl, its text drawn to a CanvasTexture at 2x so it stays sharp when tilted, in monospace.

PRINT IN STEPS: the paper advances one line height in 3 frames, stops 2 frames, repeats; one line prints at a time, the earliest lines travelling furthest. Lines at frames 2, 7, 12, 17, 22, 27, 32, 34: "[Store name]" 48px centred; "[Subtitle]" 32px; "[Receipt title]" 36px with a dashed rule; three item lines "[Item] $[price]" at 38px with prices right-aligned; a free line "[Item] $0.00"; then a dashed rule and "Total cost $[sum]" at 64px bold with a single underline. Make the item prices add up to the total exactly.

FINISH: frame 38 tear: a sharp 2-frame jolt of 6px, the torn edge becomes jagged, one corner curls. Frames 40-52: the receipt rises off the table on one smooth ease-out, scale 1 to 1.08, tilting 14 degrees toward the lens to y 420-1400 with the total near y 1240. The shadow stays on the table as a separate shape, growing softer, larger and offset to the lower right. Depth of field: focus on the total while the printer and table blur to about 12px over frames 40-52. Frames 52-59: the paper drifts 1 degree and the LED pulses once.

RULES: keep text above y 1536. Preview, then render to out/receipt.mp4 and tell me the command.
```

## 12 · Money stack

```
Create a new Remotion project in this folder (TypeScript, 1080x1920, 30 fps, 60 frames, composition id "MoneyStack"). Use @remotion/three with React Three Fiber, three and @react-three/drei (Environment, ContactShadows). Drive every animation from useCurrentFrame, interpolate and spring only. Seeded random only (mulberry32). Render with --gl=angle.

LOOK: a pale clean studio with one empty wooden pallet. Banded bricks of cash drop from the top of the frame and land on it, faster and faster, ten of them, each hit pressing the whole stack down and letting it spring back so you feel the weight build. A big counter above rolls forward exactly on each landing until the last brick comes down hardest, a low ring of dust runs across the floor, and the counter lands on the total.

PALETTE: stage #f7f9fc, #eef2f8, #e3e9f2; note face #f4efe5; note print and strap #1f5c4a; wood #a4927d, dark wood #6d5d4c; ink #0d1324; secondary ink #4c566e; counter hit #1f5c4a; floor ring #2f5bff; shadow #0c1a3a.

BUILD (all in code): pallet of slatted wood, 620 wide, at y 1360-1460. Bricks: rounded boxes 300 wide, 76 tall, 150 deep, so two sit side by side; thin note edges on the sides, a printed top face, one wide strap across the middle. Each brick's small seeded rotation (up to 3 degrees) settles to 0 on landing. Lighting: a drei studio Environment plus soft shadows on a pale stage, no texture noise.

TIMELINE: ten bricks in five layers of two, left then right on each layer, reaching about y 980. Each falls from above the frame on an ease-in over 8 frames with vertical motion blur, landing at frames 2, 10, 17, 23, 28, 32, 36, 39, 42, 46. On each landing the stack dips 6px and returns over 8 frames and the shadow tightens. The last brick at frame 46: a floor ring from a pressure disc growing from 120 to 1500 wide over 16 frames, a few strap and paper scraps, and one 18px shake decaying over 5 frames. No white flash.

TEXT (screen space): "[Headline, e.g. $1M, in real size]" 60px ink at y 350-420 from frame 0. A counter 136px heavy tabular at y 440-600 starting at $0 and stepping up by one tenth of [total] on each landing frame, with a digit roll of at most 3 frames between steps. At frame 49 it lands on "[total]" with a 1 to 1.08 to 1 pop in the hit colour. Label "[Caption]" 34px at y 610-650.

CAMERA: front-on, 12 degrees above, rising to follow the stack in one eased curve over frames 0-48, then a 1% slow push.

RULES: keep text above y 1536. Preview, then render to out/money-stack.mp4 and tell me the command.
```

## 27 · Lock-screen notifications

```
Create a new Remotion project in this folder (TypeScript, 1080x1920, 30 fps, 60 frames, composition id "Notifications"). Use CSS and SVG, and @remotion/noise. Drive every animation from useCurrentFrame, interpolate and spring. Seeded random only (mulberry32).

LOOK: the whole frame is a phone lock screen on a deep-green-to-teal wallpaper, at 9:41 on a Monday. One order notification rises from the bottom edge and lands with a small haptic thud. Then another, and the stack shoves upward. They come faster and faster, each one pressing the pile down and pushing it up the screen, until the cards have buried the clock and run off the top of the phone. A dark pill holds the day's total in front of it all, rolling up with every landing, and landing as the last card hits.

PALETTE: wallpaper #1f5c4a to #00b39a to #3ee6d0; lock ink #f2f5ff; card surface rgba(255,255,255,0.92); card ink #0d1324; card secondary ink #4c566e; app icon #1f5c4a; pill #111827 with ink #f2f5ff and secondary #a9b4d0; shadow #0c1a3a.

SCREEN (frontal, no phone body): vertical wallpaper gradient plus two very soft light blobs drifting on noise2D with a fixed seed. Status icons only (signal, battery, no text) at y 60-100. Clock "9:41" 168px light sans at y 350-510; "Monday" 40px at y 520-570. Pill: x 220-860, y 600-710, label "[Pill label, e.g. Today's sales]" 32px, value 56px tabular, always the top layer with a soft shadow.

CARDS: 1000x168 at x 40, radius 36, with a hairline and two soft shadows that tighten on landing; an 84px rounded-square app icon on the left; "[Shop name]" 34px, "now" 32px right-aligned, and an order line 38px with the amount semibold. No backdrop blur. Nine orders, in this order, with a running total in the pill (replace the amounts with your own and keep the running total in step): 84.00 (1 item), 126.00 (2 items), 42.00 (1 item), 210.00 (3 items), 84.00 (1 item), 168.00 (2 items), 58.00 (1 item), 96.00 (2 items), 132.00 (2 items); totals 84, 210, 252, 462, 546, 714, 772, 868, 1000.

LANDINGS at frames 2, 12, 20, 26, 31, 35, 38, 41, 44. Each card rises 600px from below the frame to the lowest slot (y 1342-1510) over 8 frames (6 for the last four) on bezier(0.45,0.05,0.25,1.12), with alternating 2-degree tilts flattening and scale 1.06 to 1; its text stays hidden until the card top passes above y 1536, so nothing readable sits below it. On each landing the existing stack rises one 184px step on the same curve and the whole pile presses down 6px and rebounds over 8 frames (summed pulses clamped to 10px). Oldest cards pass behind the pill, over the clock and off the top edge. The pill value rolls to each new total in step with the landing, 6 frames per roll, and lands the final total at frame 50 with scale 1.04 to 1 over 4 frames.

FINISH: frames 48-59 one glaze 360px wide, rotated 14 degrees, soft-light, clipped to each card's corners, the only sheen in the scene. Camera: one continuous zoom 1.06 to 1 over the whole clip. The last frames stay alive through wallpaper drift and a 2px card float.

RULES: keep text above y 1536. Preview, then render to out/notifications.mp4 and tell me the command.
```

## 24 · Day counter

```
Create a new Remotion project in this folder (TypeScript, 1080x1920, 30 fps, 60 frames, composition id "DayCounter"). Use CSS 3D and SVG, and Archivo Black from @remotion/google-fonts. Drive every animation from useCurrentFrame, interpolate and spring. Seeded random only (mulberry32).

LOOK: an off-white page with small caps "[ONE LINE ABOVE THE COUNTER]" above a huge red "DAY 1". Below it, a ring-bound desk calendar sits on the table with real thickness and a contact shadow. A red tick stamps day 1, then day 2, and the counter rolls with every stamp. The stamps come slowly and then in a blur, the digits racing, until day 29. Everything breathes for a beat. Then one last oversized tick falls onto day 30, the sheet dips and bounces on its rings, and the counter locks at DAY 30.

PALETTE: page #f6f2ea, #f0ebe1, #e7e0d3; sheet #fffdf8; sheet under #f4efe5; ink #17130f; secondary ink #5e554b; day numerals #9b9184; red #e5432d; ring #9b9184; shadow #2a1d10.

LAYOUT: caps 40px letterspaced secondary ink at y 350-400. Counter "DAY" plus digits in Archivo Black 220px red at y 420-680, centred; the digits roll one step per stamp, each step 2 frames on bezier(0.25,0.8,0.25,1), slightly blurred on the fastest steps. Calendar: CSS 3D perspective 1800, rotateX 4 degrees, a 980px-wide sheet at y 740-1470 with fibre grain, three sheets underneath offset 6px each for thickness, two separate shadows (a contact core plus ambient), a row of 14 ring loops along the top edge at y 720-770. Grid 7 columns by 5 rows, cell 128x116, y 830-1400, numerals 1 to 30 at 40px, the last five cells blank. "[Caption]" 32px at y 1420.

STAMPS: day n stamps at frame 2 + round(34 x ((n-1)/28)^0.55) for n = 1 to 29, which starts with gaps of about 5 frames and ends with several stamps in one frame. Each tick is a hand-marked red tick with slightly rough edges (seeded), scale 1.6 to 1 over 3 frames, no ring and no sparkle on small ones; a numeral under a stamped tick goes from the light grey to ink.

FINISH: frames 36-44 stamping stops, the counter sits on 29, and a rubber stamp block drawn in ink lifts above day 30 at frames 36-39 then falls on ease-in cubic over frames 39-44 at scale 2.2 to 1. Frame 44: the block leaves on a fast ease-out over 4 frames, revealing a larger tick in day 30's cell. Paper bounce: the sheet stack moves down 14px at scale 0.99, stuck for 2 frames, then a 5-frame rebound, with the contact shadow tightening then releasing. Element only, no frame shake. Frame 46: the counter locks at DAY 30 with scale 1.03 to 1 over 4 frames. Frames 53-59: the sheet swings 1 degree around the rings on a damped sine. Camera: one continuous 1.04 to 1 push over the whole clip.

RULES: keep text above y 1536. Preview, then render to out/day-counter.mp4 and tell me the command.
```

## 28 · Type slam

```
Create a new Remotion project in this folder (TypeScript, 1080x1920, 30 fps, 60 frames, composition id "TypeSlam"). Use CSS and SVG, and Archivo Black from @remotion/google-fonts, loaded before the first paint. Drive every animation from useCurrentFrame, interpolate and spring.

LOOK: off-black. A short word falls out of the lens from oversized and slams into the frame, the whole picture flipping to its negative for two frames and shaking. A second word hits under it and knocks the first up a few pixels. Then a third word drops from above the lens, so big its letters run edge to edge and from the top of the frame down into a solid floor. Slowly, orange rises through the letters from the floor up, like a level meter topping out.

PALETTE: stage #17181b, #0e0f11, #08080a with static grain from a fixed seed; type #f4f4f2; inverted ground #f4f4f2; inverted type #0e0f11; charge #ff6b2c.

TYPE: Archivo Black, all caps, tight tracking. Words "[WORD ONE]", "[WORD TWO]", "[WORD THREE]" (short; the third is the big one). Hit frames: first word 5, second 18, third 32, kept 13 or more frames apart so the clip never strobes.

First word: frame 0 starts at scale 2.6 with 10px blur at 60% opacity, falls on ease-in (quad) to 0.965 at frame 5, then spring(damping 14) to 1.
Second word: appears at frame 12 at scale 2.75 to 2.6, falls frames 13-18 on the same curve. At frame 18 the first word jumps up 12px with a damped return over 8 frames.
Third word: hangs frames 22-26 at scale 2.75 to 2.6 over the frame with 10px blur at 60% opacity, falling frames 26-32 on the same curve. At frame 32 the first two words are cut on the hit frame.
HIT PACKAGE for all three: swap to the inverted ground and type for 2 frames on the first (frames 5-6) and second (18-19) and 3 frames on the third (32-34), then all gone. Shake 18px, mostly vertical, exponential decay over 5 frames, applied to the effect layer only. These three are the clip's entire budget of whole-frame hits.

THIRD WORD LAYOUT: measure the word with canvas measureText after the font loads, then scale non-uniformly so glyphs span x 0-1080 and cap height spans y 0-1536, overscanning 8px at left, right and top. Add a solid block in the same fill from y 1536 to y 1920, merging with the letters' feet, so the frame is full and no readable glyph edge exists below y 1536.

CHARGE: frames 40-56, the charge colour fills the letters and floor from the bottom edge upward through a horizontal mask with a soft 40px edge on one ease-in-out. Frames 34-59: the letters swell 1 to 1.012 from the centre, overscan covering the edges; grain continues. No sparks, no ring, no shards.

RULES: keep text above y 1536. Preview, then render to out/type-slam.mp4 and tell me the command.
```

## 29 · Particle word (logo)

```
Create a new Remotion project in this folder (TypeScript, 1080x1920, 30 fps, 60 frames, composition id "ParticleLogo"). Use three.js Points in @remotion/three, or one 2D canvas if that holds the frame rate better, plus @remotion/noise and a heavy grotesque from @remotion/google-fonts. Drive every animation from useCurrentFrame, interpolate and spring. Seeded random only (mulberry32).

LOOK: a black void where ten thousand fine points of dust turn in a slow galaxy, pulled by something you never see. The swirl tightens and speeds up, its centre thickening with light as every grain leans inward. Then the whole cloud snaps, in less than half a second, into one heavy word, each letter built only from dust and catching electric lime as it lands. A few hundred stray grains keep orbiting, and a soft shimmer runs across the letters as they breathe.

PALETTE: void #070806, void top #141612, dust #aab09e, bright dust #f6f8f0, word #c6f432, key light #b8ff3a.

PARTICLES: exactly 10,000. Each particle's position, size and colour are a pure function of (frame, index), seeded with mulberry32 or Remotion's random(), never stepped and never Math.random. Targets: load the font first, draw "[WORD]" (up to five capital letters) in a heavy grotesque on an offscreen canvas about 900px wide centred at x 540, y 950, sample 9,500 points from its filled pixels with a fixed seed and store them once in useMemo. The other 500 stay strays. Stage: a vertical gradient from void top to void.

TIMELINE:
Frames 0-12, wide galaxy: particles on a slow spiral around x 540, y 950 with radius up to 1100px, colour dust, sizes 1.5-3px, spin 0.012 rad per frame near the rim.
Frames 12-32, tighten: radius falls by 60% on an ease-in curve, spin rises to about 0.05 rad per frame, inner particles shift to bright dust so the centre thickens with light; add curl from noise2D for an organic path. The force stays invisible.
Frames 32-42, snap: each of the 9,500 eases to its target with a strong ease-out and 8% overshoot, delayed 0-3 frames by its current distance from its target; colour ramps from bright dust to the word colour as it lands.
Frames 42-50, glow envelope: burst 0.3, peak 0.7 at landing, settle to 0.45 so warmth remains, as an additive soft layer clipped to the word area. It never fills the frame and adds no flash.
Frames 44-59, live breath: each landed particle offsets at most 2px by noise on a slow time axis so the letters stay solid. Frames 50-59: one soft shimmer wave crosses left to right as a brightness lift. The 500 strays keep orbiting the word at low opacity to the last frame.

RULES: keep text above y 1536. Preview, then render to out/particle-logo.mp4 and tell me the command.
```
