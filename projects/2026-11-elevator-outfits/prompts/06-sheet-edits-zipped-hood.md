# 06: Sheet edits for extend v2 (Banana Pro edit, 16:9)

Cause: in extend v1 (hf_20261119_200522) the blue sleeves stayed open because `sheet-blue-noface.jpg`
shows them open. The reference beats the text. The hood stayed small because `sheet-black` shows the hood down.

## A: blue, sleeves zipped
References, in this order: 1. `refs/sheet-blue.jpg` (the full sheet, with the face)  2. `refs/hood-sleeve-ref.jpg`

```
Keep the supplied image 1 exactly: same three panels, same woman, same face, hair, skin, cobalt hoodie dress, hood down, logo, cream-white boots, pose, backdrop, light, grade and grain. Change ONE thing only: both sleeves are zipped closed from the shoulder seam to the cuff, like the sleeves in image 2. Her arms are inside the sleeves: wide, soft cobalt fleece through the upper arm, the closed silver zipper a thin line along the outer seam, a snug cobalt ribbed cuff at each wrist with only her hands showing. Image 2 gives the sleeve shape only; the woman, her face and every other detail come from image 1. The logo panel stays untouched.
```

## B: black, large hood up
References, in this order: 1. `refs/sheet-black-v3.jpg`  2. `refs/hood-sleeve-ref.jpg`

```
Keep the supplied image 1 exactly: same three panels, same woman, same face, skin, black hoodie dress, open sleeves with teal satin lining, logo, black patent boots, pose, backdrop, light, grade and grain. Change ONE thing only, in the left and centre panels: the hood is raised over her head, large and roomy like the hood in image 2. Its rounded crown rises 10 cm above the top of her head with soft volume, the sides stand away from her cheeks, the front edge sits at her hairline, and the wide, deep opening frames her whole face with a broad band of glossy deep teal satin lining on both sides. The hood drapes in soft heavy folds onto her shoulders and back. Her bun sits hidden inside the hood, her face fully visible. Image 2 gives the hood shape and size only; the woman, her face and every other detail come from image 1. The logo panel stays untouched.
```

## After generation
Send me both sheets and I'll take the face out of the centre panel (as with the earlier noface sheets).
Then extend v2 from `montage/src-seg1-2-v4.mp4`, with the new sheets as @image1 and @image3,
without the sleeve crop and without hood-sleeve-ref, because the sheets now show both.


## v2: double collar on all three sheets
Feedback: "it looks like it has two collars, the inner one up to the throat, then the hood over it" + "this applies to all the photos".
Neckline reference: `refs/double-collar-crop.jpg` (the brown photo, cropped without the face). Black detail: `refs/black-collar-detail.jpg`.

### A2: blue, zipped sleeves + double collar
References: 1. `refs/sheet-blue.jpg`  2. `refs/sleeve-zipped-crop.jpg`  3. `refs/double-collar-crop.jpg`
```
Keep the supplied image 1 exactly: same three panels, same woman, same face, hair, skin, cobalt hoodie dress, hood down, logo, cream-white boots, pose, backdrop, light, grade and grain. Change only the sleeves and the neckline. Both sleeves are zipped closed from the shoulder seam to the cuff, like the sleeves in image 2: her arms are inside the sleeves, wide soft cobalt fleece through the upper arm, the closed silver zipper a thin line along the outer seam, a snug cobalt ribbed cuff at each wrist with only her hands showing. The neckline has two layers, like image 3: a separate snug ribbed crew-neck collar sits close around the base of her throat, and the hood is attached outside it, its two front edges crossing over each other in a soft overlap just below the crew-neck collar, the glossy cobalt satin hood lining visible along its inner edge. The crew-neck collar is cobalt ribbed knit. Image 2 gives the sleeve shape only and image 3 gives the neckline construction only; the woman, her face, the colour and every other detail come from image 1. The logo panel stays untouched.
```

