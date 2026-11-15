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
S.frame_start = 1; S.frame_end = 456
S.render.resolution_x = 1080; S.render.resolution_y = 1920; S.render.resolution_percentage = 100
if S.world is None: S.world = bpy.data.worlds.new('WORLD_navy')
S.world.color = hexcol('#0B1626')[:3]
try:
    S.world.use_nodes = True
    bg = S.world.node_tree.nodes.get('Background')
    if bg: bg.inputs['Color'].default_value = hexcol('#0B1626'); bg.inputs['Strength'].default_value = 1.0
except Exception: pass
S.view_settings.view_transform = 'Standard'


# ---------- digital space (block B) ----------
dfloor = box('ENV_floor_digital', (40, 40, 0.02), (2, 0, -0.013), M['dfloor'])
grid_mat = mat('MAT_grid', '#2EE6D6', emit=True)
for i in range(-10, 21):
    box('ENV_grid_x_%d' % i, (0.01, 30, 0.002), (i * 1.0, 0, 0.001), grid_mat)
for j in range(-15, 16):
    box('ENV_grid_y_%d' % j, (40, 0.01, 0.002), (2, j * 1.0, 0.001), grid_mat)
for k, (x, y) in enumerate(((-3, 9), (8, 10), (2, 14), (12, 6), (-6, 4))):
    box('ENV_light_column_%d' % k, (0.25, 0.25, 12), (x, y, 6), grid_mat)
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


phone = bpy.data.objects['PROP_phone']; phone.scale = (0, 0, 0)
st_mat = mat('MAT_stethoscope', '#111111')
bm = bmesh.new(); bmesh.ops.create_circle(bm, cap_ends=False, segments=24, radius=0.11)
ring = mesh_obj('PROP_steth_ring', bm, st_mat, parent=FIG, loc=(0, -0.02, 1.43)); ring.modifiers.new('skin', 'SKIN')

# figure walks along +X (faces +X: rotation 90 deg), panels on his left (+Y)
key(FIG, 'rotation_euler', 1, (0, 0, math.radians(90)))
key(FIG, 'location', 1, (0, 0, 0), 'LINEAR'); key(FIG, 'location', 205, (3.9, 0, 0)); key(FIG, 'location', 215, (4.0, 0, 0))
key(FIG, 'rotation_euler', 212, (0, 0, math.radians(90))); key(FIG, 'rotation_euler', 222, (0, 0, math.radians(180)))   # turns to the shield (+Y)
key(FIG, 'rotation_euler', 266, (0, 0, math.radians(180))); key(FIG, 'rotation_euler', 280, (0, 0, 0))                  # turns to camera (-Y)
# PHR is the LEFT hand driver (phone hidden in pocket). Local coords: -Y = his front, +X = his left side.
for f, p in ((1, (0.24, -0.06, 0.95)), (40, (0.24, -0.06, 0.95)), (55, (0.55, -0.20, 1.40)), (70, (0.24, -0.06, 0.95)),
             (88, (0.24, -0.06, 0.95)), (101, (0.55, -0.15, 1.38)), (115, (0.30, -0.10, 1.05)), (126, (0.30, -0.10, 1.05)),
             (134, (0.55, -0.25, 1.45)), (150, (0.24, -0.06, 0.95)), (180, (0.24, -0.06, 0.95)), (196, (0.45, -0.30, 1.30)), (212, (0.24, -0.06, 0.95)),
             (330, (0.24, -0.06, 0.95)), (345, (0.42, -0.30, 1.20)), (370, (0.24, -0.06, 0.95))):
    key(PHR, 'location', f, p)
# right hand: gestures while talking, stethoscope from neck onto the shield (226-262), gestures to camera
for f, p in ((1, (-0.24, -0.15, 1.02)), (30, (-0.18, -0.30, 1.22)), (60, (-0.24, -0.15, 1.02)), (160, (-0.15, -0.32, 1.25)), (190, (-0.24, -0.15, 1.02)),
             (221, (-0.24, -0.15, 1.02)), (230, (-0.05, -0.10, 1.40)), (240, (0.0, -0.62, 1.45)), (262, (0.0, -0.62, 1.45)), (272, (-0.05, -0.12, 1.38)),
             (285, (-0.24, -0.15, 1.02)), (300, (-0.18, -0.35, 1.25)), (320, (-0.24, -0.15, 1.02)), (380, (-0.15, -0.32, 1.25)), (420, (-0.24, -0.15, 1.02))):
    key(haR, 'location', f, p)
chest = cyl('PROP_steth_chestpiece', 0.022, 0.012, (0, 0, 0), M['dev'], parent=haR)
key(chest, 'scale', 1, (0, 0, 0), 'CONSTANT'); key(chest, 'scale', 228, (1, 1, 1), 'CONSTANT'); key(chest, 'scale', 274, (0, 0, 0), 'CONSTANT')

# exhibition panels (portrait 0.6 x 0.9, face -Y toward his path)
def panel(name, loc, rz=0):
    p = box(name, (0.60, 0.006, 0.90), loc, M['panel']); p.rotation_euler = (0, 0, math.radians(rz)); return p
P_IG = panel('FX_panel_instagram', (1.1, 0.75, 1.5))
P_WA = panel('FX_panel_whatsapp', (2.2, 0.75, 1.5))
P_AD = panel('FX_panel_ads', (3.2, 0.75, 1.5))
P_SH = panel('FX_panel_shield', (4.0, 0.75, 1.45))
for p, f in ((P_IG, 55), (P_WA, 101), (P_AD, 134)):      # glow pulse when touched
    key(p, 'scale', f - 4, (1, 1, 1)); key(p, 'scale', f + 2, (1.12, 1.12, 1.12)); key(p, 'scale', f + 12, (1, 1, 1))
