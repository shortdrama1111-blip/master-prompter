"""Shot 1 final render: mocha elevator shelves with the client's real product labels.

Labels come straight from the product photos (blender/tex/*.png), so every word is the real one.
  blender.exe -b --factory-startup --python shot1_final.py -- OUTDIR [test|full]
test = first + last frame, full = every frame. 1080x1920, 24 fps, 2.5 s (trim to ~1.7 s in the edit).
Look (client, 2026-11-19): mocha / dark taupe, darker shelf interiors, warm 3200K LED strips,
champagne shelves, soft front light so labels read, clear contrast cream bottles vs dark background.
"""
import bpy, bmesh, sys, os, math, random
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = argv[0] if argv else os.path.join(os.getcwd(), "shot1_out")
MODE = argv[1] if len(argv) > 1 else "test"
TEX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tex")
FPS, W, H, DUR = 24, 1080, 1920, 2.5
rng = random.Random(11)

for o in list(bpy.data.objects):
    bpy.data.objects.remove(o)
sc = bpy.context.scene
ENGINE = os.environ.get("SHOT1_ENGINE", "EEVEE").upper()
sc.render.engine = "CYCLES" if ENGINE == "CYCLES" else "BLENDER_EEVEE"
if ENGINE == "CYCLES":
    sc.cycles.device = "GPU"
    try:
        prefs = bpy.context.preferences.addons["cycles"].preferences
        prefs.compute_device_type = "METAL"
        prefs.get_devices()
        for d in prefs.devices:
            d.use = True
    except Exception as ex:
        print("[shot1] gpu:", ex)
    sc.cycles.samples = int(os.environ.get("SHOT1_SAMPLES", "128"))
    sc.cycles.use_denoising = True
    sc.cycles.max_bounces, sc.cycles.transmission_bounces, sc.cycles.glossy_bounces = 12, 12, 6
sc.eevee.taa_render_samples = 32
try:
    sc.eevee.use_raytracing = True
except Exception:
    pass
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = W, H, 100
sc.render.fps = FPS
sc.render.image_settings.file_format = "PNG"
sc.view_settings.view_transform = "AgX"

LED = (1.0, 0.68, 0.40)        # ~3200K
KEY = (1.0, 0.80, 0.60)

world = bpy.data.worlds.new("W")
sc.world = world
try:
    world.use_nodes = True
except Exception:
    pass
bg = world.node_tree.nodes.get("Background")
bg.inputs["Color"].default_value = (0.09, 0.065, 0.05, 1)
bg.inputs["Strength"].default_value = 0.12


def principled(name):
    m = bpy.data.materials.new(name)
    try:
        m.use_nodes = True
    except Exception:
        pass
    return m, m.node_tree.nodes.get("Principled BSDF"), m.node_tree


