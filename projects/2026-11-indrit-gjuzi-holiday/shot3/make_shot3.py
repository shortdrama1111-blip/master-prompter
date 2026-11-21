"""Shot 3 v7: girlanda spirale ne Blender (Eevee), produktet rreshqasin pergjate tubit dhe dalin nga kuadri.

Plate: refs/shot3-plate-empty.jpg (muri mocha + kolona champagne, pa spirale), si plan emission
prapa skenes, i hartuar sakte ne kuadrin e kameres (xhami i tubit dhe i vajit e thyen plate-in).
Produktet: gjeometria e shot1/blender_cards.py (etiketat nga fotot reale), ne madhesi reale.
Varesja: grep unaze + zinxhir i holle champagne-gold; lekundja eshte lavjerres i simuluar.

blender -b --factory-startup -P shot3/make_shot3.py -- [--still F] [--pct 50] [--frames A-B]
Dalja: shot3/frames/f###.png (ose shot3/still_F.png)
"""
import sys, os, math, random
import bpy

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(PROJ, 'shot1'))
os.environ.setdefault('ENGINE', 'EEVEE')
import blender_cards as bc            # noqa: E402

ARGS = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []


def arg(name, default=None):
    return ARGS[ARGS.index(name) + 1] if name in ARGS else default


FPS, DUR = 30, 4.0
NF = int(FPS * DUR)
W, H = 1080, 1920
PCT = int(arg('--pct', 100))

# --- gjeometria (metra). Kamera ne (0,-CAM_D,0) shikon +y; boshti i spirales vertikal ne (AX,0) ---
CAM_D = 1.6
BG_D = 1.5                    # muri 1.5 m pas boshtit
VFOV = math.radians(float(os.environ.get('VFOV', 32)))
AX = -0.04
R = 0.27                      # rrezja e spirales
PITCH = 0.46                  # ngritja per nje rrotullim
Z_TOP, Z_BOT = 1.25, -1.35    # spiralja vazhdon jashte kuadrit lart e poshte
TUBE_R = 0.015                # tub 3 cm
SPACING = 0.18                # hapi i produkteve pergjate tubit (m)
SPEED = 0.12                  # m/s pergjate tubit, zbret
CHAIN_L = 0.05
SCALE = 0.0356                # njesite e blender_cards (1 = 100 px) -> metra: maska 4.5 -> 16 cm
G = 9.81

TURN_L = math.hypot(2 * math.pi * R, PITCH)
TOTAL_L = (Z_TOP - Z_BOT) / PITCH * TURN_L


def helix(s):
    """pika ne tub per gjatesine s nga maja (s rritet -> zbret)."""
    phi = 2 * math.pi * s / TURN_L + math.radians(110)
    return (AX + R * math.cos(phi), R * math.sin(phi), Z_TOP - PITCH * s / TURN_L), phi


def mat_metal(name, color, rough=0.22):
    m = bpy.data.materials.new(name); m.use_nodes = True
    p = m.node_tree.nodes['Principled BSDF']
    p.inputs['Base Color'].default_value = (*color, 1)
    p.inputs['Metallic'].default_value = 1.0
    p.inputs['Roughness'].default_value = rough
    return m


def clear_glass(nt, ior=1.49, base=0.06, tint=(1, 1, 1)):
    """xham per Eevee: kryesisht i tejdukshem, reflektim i forte ne buze (fresnel). Kthen node-in shader."""
    tr = nt.nodes.new('ShaderNodeBsdfTransparent'); tr.inputs['Color'].default_value = (*tint, 1)
    gl = nt.nodes.new('ShaderNodeBsdfGlossy'); gl.inputs['Roughness'].default_value = 0.04
    fr = nt.nodes.new('ShaderNodeFresnel'); fr.inputs['IOR'].default_value = ior
    add = nt.nodes.new('ShaderNodeMath'); add.operation = 'ADD'; add.use_clamp = True; add.inputs[1].default_value = base * 0.5
    nt.links.new(fr.outputs['Fac'], add.inputs[0])
    mx = nt.nodes.new('ShaderNodeMixShader')
    nt.links.new(add.outputs['Value'], mx.inputs['Fac'])
    nt.links.new(tr.outputs['BSDF'], mx.inputs[1]); nt.links.new(gl.outputs['BSDF'], mx.inputs[2])
    return mx


