import bpy, bmesh, math, random
from mathutils import Vector, Euler
S = bpy.context.scene
random.seed(7)

def lin(c): return ((c+0.055)/1.055)**2.4 if c > 0.04045 else c/12.92
def hexcol(h, a=1.0):
    h = h.lstrip('#'); r, g, b = [int(h[i:i+2], 16)/255 for i in (0, 2, 4)]
    return (lin(r), lin(g), lin(b), a)
def mat(name, h, emit=False, alpha=1.0):
    m = bpy.data.materials.new(name)
    try: m.use_nodes = True
    except Exception: pass
    c = hexcol(h, alpha); m.diffuse_color = c
    nt = m.node_tree
    b = nt.nodes.get('Principled BSDF') if nt else None
    if b:
        b.inputs['Base Color'].default_value = c[:3]+(1,)
        if emit:
            b.inputs['Emission Color'].default_value = c[:3]+(1,)
            b.inputs['Emission Strength'].default_value = 3.0
        if alpha < 1: b.inputs['Alpha'].default_value = alpha
    if alpha < 1:
        for attr, val in (('surface_render_method', 'BLENDED'), ('blend_method', 'BLEND')):
            try: setattr(m, attr, val)
            except Exception: pass
    return m

M = dict(
    wall=mat('MAT_wall_navy', '#0B1626'), floor=mat('MAT_floor_cabinet', '#1E2329'),
    dev=mat('MAT_device', '#2C3A4D'), coat=mat('MAT_coat_white', '#F2F2F2'),
    skin=mat('MAT_skin_head', '#C99B7A'), pants=mat('MAT_pants_black', '#111111'),
    phone=mat('MAT_phone_body', '#0E0E0E'), screen=mat('MAT_phone_screen', '#2EE6D6', emit=True),
    panel=mat('MAT_panel_holo', '#2EE6D6', emit=True, alpha=0.6), thread=mat('MAT_light_thread', '#2EE6D6', emit=True),
    dfloor=mat('MAT_floor_digital', '#050B14'))
M['dfloor'].metallic = 0.8; M['dfloor'].roughness = 0.1

def link(o):
    S.collection.objects.link(o); return o
def mesh_obj(name, bm, m, parent=None, loc=(0, 0, 0)):
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    o = link(bpy.data.objects.new(name, me)); me.materials.append(m)
    o.parent = parent; o.location = loc
    for p in me.polygons: p.use_smooth = True
    return o
def box(name, dims, loc, m, parent=None):
    bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts: v.co.x *= dims[0]; v.co.y *= dims[1]; v.co.z *= dims[2]
    o = mesh_obj(name, bm, m, parent, loc)
    for p in o.data.polygons: p.use_smooth = False
    return o
def sphere(name, r, loc, m, parent=None):
    bm = bmesh.new(); bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, radius=r)
    return mesh_obj(name, bm, m, parent, loc)
def cyl(name, r, depth, loc, m, parent=None, along_y_from0=False, seg=20):
    bm = bmesh.new(); bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=seg, radius1=r, radius2=r, depth=depth)
    if along_y_from0:
        for v in bm.verts:
            x, y, z = v.co; v.co = Vector((x, z + depth/2, y))
    return mesh_obj(name, bm, m, parent, loc)
def capsule(name, r, length, loc, m, parent=None, ysc=1.0):
    bm = bmesh.new(); bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, radius=r)
    for v in bm.verts:
        v.co.z += (length/2 if v.co.z > 1e-6 else (-length/2 if v.co.z < -1e-6 else 0)); v.co.y *= ysc
    return mesh_obj(name, bm, m, parent, loc)
def empty(name, loc, parent=None):
    o = link(bpy.data.objects.new(name, None)); o.parent = parent; o.location = loc
    o.empty_display_size = 0.05; return o

def key(o, path, frame, val, interp='BEZIER'):
    setattr(o, path, val) if not isinstance(val, tuple) else setattr(o, path, val)
    o.keyframe_insert(data_path=path, frame=frame)
    for fc in fcurves_of(o):
        if fc.data_path == path:
            for kp in fc.keyframe_points:
                if abs(kp.co.x - frame) < 1e-3: kp.interpolation = interp
