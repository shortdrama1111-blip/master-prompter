# Mësimet nga projektet

Shto mësimet më të rejat sipër. Format:

```
## YYYY-MM-DD — emri i projektit (modeli)
- [funksionoi / dështoi] çfarë → shkaku → zgjidhja
- Statusi: i ri | konfirmuar 2x → kaluar te <skill>
```

---

## 2026-11-21 — burim i jashtëm: "Nexus LENS — Anamorphic Blockbuster" (Seedance + Seedream)
- [për t'u provuar] Plate drite me key të fortë, të fotografuar nga ana e hijes + bllok drite i
  testuar në 5–10 gjenerime → Seedance nuk i sheshon shot-et. Kaloi te `cinematic-ai-video` §3.
- [për t'u provuar] Referenca me "fetë" (një rresht për çdo @image: çfarë merret) → modeli s'e
  kopjon kompozimin e plate-it të dritës. Kaloi te `seedance-clean` → Reference slicing.
- [vendim] "Edit mbi edit e zbut imazhin" pajtohet me rregullin #8: një editim po, zinxhir jo.
- [vendim] Rreshti "NEVER" i dritës u kthye në pohore ("the light stays ...").
- Statusi: i ri.

## 2026-11-21 — burim i jashtëm: "Nexus Blender Storyboard Workflow" (Seedance)
- [për t'u provuar] Blockout 3D në Blender → kamera reale → storyboard gri si referencë → modeli
  ruan përmasat, drejtimin në ekran dhe pozicionet më mirë se me tekst vetëm. Shkaku: modelet janë
  të dobëta në logjikë hapësinore. Zgjidhja: skill `blender-blockout` + `seedance-clean` → SPATIAL LOCK.
- [për t'u provuar] Busull e fiksuar (N/E/S/W me sfond të njohur) + `CAM FACING` për çdo shot
  ruan rregullin 180° nëpër prerje.
- Statusi: i ri. Shembulli i tyre përdor emra pajisjesh dhe 9 shot-e në një gjenerim, gjë që bie
  ndesh me konfliktet e hapura; s'u mor.
