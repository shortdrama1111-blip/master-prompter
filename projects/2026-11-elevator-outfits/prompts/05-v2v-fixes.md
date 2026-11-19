# 05: Seedance video-to-video fixes, applied to the montage

Feedback: "in one of the pics the arms need to be zipped and in the last one, the hoodie is bigger, look like this".
Reference: `refs/hood-sleeve-ref.jpg` (blue, sleeves zipped, large hood).
Rule: edit instead of regenerating. Each segment is edited on its own, 5 s, from the clip that's already approved.

## A: blue segment, sleeves zipped
Source `@video1` = `montage/src-seg3-blue-v4.mp4` (5.04 s). `@image1` = `refs/sleeve-zipped-crop.jpg`. Duration 5 s, 9:16.

```
SCENE CONTEXT
Edit of @video1: a woman in a cobalt-blue hoodie dress talks on her phone inside a stainless-steel elevator while the doors open and close in front of her. One change only: the sleeves of the hoodie dress are zipped closed.

ACTIVE REFERENCES
@video1: master for camera, framing, focus, door motion, her body motion, phone motion, expression timing, face, hair, boots, background, lighting, grain and duration.
@image1: sleeve reference only. A fully closed cobalt fleece sleeve with the silver zipper shut along its full length, wide and soft through the upper arm, gathering into a snug ribbed cuff at the wrist. 100% matches the reference.

EDIT
Both sleeves of the cobalt hoodie dress are zipped closed from the shoulder seam to the cuff. Her arms are inside the sleeves the whole time: the right arm inside its sleeve as she holds the phone to her right ear, the left arm inside its sleeve hanging relaxed at her side. Each sleeve is wide and soft cobalt fleece, the closed silver zipper a thin line along the outer seam, a snug cobalt ribbed cuff at each wrist with only her hands showing. The fleece folds softly at the bent right elbow and hangs straight along the left arm.

PHYSICS
The sleeves move with her arms as one piece of fabric, heavy fleece that settles 0.3 seconds after each movement.

LIGHTING
One source: the white ceiling light panel inside the cabin, 4500K, soft and even from above, a gentle shadow under the chin and under the hem. The stainless-steel walls bounce the light back softly onto her front. The landing side is 1 stop darker than the cabin, so the open doorway glows. The same light and the same exposure in all four segments.

AUDIO
The audio of @video1 unchanged. No music.

POSITIVE LOCKS
Every pixel outside the two sleeves stays exactly as in @video1: same face, same hair, same cream-white boots, same phone call, same door timing, same steel cabin, same light. The woman's face comes from @video1 only. Both sleeves stay zipped closed with her arms inside them in every frame. The embroidered logo stays on the lower front hem on her right side.
```

## B: hood-up segment, bigger hood
Source `@video1` = `montage/src-seg4-hood-v3.mp4` (5.05 s). `@image1` = `refs/hood-sleeve-ref.jpg`. Duration 5 s, 9:16.