def fcurves_of(o):
    ad = o.animation_data
    if not ad or not ad.action: return []
    act = ad.action
    try: return list(act.fcurves)
    except AttributeError:
        from bpy_extras import anim_utils
        cb = anim_utils.action_get_channelbag_for_slot(act, ad.action_slot)
        return list(cb.fcurves) if cb else []

# ---------- scene settings ----------
S.render.fps = 24; S.render.fps_base = 1.0
S.frame_start = 1; S.frame_end = 312
S.render.resolution_x = 1080; S.render.resolution_y = 1920; S.render.resolution_percentage = 100
if S.world is None: S.world = bpy.data.worlds.new('WORLD_navy')
S.world.color = hexcol('#0B1626')[:3]
try:
    S.world.use_nodes = True
    bg = S.world.node_tree.nodes.get('Background')
    if bg: bg.inputs['Color'].default_value = hexcol('#0B1626'); bg.inputs['Strength'].default_value = 1.0
except Exception: pass
S.view_settings.view_transform = 'Standard'

# ---------- cabinet ----------
ENV = []
floor = box('ENV_floor_cabinet', (6, 6, 0.02), (0, 0.5, -0.01), M['floor'])
dfloor = box('ENV_floor_digital', (40, 40, 0.02), (0, 0, -0.013), M['dfloor'])
wall_b = box('ENV_wall_back', (6.2, 0.1, 3.0), (0, 3.55, 1.5), M['wall'])
wall_l = box('ENV_wall_side_neg_x', (0.1, 6.0, 3.0), (-3.05, 0.5, 1.5), M['wall'])
wall_r = box('ENV_wall_side_pos_x', (0.1, 6.0, 3.0), (3.05, 0.5, 1.5), M['wall'])
table = box('ENV_exam_table', (1.9, 0.7, 0.75), (1.6, 1.8, 0.375), M['dev'])
monitor = box('ENV_side_monitor', (0.5, 0.04, 0.35), (-1.4, 3.3, 1.7), M['dev'])
mon_arm = box('ENV_side_monitor_arm', (0.04, 0.2, 0.04), (-1.4, 3.4, 1.7), M['dev'])
iv = empty('ENV_iv_stand', (-2.0, 2.4, 0))
cyl('ENV_iv_pole', 0.015, 1.8, (0, 0, 0.9), M['dev'], parent=iv)
cyl('ENV_iv_base', 0.25, 0.04, (0, 0, 0.02), M['dev'], parent=iv)
box('ENV_iv_hook', (0.3, 0.02, 0.02), (0, 0, 1.79), M['dev'], parent=iv)
box('ENV_iv_bag', (0.12, 0.04, 0.2), (0.12, 0, 1.65), M['dev'], parent=iv)
glass = box('ENV_glass_cabinet', (1.0, 0.45, 1.9), (0.6, 3.25, 0.95), M['dev'])
DEVICES = [table, monitor, mon_arm, iv, glass]
WALLS = [wall_b, wall_l, wall_r]

# ---------- figure ----------
FIG = empty('HERO_fig_root', (0, 0, 0))
for sx, nm in ((0.1, 'L'), (-0.1, 'R')):
    cyl('HERO_leg_' + nm, 0.075, 0.9, (sx, 0, 0.45), M['pants'], parent=FIG)
capsule('HERO_torso_coat', 0.2, 0.58, (0, 0, 0.99), M['coat'], parent=FIG, ysc=0.65)
cyl('HERO_neck', 0.06, 0.16, (0, 0, 1.5), M['skin'], parent=FIG)
sphere('HERO_head', 0.13, (0, 0, 1.67), M['skin'], parent=FIG)

PHR = empty('PROP_phone_root', (0.12, -0.30, 1.25), parent=FIG)
phone = box('PROP_phone', (0.07, 0.15, 0.01), (0, 0, 0), M['phone'], parent=PHR)
phone.rotation_euler = Euler((math.radians(-37), 0, 0))
box('PROP_phone_screen', (0.064, 0.14, 0.002), (0, 0, 0.0055), M['screen'], parent=phone)