### B2: black, big hood + double collar
References: 1. `refs/sheet-black-v3.jpg`  2. `refs/hood-sleeve-ref.jpg`  3. `refs/double-collar-crop.jpg`
```
Keep the supplied image 1 exactly: same three panels, same woman, same face, skin, black hoodie dress, open sleeves with teal satin lining, logo, black patent boots, pose, backdrop, light, grade and grain. Change only the hood and the neckline, in the left and centre panels. The hood is raised over her head, large and roomy like the hood in image 2: its rounded crown rises 10 cm above the top of her head with soft volume, the sides stand away from her cheeks, the front edge sits at her hairline, and the wide, deep opening frames her whole face with a broad band of glossy deep teal satin lining on both sides, the hood draping in soft heavy folds onto her shoulders and back. Her bun sits hidden inside the hood, her face fully visible. The neckline has two layers, like image 3: a separate snug ribbed crew-neck collar sits close around the base of her throat, and the hood is attached outside it, its two front edges crossing over each other in a soft overlap just below the crew-neck collar, the teal satin hood lining visible along its inner edge. The crew-neck collar is black ribbed knit, visible at her throat inside the raised hood. Image 2 gives the hood shape and size only and image 3 gives the neckline construction only; the woman, her face and every other detail come from image 1. The logo panel stays untouched.
```

### C2: brown, double collar
References: 1. `refs/sheet-brown.jpg`  2. `refs/double-collar-crop.jpg`
```
Keep the supplied image 1 exactly: same three panels, same woman, same face, hair, skin, chocolate-brown hoodie dress, hood down, open sleeves, logo, brown boots, pose, backdrop, light, grade and grain. Change ONE thing only, the neckline. The neckline has two layers, like image 2: a separate snug ribbed crew-neck collar sits close around the base of her throat, and the hood is attached outside it, its two front edges crossing over each other in a soft overlap just below the crew-neck collar, the brown satin hood lining visible along its inner edge. The crew-neck collar is chocolate-brown ribbed knit. Image 2 gives the neckline construction only; the woman, her face and every other detail come from image 1. The logo panel stays untouched.
```

### D2: black, hood DOWN + double collar (for segment 1)
Segment 1 needs the black with the hood down, so black gets two sheets: D2 (hood down) and B2 (hood up).
References: 1. `refs/sheet-black-v3.jpg`  2. `refs/double-collar-crop.jpg`
```
Keep the supplied image 1 exactly: same three panels, same woman, same face, hair, skin, black hoodie dress, hood down, open sleeves with teal satin lining, logo, black patent boots, pose, backdrop, light, grade and grain. Change ONE thing only, the neckline. The neckline has two layers, like image 2: a separate snug ribbed crew-neck collar sits close around the base of her throat, and the hood is attached outside it, its two front edges crossing over each other in a soft overlap just below the crew-neck collar, the teal satin hood lining visible along its inner edge. The crew-neck collar is black ribbed knit. Image 2 gives the neckline construction only; the woman, her face and every other detail come from image 1. The logo panel stays untouched.
```

### File names after the face is removed
- D2 → `refs/sheet-black-collar-noface.jpg` (@image1 in the final video)
- C2 → `refs/sheet-brown-collar-noface.jpg` (@image2)
- A2 → `refs/sheet-blue-zip-noface.jpg` (@image3)
- B2 → `refs/sheet-black-hood-noface.jpg` (@image4)


## v3: panel locks (after the result `refs/sheet-black-collar-v1.jpg`)
Result D2 v1: the collar is visible in the centre, but (1) it isn't in the left face panel, and (2) the right panel turned into a
neckline close-up instead of the logo. Cause: the prompt said "change the neckline" without naming the panels, and the
collar reference (a close-up) got copied as the third panel. Fix: name every panel and lock the logo panel.

### D3: black hood down, fixing v1
Images: 1. `refs/sheet-black-collar-v1.jpg`  2. `refs/sheet-black-v3.jpg` (for the logo panel)
```
Keep the supplied image 1 exactly: same three panels, same woman, same face, hair, skin, black hoodie dress, open sleeves with teal satin lining, black patent boots, pose, backdrop, light, grade and grain. Change two things only. In the left face close-up panel: a snug black ribbed crew-neck collar is clearly visible around the base of her throat inside the hood opening, with the two crossed hood edges just below it and the teal satin lining along the inner edge of the hood, exactly like the neckline in the right panel of image 1. The right panel becomes the logo close-up from the right panel of image 2: tight crop on the lower front hem, the teal embroidered half sun with radiating rays above the word "VIVAMUS", sharp and centred, raised thread texture and black fleece weave visible. The centre panel stays untouched.
```
Once this is approved, it becomes `sheet-black-collar.jpg` and is the base for the hood sheet (B3).

