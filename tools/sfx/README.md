# SFX: tre veglat për efektet zanore

Regjistruar më 2026-11-21 me kërkesë të përdoruesit: "mendoj se na duhen".
**Kur përdoruesi thotë "shto SFX", "zë", "zile", "tingull" ose diçka të ngjashme, merren nga këtu.**
Testuar në cloud (Python 3.13, ffmpeg 6.1, node 22): të treja funksionojnë.

| Vegla | Çfarë bën | Kur |
|---|---|---|
| **Openverse** (api.openverse.org) | Kërkim falas për tinguj Creative Commons, kryesisht nga Freesound | Burimi i tingujve realë. Për klientë: vetëm `license=cc0` |
| **real-sfx** (Clipwing/skills, `skills/real-sfx`) | Vendos tinguj realë në frame-in e saktë, ruan muzikën ose zërin, nxjerr MP4 + WAV të veçantë + raport | Video e montuar që ka nevojë për SFX realë: zile, makina, hapa, foley |
| **earshot** (Leonxlnx/earshot) | Sintetizon tinguj me kod, pa model dhe pa rrjet (922 receta) | Tinguj mekanikë ose UI: printer, njoftim, whoosh, ambient ere. Shpejt, pa licenca |

## Instalimi (i testuar)

```bash
python3 -m venv .venv-sfx
.venv-sfx/bin/pip install "earshot @ git+https://github.com/Leonxlnx/earshot"
git clone --depth 1 --filter=blob:none --sparse https://github.com/Clipwing/skills clipwing
cd clipwing && git sparse-checkout set skills/real-sfx && cd skills/real-sfx
../../../.venv-sfx/bin/python scripts/setup.py check
```

Mjedisi cloud `master-prompter` i lejon tashmë: `api.openverse.org`, `cdn.freesound.org`,
`freesound.org`, `upload.wikimedia.org`.

## Shembuj

```bash
# Openverse: kërkim CC0 (URL-ja e skedarit është te fusha "url")
curl -s "https://api.openverse.org/v1/audio/?q=telephone%20ring&license=cc0&page_size=10"

# earshot: me fjalë ose me id nga katalogu (`earshot sounds`)
earshot make "a thermal receipt printer printing a long receipt" -o printer.wav
earshot make --sound wind/mountain -o wind.wav

# real-sfx: lista e ngjarjeve -> tinguj realë në kohën e saktë
echo '[{"t":0.4,"type":"chime"}]' | python scripts/from_cues.py - --video film.mp4 --out work/cues.json --ui library
python scripts/mix.py work/cues.json --out result/film_sfx.mp4 --voice-safe
```

## Çfarë dolën testet (2026-11-21)

- Openverse: "telephone ring" 187 tinguj CC0, "receipt printer" 17, "eagle wings" 1. Të gjithë nga Freesound.
- earshot: zilja e telefonit, printeri (me recetë), krahët (`wings/flap`), lëkura (`leather/grab`),
  sirena (`siren/pass`) dhe era (`wind/mountain`) dolën. Nuk i kupton fjalët "eagle", "megaphone", "rotary":
  përdor id-të e katalogut.
- real-sfx: `setup.py check` ok. Nuk vjen me bibliotekë tingujsh realë (vetëm 78 tinguj UI CC0): biblioteka
  mbushet nga Openverse, pastaj `setup.py add-library` + `build_index.py`.

## Rregullat (nga projektet e mëparshme)

- Jep gjithmonë **dy versione: pa zë dhe me SFX** (per-class-black-friday).
- SFX në sfond, rreth **−16 dB peak** (printeri u ul dy herë te per-class-black-friday).
- Licenca: vetëm `CC0` për reklama me pagesë. `CC-BY` kërkon kredit, `NC` ndalohet.

## Regjistri i përdorimit

Shto një rresht sa herë përdoret një vegël. Në mbylljen e çdo projekti, kontrollo këtë tabelë: nëse asnjë vegël
nuk është përdorur në **3 projektet e fundit**, thuaja përdoruesit dhe pyet nëse i mbajmë.

| Data | Projekti | Vegla | Për çfarë |
|---|---|---|---|
| 2026-11-21 | 2026-11-shqiponja-e-agimit | të treja | Vetëm test instalimi, pa përdorim në video |
