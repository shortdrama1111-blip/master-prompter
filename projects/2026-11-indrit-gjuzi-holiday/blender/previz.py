"""Grey-box previz for the Indrit Gjuzi holiday film (camera + blocking reference for Seedance).

Run headless with the installed Blender:
  blender.exe -b --factory-startup --python previz.py -- OUTDIR [test|full|s1..s6]

test = first + last frame of every shot (framing check), full = every frame.
Frames land in OUTDIR/<shot>/f0000.png; assemble with ffmpeg afterwards.
Scale is real metres. 24 fps, 720x1280 (9:16).
"""
import bpy, bmesh, sys, os, math, random
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = argv[0] if argv else os.path.join(os.getcwd(), "previz_out")
MODE = argv[1] if len(argv) > 1 else "test"
FPS, W, H = 24, 720, 1280
rng = random.Random(7)

# ---------------------------------------------------------------- scene setup
for o in list(bpy.data.objects):
    bpy.data.objects.remove(o)
sc = bpy.context.scene
sc.render.engine = "CYCLES"
sc.cycles.device = "CPU"
sc.cycles.samples = 4
sc.cycles.use_denoising = False
sc.cycles.max_bounces = 2
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = W, H, 100
sc.render.fps = FPS
sc.render.image_settings.file_format = "PNG"
sc.view_settings.view_transform = "Standard"

world = bpy.data.worlds.new("W")
sc.world = world
try:
    world.use_nodes = True
except Exception:
    pass
bg = world.node_tree.nodes.get("Background")
bg.inputs["Color"].default_value = (0.5, 0.5, 0.5, 1)
bg.inputs["Strength"].default_value = 0.5

sun_data = bpy.data.lights.new("Sun", "SUN")
sun_data.energy = 3.0
sun_data.angle = math.radians(15)
sun = bpy.data.objects.new("Sun", sun_data)
sun.rotation_euler = (math.radians(50), 0, math.radians(25))
sc.collection.objects.link(sun)

cam_data = bpy.data.cameras.new("Cam")
cam_data.sensor_fit = "VERTICAL"
cam = bpy.data.objects.new("Cam", cam_data)
sc.collection.objects.link(cam)
sc.camera = cam


# ---------------------------------------------------------------- helpers
def mat(name, v, rough=0.8, emit=0.0):
    m = bpy.data.materials.new(name)
    try:
        m.use_nodes = True
    except Exception:
        pass
    b = m.node_tree.nodes.get("Principled BSDF")
    b.inputs["Base Color"].default_value = (v, v, v, 1)
    b.inputs["Roughness"].default_value = rough
    if emit:
        b.inputs["Emission Color"].default_value = (1, 1, 1, 1)
        b.inputs["Emission Strength"].default_value = emit
    return m


M_WALL = mat("wall", 0.50)
M_SET = mat("set", 0.62)
M_BODY = mat("bottle_body", 0.78, 0.5)
M_CAP = mat("cap_white", 0.92, 0.35)
M_OILCAP = mat("cap_black", 0.06, 0.3)
M_GLASS = mat("glass", 0.85, 0.15)
M_PACK = mat("pack", 0.70)
M_DUO = mat("duo_box", 0.58)
M_BAG = mat("bag_accent", 0.28)
M_RIBBON = mat("ribbon", 0.88, 0.4)
M_TAG = mat("tag", 0.80)
M_BACKLIT = mat("backlit", 0.95, 0.8, emit=0.6)


def newcoll(name):
    c = bpy.data.collections.new(name)
    sc.collection.children.link(c)
    return c


def _obj(coll, name, bm, m, smooth=False):
    if smooth:
        for f in bm.faces:
            f.smooth = abs(f.normal.z) < 0.5
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    me.materials.append(m)
    o = bpy.data.objects.new(name, me)
    coll.objects.link(o)
    return o


