# Krahasimi i ramp-eve: referenca vs montage v8 (flow.py, ORB + diff + Laplacian)

| | Referenca (camera-ref-cut, 30fps) | Ne (v8, 24fps, 8.3–15.8 s) |
|---|---|---|
| Lëvizja mes frame-ve | diff 10–64 në ÇDO frame, s'ka asnjë frame të ndalur | pozat diff 1–5 (të ngrira), pastaj shpërthim 20–47, pastaj prapë ngrirë |
| Ku bie prerja | në mes të lëvizjes (prerja 5→6 me zoom out 10%/frame që vazhdon) | në poza të ndalura; ramp-i nis nga 1× dhe mbaron në 1× brenda shot-it |
| Gjatësia e shot-it | 5–9 frame (0.17–0.30 s) | 0.5–1.4 s |
| Madhësia e lëvizjes | subjekti 100% → 41% në 9 frame | ndryshim 1–4% për frame, 4–6 frame |
| Mprehtësia | e njëtrajtshme (30–58), pa "pulsim" | 250 → 30 → 250: e mprehtë / njollë / e mprehtë |
| Frame të dyfishta | asnjë | diff 0.0 te 9.18, 10.18, 14.76 → ngecje |

Përfundimi: ritmi ynë = lëviz–ndalo–lëviz (mekanik). Referenca = lëvizje që s'ndalon kurrë, prerje mbi lëvizje.

Rregullimet:
1. Pa ndalesa: prej pozës merren vetëm 4–8 frame; prerja bie kur kamera ende lëviz (pa ngadalësim deri 1×).
2. Prerje mbi lëvizje: fundi i një lëvizjeje me shpejtësi të lartë → fillimi i lëvizjes tjetër me të njëjtin drejtim.
3. Pa frame të dyfishta: burimi interpolohet me optical flow (minterpolate 96 fps) para ramp-it.
4. Blur më i lehtë: mesatare e 2 frame-ve të interpoluara, jo 3–6 frame-ve.
5. Te gjenerimi tjetër: kamera nuk ndalon kurrë (zvarritje 0.2 m/s gjatë pozave); ajo nis lëvizjen 0.2 s para kamerës.