def mat_acrylic():
    m = bpy.data.materials.new('acrylic'); m.use_nodes = True
    nt = m.node_tree; nt.nodes.clear()
    out = nt.nodes.new('ShaderNodeOutputMaterial')
    nt.links.new(clear_glass(nt, base=0.08, tint=(0.97, 0.98, 1.0)).outputs['Shader'], out.inputs['Surface'])
    return m


def fix_oil_glass():
    """blender_cards perdor Glass BSDF (Cycles); ne Eevee e zevendesojme me xhamin e tejdukshem."""
    m = bpy.data.materials.get('glass')
    if not m:
        return
    nt = m.node_tree
    g = next(n for n in nt.nodes if n.type == 'BSDF_GLASS')
    mix_in = g.outputs['BSDF'].links[0].to_socket
    nt.links.new(clear_glass(nt, ior=1.47, base=0.05).outputs['Shader'], mix_in)
    nt.nodes.remove(g)


def setup_scene():
    sc = bc.reset()
    sc.render.film_transparent = False
    sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = W, H, PCT
    sc.render.fps = FPS
    sc.frame_start, sc.frame_end = 1, NF
    sc.render.use_motion_blur = True
    sc.render.motion_blur_shutter = 0.5
    sc.render.image_settings.color_mode = 'RGB'
    # kamera
    cd = bpy.data.cameras.new('cam'); cd.sensor_fit = 'VERTICAL'; cd.angle = VFOV
    cd.dof.use_dof = True; cd.dof.focus_distance = CAM_D - 0.12; cd.dof.aperture_fstop = 3.2
    cam = bpy.data.objects.new('cam', cd); sc.collection.objects.link(cam)
    cam.location = (0, -CAM_D, 0); cam.rotation_euler = (math.radians(90), 0, 0)
    sc.camera = cam
    # plate-i si emission, mbush sakte kuadrin ne distancen e murit
    dist = CAM_D + BG_D
    ph = 2 * dist * math.tan(VFOV / 2); pw = ph * W / H
    bpy.ops.mesh.primitive_plane_add(size=1, location=(0, BG_D, 0), rotation=(math.radians(90), 0, 0))
    bg = bpy.context.active_object; bg.scale = (pw, ph, 1)
    m = bpy.data.materials.new('plate'); m.use_nodes = True
    nt = m.node_tree; nt.nodes.clear()
    out = nt.nodes.new('ShaderNodeOutputMaterial'); em = nt.nodes.new('ShaderNodeEmission')
    t = nt.nodes.new('ShaderNodeTexImage'); t.image = bpy.data.images.load(os.path.join(PROJ, 'refs', 'shot3-plate-empty.jpg'))
    t.extension = 'EXTEND'
    nt.links.new(t.outputs['Color'], em.inputs['Color']); nt.links.new(em.outputs['Emission'], out.inputs['Surface'])
    bg.data.materials.append(m)
    bg.visible_shadow = False
    # dritat: key i bute 4000K nga lart-majtas perpara, LED 3200K i kolones nga e djathta, fill i ngrohte
    def area(name, loc, rot, size, energy, k, sy=None):
        bpy.ops.object.light_add(type='AREA', location=loc, rotation=[math.radians(a) for a in rot])
        L = bpy.context.active_object; L.name = name
        L.data.size = size; L.data.energy = energy; L.data.color = bc.kelvin(k)
        if sy:
            L.data.shape = 'RECTANGLE'; L.data.size_y = sy
        return L
    area('key', (-1.3, -1.4, 1.2), (60, 0, -40), 1.6, float(os.environ.get('KEY3', 60)), 4000)
    area('led', (0.75, 0.4, 0.0), (0, 90, 0), 0.08, float(os.environ.get('LED3', 45)), 3200, sy=2.8)
    area('fill', (0.4, -2.2, -0.3), (95, 0, 15), 2.5, float(os.environ.get('FILL3', 18)), 3600)
    return sc