shL = empty('RIG_shoulder_L', (0.21, 0, 1.40), parent=FIG)
shR = empty('RIG_shoulder_R', (-0.21, 0, 1.40), parent=FIG)
elL = empty('RIG_elbow_L', (0.27, -0.08, 1.08), parent=FIG)
elR = empty('RIG_elbow_R', (-0.26, -0.06, 1.08), parent=FIG)
haL = empty('RIG_hand_L', (0.03, 0.02, -0.03), parent=PHR)
haR = empty('RIG_hand_R', (0.02, -0.32, 1.27), parent=FIG)
def arm(name, a, b, r):
    o = cyl(name, r, 1.0, (0, 0, 0), M['coat'], along_y_from0=True)
    c = o.constraints.new('COPY_LOCATION'); c.target = a
    c2 = o.constraints.new('STRETCH_TO'); c2.target = b; c2.rest_length = 1.0; c2.volume = 'NO_VOLUME'
    return o
arm('HERO_arm_upper_L', shL, elL, 0.05); arm('HERO_arm_fore_L', elL, haL, 0.042)
arm('HERO_arm_upper_R', shR, elR, 0.05); arm('HERO_arm_fore_R', elR, haR, 0.042)
sphere('HERO_hand_L', 0.045, (0, 0, 0), M['skin'], parent=haL)
sphere('HERO_hand_R', 0.045, (0, 0, 0), M['skin'], parent=haR)

# figure animation
key(haR, 'location', 1, (0.02, -0.32, 1.27)); key(haR, 'location', 80, (0.02, -0.32, 1.27))
key(haR, 'location', 89, (-0.15, -0.03, 1.66)); key(haR, 'location', 100, (-0.08, -0.20, 1.28))
key(elR, 'location', 80, (-0.26, -0.06, 1.08)); key(elR, 'location', 89, (-0.33, -0.12, 1.38)); key(elR, 'location', 100, (-0.26, -0.08, 1.06))
key(PHR, 'location', 100, (0.12, -0.30, 1.25)); key(PHR, 'location', 125, (0.12, -0.30, 1.15))
key(elL, 'location', 100, (0.27, -0.08, 1.08)); key(elL, 'location', 125, (0.27, -0.07, 1.03))
key(FIG, 'location', 165, (0, 0, 0)); key(FIG, 'location', 190, (0, -0.6, 0))

# small panels (frames 1-72)
SMALL = []
for i, dx in enumerate((-0.06, 0.0, 0.06)):
    p = box('FX_panel_small_%d' % (i+1), (0.07, 0.003, 0.05), (dx, 0, 0.01), M['panel'], parent=PHR)
    key(p, 'location', 1, (dx, 0, 0.01)); key(p, 'location', 72, (dx, 0, 0.11))
    key(p, 'scale', 1, (0.2, 0.2, 0.2)); key(p, 'scale', 24, (1, 1, 1)); key(p, 'scale', 175, (1, 1, 1)); key(p, 'scale', 185, (0, 0, 0))
    SMALL.append(p)

# dissolve 165-215
def dissolve(o, f0, f1):
    key(o, 'scale', f0, (1, 1, 1)); key(o, 'scale', f1, (0, 0, 0))
for o, (f0, f1) in zip(DEVICES, ((165, 192), (168, 190), (168, 190), (172, 197), (175, 200))):
    dissolve(o, f0, f1)
for o, (f0, f1) in zip(WALLS, ((182, 215), (178, 212), (178, 212))):
    dissolve(o, f0, f1)
