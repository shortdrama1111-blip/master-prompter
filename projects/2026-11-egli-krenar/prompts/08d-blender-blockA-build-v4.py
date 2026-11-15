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
S.frame_start = 1; S.frame_end = 384
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



# ================= v4 animation (16 s, 384 frames) =================
box('ENV_bed_foreground', (0.7, 1.9, 0.12), (-1.0, -1.2, 0.72), M['coat'])
box('ENV_bed_foreground_base', (0.6, 1.8, 0.66), (-1.0, -1.2, 0.33), M['dev'])
st_mat = mat('MAT_stethoscope', '#111111')
bm = bmesh.new(); bmesh.ops.create_circle(bm, cap_ends=False, segments=24, radius=0.11)
ring = mesh_obj('PROP_steth_ring', bm, st_mat, parent=FIG, loc=(0, -0.02, 1.43)); ring.modifiers.new('skin', 'SKIN')
phone = bpy.data.objects['PROP_phone']

# --- right hand: searches for the heartbeat on 3 spots, then removes the stethoscope by the Y under the chin
for f, p in ((1, (0.02, -0.32, 1.27)), (12, (0.02, -0.32, 1.27)), (18, (0.07, -0.34, 1.31)), (36, (0.07, -0.34, 1.31)),
             (42, (-0.01, -0.30, 1.22)), (73, (-0.01, -0.30, 1.22)),
             (79, (0.0, -0.12, 1.46)), (86, (0.0, -0.30, 1.50)), (96, (-0.05, -0.12, 1.40)),
             (110, (-0.22, -0.25, 1.12)), (125, (-0.18, -0.30, 1.25)), (145, (-0.26, -0.22, 1.10)), (165, (-0.15, -0.32, 1.28)),
             (193, (-0.24, -0.15, 1.02)), (203, (-0.08, -0.42, 1.30)), (215, (-0.48, -0.45, 1.42)), (245, (-0.24, -0.15, 1.02)),
             (320, (-0.24, -0.15, 1.02)), (340, (-0.05, -0.55, 1.45)), (360, (-0.20, -0.20, 1.10))):
    key(haR, 'location', f, p)
key(elR, 'location', 73, (-0.26, -0.06, 1.08)); key(elR, 'location', 79, (-0.22, -0.18, 1.20)); key(elR, 'location', 96, (-0.27, -0.10, 1.12))
key(elR, 'location', 203, (-0.22, -0.22, 1.12)); key(elR, 'location', 215, (-0.36, -0.22, 1.18)); key(elR, 'location', 245, (-0.26, -0.06, 1.08))
# --- left hand (phone root): phone into pocket 96-112, then both hands open the world 193-215
for f, p in ((1, (0.12, -0.30, 1.25)), (96, (0.12, -0.30, 1.25)), (110, (0.17, -0.14, 0.92)), (125, (0.24, -0.06, 0.95)),
             (193, (0.24, -0.06, 0.95)), (203, (0.08, -0.42, 1.30)), (215, (0.48, -0.45, 1.42)), (245, (0.24, -0.06, 0.95))):
    key(PHR, 'location', f, p)
key(phone, 'scale', 106, (1, 1, 1)); key(phone, 'scale', 112, (0, 0, 0))
key(elL, 'location', 96, (0.27, -0.08, 1.08)); key(elL, 'location', 110, (0.28, -0.04, 1.12))
key(elL, 'location', 203, (0.22, -0.22, 1.12)); key(elL, 'location', 215, (0.36, -0.22, 1.18)); key(elL, 'location', 245, (0.27, -0.06, 1.08))
# --- walk: toward camera 98-190, keeps walking through the dissolve 193-288, turns and walks sideways 289-384
key(FIG, 'location', 1, (0, 0, 0)); key(FIG, 'location', 98, (0, 0, 0)); key(FIG, 'location', 190, (0, -1.2, 0))
key(FIG, 'location', 288, (0, -2.0, 0)); key(FIG, 'location', 384, (2.0, -2.0, 0), 'LINEAR')
key(FIG, 'rotation_euler', 285, (0, 0, 0)); key(FIG, 'rotation_euler', 300, (0, 0, math.radians(70)))

