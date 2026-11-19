# v2: e gjithë videoja me 1 gjenerim (Seedance 2.5)

## Ndryshimet nga v1 (pse)
| Problemi te v1 | Shkaku | Ndryshimi te v2 |
|---|---|---|
| Produkte të vogla në kuadër | Kamerat e previz-it larg | Previz v3: kamera 2–3× më afër, stolira më të mëdha |
| Dritë e sheshtë, hije të forta | Llamba sun në previz | Previz v3: softbox; prompti: glow, rim light, bloom |
| Pa thellësi | "soft natural falloff" shumë e dobët | Previz v3 me DOF; prompti: f/2.8 si look, plan i parë i turbullt |
| Gjithçka pjeshkë | 60:30:10 pa nuancë të dytë | Ar i butë metalik si nuancë e dytë te seti |
| Stolira kube të vegjël | Previz + "thin gold threads" | Stolira të mëdha me dritare dhe fije 2 cm |
| Prerjet në kohë të gabuar | 5 prerje në 1 gjenerim | Kohëzgjatja e çdo shot-i e thënë 3 herë |
| Logoja e çantës e shtrembër | Modeli s'riprodhon shkrimin | Kuadri i fundit mbi pjesën e sipërme të çantës, logoja jashtë kuadrit |
| Shot 1 (kërkesë e re) | — | Kolonat si ashensor: mesi lart, anët poshtë |

## Cilësimet
- Kohëzgjatja: **16s** · Formati: **9:16** · Modeli: Seedance 2.5
- Ngarko në këtë rend:

| Tag | Skedari |
|---|---|
| `@video1` | `previz/previz_v3_full.mp4` |
| `@image1` | `refs/peptide-mask.jpg` |
| `@image2` | `refs/dreamduo-box.jpg` |
| `@image3` | `refs/holiday-bag-red.jpg` |
| `@image4` | `refs/hair-oil-with-box.jpg` |
| `@image5` | `refs/leave-in-conditioner.jpg` |

Dorëshkrimi mbi kartë, logoja e mbylljes dhe muzika shtohen në montim.

## Prompti

