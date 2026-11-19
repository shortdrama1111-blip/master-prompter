# v5: Seedance 2.5 extend, shot-et 5–6 (6 s) mbi montimin Blender të shot-eve 1–4

| Ngarko si | Skedari |
|---|---|
| `@video1`, videoja që zgjatet | `renders/cut_s1-s4_v1.mp4` (10.4 s) |
| `@image1` | `refs/holiday-bag-red.jpg` |
| `@image2` | `refs/dreamduo-box.jpg` |
| `@image3` | `refs/hair-oil-with-box.jpg` |

- **Zgjatja:** 6 s. Shot-i 5 zë 0.0–2.0 s, shot-i 6 zë 2.0–6.0 s.
- **Në montim:** shot-i 5 pritet në ~1.7 s. Shkrimi i kartës, logoja dhe muzika shtohen në montim.
- **Rreziku:** teksti i vogël i printit të çantës, i DreamDuo-s dhe i kutisë së vajit mund të dalë i shpikur.
  Nëse ndodh, shot-i 5 bëhet në Blender (`blender/shot5_final.py`, testi është gati).

```
SCENE CONTEXT
The extension of @video1: a six-second ending for a luxury holiday haircare film in the same soft mocha studio. First a pyramid of wrapped gifts with the red holiday bags and the haircare products, where a small gift drops onto the very top; then a close-up of the top of a red holiday bag with a small blank tag swaying on its handle.

ACTIVE REFERENCES
@video1: the clip being extended. Master for the studio look carried into the new shots: soft mocha-brown walls, brushed champagne metal, warm gold LED lines, soft neutral front light, clean product colour, shallow depth of field and smooth eased camera moves.
@image1: deep red holiday gift bag, white snowflakes across the upper face, white "INDRIT GJUZI HAIRCARE" wordmark in the centre, illustrated winter figures along the bottom, flat white satin ribbon handles. 100% matches the reference.
@image2: DreamDuo Limited Edition gift box, peach box with flowing gold and cream waves, two cream bottles pictured on the front, serif "DreamDuo" title at the top. 100% matches the reference.
@image3: Nourishing Hair Oil, 40 ml clear glass bottle with a glossy black cap and white dip tube, beside its tall pale-peach box with vertical white "INDRIT GJUZI" lettering. 100% matches the reference.

LOCATION MAP
The same studio as @video1: a soft mocha-brown wall 1.5 metres behind the set, a mocha floor. Shot five: the gift pyramid stands centre frame on the floor, camera straight in front at the height of its middle tier. Shot six: one @image1 bag stands on a low mocha plinth against the same wall, camera facing its front just above the top edge. Light comes from camera-left in both shots.

FIRST FRAME / BLOCKING
0.0s: a pyramid of wrapped gifts fills the lower two-thirds of the frame, three boxes on the base, two on the middle tier, one on top, each turned a few degrees off square, wrapped in cream, champagne and soft gold paper with deep red satin ribbon crossing each box and a full red bow on top. An @image1 bag stands on the middle tier at the right beside the top gift. A second @image1 bag stands angled at the front left on the floor, its snowflakes and winter figures facing camera. An @image2 DreamDuo box leans upright at the front centre, its front facing camera. An @image3 beige oil box stands at the front right with the clear @image3 oil bottle just in front of it. A small cream gift box with a red bow hangs 30 cm above the top gift, already falling.

FORMAT MODE
Timed multishot with one cut. Cuts only at the specified points, the camera does not cut on its own. The extension opens with a HARD CUT out of the last frame of @video1.

OPTICS
0.0s to 2.0s: 29° front shot, rectilinear, focus locked on the front products, the wall in soft warm bokeh, no drift mid-segment.
2.0s to 6.0s: 29° close-up, rectilinear, focus locked on the tag, the tissue paper and wall behind falling into warm bokeh, no drift mid-segment.

CAMERA
0.0s to 2.0s: eye level with the middle tier, a slow eased push-in of 15 cm.
2.0s to 6.0s: slightly above the bag's top edge, a slow eased push-in of 4 cm, settling at the end. Tonal character: rich soft shadows with detail, gentle highlight roll-off, pure whites, true peach and red.

ACTION
0.0s HARD CUT from the last frame of @video1.
0.0s to 2.0s — The small cream gift drops straight down onto the top gift, lands at 0.4s with one soft 1 cm bounce and settles; its bow presses flat for a moment and springs back. Every other gift, bag and product rests still while the camera pushes in.
2.0s HARD CUT
2.0s to 6.0s — Close-up on the top third of an @image1 bag: the red face printed with small white snowflakes fills the lower two-thirds of the frame, the top edge crosses the upper third, the flat white satin handle arches above it and pale champagne tissue paper rises from the opening. A small blank cream tag with rounded corners hangs on a short white satin ribbon from the handle, centred and sharp, swaying ±3° at 0.4 swings per second; the tissue paper lifts 5 mm in a slow breath of air.

PHYSICS
Gifts have real weight, stacked solidly with soft contact shadows on the tier below. The falling gift accelerates under gravity and stops with a small elastic bounce. Satin ribbon and bows hold their folds; the tag swings like a light card on a ribbon.

LIGHTING
Warm luxury studio light: slim 3200K LED strips glow warm gold along the edges of the set and wash softly down over the products; one large soft neutral-white front key from camera-left at 30° height evenly lights every product face so each label reads crisp; soft mocha-brown walls take a gentle warm spill and fall off into deeper brown shadow; champagne metal edges catch thin bright highlights. White caps read pure white and the peach and cream packaging keeps its true printed colour, standing out clearly against the soft mocha.

COLOR GRADE
Soft mocha wall and floor carry 60% of the frame; cream, champagne and soft gold wrapping with the peach @image2 and @image3 packaging carry 25%; deep festive red in the @image1 bags, satin ribbons and bows carries 15% as the reserved accent. Blacks are warm brown, whites are clean.

AUDIO
No music. A soft paper tap as the gift lands, a faint rustle of tissue paper.

STYLE
Photoreal luxury product commercial, soft warm studio, crisp printed card, satin and paper textures, fine subtle grain, matching the look of @video1.

OUTPUT SETTINGS
9:16 vertical, 6-second extension, real-time speed, 24 fps.

POSITIVE LOCKS
Every bag, box and bottle keeps the exact shape, colour and print layout of its reference. The @image1 bag stays deep red with white snowflakes and white satin handles; the @image2 box stays peach with gold and cream waves; the @image3 bottle stays clear glass with a black cap. The tag stays clean and blank. The studio stays soft mocha with champagne and warm gold accents, as in @video1.
```