def box(coll, size, loc, m, bevel=0.0, name="box", parent=None):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co = Vector((v.co.x * size[0], v.co.y * size[1], v.co.z * size[2]))
    o = _obj(coll, name, bm, m)
    o.location = loc
    if bevel:
        mod = o.modifiers.new("bev", "BEVEL")
        mod.width, mod.segments = bevel, 3
    if parent:
        o.parent = parent
    return o


def cyl(coll, r, h, loc, m, r2=None, seg=32, name="cyl", parent=None, axis="Z"):
    """Cylinder/cone with its BASE at loc (axis Z), or centred (axis Y)."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=seg,
                          radius1=r, radius2=r if r2 is None else r2, depth=h)
    if axis == "Z":
        for v in bm.verts:
            v.co.z += h / 2
    o = _obj(coll, name, bm, m, smooth=True)
    o.location = loc
    if axis == "Y":
        o.rotation_euler = (math.radians(90), 0, 0)
    if parent:
        o.parent = parent
    return o


def empty(coll, name, loc=(0, 0, 0), parent=None):
    e = bpy.data.objects.new(name, None)
    coll.objects.link(e)
    e.location = loc
    if parent:
        e.parent = parent
    return e


def curve(coll, pts, radius, m, name="curve"):
    cu = bpy.data.curves.new(name, "CURVE")
    cu.dimensions = "3D"
    cu.bevel_depth = radius
    cu.bevel_resolution = 4
    sp = cu.splines.new("POLY")
    sp.points.add(len(pts) - 1)
    for p, c in zip(sp.points, pts):
        p.co = (c[0], c[1], c[2], 1)
    cu.materials.append(m)
    o = bpy.data.objects.new(name, cu)
    coll.objects.link(o)
    return o


# product proxies (real sizes): 150 ml bottle, 40 ml oil bottle, oil box, DreamDuo box
def bottle150(coll, base, parent=None):
    e = empty(coll, "bottle150", base, parent)
    cyl(coll, 0.0225, 0.105, (0, 0, 0), M_BODY, parent=e)
    cyl(coll, 0.0215, 0.060, (0, 0, 0.105), M_CAP, parent=e)
    return e


def oil_bottle(coll, base, parent=None):
    e = empty(coll, "oil", base, parent)
    cyl(coll, 0.019, 0.070, (0, 0, 0), M_GLASS, r2=0.016, parent=e)
    cyl(coll, 0.0165, 0.042, (0, 0, 0.070), M_OILCAP, parent=e)
    return e


def oil_box(coll, base, parent=None):
    return box(coll, (0.045, 0.045, 0.13), (base[0], base[1], base[2] + 0.065), M_PACK, 0.002, "oilbox", parent)


def duo_box(coll, center, parent=None):  # 13 x 6 x 19 cm, front face = local -Y
    return box(coll, (0.13, 0.06, 0.19), center, M_DUO, 0.003, "duo", parent)


def smooth(x):
    x = min(max(x, 0.0), 1.0)
    return x * x * (3 - 2 * x)


def lerp(a, b, s):
    return [a[i] + (b[i] - a[i]) * s for i in range(len(a))]


def aim(loc, target, fov_deg):
    cam.location = Vector(loc)
    cam.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
    cam_data.angle_y = math.radians(fov_deg)


def room(coll, back_y=2.5, w=8.0):
    box(coll, (w, w, 0.02), (0, 0, -0.01), M_WALL, name="floor")
    box(coll, (w, 0.02, 4.0), (0, back_y, 2.0), M_WALL, name="backwall")


# ---------------------------------------------------------------- SHOT 1: lit shelf wall, camera rises
# 0.00-1.67 s. Camera 1.10 m from the wall, FOV 46 deg, pedestal up 0.30 m (0.18 m/s), level.
def shot1():
    C = newcoll("s1_shelf")
    box(C, (8, 8, 0.02), (0, 0, -0.01), M_WALL, name="floor")
    cols, cw, depth, t = 7, 0.19, 0.14, 0.012
    x0 = -cw * cols / 2
    kinds = ["mask", "cond", "oil", "oilbox", "mask", "oil"]
    for c in range(cols + 1):
        box(C, (t, depth, 3.2), (x0 + c * cw, -depth / 2, 1.6), M_SET, name="divider")
    for c in range(cols):
        xc = x0 + c * cw + cw / 2
        box(C, (cw, 0.01, 3.2), (xc, 0.005, 1.6), M_BACKLIT, name="backlight")
        z = 0.15 + rng.uniform(0, 0.12)
        while z < 3.0:
            box(C, (cw, depth, t), (xc, -depth / 2, z), M_SET, name="board")
            k = rng.choice(kinds)
            base = (xc + rng.uniform(-0.02, 0.02), -depth * 0.5, z + t / 2)
            if k in ("mask", "cond"):
                bottle150(C, base)
            elif k == "oil":
                oil_bottle(C, base)
            else:
                oil_box(C, base)
            z += rng.uniform(0.22, 0.30)

    def update(t):
        s = smooth(t / 1.667)
        z = 1.25 + 0.30 * s
        aim((0.04, -1.10, z), (0.04, 0, z), 46)

    return C, update, 40


# ---------------------------------------------------------------- SHOT 2: helical belt around a column
# 1.67-4.67 s. Boxes ride the belt at 0.12 m/s. Camera 1.25 m out, 15 deg down, FOV 38,
# drifts 0.20 m to the left.
def shot2():
    C = newcoll("s2_helix")
    room(C, back_y=3.0)
    R, pitch, z0 = 0.55, 0.32, 0.90
    th_min, th_max = -3 * math.pi, 3 * math.pi

    def P(th, up=0.0):
        return Vector((R * math.cos(th), R * math.sin(th), z0 + pitch * th / (2 * math.pi) + up))

    slope = math.atan(pitch / (2 * math.pi * R))
    cyl(C, 0.40, z0 + pitch * 1.5 + 0.10, (0, 0, 0), M_SET, seg=64, name="core")
    for r_off in (-0.12, 0.12):  # belt lips
        pts = []
        for i in range(400):
            th = th_min + (th_max - th_min) * i / 399
            p = P(th, 0.02)
            pts.append((p.x * (R + r_off) / R, p.y * (R + r_off) / R, p.z))
        curve(C, pts, 0.012, M_SET, "lip")
    bm = bmesh.new()  # continuous belt deck + outer skirt
    N = 500
    rows = []
    for i in range(N):
        th = th_min + (th_max - th_min) * i / (N - 1)
        c, s_ = math.cos(th), math.sin(th)
        zc = z0 + pitch * th / (2 * math.pi)
        rows.append([bm.verts.new(((R + dr) * c, (R + dr) * s_, zc + dz))
                     for dr, dz in ((-0.12, 0.0), (0.12, 0.0), (0.12, -0.07), (-0.12, -0.07))])
    for a, b in zip(rows, rows[1:]):
        for k in range(4):
            bm.faces.new((a[k], a[(k + 1) % 4], b[(k + 1) % 4], b[k]))
    _obj(C, "belt_deck", bm, M_SET)
    n_slats = int((th_max - th_min) * R / 0.034)
    slats = [box(C, (0.22, 0.024, 0.008), (0, 0, 0), M_RIBBON, name="slat") for _ in range(n_slats)]
    span = th_max - th_min
    omega = 0.12 / R

    items = []
    front = -math.pi / 2
    for i in range(9):
        th = front - 1.4 + i * 0.42
        o = duo_box(C, (0, 0, 0)) if i % 3 != 2 else oil_box(C, (0, 0, 0))
        items.append((o, th, 0.095 if i % 3 != 2 else 0.065))
    for i in range(6):  # traffic on the turn above and below
        th = front - 2 * math.pi + i * 0.6
        items.append((duo_box(C, (0, 0, 0)), th, 0.095))
        th = front + 2 * math.pi - 1.0 + i * 0.6
        items.append((oil_box(C, (0, 0, 0)), th, 0.065))

    # second, taller column in the background with bottles on top
    cyl(C, 0.45, 1.55, (1.25, 1.6, 0), M_SET, seg=64, name="column2")
    for i in range(9):
        a = i * 2 * math.pi / 9
        f = bottle150 if i % 3 else oil_bottle
        f(C, (1.25 + 0.36 * math.cos(a), 1.6 + 0.36 * math.sin(a), 1.55))

    def update(t):
        for k, o in enumerate(slats):
            th = th_min + ((k * span / n_slats + omega * t) % span)
            o.location = P(th, 0.004)
            o.rotation_euler = (slope, 0, th)
        for o, th0, half_h in items:
            th = th0 + omega * t
            p = P(th, 0.008 + half_h)
            o.location = p
            o.rotation_euler = (0, 0, th + math.pi / 2)  # front face points outward
        s = smooth(t / 3.0)
        x = 0.30 - 0.20 * s
        aim((x, -1.75, 1.18), (x * 0.4, -0.45, 0.86), 38)

    return C, update, 72


# ---------------------------------------------------------------- SHOT 3: hanging boxes slide along a clear rail
# 4.67-7.67 s. Ornaments travel 0.08 m/s and sway +-9 deg. Camera 10 deg below the rail,
# FOV 45, orbits 5 deg around the loop centre.
def shot3():
    C = newcoll("s3_garland")
    room(C, back_y=1.3)
    cyl(C, 0.28, 3.0, (-0.62, 0.75, 0), M_SET, seg=64, name="pillar")
    a_min, a_max = -0.9 * math.pi, 1.1 * math.pi

    def P(a):
        return Vector((0.55 * math.cos(a), 0.35 * math.sin(a), 1.25 + 0.12 * a))

    curve(C, [P(a_min + (a_max - a_min) * i / 299)[:] for i in range(300)], 0.022, M_GLASS, "rail")
    orns = []
    n = 22
    for i in range(n):
        piv = empty(C, "pivot")
        cyl(C, 0.0015, 0.05, (0, 0, -0.05), M_SET, seg=8, parent=piv, name="string")
        if i % 2:
            box(C, (0.065, 0.065, 0.16), (0, 0, -0.13), M_PACK, 0.003, "orn_tall", piv)
        else:
            box(C, (0.10, 0.05, 0.11), (0, 0, -0.105), M_TAG, 0.003, "orn_flat", piv)
        orns.append((piv, i * (a_max - a_min) / n, rng.uniform(0, 6.28)))
    span = a_max - a_min
    omega = 0.08 / 0.47

    def update(t):
        for piv, off, ph in orns:
            a = a_min + ((off + omega * t) % span)
            p, q = P(a), P(a + 0.01)
            piv.location = p
            heading = math.atan2(q.y - p.y, q.x - p.x)
            swing = math.radians(9) * math.sin(2 * math.pi * 0.55 * t + ph)
            piv.rotation_euler = (swing, 0, heading + math.radians(12) * math.sin(0.8 * t + ph))
        s = smooth(t / 3.0)
        ang = math.radians(-95 + 5 * s)
        aim((0.95 * math.cos(ang), 0.95 * math.sin(ang), 1.00), (0.05, 0, 1.20), 44)

    return C, update, 72


# ---------------------------------------------------------------- SHOT 4: two diagonal belts, high angle
# 7.67-10.33 s. Items run down-left at 0.15 m/s on a 14 deg slope. Camera 50 deg down,
# FOV 42, drifts 0.06 m.
def shot4():
    C = newcoll("s4_diagonal")
    room(C, back_y=2.2)
    root = empty(C, "belts_root")
    root.rotation_euler = (0, 0, math.radians(35))
    al = math.radians(14)
    nrm = Vector((-math.sin(al), 0, math.cos(al)))
    belts = [  # (y, z0, u_from, u_to)
        (0.0, 0.70, -1.6, 1.6),
        (0.55, 1.05, -0.35, 1.8),
    ]

    def W(y, z0, u):
        return Vector((u * math.cos(al), y, z0 + u * math.sin(al)))

    slats, items = [], []
    for bi, (y, z0, u0, u1) in enumerate(belts):
        L = u1 - u0
        c = W(y, z0, (u0 + u1) / 2)
        b = box(C, (L, 0.32, 0.04), c, M_SET, name="belt", parent=root)
        b.rotation_euler = (0, -al, 0)
        for side in (-0.17, 0.17):
            r = box(C, (L, 0.02, 0.06), W(y + side, z0, (u0 + u1) / 2) + nrm * 0.02, M_SET, name="rail", parent=root)
            r.rotation_euler = (0, -al, 0)
        if bi == 1:
            cyl(C, 0.045, 0.34, W(y, z0, u0) - nrm * 0.005, M_RIBBON, axis="Y", name="roller", parent=root)
        for k in range(int(L / 0.05)):
            s_ = box(C, (0.012, 0.30, 0.008), (0, 0, 0), M_RIBBON, name="slat", parent=root)
            s_.rotation_euler = (0, -al, 0)
            slats.append((s_, y, z0, u0, L, k * 0.05))
        for k in range(int((L - 0.2) / 0.26)):
            u = u0 + 0.30 + k * 0.26
            if k % 2 == 0:
                o, hh = duo_box(C, (0, 0, 0), parent=root), 0.095
            else:
                o, hh = oil_box(C, (0, 0, 0), parent=root), 0.065
            o.rotation_euler = (0, -al, math.radians(rng.uniform(-8, 8)))
            items.append((o, y + rng.uniform(-0.04, 0.04), z0, u, hh))
    v = 0.15

    def update(t):
        for s_, y, z0, u0, L, off in slats:
            u = u0 + ((off - v * t) % L)
            s_.location = W(y, z0, u) + nrm * 0.024
        for o, y, z0, u, hh in items:
            o.location = W(y, z0, u - v * t) + nrm * (0.02 + hh)
        s = smooth(t / 2.667)
        aim((0.55 - 0.06 * s, -0.95, 1.85), (0.02, 0.18, 0.95), 36)

    return C, update, 64


# ---------------------------------------------------------------- SHOT 5: gift pile, a box lands on top
# 10.33-12.00 s. Frontal, slightly low, FOV 34, push-in 0.15 m. Top box lands in 0.40 s.
def shot5():
    C = newcoll("s5_pile")
    room(C, back_y=1.6)

    def gift(size, base, m=M_PACK):
        o = box(C, size, (base[0], base[1], base[2] + size[2] / 2), m, 0.004, "gift")
        box(C, (0.035, size[1] + 0.004, size[2] + 0.004), (0, 0, 0), M_RIBBON, name="ribbon", parent=o)
        return o

    def bag(base, scale=1.0):
        w, d, h = 0.40 * scale, 0.12 * scale, 0.34 * scale
        o = box(C, (w, d, h), (base[0], base[1], base[2] + h / 2), M_BAG, 0.003, "bag")
        pts = [(-0.09 * scale + 0.18 * scale * i / 20, -d / 2 - 0.002,
                h / 2 + 0.11 * scale * math.sin(math.pi * i / 20)) for i in range(21)]
        hnd = curve(C, pts, 0.006, M_RIBBON, "handle")
        hnd.parent = o
        return o

    # every layer rests on the one below: row0 tops at 0.30, row1 tops at 0.54
    for x, w, d in [(-0.52, 0.36, 0.34), (-0.13, 0.42, 0.38), (0.27, 0.34, 0.32), (0.62, 0.30, 0.34)]:
        gift((w, d, 0.30), (x, 0, 0))
    for x, w in [(-0.34, 0.40), (0.08, 0.36), (0.45, 0.32)]:
        gift((w, 0.28, 0.24), (x, 0.02, 0.30))
    duo_box(C, (0.08, -0.17, 0.30 + 0.095))
    gift((0.34, 0.26, 0.22), (-0.22, 0.03, 0.54))
    bag((0.26, 0.03, 0.54), 0.75)
    bag((-0.30, -0.30, 0), 0.85)
    oil_box(C, (0.12, -0.30, 0))
    oil_bottle(C, (0.21, -0.33, 0))
    drop = gift((0.18, 0.18, 0.14), (-0.20, 0.03, 0.76), M_TAG)
    rest_z = drop.location.z

    def update(t):
        if t < 0.40:
            s = t / 0.40
            drop.location.z = rest_z + 0.35 * (1 - s * s)
        else:
            drop.location.z = rest_z + 0.012 * math.exp(-12 * (t - 0.40)) * abs(math.sin(25 * (t - 0.40)))
        s = smooth(t / 1.667)
        aim((0.02, -2.30 + 0.15 * s, 0.62), (0.02, 0, 0.55), 34)

    return C, update, 40


# ---------------------------------------------------------------- SHOT 6: bag close-up with blank tag
# 12.00-15.83 s. Camera 0.55 m from the bag face, FOV 32, push-in 0.04 m. Tag sways +-3 deg.
# Tag stays blank: handwriting goes in the edit.
def shot6():
    C = newcoll("s6_tag")
    room(C, back_y=1.0)
    box(C, (1.4, 0.8, 0.60), (0, 0.05, 0.30), M_SET, name="plinth")
    w, d, h, zb = 0.42, 0.13, 0.34, 0.60
    box(C, (w, d, h), (0, 0, zb + h / 2), M_BAG, 0.003, "bag")
    for y in (-d / 2 - 0.002, d / 2 + 0.002):
        pts = [(-0.10 + 0.20 * i / 30, y, zb + h + 0.10 * math.sin(math.pi * i / 30)) for i in range(31)]
        curve(C, pts, 0.007, M_RIBBON, "handle")
    for i in range(3):  # tissue paper
        tp = box(C, (0.16, 0.004, 0.12), (-0.10 + i * 0.09, 0.0, zb + h + 0.03), M_CAP, name="tissue")
        tp.rotation_euler = (math.radians(rng.uniform(-25, 25)), math.radians(rng.uniform(-30, 30)), math.radians(rng.uniform(-20, 20)))
    piv = empty(C, "tag_pivot", (0.03, -d / 2 - 0.012, zb + h + 0.02))
    box(C, (0.014, 0.002, 0.13), (0, 0, -0.065), M_RIBBON, name="tag_ribbon", parent=piv)
    tag = box(C, (0.075, 0.003, 0.115), (0.0, -0.004, -0.115), M_TAG, 0.008, "tag", piv)
    tag.rotation_euler = (0, math.radians(-22), 0)

    def update(t):
        piv.rotation_euler = (math.radians(3) * math.sin(2 * math.pi * 0.4 * t), math.radians(14), 0)
        s = smooth(t / 3.833)
        aim((0.05, -0.66 + 0.04 * s, zb + 0.40), (0.0, 0, zb + 0.27), 34)

    return C, update, 92


# ---------------------------------------------------------------- render
SHOTS = [("s1_shelf", shot1), ("s2_helix", shot2), ("s3_garland", shot3),
         ("s4_diagonal", shot4), ("s5_pile", shot5), ("s6_tag", shot6)]
built = [(name, *fn()) for name, fn in SHOTS]
for name, coll, update, nframes in built:
    if MODE.startswith("s") and not name.startswith(MODE):
        continue
    for _, other, _, _ in built:
        other.hide_render = other is not coll
    frames = [0, nframes - 1] if MODE == "test" else range(nframes)
    os.makedirs(os.path.join(OUT, name), exist_ok=True)
    for f in frames:
        update(f / FPS)
        sc.render.filepath = os.path.join(OUT, name, f"f{f:04d}.png")
        bpy.ops.render.render(write_still=True)
        print(f"[previz] {name} frame {f}/{nframes - 1}", flush=True)
