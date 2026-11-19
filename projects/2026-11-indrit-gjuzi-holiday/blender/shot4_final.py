"""Shot 4 final render: two diagonal champagne belts carry DreamDuo and Hair Oil cartons down-left.

Motion, camera and timing follow previz.py shot4 (2.67 s, 64 frames, high angle, FOV 29); look from
final_common.py. Products are only the client's references: DreamDuo box and Hair Oil box.
  Blender -b --factory-startup --python shot4_final.py -- OUTDIR [still|test|full]
"""
import os, sys, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import final_common as F
from final_common import bpy, Vector

N = 64
rng = random.Random(7)

F.box("floor", (8, 8, 0.02), (0, 0, -0.01), F.M_ROOM)
F.box("backwall", (8, 0.02, 4.0), (0, 2.2, 2.0), F.M_ROOM)
root = F.link(bpy.data.objects.new("belts_root", None))
root.rotation_euler = (0, 0, math.radians(35))
al = math.radians(14)
nrm = Vector((-math.sin(al), 0, math.cos(al)))
belts = [(0.0, 0.70, -1.6, 1.6), (0.42, 0.95, -0.35, 1.8)]      # (y, z0, u_from, u_to)


def W(y, z0, u):
    return Vector((u * math.cos(al), y, z0 + u * math.sin(al)))


slats, items = [], []
for bi, (y, z0, u0, u1) in enumerate(belts):
    L = u1 - u0
    b = F.box("belt", (L, 0.32, 0.04), W(y, z0, (u0 + u1) / 2), F.M_DECK, root)
    b.rotation_euler = (0, -al, 0)
    for side in (-0.17, 0.17):
        r = F.box("rail", (L, 0.02, 0.06), W(y + side, z0, (u0 + u1) / 2) + nrm * 0.02, F.M_CHAMP, root)
        r.rotation_euler = (0, -al, 0)
        led = F.box("rail_led", (L, 0.004, 0.004), W(y + side * 0.93, z0, (u0 + u1) / 2) + nrm * 0.048, F.M_LED, root)
        led.rotation_euler = (0, -al, 0)          # warm 3200K line along the inside of each rail
    if bi == 1:
        bm = F.bmesh.new()
        F.cylinder(bm, 0.045, 0.34, -0.17, seg=64)
        ro = F.mesh_obj("roller", bm, F.M_CHAMP, root)
        ro.location = W(y, z0, u0) - nrm * 0.005
        ro.rotation_euler = (math.radians(90), 0, 0)
    for k in range(int(L / 0.05)):
        s_ = F.box("slat", (0.012, 0.30, 0.008), (0, 0, 0), F.M_CHAMP, root)
        s_.rotation_euler = (0, -al, 0)
        slats.append((s_, y, z0, u0, L, k * 0.05))
    for k in range(int((L - 0.2) / 0.22)):
        u = u0 + 0.28 + k * 0.22
        if k % 2 == 0:
            o, hh = F.duo_box(root), 0.095
        else:
            o, hh = F.oil_box_centred(root), 0.0675
        o.rotation_euler = (0, -al, math.radians(rng.uniform(-8, 8)))
        items.append((o, y + rng.uniform(-0.04, 0.04), z0, u, hh))
v = 0.15

# light: soft key from camera-left 30 deg up, 3200K wash from above, warm rim from behind
F.area("Key", (-0.9, -1.3, 1.6), (0.0, 0.0, 0.85), 1.6, 70, F.KEY)
F.area("TopWash", (0.0, 0.2, 2.6), (0.0, 0.1, 0.8), 2.0, 60, F.LED)
F.area("Rim", (-0.6, 1.4, 1.6), (0.0, 0.1, 0.85), 1.0, 30, F.LED)


def update(t):
    for s_, y, z0, u0, L, off in slats:
        u = u0 + ((off - v * t) % L)
        s_.location = W(y, z0, u) + nrm * 0.024
    for o, y, z0, u, hh in items:
        o.location = W(y, z0, u - v * t) + nrm * (0.02 + hh)
    s = min(max(t / 2.667, 0), 1)
    s = s * s * (3 - 2 * s)
    F.aim((0.55 - 0.06 * s, -0.95, 1.80), (0.0, 0.0, 0.85), 29)


F.render(update, N, "shot4")
