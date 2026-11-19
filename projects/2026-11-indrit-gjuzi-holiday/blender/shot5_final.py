"""Shot 5 final render: gift pyramid with the red holiday bags, DreamDuo and Hair Oil; a small gift drops on top.

Layout, drop and camera follow previz.py shot5 (1.67 s, 40 frames, FOV 34, push-in 15 cm); look from
final_common.py. Products are only the client's references: red bag (print from the photo), DreamDuo
box, Hair Oil bottle and box. The wrapped gifts are set dressing in cream, champagne and soft gold
paper with red satin ribbon, as in the brief.
  Blender -b --factory-startup --python shot5_final.py -- OUTDIR [still|test|full]
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import final_common as F
from final_common import bpy, Vector

N = 40
PAPERS = [F.flat("paper_cream", (0.80, 0.72, 0.60), 0.55),
          F.flat("paper_champagne", (0.62, 0.50, 0.34), 0.35, metal=0.6),
          F.flat("paper_gold", (0.70, 0.52, 0.28), 0.30, metal=0.8)]
M_DROP = F.flat("paper_drop", (0.85, 0.78, 0.66), 0.5)

F.box("floor", (8, 8, 0.02), (0, 0, -0.01), F.M_ROOM)
F.box("backwall", (8, 0.02, 4.0), (0, 1.6, 2.0), F.M_ROOM)


def gift(size, base, mat, rz=0.0):
    """Wrapped gift on its base, crossed with red satin ribbon and a flat bow on top."""
    w, d, h = size
    e = F.link(bpy.data.objects.new("gift", None))
    e.location, e.rotation_euler = base, (0, 0, math.radians(rz))
    F.box("paper", (w, d, h), (0, 0, h / 2), mat, e)
    F.box("ribbon_x", (0.035, d + 0.004, h + 0.004), (0, 0, h / 2), F.M_SATIN_RED, e)
    F.box("ribbon_y", (w + 0.004, 0.035, h + 0.004), (0, 0, h / 2), F.M_SATIN_RED, e)
    for a in (35, -35):                                      # bow loops
        loop = F.box("bow", (0.07, 0.03, 0.012), (0, 0, h + 0.012), F.M_SATIN_RED, e)
        loop.rotation_euler = (math.radians(25), 0, math.radians(a))
    return e


# pyramid sized for 9:16: the previz pile was 1.3 m wide and only 0.6 m fits the vertical frame, so
# the gifts shrink to about 60% and the real products (true size) come forward and read larger.
for i, (x, w, d, rz) in enumerate([(-0.22, 0.22, 0.22, -4), (0.02, 0.24, 0.24, 3), (0.25, 0.20, 0.22, -2)]):
    gift((w, d, 0.20), (x, 0, 0), PAPERS[i % 3], rz)
for i, (x, w, rz) in enumerate([(-0.11, 0.20, 6)]):
    gift((w, 0.18, 0.17), (x, 0.02, 0.20), PAPERS[(i + 1) % 3], rz)
gift((0.16, 0.15, 0.14), (0.0, 0.03, 0.37), PAPERS[2], -7)
b1 = F.bag(0.5)
b1.location, b1.rotation_euler = (0.14, 0.02, 0.20), (0, 0, math.radians(10))   # second-row right, beside the top gift
b2 = F.bag(0.7)
b2.location, b2.rotation_euler = (-0.26, -0.25, 0), (0, 0, math.radians(-16))
dd = F.duo_box()
dd.location, dd.rotation_euler = (0.0, -0.22, 0.095), (math.radians(-10), 0, math.radians(6))
F.oil_box((0.12, -0.24, 0), None)
oe = F.link(bpy.data.objects.new("oil_e", None))
oe.location = (0.19, -0.33, 0)
F.oil_bottle((0, 0, 0), oe)
drop = gift((0.10, 0.10, 0.08), (0.0, 0.03, 0.51), M_DROP, 12)
rest_z = drop.location.z

F.area("Key", (-1.0, -1.8, 1.0), (0.0, -0.1, 0.30), 1.6, 90, F.KEY)
F.area("TopWash", (0.0, -0.4, 2.4), (0.0, 0.0, 0.5), 2.0, 70, F.LED)
F.area("WallGlow", (0.0, 1.0, 0.3), (0.0, 1.6, 1.2), 1.5, 30, F.LED)
F.area("Rim", (1.3, 0.6, 1.2), (0.0, 0.0, 0.5), 1.0, 40, F.LED)


def update(t):
    if t < 0.40:
        s = t / 0.40
        drop.location.z = rest_z + 0.30 * (1 - s * s)
    else:
        drop.location.z = rest_z + 0.012 * math.exp(-12 * (t - 0.40)) * abs(math.sin(25 * (t - 0.40)))
    s = min(max(t / 1.667, 0), 1)
    s = s * s * (3 - 2 * s)
    F.aim((0.0, -1.75 + 0.15 * s, 0.36), (0.0, 0, 0.30), 34)


F.render(update, N, "shot5")