```
SCENE CONTEXT
Edit of @video1: a woman in a black hoodie dress with the hood up stands in a stainless-steel elevator, typing on her phone, then lowers it and looks into the lens as the doors open in front of her. One change only: the hood is bigger.

ACTIVE REFERENCES
@video1: master for camera, framing, focus, door motion, her body motion, phone motion, expression timing, face, open sleeves, boots, background, lighting, grain and duration.
@image1: hood shape reference only. A large, roomy, deep hood that stands up off the head with soft volume, its rounded crown rising well above the top of the head, the opening wide and deep so it frames the face like a soft tunnel, the inner lining clearly visible around the face. 100% matches the reference in shape and size.

EDIT
The hood of the black hoodie dress is large and roomy, in black brushed fleece lined with deep teal satin. Its rounded crown rises 10 cm above the top of her head with soft air inside it, the sides stand 6 cm away from her cheeks, and the front edge sits at her hairline, so the wide, deep opening frames her whole face with a broad band of glossy teal satin lining on both sides. The hood drapes in soft heavy folds onto her shoulders and back. Her face sits fully visible inside the opening.

PHYSICS
The large hood keeps its rounded volume and moves gently with her head as one soft heavy piece of fleece, settling 0.3 seconds after each movement.

LIGHTING
One source: the white ceiling light panel inside the cabin, 4500K, soft and even from above, a gentle shadow under the chin and under the hem. The stainless-steel walls bounce the light back softly onto her front. The landing side is 1 stop darker than the cabin, so the open doorway glows. The same light and the same exposure in all four segments.

AUDIO
The audio of @video1 unchanged. No music.

POSITIVE LOCKS
Every pixel outside the hood stays exactly as in @video1: same face, same open sleeves hanging straight down, same black patent boots, same phone action, same door timing, same steel cabin, same light. The woman's face comes from @video1 only; @image1 gives the hood shape only. The hood stays black fleece with teal satin lining in every frame.
```

## After generation
Give me the two clips and I'll replace segments 3 and 4 in the montage, cutting again on the closed doors.

## C: a single prompt for both fixes (on the whole montage)
Feedback: "cant u give me one". Source `@video1` = `montage/elevator-v4-v3-cut-A.mp4` (19.34 s).
`@image1` = `refs/sleeve-zipped-crop.jpg`, `@image2` = `refs/hood-sleeve-ref.jpg`. Duration 19 s (as close as possible to the source), 9:16.
Risk: an edit of the whole video can also touch scenes 1–2. If it does, use A and B separately.

```
SCENE CONTEXT
Edit of @video1: a woman in a stainless-steel elevator appears in a new hoodie dress each time the doors open, four looks in total. Two changes only: in the cobalt-blue look the sleeves are zipped closed, and in the final black look with the hood up the hood is bigger.

ACTIVE REFERENCES
@video1: master for camera, framing, focus, door motion, cuts, her body motion, phone motion, expression timing, face, hair, outfits, boots, background, lighting, grain and duration.
@image1: sleeve reference only. A fully closed cobalt fleece sleeve with the silver zipper shut along its full length, wide and soft through the upper arm, gathering into a snug ribbed cuff at the wrist. 100% matches the reference.
@image2: hood shape reference only. A large, roomy, deep hood that stands up off the head with soft volume, its rounded crown rising well above the top of the head, the wide deep opening framing the face like a soft tunnel, the inner lining clearly visible around the face. 100% matches the reference in shape and size.

EDIT TIMELINE
0.0s to 10.0s — the black look and the chocolate-brown look stay exactly as in @video1, every pixel unchanged.
10.0s to 15.0s — the cobalt-blue look on the phone call: both sleeves are zipped closed from the shoulder seam to the cuff, as in @image1. Her arms are inside the sleeves the whole time: the right arm inside its sleeve as she holds the phone to her right ear, the left arm inside its sleeve hanging relaxed at her side. Wide soft cobalt fleece, the closed silver zipper a thin line along the outer seam, a snug cobalt ribbed cuff at each wrist with only her hands showing, soft folds at the bent right elbow.
15.0s to the end — the black look with the hood up: the hood is large and roomy, as in @image2, black brushed fleece lined with deep teal satin. Its rounded crown rises 10 cm above the top of her head with soft air inside it, the sides stand 6 cm away from her cheeks, the front edge sits at her hairline, and the wide deep opening frames her whole face with a broad band of glossy teal satin lining on both sides. The hood drapes in soft heavy folds onto her shoulders and back. The sleeves of this look stay open, hanging straight down as in @video1.

PHYSICS
Heavy fleece moves with her body and settles 0.3 seconds after each movement. The zipped blue sleeves move with her arms as one piece of fabric. The large hood keeps its rounded volume and moves gently with her head.

LIGHTING
One source: the white ceiling light panel inside the cabin, 4500K, soft and even from above, a gentle shadow under the chin and under the hem. The stainless-steel walls bounce the light back softly onto her front. The landing side is 1 stop darker than the cabin, so the open doorway glows. The same light and the same exposure in all four segments.

AUDIO
The audio of @video1 unchanged. No music.

POSITIVE LOCKS
Every pixel outside the blue sleeves and the final hood stays exactly as in @video1: same face, same hair, same four outfits in the same order, same boots, same phone actions, same door timing and cuts, same steel cabin, same light. The woman's face comes from @video1 only; @image1 gives the sleeve shape only and @image2 gives the hood shape only. The embroidered logo stays on the lower front hem on her right side in every look.
```