# small panels rise off the screen (1-72), vanish into the pocket move
for i, dx in enumerate((-0.06, 0.0, 0.06)):
    p = box('FX_panel_small_%d' % (i+1), (0.07, 0.003, 0.05), (dx, 0, 0.01), M['panel'], parent=PHR)
    key(p, 'location', 1, (dx, 0, 0.01)); key(p, 'location', 72, (dx, 0, 0.25))
    key(p, 'scale', 1, (0.2, 0.2, 0.2)); key(p, 'scale', 24, (1, 1, 1)); key(p, 'scale', 100, (1, 1, 1)); key(p, 'scale', 108, (0, 0, 0))

# room dissolve 205-255 (triggered by his hands opening)
def dissolve(o, f0, f1):
    key(o, 'scale', f0, (1, 1, 1)); key(o, 'scale', f1, (0, 0, 0))
for o, (f0, f1) in zip(DEVICES, ((205, 232), (208, 230), (208, 230), (212, 236), (214, 240))):
    dissolve(o, f0, f1)
for o, (f0, f1) in zip(WALLS, ((222, 255), (218, 250), (218, 250))):
    dissolve(o, f0, f1)
for nm in ('ENV_bed_foreground', 'ENV_bed_foreground_base'):
    dissolve(bpy.data.objects[nm], 205, 228)
dissolve(floor, 215, 255)
key(dfloor, 'hide_render', 1, True, 'CONSTANT'); key(dfloor, 'hide_render', 205, False, 'CONSTANT')
key(dfloor, 'hide_viewport', 1, True, 'CONSTANT'); key(dfloor, 'hide_viewport', 205, False, 'CONSTANT')
S.frame_set(1)
srcs = DEVICES + WALLS
for i in range(140):
    src = srcs[i % len(srcs)]
    if src is iv: c, d = Vector((-2.0, 2.4, 0.9)), Vector((0.2, 0.2, 1.8))
    else: c, d = src.location.copy(), Vector(src.dimensions)
    pos = c + Vector(((random.random()-0.5)*d.x, (random.random()-0.5)*d.y, (random.random()-0.5)*d.z)); pos.z = max(pos.z, 0.05)
    t0 = random.randint(205, 240); t1 = t0 + random.randint(14, 22)
    pt = box('FX_particle_%03d' % i, (0.04, 0.04, 0.04), pos, M['panel'])
    key(pt, 'scale', 1, (0, 0, 0), 'CONSTANT'); key(pt, 'scale', t0, (1, 1, 1), 'LINEAR'); key(pt, 'scale', t1, (0, 0, 0))
    key(pt, 'location', t0, tuple(pos), 'LINEAR'); key(pt, 'location', t1, tuple(pos + Vector((0, 0, 2.0))))

# big panels burst out from between his hands (205-245) and settle in front of and beside him
FINALS = [(-1.3, -2.9, 1.6, -35), (-0.8, -1.2, 2.1, -10), (0.9, -1.1, 1.4, 12), (1.3, -2.8, 1.8, 35)]
BIG = []
for i, (x, y, h, rz) in enumerate(FINALS):
    s0 = 205 + 4*i; e0 = s0 + 30
    S.frame_set(s0)
    start = FIG.matrix_world @ Vector((0, -0.45, 1.32))
    fin = Vector((x, y, h))
    p = box('FX_panel_big_%d' % (i+1), (0.60, 0.005, 0.40), tuple(start), M['panel'])
    key(p, 'scale', 1, (0, 0, 0), 'CONSTANT'); key(p, 'scale', s0, (0.05, 0.05, 0.05)); key(p, 'scale', e0, (1, 1, 1))
    key(p, 'location', s0, tuple(start)); key(p, 'location', e0, tuple(fin))
    key(p, 'rotation_euler', s0, (0, 0, 0)); key(p, 'rotation_euler', e0, (0, 0, math.radians(rz)))
    BIG.append((p, fin))
