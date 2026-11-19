"""Shot 2 final render: DreamDuo boxes ride a champagne spiral conveyor round a mocha column.

Motion, camera and timing follow previz.py shot2 (3.0 s, 72 frames); the look is the approved
shot-1 v4 look from final_common.py. Products are only the client's references: DreamDuo box
(front printed with refs/dreamduo-box.jpg, tex/duo.png), Hair Oil box, and on the background
column Peptide Mask, Leave-In Conditioner and Hair Oil bottles.
  Blender -b --factory-startup --python shot2_final.py -- OUTDIR [still|test|full]
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import final_common as F
from final_common import bpy, bmesh, Vector

N = 72                                   # 3.0 s at 24 fps
LED_RGB = F.LED

# DreamDuo carton 13 x 6 x 19 cm; front print from the photo, sides the photo's side-panel peach
M_DUO = F.textured("duo_print", "duo.png", 0.45)
M_DUOSIDE = F.flat("duo_side", (0.49, 0.234, 0.13), 0.5)      # linear of photo sRGB (0.729, 0.52, 0.397)
M_SLAT = F.flat("slat_champagne", (0.80, 0.68, 0.50), 0.35, metal=1.0)
M_DECK = F.flat("deck_dark", (0.05, 0.04, 0.035), 0.6, metal=0.6)
# no shelf LEDs here, so the set takes a true mocha albedo (shot 1's grey taupe only reads mocha
# under its 3200K cubby wash)
M_VELVET = F.flat("column_velvet", (0.14, 0.095, 0.068), 0.95)
M_ROOM = F.flat("room_mocha", (0.10, 0.068, 0.050), 0.8)


def duo_box(parent=None):
    w, d, h = 0.13, 0.06, 0.19
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co = Vector((v.co.x * w, v.co.y * d, v.co.z * h))
    uv = bm.loops.layers.uv.verify()
    for f in bm.faces:
        f.material_index = 0 if f.normal.y < -0.9 else 1
        for l in f.loops:
            l[uv].uv = ((l.vert.co.x + w / 2) / w, (l.vert.co.z + h / 2) / h)
    return F.mesh_obj("duo", bm, [M_DUO, M_DUOSIDE], parent, smooth_sides=False)


def tube_curve(pts, radius, mat, name):
    cu = bpy.data.curves.new(name, "CURVE")
    cu.dimensions, cu.bevel_depth, cu.bevel_resolution = "3D", radius, 4
    sp = cu.splines.new("POLY")
    sp.points.add(len(pts) - 1)
    for p, c in zip(sp.points, pts):
        p.co = (c[0], c[1], c[2], 1)
    cu.materials.append(mat)
    return F.link(bpy.data.objects.new(name, cu))


# ---------------------------------------------------------------- set
F.box("floor", (8, 8, 0.02), (0, 0, -0.01), M_ROOM)
F.box("backwall", (8, 0.02, 4.0), (0, 3.0, 2.0), M_ROOM)

R, pitch, z0 = 0.55, 0.32, 0.90
th_min, th_max = -3 * math.pi, 3 * math.pi


def P(th, up=0.0):
    return Vector((R * math.cos(th), R * math.sin(th), z0 + pitch * th / (2 * math.pi) + up))


slope = math.atan(pitch / (2 * math.pi * R))
bm = bmesh.new()
F.cylinder(bm, 0.40, z0 + pitch * 1.5 + 0.10, 0.0, seg=96)
F.mesh_obj("core", bm, M_VELVET)

# belt lips: champagne rails, the inner one carries a warm 3200K LED line
for r_off, mat, rad in ((-0.12, F.M_LED, 0.006), (0.12, F.M_CHAMP, 0.010)):
    pts = []
    for i in range(500):
        th = th_min + (th_max - th_min) * i / 499
        p = P(th, 0.02)
        pts.append((p.x * (R + r_off) / R, p.y * (R + r_off) / R, p.z))
    tube_curve(pts, rad, mat, "lip")

bm = bmesh.new()                         # continuous deck + outer skirt
rows = []
for i in range(600):
    th = th_min + (th_max - th_min) * i / 599
    c, s_ = math.cos(th), math.sin(th)
    zc = z0 + pitch * th / (2 * math.pi)
    rows.append([bm.verts.new(((R + dr) * c, (R + dr) * s_, zc + dz))
                 for dr, dz in ((-0.12, 0.0), (0.12, 0.0), (0.12, -0.07), (-0.12, -0.07))])
for a, b in zip(rows, rows[1:]):
    for k in range(4):
        bm.faces.new((a[k], a[(k + 1) % 4], b[(k + 1) % 4], b[k]))
for f in bm.faces:
    f.smooth = True
F.mesh_obj("belt_deck", bm, M_DECK, smooth_sides=False)

n_slats = int((th_max - th_min) * R / 0.034)
slats = [F.box("slat", (0.22, 0.024, 0.008), (0, 0, 0), M_SLAT) for _ in range(n_slats)]
span = th_max - th_min
omega = 0.12 / R

items = []
front = -math.pi / 2
for i in range(9):
    th = front - 1.4 + i * 0.42
    if i % 3 != 2:
        items.append((duo_box(), th, 0.095, True))
    else:
        e = F.link(bpy.data.objects.new("oilbox_e", None))
        F.oil_box((0, 0, -0.0675), e)
        items.append((e, th, 0.0675, True))
for i in range(6):                       # traffic on the turns above and below
    items.append((duo_box(), front - 2 * math.pi + i * 0.6, 0.095, True))
    e = F.link(bpy.data.objects.new("oilbox_e", None))
    F.oil_box((0, 0, -0.0675), e)
    items.append((e, front + 2 * math.pi - 1.0 + i * 0.6, 0.0675, True))

# second, taller column in the background with a ring of the real bottles on top
bm = bmesh.new()
F.cylinder(bm, 0.45, 1.55, 0.0, seg=96)
F.mesh_obj("column2", bm, M_VELVET)
for i in range(9):
    a = i * 2 * math.pi / 9
    e = F.link(bpy.data.objects.new("ring", None))
    e.location = (1.25 + 0.36 * math.cos(a), 1.6 + 0.36 * math.sin(a), 1.55)
    e.rotation_euler = (0, 0, a + math.pi / 2)
    if i % 3 == 2:
        F.oil_bottle((0, 0, 0), e)
    else:
        F.bottle150(F.M_MASK if i % 3 == 0 else F.M_COND, (0, 0, 0), e)
F.box("column2_led", (0.02, 0.02, 0.02), (1.25, 1.6, 1.62), F.M_LED)

# ---------------------------------------------------------------- light
# soft front key from camera-left, 30 deg up; 3200K top wash and a warm rim from back-right
F.area("Key", (-1.10, -1.60, 1.70), (0.0, -0.50, 0.90), 1.4, 60, F.KEY)
F.area("TopWash", (0.0, -0.3, 2.4), (0.0, -0.4, 0.9), 1.6, 40, LED_RGB)
F.area("Rim", (1.4, 0.6, 1.6), (0.2, -0.4, 0.9), 0.8, 25, LED_RGB)
F.area("Col2Glow", (1.25, 1.0, 2.3), (1.25, 1.6, 1.55), 0.6, 12, LED_RGB)


def update(t):
    for k, o in enumerate(slats):
        th = th_min + ((k * span / n_slats + omega * t) % span)
        o.location = P(th, 0.004)
        o.rotation_euler = (slope, 0, th)
    for o, th0, half_h, _ in items:
        th = th0 + omega * t
        o.location = P(th, 0.008 + half_h)
        o.rotation_euler = (0, 0, th + math.pi / 2)          # front face points outward
    s = t / 3.0
    s = min(max(s, 0), 1)
    s = s * s * (3 - 2 * s)
    x = 0.30 - 0.20 * s
    F.aim((x * 0.6 + 0.05, -1.45, 1.10), (x * 0.3, -0.50, 0.86), 38)


F.render(update, N, "shot2")