def flat(name, rgb, rough=0.7, metal=0.0, emit=None, strength=0.0):
    m, b, _ = principled(name)
    b.inputs["Base Color"].default_value = (*rgb, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if emit:
        b.inputs["Emission Color"].default_value = (*emit, 1)
        b.inputs["Emission Strength"].default_value = strength
    return m


def textured(name, img, rough=0.5, alpha=False, base_rgb=None):
    m, b, nt = principled(name)
    t = nt.nodes.new("ShaderNodeTexImage")
    t.image = bpy.data.images.load(os.path.join(TEX, img))
    t.extension = "EXTEND"
    if alpha:
        m.surface_render_method = "BLENDED"
        b.inputs["Base Color"].default_value = (0.02, 0.02, 0.02, 1)
        nt.links.new(t.outputs["Alpha"], b.inputs["Alpha"])
    else:
        nt.links.new(t.outputs["Color"], b.inputs["Base Color"])
    b.inputs["Roughness"].default_value = rough
    return m


# Cycles adds bounce light (~25% brighter walls than EEVEE), so the albedo drops to keep the
# approved v2 dark taupe on screen.
DK = 0.62 if ENGINE == "CYCLES" else 1.0
M_MOCHA = flat("mocha", (0.07 * DK, 0.048 * DK, 0.035 * DK), 0.75)          # dark taupe
M_INSIDE = flat("inside_taupe", (0.035 * DK, 0.025 * DK, 0.019 * DK), 0.85)  # a step darker
M_CHAMP = flat("champagne", (0.80, 0.68, 0.50), 0.30, metal=1.0)
M_LED = flat("led", (1, 1, 1), 0.5, emit=LED, strength=12.0)
M_MASK = textured("mask_label", "mask.png", 0.45)
M_COND = textured("cond_label", "cond.png", 0.45)
M_BOX = textured("oilbox_print", "oilbox.png", 0.55)
M_BOXSIDE = flat("oilbox_side", (0.92, 0.69, 0.43), 0.55)   # linear of the photo peach sRGB (0.965, 0.851, 0.69)
M_DECAL = textured("oil_decal", "oil_decal.png", 0.3, alpha=True)
M_CAPBLACK = flat("cap_black", (0.008, 0.008, 0.008), 0.08)
M_CAPWHITE = flat("cap_white", (0.90, 0.89, 0.87), 0.22)
M_TUBE = flat("dip_tube", (0.9, 0.9, 0.9), 0.4)
# Clear glass: real refraction. EEVEE needs raytraced refraction on the material, otherwise the
# transmission only sees the dark world probe and the bottle renders black. The bottle is full of
# clear oil (IOR ~1.47), so a solid refracting body behaves like the real one: it bends the shelf
# behind it, magnifies the dip tube and throws bright edges where it catches the LEDs.
m, b, _ = principled("glass")
b.inputs["Base Color"].default_value = (1, 1, 1, 1)
b.inputs["Roughness"].default_value = 0.0
b.inputs["IOR"].default_value = 1.47
b.inputs["Transmission Weight"].default_value = 1.0
for attr, val in (("surface_render_method", "DITHERED"), ("use_raytrace_refraction", True),
                  ("thickness_mode", "SPHERE"), ("use_backface_culling", False)):
    try:
        setattr(m, attr, val)
    except Exception as ex:
        print("[shot1] glass:", attr, ex)
M_GLASS = m

cam_data = bpy.data.cameras.new("Cam")
cam_data.sensor_fit = "VERTICAL"
cam_data.angle_y = math.radians(46)
cam_data.dof.use_dof = True
cam_data.dof.aperture_fstop = 4.0
cam = bpy.data.objects.new("Cam", cam_data)
sc.collection.objects.link(cam)
sc.camera = cam
CAM_LOC, CAM_TGT = Vector((0.0, -0.85, 1.45)), Vector((0.0, -0.07, 1.45))
cam.location = CAM_LOC
cam.rotation_euler = (CAM_TGT - CAM_LOC).to_track_quat("-Z", "Y").to_euler()
cam_data.dof.focus_distance = (CAM_TGT - CAM_LOC).length

# soft front key from camera-left, 30 deg up: reads the labels
kd = bpy.data.lights.new("Key", "AREA")
kd.shape, kd.size, kd.energy, kd.color = "SQUARE", 1.2, 30, KEY
key = bpy.data.objects.new("Key", kd)
sc.collection.objects.link(key)
key.location = Vector((-0.75, -1.25, 1.85))
key.rotation_euler = (CAM_TGT - key.location).to_track_quat("-Z", "Y").to_euler()


def link(o):
    sc.collection.objects.link(o)
    return o


def mesh_obj(name, bm, mat, parent=None, smooth_sides=True):
    if smooth_sides:
        for f in bm.faces:
            f.smooth = abs(f.normal.z) < 0.5
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    if isinstance(mat, list):
        for x in mat:
            me.materials.append(x)
    else:
        me.materials.append(mat)
    o = link(bpy.data.objects.new(name, me))
    if parent:
        o.parent = parent
    return o


def box(name, size, loc, mat, parent=None):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co = Vector((v.co.x * size[0], v.co.y * size[1], v.co.z * size[2]))
    o = mesh_obj(name, bm, mat, parent, smooth_sides=False)
    o.location = loc
    return o


def cylinder(bm, r, h, z0, r2=None, seg=48):
    geom = bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=seg,
                                 radius1=r, radius2=r if r2 is None else r2, depth=h)
    for v in geom["verts"]:
        v.co.z += z0 + h / 2
    return geom


