"""Shared set-up for the final Blender shots (2, 3, ...): the approved shot-1 v4 look.

Same render settings, Khronos PBR Neutral view, materials, real product textures and product
builders as shot1_final.py (frozen there while its render was running). Import it, build the
scene, call render(update, n_frames).
Env knobs keep the FINAL_ prefix: FINAL_SAMPLES, FINAL_EXPOSURE, FINAL_MOCHA, FINAL_KEY ...
"""
import bpy, bmesh, sys, os, math, random
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
OUT = argv[0] if argv else os.path.join(os.getcwd(), "final_out")
MODE = argv[1] if len(argv) > 1 else "test"
TEX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tex")
FPS, W, H, DUR = 24, 1080, 1920, 3.0
rng = random.Random(11)

for o in list(bpy.data.objects):
    bpy.data.objects.remove(o)
sc = bpy.context.scene
ENGINE = os.environ.get("FINAL_ENGINE", "CYCLES").upper()
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
        print("[final] gpu:", ex)
    sc.cycles.samples = int(os.environ.get("FINAL_SAMPLES", "64"))
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
sc.view_settings.view_transform = os.environ.get("FINAL_VIEW", "Khronos PBR Neutral")
for look in (os.environ.get("FINAL_LOOK", "None"), "AgX - " + os.environ.get("FINAL_LOOK", "None")):
    try:
        sc.view_settings.look = look
        break
    except Exception:
        pass
print("[final] view", sc.view_settings.view_transform, "| look", sc.view_settings.look, flush=True)
sc.view_settings.exposure = float(os.environ.get("FINAL_EXPOSURE", "-0.2"))

LED = (1.0, 0.68, 0.40)        # ~3200K
KEY = tuple(float(v) for v in os.environ.get("FINAL_KEY", "0.95,0.97,1.0").split(","))  # front key: near-neutral so products keep their photo colour

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


# v4 look (client: "kafe e butë, mocha"): Khronos PBR Neutral keeps the products in their photo
# colour; the 3200K LED wash tints everything orange, so the interior albedo is a grey taupe that
# lands on soft mocha on screen, and the white caps are a touch cool so they stay white.
# Cycles adds bounce light (~25% brighter than EEVEE), hence DK.
DK = 0.62 if ENGINE == "CYCLES" else 1.0
MO = tuple(float(v) for v in os.environ.get("FINAL_MOCHA", "0.30,0.31,0.36").split(","))
M_MOCHA = flat("mocha", tuple(c * DK for c in MO), 0.75)                       # soft mocha
M_INSIDE = flat("inside_taupe", tuple(c * DK * 0.7 for c in MO), 0.85)        # interior a step darker
M_CHAMP = flat("champagne", (0.80, 0.68, 0.50), 0.30, metal=1.0)
M_LED = flat("led", (1, 1, 1), 0.5, emit=(1.0, 0.62, 0.32), strength=float(os.environ.get("FINAL_LEDSTR", "0.7")))  # strip itself reads warm gold
M_MASK = textured("mask_label", "mask.png", 0.45)
M_COND = textured("cond_label", "cond.png", 0.45)
M_BOX = textured("oilbox_print", "oilbox.png", 0.55)
M_BOXSIDE = flat("oilbox_side", (0.92, 0.69, 0.43), 0.55)   # linear of the photo peach sRGB (0.965, 0.851, 0.69)
M_DECAL = textured("oil_decal", "oil_decal.png", 0.3, alpha=True)
M_CAPBLACK = flat("cap_black", (0.008, 0.008, 0.008), 0.08)
M_CAPWHITE = flat("cap_white", (0.84, 0.88, 0.94), 0.22)   # a touch cool so it renders white under the 3200K wash
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
        print("[final] glass:", attr, ex)
M_GLASS = m

cam_data = bpy.data.cameras.new("Cam")
cam_data.sensor_fit = "VERTICAL"
cam_data.angle_y = math.radians(46)
cam_data.dof.use_dof = True
cam_data.dof.aperture_fstop = 4.0
cam = bpy.data.objects.new("Cam", cam_data)
sc.collection.objects.link(cam)
sc.camera = cam


def aim(loc, tgt, fov=None):
    loc, tgt = Vector(loc), Vector(tgt)
    cam.location = loc
    cam.rotation_euler = (tgt - loc).to_track_quat("-Z", "Y").to_euler()
    if fov:
        cam_data.angle_y = math.radians(fov)
    cam_data.dof.focus_distance = (tgt - loc).length