key(P_SH, 'scale', 240, (1, 1, 1)); key(P_SH, 'scale', 246, (1.1, 1.1, 1.1)); key(P_SH, 'scale', 256, (1, 1, 1))
key(P_SH, 'scale', 268, (1, 1, 1)); key(P_SH, 'scale', 276, (0, 0, 0))   # shield splits into cards
# 16 lesson cards: burst from the shield (270-290), orbit him in a ring (290-350), converge into an infinity sign behind him (351-400)
C = Vector((4.0, 0.0, 1.4)); SHP = Vector((4.0, 0.75, 1.45))
for i in range(16):
    cd = box('FX_card_%02d' % (i + 1), (0.16, 0.004, 0.22), tuple(SHP), M['panel'])
    key(cd, 'scale', 1, (0, 0, 0), 'CONSTANT'); key(cd, 'scale', 270, (0.2, 0.2, 0.2)); key(cd, 'scale', 290, (1, 1, 1))
    key(cd, 'location', 270, tuple(SHP))
    for f in range(290, 352, 6):
        a = 2 * math.pi * i / 16 + math.radians(60) * (f - 290) / 24.0
        key(cd, 'location', f, (C.x + 1.3 * math.cos(a), C.y + 1.3 * math.sin(a), C.z + 0.15 * math.sin(3 * a)))
        key(cd, 'rotation_euler', f, (0, 0, a + math.pi / 2))
    t = 2 * math.pi * i / 16                                  # lemniscate of Bernoulli, 2.2 m wide, behind his head
    den = 1 + math.sin(t) ** 2
    lx = 1.1 * math.cos(t) / den; lz = 1.1 * math.sin(t) * math.cos(t) / den
    key(cd, 'location', 400, (C.x + lx, 1.4, 1.75 + lz)); key(cd, 'rotation_euler', 400, (0, 0, 0))

# ---------- cameras ----------
def camera(name, lens):
    cdat = bpy.data.cameras.new(name); cdat.lens = lens; cdat.sensor_width = 36; cdat.sensor_fit = 'AUTO'; cdat.clip_start = 0.02; cdat.clip_end = 200
    co = link(bpy.data.objects.new(name, cdat))
    tg = empty(name + '_target', (0, 0, 0))
    c = co.constraints.new('TRACK_TO'); c.target = tg; c.track_axis = 'TRACK_NEGATIVE_Z'; c.up_axis = 'UP_Y'
    return co, tg
def noise(o, strength, seed):
    for fc in fcurves_of(o):
        if fc.data_path == 'location':
            m = fc.modifiers.new('NOISE'); m.strength = strength; m.scale = 14.0; m.phase = seed + fc.array_index * 3.7
# 1: side tracking (continues block A), panels on the far side
c1, t1 = camera('CAM_B1_track_side_50', 50); t1.parent = FIG; t1.location = (0, 0, 1.45)
key(c1, 'location', 1, (-0.6, -2.5, 1.45), 'LINEAR'); key(c1, 'location', 84, (2.0, -2.5, 1.45), 'LINEAR')
# 2: behind the panel row, looking at him through the glass
c2, t2 = camera('CAM_B2_through_glass_50', 50); t2.parent = FIG; t2.location = (0, 0, 1.5)
key(c2, 'location', 85, (1.6, 1.9, 1.5), 'LINEAR'); key(c2, 'location', 168, (3.6, 1.9, 1.55), 'LINEAR')
# 3: low, in front of his path, he walks toward the lens
c3, t3 = camera('CAM_B3_low_front_35', 35); t3.parent = FIG; t3.location = (0, 0, 1.35)
key(c3, 'location', 169, (5.9, -0.9, 0.6)); key(c3, 'location', 220, (6.3, -1.3, 0.75))
# 4: three-quarter close on the stethoscope check, shield and his face
c4, t4 = camera('CAM_B4_MCU_check_85', 85)
key(c4, 'location', 221, (3.0, -0.95, 1.55)); key(c4, 'location', 268, (3.15, -0.85, 1.55)); t4.location = (4.0, 0.35, 1.5)
# 5: low orbit, opposite to the cards
c5, t5 = camera('CAM_B5_orbit_35', 35); t5.location = (4.0, 0, 1.3)
for f, ang, h in ((269, -90, 0.8), (310, -45, 1.0), (350, 0, 1.3)):
    a = math.radians(ang); key(c5, 'location', f, (4.0 + 3.2 * math.cos(a), 3.2 * math.sin(a), h))
# 6: front push-in, infinity sign forming behind his head
c6, t6 = camera('CAM_B6_pushin_50', 50); t6.location = (4.0, 0, 1.62)
key(c6, 'location', 351, (4.0, -3.0, 1.5)); key(c6, 'location', 456, (4.0, -1.7, 1.58))
for i, c in enumerate((c1, c2, c3, c4, c5, c6)):
    noise(c, 0.03, 10 * i + 3)
S.camera = c1
S.timeline_markers.clear()
for nm, fr, c in (('CUT1', 1, c1), ('CUT2', 85, c2), ('CUT3', 169, c3), ('CUT4', 221, c4), ('CUT5', 269, c5), ('CUT6', 351, c6)):
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