```
SCENE CONTEXT
A sixteen-second festive product film for a haircare brand inside a warm peach studio dreamworld: glowing elevator shelves, a spiral conveyor, a garland of ornament boxes, diagonal belts, a pyramid of gifts and a close-up gift tag. Six shots joined by hard cuts. The only objects are the products, their gift boxes, ornaments and gift bags.

ACTIVE REFERENCES
@video1: grey previz. Master for camera path, framing, shot order, cut timing and the motion of every object. Its grey blocks are stand-ins only; every surface, colour, material and light comes from the images and text below.
@image1: Leave-In Peptide Mask, 150 ml matte cream-peach cylinder bottle with a tall glossy white cap, thin black brand wordmark and centred label. 100% matches the reference.
@image5: Nourishing Leave-In Conditioner, the same matte cream-peach bottle and glossy white cap with its own centred label. 100% matches the reference.
@image4: Nourishing Hair Oil, 40 ml clear glass bottle with a glossy black cap and white dip tube, beside its tall pale-beige box with vertical white lettering. 100% matches the reference.
@image2: DreamDuo Limited Edition gift box, peach box with flowing gold and cream waves, two bottles pictured on the front, serif title at the top. 100% matches the reference.
@image3: deep red holiday gift bag with white snowflakes, illustrated winter figures along the bottom and white satin ribbon handles. 100% matches the reference.

LOCATION MAP
One continuous world. Set surfaces are warm peach velvet and soft peach plaster, trimmed with thin brushed soft-gold edges; conveyor slats are warm cream lacquer; rails are clear glass. Every shot has three layers: a soft out-of-focus foreground element within 30 cm of the lens, the products sharp in the middle, and peach walls melting into warm haze at 2 to 3 metres. Light comes from camera-left in every shot.

FIRST FRAME / BLOCKING
Frame one is already full: three tall columns of glowing shelf cubbies fill the frame edge to edge, a product standing in every cubby, products filling 25% of the frame height each. Every object is already in motion from frame one, exactly as in @video1.

FORMAT MODE
Timed multishot, six segments. Cuts only at the specified points, the camera does not cut on its own.

OPTICS
Rectilinear lens with shallow depth of field, focus locked on the nearest product of each shot, backgrounds falling into creamy bokeh, small glints blooming into soft round highlights. Segment FOV: 47° for shots 1 to 3, 29° for shots 4 to 6, no drift mid-segment. Framing in each segment matches @video1, with products large in frame.

CAMERA
The camera follows @video1 exactly: same height, distance, direction and speed of every move. Moves are smooth and eased in and out, with a calm settle at the end of each one. Tonal character: soft highlight roll-off, creamy whites, deep warm shadows with detail.

ACTION
0.0s to 1.7s, shot one, lasting 1.7 seconds — The camera is locked, facing three tall columns of square cubbies, each cubby glowing warm from behind. @image1 and @image5 bottles, @image4 oil bottles and @image4 beige boxes stand one per cubby. The columns move like elevators: the centre column glides up at 0.65 km/h while the two columns beside it glide down at the same speed, products riding along, easing to a stop together.
1.7s HARD CUT
1.7s to 4.7s, shot two, lasting 3.0 seconds — Close on a cream conveyor belt spiralling around a thick peach velvet column. Two @image2 DreamDuo boxes and one @image4 beige oil box ride the belt upright right in front of the lens, front faces turned outward, travelling left to right at 0.4 km/h; the next turn of the spiral with more boxes sits soft above and below. The camera drifts 20 cm to the left.
4.7s HARD CUT
4.7s to 7.7s, shot three, lasting 3.0 seconds — A clear glass rail sweeps diagonally through frame in a looping arc. A dense garland of cream ornament boxes hangs from it on 2 cm soft-gold threads, close together: tall ones shaped like the @image4 box and square ones, each with a soft-gold edge and a small window showing a miniature bottle inside. They glide along the rail at 0.3 km/h and swing 9° on their threads, each at its own rhythm. The nearest ornaments fill a third of the frame. The camera looks slightly up and orbits 5° to the right.
7.7s HARD CUT
7.7s to 10.3s, shot four, lasting 2.6 seconds — High angle down onto two parallel cream conveyor belts running diagonally down to the left, slats scrolling. @image2 DreamDuo boxes alternate with @image4 beige oil boxes, standing upright, close together, riding down-left at 0.5 km/h. The camera holds high and drifts 6 cm.
10.3s HARD CUT
10.3s to 12.0s, shot five, lasting 1.7 seconds — Front view of a pyramid of wrapped gifts, each box turned at its own slight angle: cream, peach and soft-gold paper tied with deep red satin ribbon and full bows. An @image3 bag sits angled on top beside a gift, a second @image3 bag leans at the front left, an @image2 DreamDuo box leans at the centre front, an @image4 oil bottle and its beige box stand at the base. A small cream gift box drops 35 cm onto the very top, lands with a soft bounce and settles by 10.8s. The camera pushes in 15 cm.
12.0s HARD CUT
12.0s to 15.8s, shot six, lasting 3.8 seconds — Close-up on the top edge of the @image3 bag: red paper with white snowflakes fills the lower frame, two thin white satin handles arch over the top, pale peach tissue paper rises from the opening. A small blank cream rounded tag hangs on a thin white satin ribbon from the front handle, tilted 14°, swaying 3° side to side, sharp in the centre of frame. The bag wordmark sits below the bottom edge of the frame; the tag face is clean and empty. The camera pushes in 4 cm and settles.

PHYSICS
Boxes have real weight: they sit firmly on the slats with soft contact shadows and stay upright on curves. Shelf columns glide on smooth rails, products steady on their shelves. Ornaments swing as pendulums on their threads and ease back to rest. The dropped gift box compresses its bow slightly on landing. Satin ribbons hang with soft weight.

LIGHTING
Soft warm studio light: one large diffused key from camera-left at 45° height, 4000K, wrapping gently around bottles and boxes with soft contact shadows; a warm 3500K rim from behind camera-right outlines every product edge with a thin glowing line; warm peach bounce fill from the set at 30% of the key; the shelf cubbies glow evenly from behind at 3500K with a gentle bloom. White caps and the cream tag sit just below clipping, glass and gold catch one long soft highlight.

COLOR GRADE
Warm peach velvet and plaster carry 60% of every frame; cream-beige bottles, boxes and slats carry 25%; soft brushed gold on trims, threads and ornament edges carries 5%; deep festive red lives only in the @image3 bags and satin ribbons, 10%, the single reserved accent. Blacks are warm brown-black, whites are creamy.

AUDIO
No music. Soft mechanical glide of the shelf columns, gentle conveyor hum, cardboard taps on the slats, faint glass ticks from the ornaments, one soft cardboard landing on the gift pyramid, a quiet satin rustle as the tag sways.

STYLE
Photoreal premium product commercial, 3D studio dreamworld, tactile velvet, lacquer, glass and paper materials, fine subtle grain.

OUTPUT SETTINGS
9:16 vertical, 16 seconds, real-time speed throughout, 24 fps.

POSITIVE LOCKS
Every bottle, box and bag keeps the exact shape, colour, cap and label layout of its reference in every shot. Products stand upright and fill a large part of the frame. The set stays warm peach with soft-gold trims in all six shots; deep red appears only on the @image3 bags and ribbons. The tag stays clean and blank. Shot lengths are 1.7, 3.0, 3.0, 2.6, 1.7 and 3.8 seconds; cuts land exactly at 1.7s, 4.7s, 7.7s, 10.3s and 12.0s.
```