def front_uv(bm, half_w, height, z0=0.0, inset=0.0):
    """Planar projection from the front (-Y): the product photo maps 1:1 onto the visible face.
    inset trims the photo edge (anti-aliased black background) off the bottle sides."""
    uv = bm.loops.layers.uv.verify()
    for f in bm.faces:
        for l in f.loops:
            x, z = l.vert.co.x, l.vert.co.z
            u = (x + half_w) / (2 * half_w)
            l[uv].uv = (inset + u * (1 - 2 * inset), (z - z0) / height)


def bottle150(label_mat, base, parent):
    """150 ml bottle: body r 22.5 mm x 105 mm + cap r 21.5 mm x 60 mm; one photo covers both."""
    e = link(bpy.data.objects.new("bottle150", None))
    e.parent, e.location = parent, base
    bm = bmesh.new()
    cylinder(bm, 0.0225, 0.105, 0.0)
    front_uv(bm, 0.0225, 0.165, inset=0.025)   # body takes the lower 105/165 of the photo
    mesh_obj("bottle_body", bm, label_mat, e)
    bm = bmesh.new()
    cylinder(bm, 0.0215, 0.060, 0.105)          # cap: plain glossy white, like the photo
    mesh_obj("bottle_cap", bm, M_CAPWHITE, e)
    return e


def glass_body(r0, r1, h, bev, seg=64):
    """Tapered solid glass with rounded rims: the bevels are what catch the thin bright edges."""
    bm = bmesh.new()
    cylinder(bm, r0, h, 0.0, r2=r1, seg=seg)
    rims = [e for e in bm.edges if len(e.link_faces) == 2
            and abs(e.link_faces[0].normal.z - e.link_faces[1].normal.z) > 0.5]
    bmesh.ops.bevel(bm, geom=rims, offset=bev, segments=4, profile=0.5, affect="EDGES")
    for f in bm.faces:
        f.smooth = abs(f.normal.z) < 0.999
    return bm


def oil_bottle(base, parent):
    """40 ml bottle, matched to refs/hair-oil-with-box.jpg: clear tapered glass full of clear oil,
    glossy black cap, white dip tube, black front print."""
    e = link(bpy.data.objects.new("oil", None))
    e.parent, e.location = parent, base
    mesh_obj("oil_glass", glass_body(0.0185, 0.0165, 0.068, 0.0025), M_GLASS, e, smooth_sides=False)
    bm = bmesh.new(); cylinder(bm, 0.0168, 0.044, 0.068, seg=64)
    for f in bm.faces:
        f.smooth = abs(f.normal.z) < 0.5
    mesh_obj("oil_cap", bm, M_CAPBLACK, e, smooth_sides=False)
    bm = bmesh.new(); cylinder(bm, 0.0018, 0.058, 0.010, seg=12)   # ends above the thick base
    mesh_obj("oil_tube", bm, M_TUBE, e)
    # front print: the photo spans 0..0.112 m tall; it sits just in front of the glass face
    dh, dw = 0.112, 0.112 * 123 / 404
    bm = bmesh.new()
    verts = [bm.verts.new((x, -0.0192, z)) for x, z in ((-dw / 2, 0), (dw / 2, 0), (dw / 2, dh), (-dw / 2, dh))]
    bm.faces.new(verts)
    front_uv(bm, dw / 2, dh)
    mesh_obj("oil_label", bm, M_DECAL, e, smooth_sides=False)
    # two slim vertical LED strips on the cubby side walls: product-photo strip lights that draw
    # the bright vertical edges down both sides of the glass
    for sx in (-1, 1):
        ld = bpy.data.lights.new("oil_strip", "AREA")
        ld.shape, ld.size, ld.size_y = "RECTANGLE", 0.006, 0.10
        ld.energy, ld.color, ld.spread = 0.35, LED, math.radians(35)   # narrow beam: edges, not walls
        lo = link(bpy.data.objects.new("oil_strip", ld))
        lo.parent, lo.location = e, (sx * 0.060, 0.005, 0.055)      # beside the glass, facing it
        lo.rotation_euler = (math.radians(90), 0, math.radians(sx * 90))
    return e


