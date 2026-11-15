# Gjendja e projektit: 2026-11-egli-krenar (ruajtur 2026-11-15, në pauzë)

Ky skedar mjafton që një thread i ri ta vazhdojë punën pa historinë e bisedës.
Projekti NUK është mbyllur. Mbyllja dhe merge-i në `main` bëhen vetëm kur përdoruesi thotë "kam mbaruar".

## Çfarë është
Reklamë Reels 9:16, rreth 50 s, për kursin "Gjithçka që duhet të dish rreth Meta" të Krenar Myrtezës
(80% zbritje, 4 ditë, akses përgjithmonë, 16 leksione bonus sigurie). Koncepti: Krenari si "doktori i Meta-s".
Me stetoskop dëgjon telefonin; nga ekrani dalin panele hologram; kabineti shkrihet në një botë digjitale.
Scripti origjinal: `references/brief-Ide_Video_AI_Trajnimi_Meta.pdf`. Historia në prozë: `story.md`.

## Rruga e punës (e konfirmuar)
1. Historia/skena në prozë shqip → miratim → prompt (rregull i përdoruesit).
2. Një hap në një mesazh ("me radhë").
3. Audio në ElevenLabs: zëri **Nikola – Balkan Pro** (`DAGnQ7r9sMtV0Q44g1Mi`), modeli **eleven_v4**, një skedar për çdo linjë.
   Flow: https://elevenlabs.io/app/flows/VCsVJZqQ23Y3ko7yaAbA. Voice Design s'e pranon shqipen.
4. Blockout në **Blender lokal të përdoruesit**: Claude shkruan brief + skript Python, përdoruesi e ekzekuton në chat-in e tij
   lokal me Blender MCP dhe dërgon MP4. (Sesioni cloud s'e sheh Blender-in lokal; 3D Jutsu i Higgsfield nuk përdoret.)
5. Seedance 2.5 në Higgsfield, **manualisht nga përdoruesi**: @video1 = blockout (master për kamerën/prerjet/lëvizjen)
   + @krenar-doctor-v2 + referencat e dizajnit + audiot. Claude jep promptin dhe referencat me radhë.
6. Kamera dinamike: Krenari ecën dhe ka veprim në çdo shot; asnjë kuadër statik (përveç freeze-it final të kërkuar).

## Referencat aktive
| Roli | Skedari | Shënim |
|---|---|---|
| Personazhi | `references/krenar-sheet-v2.jpg` | Element Higgsfield **krenar-doctor-v2** (`7c3598f0-6cd0-4035-8ad8-e89eb3ca3561`). Ora dora e majtë, byzylyk djathtas, badge "DR. KRENAR MYRTEZA" |
| Kabineti | `references/kabinet-v3-user.jpg` | vetëm blloku A |
| Panelet | `references/panels-design-v2-user.jpg` | dizajni i çdo paneli |
| Bota digjitale | `references/world-design-v1-user.jpg` | nga kalimi te blloku A e tutje |
| Audio 01–04 | `audio/krenar-audio-1..4.mp3` | 4.52 / 7.39 / 8.91 / 7.08 s |
Blloku i dritës dhe paleta 60:30:10: `decisions.md`.

## Ku jemi
| Blloku | Skript | Gjendja |
|---|---|---|
| A (0–16 s) | linjat 01–02 | ✅ **APROVUAR**: `renders/blockA-v5-APROVUAR.mp4` (blockout v4 + prompti `prompts/14-block-A-video-blockout-v5.md`). TODO: heqja e stetoskopit |
| B (16–35 s) | linjat 03–04 | Proza e miratuar (`story.md`). Blockout v1 i dërguar: `prompts/15-blender-blockB-build-v1.py` + brief. **Pritet render-i MP4 nga përdoruesi** → kontroll → prompti i Seedance |
| C (oferta) | linjat 05–06 | Pa nisur: proza → audio 05–06 → blockout → Seedance. Finali: freeze 2 s (kërkesë e klientit) |
| Montimi | — | Tekstet, kopertina reale, −80%, data, linku, muzika në montim |

## Hapi tjetër
Kur vjen render-i i blockout-it B: kontrollo kuadrot (një në 0.5 s), pastaj shkruaj promptin Seedance të bllokut B
sipas modelit të `prompts/14-block-A-video-blockout-v5.md` (@video1 blockout B, @krenar-doctor-v2, @image1 panelet, @image2 bota,
@audio1 = audio 3, @audio2 = audio 4; kuadri i parë vazhdon `references/blockA-lastframe.jpg`).
