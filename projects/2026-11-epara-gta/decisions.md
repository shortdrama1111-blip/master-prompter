# Vendimet e ngulitura

## Blloku i dritës (fjalë për fjalë në çdo prompt)
```
Light: golden hour over Tirana, low sun from the west at 8° elevation, warm 3200 K key light, long soft shadows across the pavement, cool 7000 K skylight filling the shadows, warm rim light on hair and shoulders, light haze over the distant mountains. Indoors the same low 3200 K sun pours through the glass shop front and mixes with cool white 6500 K neon tubes and soft cyan neon accents.
```
(v1, draft. Neoni i dyqanit: i bardhë + cyan, jo vjollcë, sepse vjollca është e kartës.)

## Ngjyra: 60:30:10, aksenti i rezervuar
Aksenti i rezervuar = **violet-magenta e kartës epara** (hex nga logo SVG: magenta `#D2007F`, indigo `#312783`, blu `#0080C9`, koral `#E94C45`) (blu-indigo → vjollcë, me logon e bardhë vertikale).
Shfaqet VETËM te karta, te ekrani i POS-it dhe te HUD-i epara. Rrobat dhe bota pa vjollcë/magenta.

## Elementet / referencat
| Tag | Çfarë është | Shënime |
|---|---|---|
| `@Djali-GTA-Plastik` | djalë ~25 vjeç, i gjeneruar, lëkurë plastike GTA | `chars/djali_plastik_forte_pa-koke.png` (koka e mbuluar te paneli 3) → Higgsfield Element |
| `@Karta-epara` | karta fizike epara, **vertikale**, gradient magenta-vjollcë → indigo, çip, contactless, logo **lavandë** (jo e bardhë), Mastercard poshtë djathtas | `refs/epara-card_front_crop.png` → edit prompts/04 → Element. **Vetëm pjesa e parme.** |
| `@Atletet-Reja` | atlete të reja të bardha, pa logo, një shenjë e vogël vjollcë epara | `prompts/03-atletet-reja.md`; përjashtimi i vetëm nga aksenti |
| (dyqani) | dyqan atletesh modern me neon, Tiranë | plate pa njerëz |

## HUD
- Lart djathtas: logo epara + bilanci në LEK (në vend të parave GTA). Logo: `refs/epara-logo.svg` / `epara-logo_1600.png`. Logo është e errët (indigo) → mbi video i duhet kontur i bardhë ose sfond i butë.
- Teksti i HUD-it: **anglisht** si në lojë.
- Narratori: **shqip**, zë i rëndë gangsteri.
- Pa logo Rockstar, pa "GTA", pa "Vice City".

## Konflikte të zgjidhura për këtë projekt (shih CLAUDE.md)
(pa vendim ende)
