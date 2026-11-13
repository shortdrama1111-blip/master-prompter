# Plate i makinës — image, 9:16 — v1
Model i rekomanduar: Nano Banana Pro ose Seedream (interiore pa njerëz). 4 variante.

```
Empty rear seat of a modern luxury sedan photographed from inside the car. The camera sits low between the two front seats at seat-cushion height, looking straight back at the rear bench, ultra-wide 107-degree view with gentle natural wide-angle stretch at the edges. Foreground: the backs of the two front seats frame the image on the left and right edges, each filling about 18% of the frame width, softly out of focus, cream quilted leather. Middle ground: the rear bench in smooth cream nappa leather with fine tonal stitching, three headrests, a folded centre armrest, seat belts resting in their holders, the seat cushion empty and clean with space for one person to sit in the centre. Above: black alcantara headliner. Background: both rear side windows and the rear windscreen show a bright, softly blurred green tree-lined street.
Soft natural daylight at 5600K enters through the left and right rear side windows and the rear windscreen, diffused by light cloud, wrapping the rear bench evenly from both sides. The cream leather bounces a warm soft fill upward; the black headliner stays deep and dark. Exposure is set for skin, so the window glass glows bright with the street outside softly overexposed. Neutral white balance 5600K, gentle contrast, clean whites, rich true blacks.
The cabin is spotless and holds only the seats, belts and armrest. Unretouched photograph, true-to-life leather texture, fine natural grain, vertical 9:16.
```

## Rezultati v1 (16:9, mbështetësja e krahut poshtë) → rruga: crop + 2 edit-e
Gabimi te prompti v1: rreshti "three headrests, a folded centre armrest" → modeli e uli mbështetësen.
Formati 16:9: raporti në UI të platformës ishte 16:9; teksti "vertical 9:16" nuk e mbivendos.
Claude preu katrorin qendror 1125×1125 → `refs/plate-v1-crop-square.png` (emblema e kokëmbajtëses mbetet jashtë).

### Edit 1 — mbështetësja lart (input: plate-v1-crop-square.png, output 1:1)
```
Keep the supplied image exactly — same camera, framing, seats, belts, lighting, grade and grain. Change ONE thing only: the centre armrest of the rear bench is folded up and stored flush inside the backrest, so the middle seat back is one continuous smooth cream nappa leather surface with the same vertical stitching lines as the two outer seats, and the middle seat cushion is open, flat and empty, ready for one person to sit in the centre. Everything else untouched.
```

### Edit 2 — zgjerimi në 9:16 (input: rezultati i Edit 1, raporti 9:16 në UI)
```
Keep the supplied image exactly — same camera, seats, belts, lighting, grade and grain, with all existing content unchanged in the middle of the frame. Change ONE thing only: extend the canvas to vertical 9:16. Above, continue the dark taupe headliner and the grab handle on the right up to the top edge. Below, continue the front edge of the cream rear seat cushion, then the dark carpeted rear footwell floor, with the lower parts of the two cream front seatbacks still framing the left and right edges. Everything else untouched.
```

## v2 — rigjenerim nga zero, mbështetësja e mbyllur që në fillim (raporti 9:16 në UI)
```
Empty rear seat of a modern luxury sedan photographed from inside the car, vertical 9:16. The camera sits low between the two front seats at seat-cushion height, looking straight back at the rear bench, ultra-wide 107-degree view with gentle natural wide-angle stretch at the edges. Foreground: the backs of the two front seats frame the image on the left and right edges, each filling about 18% of the frame width, softly out of focus, smooth cream leather. Middle ground: a continuous three-seat rear bench in smooth cream nappa leather with fine tonal vertical stitching. The backrest is one unbroken leather surface from the left door to the right door: the centre armrest is folded up and stored flush inside the backrest, its leather face level with the seat back around it, so the middle seat back looks exactly like the two outer seat backs. The middle seat cushion is open, flat and empty, the widest clear space on the bench, ready for one person to sit in the centre. Three cream headrests, black seat belts resting along the outer seats. Above: dark taupe headliner with a grab handle on the right. Background: both rear side windows and the rear windscreen show a bright, softly blurred green tree-lined street.
Soft natural daylight at 5600K enters through the left and right rear side windows and the rear windscreen, diffused by light cloud, wrapping the rear bench evenly from both sides. The cream leather bounces a warm soft fill upward; the dark taupe headliner stays deep and shadowed. Exposure is set for skin, so the window glass glows bright with the street outside softly overexposed. Neutral white balance 5600K, gentle contrast, clean whites, rich true blacks.
The cabin is spotless and holds only the seats, headrests and belts; every leather surface is plain and unbranded. Unretouched photograph, true-to-life leather texture, fine natural grain.
```

## v3 → Opsioni B (zgjedhur nga përdoruesi): zoom-out me shpinoret e përparme
Rruga 1 (edit direkt mbi `refs/plate-v3-916.jpg`):
```
Keep the supplied image exactly — same rear bench, headrests, belts, windows, trees, lighting, grade and grain. Change ONE thing only: the camera moves 60 cm backward and sits low between the two front seats at seat-cushion height, widening the view to an ultra-wide 107-degree angle. The whole current scene becomes smaller in the centre of the frame, and the backs of the two front seats now frame the left and right edges, each filling about 18% of the frame width, softly out of focus, in the same smooth cream leather. Above, more of the dark taupe headliner; below, the front edge of the rear cushion and the dark carpeted footwell floor. Everything else untouched.
```
Rruga 2 (rezervë, nëse rruga 1 e ndryshon sediljen): outpaint mbi `refs/plate-v3-outpaint-canvas.png`
(plate-i i zvogëluar 62% në qendër, kornizë gri për t'u mbushur):
```
Fill only the flat grey border around the supplied photo; keep the photo in the centre exactly as it is. The filled area continues the same car interior seen from low between the two front seats: the backs of the two front seats in smooth cream leather frame the left and right edges, softly out of focus; above, the dark taupe headliner with a grab handle on the right; below, the front edge of the cream rear cushion and the dark carpeted footwell floor; at the far left and right, the rear door panels in cream leather. Same soft 5600K daylight, same grade and grain, seamless edges.
```
