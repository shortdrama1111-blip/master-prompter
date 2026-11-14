# Skriptet e montimit

Kopje nga projekti `projects/2026-11-egli-SINDI-CAR/`. Ekzekutohen nga folderi i projektit
(presin `renders/`, `audio/`, `edit/`). Kohët e prerjeve, zoom-i dhe tekstet janë të atij
projekti: ndrysho vlerat në krye të çdo segmenti para përdorimit.

| Skripti | Çfarë bën |
|---|---|
| `grade.py <input> <output>` | Pass ngjyre: heq nuancën e verdhë/portokalli nga hijet, ngre pak hijet, ruan të zezat. Për plate-t. |
| `edit.sh` | Versioni A (segmentet të plota) dhe B (prerje + punch-in me `seg <out> <src> <start> <end> <zoom> <cx> <cy>`). |
| `final.sh` | B + mbyllja (zoom smoothstep + slow), tekst me drawtext (font Inter), muzika me offset që button-i bie te teksti, loudnorm -14 LUFS. |

Kujdes në ffmpeg: `-t` vendoset **para** `-i` kur ka `setpts` (ndryshe pret daljen); `%` në tekst kërkon `expansion=none`.