dissolve(floor, 175, 215)
key(dfloor, 'hide_render', 1, True, 'CONSTANT'); key(dfloor, 'hide_render', 159, False, 'CONSTANT')
key(dfloor, 'hide_viewport', 1, True, 'CONSTANT'); key(dfloor, 'hide_viewport', 159, False, 'CONSTANT')
# particles rising 2 m
S.frame_set(1)
srcs = DEVICES + WALLS
n_part = 0
for i in range(140):
    src = srcs[i % len(srcs)]
    if src is iv: c, d = Vector((-2.0, 2.4, 0.9)), Vector((0.2, 0.2, 1.8))
    else: c, d = src.location.copy(), Vector(src.dimensions)
    pos = c + Vector(((random.random()-0.5)*d.x, (random.random()-0.5)*d.y, (random.random()-0.5)*d.z))
    pos.z = max(pos.z, 0.05)
    t0 = random.randint(165, 200); t1 = t0 + random.randint(14, 22)
    pt = box('FX_particle_%03d' % i, (0.04, 0.04, 0.04), pos, M['dev'])
    key(pt, 'scale', 1, (0, 0, 0), 'CONSTANT'); key(pt, 'scale', t0, (1, 1, 1), 'LINEAR'); key(pt, 'scale', t1, (0, 0, 0))
    key(pt, 'location', t0, tuple(pos), 'LINEAR'); key(pt, 'location', t1, tuple(pos + Vector((0, 0, 2.0))))
    n_part += 1

# big panels 175-220
screen = bpy.data.objects['PROP_phone_screen']
C = Vector((0, -0.6, 0))
BIG = []
for i, (ang, h) in enumerate(((-110, 1.5), (-50, 1.9), (50, 1.3), (110, 1.7))):
    s0 = 175 + 5*i; e0 = s0 + 30 if i < 3 else 220
    S.frame_set(s0); start = screen.matrix_world.translation.copy()
    th = math.radians(ang)
    fin = Vector((C.x + 1.5*math.sin(th), C.y - 1.5*math.cos(th), h))
    p = box('FX_panel_big_%d' % (i+1), (0.60, 0.005, 0.40), start, M['panel'])
    key(p, 'scale', 1, (0, 0, 0), 'CONSTANT'); key(p, 'scale', s0, (0.05, 0.05, 0.05)); key(p, 'scale', e0, (1, 1, 1))
    key(p, 'location', s0, tuple(start)); key(p, 'location', e0, tuple(fin))
    key(p, 'rotation_euler', s0, (0, 0, 0)); key(p, 'rotation_euler', e0, (0, 0, th))
    BIG.append((p, fin))

# light threads 240-300
for i in range(3):
    a = BIG[i][1]; b = BIG[i+1][1]; d = b - a; L = d.length
    t = cyl('FX_light_thread_%d' % (i+1), 0.005, 1.0, tuple(a), M['thread'], along_y_from0=True, seg=8)
    t.rotation_mode = 'QUATERNION'; t.rotation_quaternion = Vector((0, 1, 0)).rotation_difference(d.normalized())
    f0 = 240 + 20*i; f1 = f0 + 20
    key(t, 'scale', 1, (0, 0, 0), 'CONSTANT'); key(t, 'scale', f0, (1, 0.001, 1)); key(t, 'scale', f1, (1, L, 1))

# ---------- cameras ----------
def camera(name, lens):
    cd = bpy.data.cameras.new(name); cd.lens = lens; cd.sensor_width = 36; cd.sensor_fit = 'AUTO'; cd.clip_start = 0.02; cd.clip_end = 200
    co = link(bpy.data.objects.new(name, cd))
    tg = empty(name + '_target', (0, 0, 0))
    c = co.constraints.new('TRACK_TO'); c.target = tg; c.track_axis = 'TRACK_NEGATIVE_Z'; c.up_axis = 'UP_Y'
    return co, tg
def noise(o, strength, seed):
    for fc in fcurves_of(o):
        if fc.data_path == 'location':
            m = fc.modifiers.new('NOISE'); m.strength = strength; m.scale = 14.0; m.phase = seed + fc.array_index*3.7
cams = []
c1, t1 = camera('CAM_shot1_MS_50', 50)
a = Vector((0.25, -2.4, 1.45)); tgt = Vector((0.05, -0.2, 1.25)); end = a + (tgt - a).normalized()*0.55
key(c1, 'location', 1, tuple(a)); key(c1, 'location', 48, tuple(end)); t1.location = tgt
c2, t2 = camera('CAM_shot2_ECU_85', 85)
key(c2, 'location', 49, (0.35, 0.05, 1.75)); key(c2, 'location', 72, (0.33, 0.0, 1.73), 'LINEAR'); t2.location = (0.12, -0.30, 1.256)
for k in fcurves_of(c2):
    for kp in k.keyframe_points: kp.interpolation = 'LINEAR'