def build_tube():
    cu = bpy.data.curves.new('tube', 'CURVE'); cu.dimensions = '3D'
    cu.bevel_depth = TUBE_R; cu.bevel_resolution = 6; cu.use_fill_caps = True
    sp = cu.splines.new('POLY')
    n = int(TOTAL_L / 0.02)
    sp.points.add(n)
    for i in range(n + 1):
        p, _ = helix(TOTAL_L * i / n)
        sp.points[i].co = (*p, 1)
    ob = bpy.data.objects.new('tube', cu); bpy.context.collection.objects.link(ob)
    ob.data.materials.append(mat_acrylic())


def capture(fn):
    before = set(bpy.data.objects)
    fn()
    return [o for o in bpy.data.objects if o not in before]


def build_protos(gold):
    """nje prototip per cdo produkt (+ zinxhiri), i fshehur; kopjet ndajne mesh-in."""
    protos = {}
    for name, fn in (('oil', bc.build_oil), ('box', bc.build_box),
                     ('mask', lambda: bc.build_bottle('mask')), ('cond', lambda: bc.build_bottle('cond'))):
        objs = capture(fn)
        h = bc.HEIGHT[name] * SCALE
        for o in objs:
            # shkalla reale, maja e produktit ne z=0 (varet poshte)
            o.location = (o.location.x * SCALE, o.location.y * SCALE, o.location.z * SCALE - h - CHAIN_L)
            o.scale = tuple(v * SCALE for v in o.scale)
            o.hide_render = True; o.hide_viewport = True
        protos[name] = (objs, h)
        if name == 'oil':
            fix_oil_glass()
    # zinxhiri: hallka torus te alternuara 90 grade, nga grepi poshte deri te produkti
    links = []
    n = 9; step = CHAIN_L / n
    for i in range(n):
        bpy.ops.mesh.primitive_torus_add(major_radius=step * 0.62, minor_radius=0.0006, major_segments=16, minor_segments=6,
                                         location=(0, 0, -step * (i + 0.5)),
                                         rotation=(math.radians(90), 0, math.radians(90 * (i % 2))))
        o = bpy.context.active_object; o.scale = (1, 1.45, 1); links.append(o)
    bpy.ops.object.select_all(action='DESELECT')
    for o in links:
        o.select_set(True)
    bpy.context.view_layer.objects.active = links[0]; bpy.ops.object.join()
    chain = bpy.context.active_object; chain.name = 'chain'
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    chain.data.materials.append(gold); bpy.ops.object.shade_smooth()
    chain.hide_render = True; chain.hide_viewport = True
    # grepi: unaze qe mbeshtjell tubin (boshti pergjate tangjentes)
    bpy.ops.mesh.primitive_torus_add(major_radius=TUBE_R + 0.004, minor_radius=0.0012, major_segments=24, minor_segments=8)
    hook = bpy.context.active_object; hook.name = 'hook'; hook.data.materials.append(gold); bpy.ops.object.shade_smooth()
    hook.hide_render = True; hook.hide_viewport = True
    return protos, chain, hook


def instance(proto_objs, parent):
    out = []
    for o in proto_objs:
        c = o.copy(); c.data = o.data            # mesh i ndare
        c.hide_render = False; c.hide_viewport = False
        bpy.context.collection.objects.link(c)
        c.parent = parent; out.append(c)
    return out


def simulate(rng):
    """lavjerres sferik (kendet e vogla) i nxitur nga nxitimi i pikes se varjes; dt = 1/(FPS*8)."""
    L = CHAIN_L + 0.07
    w0 = math.sqrt(G / L)
    damp = 0.35
    amp = math.radians(rng.uniform(2.5, 6.0)); ph = rng.uniform(0, 2 * math.pi)
    qx, qy = amp * math.cos(ph), amp * math.sin(ph)            # kende (rad)
    vx, vy = rng.uniform(-1, 1) * amp * w0 * 0.6, rng.uniform(-1, 1) * amp * w0 * 0.6
    return qx, qy, vx, vy, w0, damp


