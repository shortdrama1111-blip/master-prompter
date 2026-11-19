"""Shot 3 final render: Hair Oil boxes hang like ornaments from a clear curved rail and glide past.

Motion, camera and timing follow previz.py shot3 (3.0 s, 72 frames); look from final_common.py.
Ornaments are only the client's Hair Oil carton (front printed with the real box photo), each hung
on a red satin ribbon: decisions.md puts the red accent mid-video in this shot.
  Blender -b --factory-startup --python shot3_final.py -- OUTDIR [still|test|full]
"""
import os, sys, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import final_common as F
from final_common import bpy, bmesh, Vector

N = 72
rng = random.Random(7)
LED_RGB = F.LED

M_ROOM = F.flat("room_mocha", (0.10, 0.068, 0.050), 0.8)
M_VELVET = F.flat("pillar_velvet", (0.14, 0.095, 0.068), 0.95)
M_RIBBON = F.flat("satin_red", (0.42, 0.012, 0.02), 0.28)
try:
    M_RIBBON.node_tree.nodes["Principled BSDF"].inputs["Sheen Weight"].default_value = 0.6
except Exception:
    pass
M_HOOK = F.flat("hook_champagne", (0.80, 0.68, 0.50), 0.25, metal=1.0)


def curve(pts, radius, mat, name):
    cu = bpy.data.curves.new(name, "CURVE")
    cu.dimensions, cu.bevel_depth, cu.bevel_resolution = "3D", radius, 6
    sp = cu.splines.new("POLY")
    sp.points.add(len(pts) - 1)
    for p, c in zip(sp.points, pts):
        p.co = (c[0], c[1], c[2], 1)
    cu.materials.append(mat)
    return F.link(bpy.data.objects.new(name, cu))


# ---------------------------------------------------------------- set
F.box("floor", (8, 8, 0.02), (0, 0, -0.01), M_ROOM)
F.box("backwall", (8, 0.02, 4.0), (0, 1.3, 2.0), M_ROOM)
bm = bmesh.new()
F.cylinder(bm, 0.28, 3.0, 0.0, seg=96)
F.mesh_obj("pillar", bm, M_VELVET)
a_min, a_max = -0.9 * math.pi, 1.1 * math.pi


def P(a):
    return Vector((0.55 * math.cos(a), 0.35 * math.sin(a), 1.25 + 0.12 * a))


rail_pts = [P(a_min + (a_max - a_min) * i / 399)[:] for i in range(400)]
curve(rail_pts, 0.022, F.M_GLASS, "rail")                       # clear acrylic tube
curve([(x, y, z + 0.028) for x, y, z in rail_pts], 0.003, F.M_LED, "rail_led")   # warm LED line on top

BOX_H = 0.135
orns = []
n = 30
for i in range(n):
    piv = F.link(bpy.data.objects.new("pivot", None))
    F.box("hook", (0.006, 0.006, 0.02), (0, 0, -0.01), M_HOOK, piv)
    # ribbon loop: two satin bands from the hook down to the carton top
    for sx in (-1, 1):
        r = F.box("ribbon", (0.008, 0.0015, 0.07), (sx * 0.006, 0, -0.055), M_RIBBON, piv)
        r.rotation_euler = (0, sx * math.radians(6), 0)
    e = F.link(bpy.data.objects.new("orn", None))
    e.parent, e.location = piv, (0, 0, -0.09 - BOX_H)
    F.oil_box((0, 0, 0), e)
    orns.append((piv, i * (a_max - a_min) / n, rng.uniform(0, 6.28)))
span = a_max - a_min
omega = 0.08 / 0.47

# ---------------------------------------------------------------- light
F.area("Key", (-0.90, -1.30, 1.45), (0.0, -0.30, 1.05), 1.2, 45, F.KEY)
F.area("TopWash", (0.0, -0.2, 2.3), (0.0, -0.2, 1.1), 1.4, 35, LED_RGB)
F.area("WallGlow", (0.3, 0.6, 0.6), (0.3, 1.3, 1.4), 1.0, 20, LED_RGB)
F.area("Rim", (1.1, 0.4, 1.4), (0.1, -0.3, 1.05), 0.6, 18, LED_RGB)


def update(t):
    for piv, off, ph in orns:
        a = a_min + ((off + omega * t) % span)
        p, q = P(a), P(a + 0.01)
        piv.location = p
        heading = math.atan2(q.y - p.y, q.x - p.x)
        swing = math.radians(9) * math.sin(2 * math.pi * 0.55 * t + ph)
        piv.rotation_euler = (swing, 0, heading + math.radians(12) * math.sin(0.8 * t + ph))
    s = min(max(t / 3.0, 0), 1)
    s = s * s * (3 - 2 * s)
    ang = math.radians(-95 + 5 * s)
    F.aim((0.92 * math.cos(ang), 0.92 * math.sin(ang), 1.00), (0.0, -0.25, 1.06), 44)


F.render(update, N, "shot3")