for i in range(3):
    a = BIG[i][1]; b = BIG[i+1][1]; d = b - a; L = d.length
    t = cyl('FX_light_thread_%d' % (i+1), 0.005, 1.0, tuple(a), M['thread'], along_y_from0=True, seg=8)
    t.rotation_mode = 'QUATERNION'; t.rotation_quaternion = Vector((0, 1, 0)).rotation_difference(d.normalized())
    f0 = 300 + 20*i; f1 = f0 + 20
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
# 1 (0-1.2 s): macro on the stethoscope searching the screen, from his left side at screen height
c1, t1 = camera('CAM_s1_ECU_macro_85', 85)
key(c1, 'location', 1, (0.55, -0.78, 1.16)); key(c1, 'location', 29, (0.50, -0.82, 1.20)); t1.location = (0.08, -0.31, 1.26)
# 2 (1.2-3 s): fast pull-back + 30 deg arc that reveals him
c2, t2 = camera('CAM_s2_pullback_arc_50', 50)
key(c2, 'location', 30, (0.35, -0.85, 1.30)); key(c2, 'location', 72, (-0.90, -2.30, 1.45))
key(t2, 'location', 30, (0.08, -0.30, 1.30)); key(t2, 'location', 72, (0, 0, 1.45))
# 3a (3-5.5 s): he removes the stethoscope, pockets the phone, walks toward the backing camera
c3, t3 = camera('CAM_s3a_MS_walk_50', 50)
t3.parent = FIG; t3.location = (0, 0, 1.55)
key(c3, 'location', 73, (-0.5, -2.0, 1.6)); key(c3, 'location', 132, (0.05, -2.75, 1.55))
# 3b (5.5-8 s): low 3/4 close from the right, travelling with him
c3b, t3b = camera('CAM_s3b_MCU_low34_85', 85)
c3b.parent = FIG; t3b.parent = FIG; t3b.location = (0, 0, 1.62)
key(c3b, 'location', 133, (1.40, -1.45, 1.22)); key(c3b, 'location', 192, (1.20, -1.30, 1.28))
# 4 (8-12 s): he opens his hands, the world bursts out; camera orbits from front-left to front-right and lifts
c4, t4 = camera('CAM_s4_orbit_35', 35)
t4.parent = FIG; t4.location = (0, 0, 1.3)
key(c4, 'location', 193, (-1.6, -3.4, 1.1)); key(c4, 'location', 240, (-0.2, -4.3, 1.4)); key(c4, 'location', 288, (1.5, -4.4, 1.7))
# 5 (12-16 s): side tracking with his walk, panel 4 wipes across the lens
c5, t5 = camera('CAM_s5_MS_track_50', 50)
t5.parent = FIG; t5.location = (0, 0, 1.4)
key(c5, 'location', 289, (-0.4, -4.0, 1.4), 'LINEAR'); key(c5, 'location', 384, (1.9, -4.0, 1.45), 'LINEAR')
for i, c in enumerate((c1, c2, c3, c3b, c4, c5)):
    noise(c, 0.03, 10*i + 1)
S.camera = c1
S.timeline_markers.clear()
for nm, fr, c in (('CUT1', 1, c1), ('CUT2', 30, c2), ('CUT3a', 73, c3), ('CUT3b', 133, c3b), ('CUT4', 193, c4), ('CUT5', 289, c5)):
    mk = S.timeline_markers.new(nm, frame=fr); mk.camera = c

for nm, typ, loc, en in (('LGT_key', 'SUN', (2, -3, 5), 3.0), ('LGT_fill', 'POINT', (-2, -2, 2.5), 150.0)):
    ld = bpy.data.lights.new(nm, typ); ld.energy = en
    lo = link(bpy.data.objects.new(nm, ld)); lo.location = loc
    if typ == 'SUN': lo.rotation_euler = Euler((math.radians(45), 0, math.radians(30)))
S.render.engine = 'BLENDER_WORKBENCH'
sh = S.display.shading
sh.light = 'FLAT'; sh.color_type = 'MATERIAL'
try: sh.show_object_outline = True
except Exception: pass
S.frame_set(1)
result = {"objects": len(bpy.data.objects), "markers": [(m.name, m.frame, m.camera.name) for m in S.timeline_markers]}