def main():
    rng = random.Random(7)
    sc = setup_scene()
    build_tube()
    gold = mat_metal('champagne_gold', (0.83, 0.66, 0.44))
    protos, chain, hook = build_protos(gold)
    order = ['oil', 'box', 'mask', 'oil', 'cond', 'box', 'oil', 'mask', 'box', 'cond']
    n_items = int(TOTAL_L / SPACING) + 1
    sub = 8; dt = 1.0 / (FPS * sub)
    for i in range(-4, n_items):
        kind = order[i % len(order)]
        objs, h = protos[kind]
        carrier = bpy.data.objects.new(f'car{i}', None); bpy.context.collection.objects.link(carrier)
        pend = bpy.data.objects.new(f'pen{i}', None); bpy.context.collection.objects.link(pend)
        hk = hook.copy(); hk.data = hook.data; hk.hide_render = hk.hide_viewport = False
        bpy.context.collection.objects.link(hk); hk.parent = carrier
        ch = chain.copy(); ch.data = chain.data; ch.hide_render = ch.hide_viewport = False
        bpy.context.collection.objects.link(ch); ch.parent = pend
        instance(objs, pend)
        s0 = i * SPACING
        qx, qy, vx, vy, w0, damp = simulate(rng)
        yaw0 = rng.uniform(-14, 14); yaw_a = rng.uniform(6, 14); yaw_w = 2 * math.pi / rng.uniform(2.2, 3.4); yaw_p = rng.uniform(0, 6.28)
        prev = None
        for f in range(NF + 2):
            t = (f - 1) / FPS
            s = s0 + SPEED * t                  # pa modulo: kush del poshte vazhdon jashte kuadrit
            p, phi = helix(s)
            # tangjentja horizontale -> boshti i grepit
            carrier.location = p
            carrier.rotation_euler = (0, math.radians(90), phi + math.radians(90))
            carrier.keyframe_insert('location', frame=f); carrier.keyframe_insert('rotation_euler', frame=f)
            # nxitimi centripetal i varjes (konstant ne shpejtesi konstante) + lavjerresi
            vh = SPEED * 2 * math.pi * R / TURN_L
            ac = vh * vh / R
            ax_, ay_ = -ac * math.cos(phi), -ac * math.sin(phi)
            if f > 0:
                for _ in range(sub):
                    axx = -w0 * w0 * qx - damp * vx - ax_ / (CHAIN_L + 0.07)
                    ayy = -w0 * w0 * qy - damp * vy - ay_ / (CHAIN_L + 0.07)
                    vx += axx * dt; vy += ayy * dt; qx += vx * dt; qy += vy * dt
            pend.location = (p[0], p[1], p[2] - TUBE_R - 0.004)
            yaw = math.radians(yaw0 + yaw_a * math.sin(yaw_w * t + yaw_p))
            # qx = zhvendosja e bob-it ne +x -> rrotullim rreth y negativ; qy -> rreth x pozitiv
            pend.rotation_euler = (qy, -qx, yaw)
            pend.keyframe_insert('location', frame=f); pend.keyframe_insert('rotation_euler', frame=f)
    print('items', n_items, 'tube length', round(TOTAL_L, 2))
    os.makedirs(os.path.join(HERE, 'frames'), exist_ok=True)
    still = arg('--still')
    if still:
        sc.frame_set(int(still))
        sc.render.filepath = os.path.join(HERE, f'still_{int(still):03d}.png')
        bpy.ops.render.render(write_still=True)
        print('still', sc.render.filepath)
        return
    if '--save' in ARGS:
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, 'IG_shot3.blend'))
    a, b = (arg('--frames') or f'1-{NF}').split('-')
    sc.frame_start, sc.frame_end = int(a), int(b)
    sc.render.filepath = os.path.join(HERE, 'frames', 'f###')
    bpy.ops.render.render(animation=True)


main()