## D: Extend (recommended): 0–10 s approved + 10 s new

Feedback: "doesnt it make sense to regenerate as an extend video just the shot with the zipped and the hoodie". `@video1` = `montage/src-seg1-2-v4.mp4` (v4 0–10.0 s, ends on closed doors). `@image1` = `refs/sheet-blue-noface.jpg`, `@image2` = `refs/sleeve-zipped-crop.jpg`, `@image3` = `refs/sheet-black-noface.jpg`, `@image4` = `refs/hood-sleeve-ref.jpg`. Extend +10 s. It continues from the dark v4 doors, so the door-tone jump goes away.

```
SCENE CONTEXT
Extend @video1 by 10 seconds. The same woman stands inside the same stainless-steel elevator cabin, seen from the landing through the doorway, the camera locked in the same position. @video1 ends on the doors fully closed; the extension continues from that exact frame. The doors open twice more, revealing her first in a cobalt-blue hoodie dress on a phone call, then in the black hoodie dress with a large hood up. Vertical 9:16.

ACTIVE REFERENCES
@video1: master for camera position, framing, lens, door look and door motion, the steel cabin, the light, the grade, the grain and her face.
@image1: the same woman in the cobalt royal-blue hoodie dress. Cobalt fleece, silver zippers, glossy cobalt satin lining, dark navy tone-on-tone embroidered logo with the word "VIVAMUS" on the lower front hem on her right side, knee-high cream-white leather block-heel boots. 100% matches the reference.
@image2: sleeve reference only. A fully closed cobalt fleece sleeve with the silver zipper shut along its full length, wide and soft through the upper arm, gathering into a snug ribbed cuff at the wrist. 100% matches the reference.
@image3: the same woman in the black hoodie dress. Black brushed fleece, hood lined in deep teal satin, sleeves unzipped full length, teal embroidered half-sun logo with the word "VIVAMUS" on the lower front hem on her right side, knee-high black glossy patent stiletto boots. 100% matches the reference.
@image4: hood shape reference only. A large, roomy, deep hood that stands up off the head with soft volume, its rounded crown rising well above the top of the head, the wide deep opening framing the face like a soft tunnel, the lining clearly visible around the face. 100% matches the reference in shape and size.
One woman throughout, with the face from @video1: same face, same slicked-back centre-parted bun, same gold ear cuffs.

FORMAT MODE
Timed multishot, two segments of 5 seconds, continuing straight from the last frame of @video1. The cut happens only at the specified point, on the still closed doors; the camera does not cut on its own.

OPTICS
Full-figure wide shot, 47° rectilinear, no drift mid-segment, the same framing and lens as @video1.

CAMERA
Locked-off camera on a tripod at chest height, 1.3 metres, perfectly level, square to the doors, in exactly the same position as in @video1. The only motion is the doors and the woman.

WARDROBE
Segment one, cobalt-blue look: both sleeves are zipped closed from the shoulder seam to the cuff, as in @image2, with her arms inside them the whole time. Wide soft cobalt fleece, the closed silver zipper a thin line along the outer seam, a snug cobalt ribbed cuff at each wrist with only her hands showing.
Segment two, black look: the hood is up, large and roomy as in @image4, black brushed fleece lined with deep teal satin. Its rounded crown rises 10 cm above the top of her head with soft air inside it, the sides stand 6 cm away from her cheeks, the front edge sits at her hairline, and the wide deep opening frames her whole face with a broad band of glossy teal satin lining on both sides, the hood draping in soft heavy folds onto her shoulders and back. The sleeves are unzipped full length: her bare arms come out through the split below each shoulder, and each empty sleeve is a flat, limp strip of fleece hanging straight down from the shoulder seam behind her arm, the empty cuff dangling at mid-thigh.

ACTION
0.0s to 0.2s — doors fully closed and still, continuing the last frame of @video1.
0.2s to 1.2s — the doors slide fully open, each leaf moving 70 cm at 2.5 km/h, revealing @image1 in the cobalt-blue hoodie dress, hood down.
1.2s to 3.8s — @image1 holds the phone to her right ear, her right arm inside its zipped sleeve, elbow tucked against her ribs, listening. Her left arm hangs relaxed at her side inside its zipped sleeve. She shifts her weight slowly from her left leg to her right leg over 1 second, nods twice, and at 2.6s gives a small closed-lip laugh, her eyes dropping to the floor and lifting back up.
3.8s to 4.8s — the doors slide fully closed in front of her at 2.5 km/h until the two leaves meet in the centre.
4.8s to 5.0s — doors fully closed and still.
5.0s HARD CUT, doors fully closed
5.0s to 5.2s — doors fully closed and still.
5.2s to 6.2s — the doors slide fully open, revealing @image3 in the black hoodie dress with the large hood up.
6.2s to 10.0s — @image3 holds the phone in both hands just below her chest, head tilted down 15° inside the hood, both thumbs typing in short bursts. At 8.0s she lowers the phone to her waist in her right hand, lifts her head and looks straight into the lens, turns her shoulders 10° to the right and holds the pose until the end, doors fully open.

PERFORMANCE
Amused and relaxed on the call, calm and direct into the lens at the end. Lips closed, small closed-lip smiles. Eyes alive, natural blinks every 3–4 seconds, catch-lights from the ceiling panel in both eyes. Pore-level skin realism with a soft natural glow on the cheekbones.

PHYSICS
Heavy fleece moves with weight and settles 0.3 seconds after each movement. The zipped blue sleeves move with her arms as one piece of fabric. The large hood keeps its rounded volume and moves gently with her head. The empty black sleeve strips sway at most 2 cm and settle back to hanging straight down within 0.5 seconds. The door leaves slide on a straight track at constant speed, with a gentle deceleration over the last 10 cm. Boot heels stay planted on the floor, with soft contact shadows.

LIGHTING
One source: the white ceiling light panel inside the cabin, 4500K, soft and even from above, a gentle shadow under the chin and under the hem. The stainless-steel walls bounce the light back softly onto her front. The landing side is 1 stop darker than the cabin, so the open doorway glows. The same light and the same exposure in all four segments.

AUDIO
A soft single elevator chime at 0.2s and 5.2s as the doors begin to open. A faint indistinct voice from the phone speaker during the call in the first segment, soft thumb taps in the second. Quiet door-motor hum and the soft slide of the door leaves. No music.

STYLE
Photoreal fashion reel, natural colour, clean neutral steel tones with the outfit colour as the only saturated element in frame, fine film grain, matching @video1.

OUTPUT SETTINGS
9:16 vertical, 10-second extension, 24 fps, real-time speed throughout.

POSITIVE LOCKS
Camera position, framing, lens, door look, steel tone and exposure identical to @video1. Segment one cobalt blue with both sleeves zipped closed and her arms inside them; segment two black with the large hood up and the sleeves open. The woman's face comes from @video1 only; @image2 gives the sleeve shape only and @image4 gives the hood shape only. The embroidered logo stays on the lower front hem on her right side. One woman with the same face throughout.
```