### C3: brown + collar
Images: 1. `refs/sheet-brown.jpg`  2. `refs/double-collar-crop.jpg`
```
Keep the supplied image 1 exactly: same three panels, same woman, same face, hair, skin, chocolate-brown hoodie dress, hood down, open sleeves, logo, brown boots, pose, backdrop, light, grade and grain. Change ONE thing only, the neckline. The neckline has two layers, like image 2: a separate snug ribbed crew-neck collar sits close around the base of her throat, and the hood is attached outside it, its two front edges crossing over each other in a soft overlap just below the crew-neck collar, the brown satin hood lining visible along its inner edge. The crew-neck collar is chocolate-brown ribbed knit. Panel by panel: in the left face close-up, the chocolate-brown ribbed crew-neck collar is clearly visible around the base of her throat inside the hood opening, with the crossed hood edges just below it. In the centre full-body panel the same double neckline is visible. The right panel stays exactly the logo close-up of image 1: the embroidered logo on the lower front hem, reading "VIVAMUS", untouched. Image 2 gives the neckline construction only; the woman, her face and every other detail come from image 1.
```

### A3: blue, zipped + collar
Images: 1. `refs/sheet-blue.jpg`  2. `refs/sleeve-zipped-crop.jpg`  3. `refs/double-collar-crop.jpg`
```
Keep the supplied image 1 exactly: same three panels, same woman, same face, hair, skin, cobalt hoodie dress, hood down, logo, cream-white boots, pose, backdrop, light, grade and grain. Change only the sleeves and the neckline. Both sleeves are zipped closed from the shoulder seam to the cuff, like the sleeves in image 2: her arms are inside the sleeves, wide soft cobalt fleece through the upper arm, the closed silver zipper a thin line along the outer seam, a snug cobalt ribbed cuff at each wrist with only her hands showing. The neckline has two layers, like image 3: a separate snug ribbed crew-neck collar sits close around the base of her throat, and the hood is attached outside it, its two front edges crossing over each other in a soft overlap just below the crew-neck collar, the glossy cobalt satin hood lining visible along its inner edge. The crew-neck collar is cobalt ribbed knit. Panel by panel: in the left face close-up, the cobalt ribbed crew-neck collar is clearly visible around the base of her throat inside the hood opening, with the crossed hood edges just below it. In the centre full-body panel the same double neckline is visible. The right panel stays exactly the logo close-up of image 1: the embroidered logo on the lower front hem, reading "VIVAMUS", untouched. Image 2 gives the sleeve shape only and image 3 gives the neckline construction only; the woman, her face, the colour and every other detail come from image 1.
```

### B3: black, big hood (from the approved D3)
Images: 1. `refs/sheet-black-collar.jpg` (the D3 result)  2. `refs/hood-sleeve-ref.jpg`
```
Keep the supplied image 1 exactly: same three panels, same woman, same face, skin, black hoodie dress, open sleeves with teal satin lining, black patent boots, pose, backdrop, light, grade and grain. Change only the hood, in the left and centre panels. The hood is raised over her head, large and roomy like the hood in image 2: its rounded crown rises 10 cm above the top of her head with soft volume, the sides stand away from her cheeks, the front edge sits at her hairline, and the wide, deep opening frames her whole face with a broad band of glossy deep teal satin lining on both sides, the hood draping in soft heavy folds onto her shoulders and back. Her bun sits hidden inside the hood, her face fully visible. The black ribbed crew-neck collar of image 1 stays clearly visible around the base of her throat inside the raised hood, with the crossed hood edges just below it, in both the left and centre panels. The right panel stays exactly the logo close-up of image 1, untouched. Image 2 gives the hood shape and size only; the woman, her face and every other detail come from image 1.
```