def oil_box(base, parent):
    """Oil box, front face printed with the real box photo.
    oilbox.png is 360x497 and the box face is only its right half (x 182..360, the left half is the
    photo's white backdrop), so the UVs use u 0.505..1.0 and the face keeps the real 178:497 ratio.
    Square section, like the real carton."""
    h = 0.135
    U0, V0 = 182 / 360, 2 / 497            # skip the white backdrop and the 1-px shadow row
    w = h * (1 - U0) * 360 / ((1 - V0) * 497)
    d = w
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co = Vector((v.co.x * w, v.co.y * d, v.co.z * h + h / 2))
    uv = bm.loops.layers.uv.verify()
    for f in bm.faces:
        front = f.normal.y < -0.9
        f.material_index = 0 if front else 1
        for l in f.loops:
            u = (l.vert.co.x + w / 2) / w
            l[uv].uv = (U0 + u * (1 - U0), V0 + (l.vert.co.z / h) * (1 - V0))
    o = mesh_obj("oilbox", bm, [M_BOX, M_BOXSIDE], parent, smooth_sides=False)
    o.location = base
    return o


# ---------------------------------------------------------------- the shelf wall
box("wall", (6, 0.02, 4), (0, 0.02, 2.0), M_MOCHA)
box("floor", (6, 6, 0.02), (0, 0, -0.01), M_MOCHA)
cols, cw, depth, t = 5, 0.15, 0.14, 0.008
x0 = -cw * cols / 2
for c in range(cols + 1):
    box("divider", (t, depth, 3.4), (x0 + c * cw, -depth / 2, 1.6), M_CHAMP)

kinds = ["mask", "cond", "oil", "oilbox"]
lifts = []
for c in range(cols):
    xc = x0 + c * cw + cw / 2
    col = link(bpy.data.objects.new(f"column{c}", None))
    lifts.append((col, 1 if (c - cols // 2) % 2 == 0 else -1))
    box("back", (cw, 0.01, 3.4), (xc, 0.003, 1.6), M_INSIDE, col)
    z = 0.10 + rng.uniform(0, 0.10)
    k = rng.randrange(4)
    while z < 3.1:
        h = rng.uniform(0.24, 0.29)
        box("board", (cw - t, depth, t), (xc, -depth / 2, z), M_CHAMP, col)
        # LED strip along the top front edge of the cubby, plus a real light washing down
        box("led", (cw - 0.02, 0.006, 0.004), (xc, -depth + 0.012, z + h - 0.010), M_LED, col)
        if 0.85 < z < 2.2:
            ld = bpy.data.lights.new("cubby", "AREA")
            ld.shape, ld.size, ld.size_y = "RECTANGLE", cw - 0.02, 0.012
            ld.energy, ld.color = 1.0, LED
            lo = link(bpy.data.objects.new("cubby_led", ld))
            lo.parent, lo.location = col, (xc, -depth + 0.02, z + h - 0.016)
        kind = kinds[k % 4]
        k += rng.choice((1, 1, 2))
        base = (xc, -depth * 0.48, z + t / 2)
        if kind == "mask":
            bottle150(M_MASK, base, col)
        elif kind == "cond":
            bottle150(M_COND, base, col)
        elif kind == "oil":
            # bottle in front of its own carton, as in refs/hair-oil-with-box.jpg: the peach face
            # behind the clear glass is what makes the black print and the glass itself read
            oil_box((xc + 0.012, -0.032, z + t / 2), col)
            oil_bottle((xc - 0.008, -0.081, z + t / 2), col)
        else:
            oil_box(base, col)
        z += h


def update(tt):
    s = min(max(tt / DUR, 0), 1)
    s = s * s * (3 - 2 * s)
    for col, sign in lifts:
        col.location.z = sign * 0.40 * (s - 0.5)


n = round(DUR * FPS)
frames = [0, n - 1] if MODE == "test" else range(n)
os.makedirs(OUT, exist_ok=True)
for f in frames:
    update(f / FPS)
    sc.render.filepath = os.path.join(OUT, f"f{f:04d}.png")
    bpy.ops.render.render(write_still=True)
    print(f"[shot1] frame {f}/{n - 1}", flush=True)
