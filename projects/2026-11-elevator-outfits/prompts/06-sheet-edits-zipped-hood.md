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