c3, t3 = camera('CAM_shot3_MCU_85', 85)
key(c3, 'location', 73, (0, -2.2, 1.65)); key(c3, 'location', 158, (0, -3.2, 1.65)); t3.location = (0, 0, 1.62)
c4, t4 = camera('CAM_shot4_WS_35', 35)
key(c4, 'location', 159, (-0.6, -3.6, 0.6)); key(c4, 'location', 230, (-0.6, -3.6, 0.8))
key(t4, 'location', 159, (0, -0.3, 1.1)); key(t4, 'location', 165, (0, -0.3, 1.1)); key(t4, 'location', 195, (0, -0.9, 1.1))
piv = empty('CAM_shot5_orbit_pivot', (0, -0.6, 0))
c5, t5 = camera('CAM_shot5_MS_50', 50)
c5.parent = piv; c5.location = (0, -2.6, 1.4)
key(c5, 'location', 231, (0, -2.6, 1.4)); key(c5, 'location', 312, (0, -2.6, 1.4))
key(piv, 'rotation_euler', 231, (0, 0, 0), 'LINEAR'); key(piv, 'rotation_euler', 312, (0, 0, math.radians(-90)), 'LINEAR')
t5.location = (0, -0.6, 1.35)
for i, c in enumerate((c1, c2, c3, c4, c5)):
    noise(c, 0.03, 10*i + 1)
S.camera = c1
S.timeline_markers.clear()
for nm, fr, c in (('CUT1', 1, c1), ('CUT2', 49, c2), ('CUT3', 73, c3), ('CUT4', 159, c4), ('CUT5', 231, c5)):
    mk = S.timeline_markers.new(nm, frame=fr); mk.camera = c

# lights (for EEVEE / viewer), workbench render setup
for nm, typ, loc, en in (('LGT_key', 'SUN', (2, -3, 5), 3.0), ('LGT_fill', 'POINT', (-2, -2, 2.5), 150.0)):
    ld = bpy.data.lights.new(nm, typ); ld.energy = en
    lo = link(bpy.data.objects.new(nm, ld)); lo.location = loc
    if typ == 'SUN': lo.rotation_euler = Euler((math.radians(45), 0, math.radians(30)))
S.render.engine = 'BLENDER_WORKBENCH'
sh = S.display.shading
sh.light = 'FLAT'; sh.color_type = 'MATERIAL'
try: sh.show_object_outline = True
except Exception: pass

# stethoscope (simple): tube around neck + earpieces + chest piece in right hand until frame 78
st_mat = mat('MAT_stethoscope', '#111111')
bm = bmesh.new(); bmesh.ops.create_circle(bm, cap_ends=False, segments=24, radius=0.11)
ring = mesh_obj('PROP_steth_ring', bm, st_mat, parent=FIG, loc=(0, -0.02, 1.43))
ring.modifiers.new('skin', 'SKIN'); 
disc = cyl('PROP_steth_disc', 0.02, 0.01, (0, 0, 0), M['dev'], parent=haR)

# ---------- v2 retime: 13 s -> 16 s (shot3 73-192, shot4 193-288, shot5 289-384) ----------
def remap(x):
    if x <= 72: return x
    if x <= 158: return 73 + (x - 73) * (119.0 / 85.0)
    if x <= 230: return 193 + (x - 159) * (95.0 / 71.0)
    return 289 + (x - 231) * (95.0 / 81.0)
seen = set()
for ob in bpy.data.objects:
    for fc in fcurves_of(ob):
        if id(fc) in seen: continue
        seen.add(id(fc))
        for kp in fc.keyframe_points:
            x = kp.co.x; nx = remap(x); d = nx - x
            kp.co.x = nx; kp.handle_left.x += d; kp.handle_right.x += d
        fc.update()
for mk in S.timeline_markers:
    mk.frame = int(round(remap(mk.frame)))
S.frame_end = 384
S.frame_set(1)
result = {"objects": len(bpy.data.objects), "particles": n_part, "markers": [(m.name, m.frame, m.camera.name) for m in S.timeline_markers],
          "big_final": [(p.name, [round(v, 3) for v in f]) for p, f in BIG]}
