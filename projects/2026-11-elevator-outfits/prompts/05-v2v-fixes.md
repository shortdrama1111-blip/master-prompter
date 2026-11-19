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