def area(name, loc, tgt, size, energy, color, size_y=None):
    d = bpy.data.lights.new(name, "AREA")
    d.shape = "RECTANGLE" if size_y else "SQUARE"
    d.size, d.energy, d.color = size, energy, color
    if size_y:
        d.size_y = size_y
    o = bpy.data.objects.new(name, d)
    sc.collection.objects.link(o)
    o.location = Vector(loc)
    o.rotation_euler = (Vector(tgt) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
    return o


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


def render(update, n, tag):
    frames = [0] if MODE == "still" else [0, n - 1] if MODE == "test" else range(n)
    os.makedirs(OUT, exist_ok=True)
    for f in frames:
        update(f / FPS)
        sc.render.filepath = os.path.join(OUT, f"f{f:04d}.png")
        if os.environ.get("RESUME") and os.path.exists(sc.render.filepath):
            continue                     # RESUME=1: keep frames already on disk
        bpy.ops.render.render(write_still=True)
        print(f"[{tag}] frame {f}/{n - 1}", flush=True)


# ---------------------------------------------------------------- shared for shots 2, 4: DreamDuo
# carton 13 x 6 x 19 cm, front printed with tex/duo.png (cut from refs/dreamduo-box.jpg), sides the
# photo's side-panel peach. Centred on its origin, front face = local -Y.
M_DUO = textured("duo_print", "duo.png", 0.45)
M_DUOSIDE = flat("duo_side", (0.49, 0.234, 0.13), 0.5)      # linear of photo sRGB (0.729, 0.52, 0.397)
M_ROOM = flat("room_mocha", (0.10, 0.068, 0.050), 0.8)     # true mocha where no shelf LEDs tint the set
M_DECK = flat("deck_dark", (0.05, 0.04, 0.035), 0.6, metal=0.6)


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
    return mesh_obj("duo", bm, [M_DUO, M_DUOSIDE], parent, smooth_sides=False)


def oil_box_centred(parent=None):
    """Hair Oil carton centred on an empty (half height 0.0675 m), for belts and rigs."""
    e = link(bpy.data.objects.new("oilbox_c", None))
    if parent:
        e.parent = parent
    oil_box((0, 0, -0.0675), e)
    return e


# ---------------------------------------------------------------- shared for shots 5, 6: red holiday bag
# Front printed straight from refs/holiday-bag-red.jpg (copied to tex/bag_photo.jpg). The photo is in
# perspective, so the front face is a 24 x 24 grid whose UVs interpolate the four photo corners of the
# front panel; the print lands square on the box. The front ribbon handle lies flat on the face in the
# photo and stays part of the print; the back handle is a real satin ribbon arch.
BAG_PX = (1456, 1080)
BAG_CORNERS = {"tl": (232, 102), "tr": (1190, 107), "bl": (214, 958), "br": (1188, 1044)}
M_BAGFRONT = textured("bag_print", "bag_photo.jpg", 0.55)
M_BAGRED = flat("bag_red", (0.43, 0.020, 0.022), 0.55)          # linear of the photo red sRGB (0.69, 0.15, 0.16)
M_SATIN_WHITE = flat("satin_white", (0.82, 0.84, 0.88), 0.25)
M_SATIN_RED = flat("satin_red", (0.42, 0.012, 0.02), 0.28)
for _m in (M_SATIN_WHITE, M_SATIN_RED):
    try:
        _m.node_tree.nodes["Principled BSDF"].inputs["Sheen Weight"].default_value = 0.6
    except Exception:
        pass


def _bag_uv(s, t):
    """s: 0 left -> 1 right, t: 0 bottom -> 1 top; bilinear over the photo corners."""
    c = BAG_CORNERS
    top = [c["tl"][i] + (c["tr"][i] - c["tl"][i]) * s for i in (0, 1)]
    bot = [c["bl"][i] + (c["br"][i] - c["bl"][i]) * s for i in (0, 1)]
    x = bot[0] + (top[0] - bot[0]) * t
    y = bot[1] + (top[1] - bot[1]) * t
    return x / BAG_PX[0], 1 - y / BAG_PX[1]


def ribbon_strip(pts, width, mat, parent, name="ribbon"):
    """Flat satin ribbon along a polyline; its width runs along local Y."""
    bm = bmesh.new()
    rows = [(bm.verts.new((p[0], p[1] - width / 2, p[2])), bm.verts.new((p[0], p[1] + width / 2, p[2]))) for p in pts]
    for a, b in zip(rows, rows[1:]):
        bm.faces.new((a[0], b[0], b[1], a[1]))
    for f in bm.faces:
        f.smooth = True
    return mesh_obj(name, bm, mat, parent, smooth_sides=False)


def bag(scale=1.0, parent=None, handle=True):
    """Open-top gift bag on an empty at its base centre, front = local -Y. Real size 42 x 12 x 36 cm."""
    w, d, h = 0.42 * scale, 0.12 * scale, 0.36 * scale
    e = link(bpy.data.objects.new("bag", None))
    if parent:
        e.parent = parent
    n = 24
    bm = bmesh.new()
    uv = bm.loops.layers.uv.verify()
    grid = [[bm.verts.new((-w / 2 + w * i / n, -d / 2, h * j / n)) for i in range(n + 1)] for j in range(n + 1)]
    for j in range(n):
        for i in range(n):
            f = bm.faces.new((grid[j][i], grid[j][i + 1], grid[j + 1][i + 1], grid[j + 1][i]))
            for l, (si, tj) in zip(f.loops, ((i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1))):
                l[uv].uv = _bag_uv(si / n, tj / n)
    mesh_obj("bag_front", bm, M_BAGFRONT, e, smooth_sides=False)
    bm = bmesh.new()                                          # back, sides, bottom; open top
    P = lambda x, y, z: bm.verts.new((x, y, z))
    quads = [((-w/2, d/2, 0), (w/2, d/2, 0), (w/2, d/2, h), (-w/2, d/2, h)),
             ((-w/2, -d/2, 0), (-w/2, d/2, 0), (-w/2, d/2, h), (-w/2, -d/2, h)),
             ((w/2, -d/2, 0), (w/2, d/2, 0), (w/2, d/2, h), (w/2, -d/2, h)),
             ((-w/2, -d/2, 0), (w/2, -d/2, 0), (w/2, d/2, 0), (-w/2, d/2, 0))]
    for q in quads:
        bm.faces.new([P(*v) for v in q])
    mesh_obj("bag_body", bm, M_BAGRED, e, smooth_sides=False)
    if handle:                                                # back handle: satin arch above the opening
        pts = [(-0.10 * scale + 0.20 * scale * i / 30, d / 2 - 0.006 * scale,
                h - 0.02 * scale + 0.13 * scale * math.sin(math.pi * i / 30)) for i in range(31)]
        ribbon_strip(pts, 0.022 * scale, M_SATIN_WHITE, e, "handle")
    return e
