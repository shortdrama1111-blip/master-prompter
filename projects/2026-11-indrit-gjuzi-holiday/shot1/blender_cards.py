"""Shot 1 v7: produktet si objekte 3D ne Blender, me driten e plate-it, te renderuara si "karta" RGBA
(produkt + hije mbi murin/raftin), qe make_shot1.py i vendos mbi kolonat qe levizin.

Ekzekutimi (bpy 5.x, python 3.11):
  <venv>/bin/python shot1/blender_cards.py [emri ...]
Dalja: shot1/assets/card_<emri>.png

Njesia: 1 = 100 px te plate-it. Kubi: gjeresi 3.54, hapi i rafteve 5.59.
"""
import sys, os, math
import numpy as np
import bpy, bmesh

HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, 'assets')

HEIGHT = {'oil': 3.40, 'box': 4.05, 'mask': 4.50, 'cond': 4.50}
COL_W = 3.54
PERIOD = 5.59
BELOW = 0.5                       # karta nis 0.5 poshte bazes
PX_PER_UNIT = float(os.environ.get('PXU', 180.6))   # 2x shkalla e daljes (0.903 * 100 * 2)
SAMPLES = int(os.environ.get('SPP', 96))
KEY = float(os.environ.get('KEY', 560))
LED = float(os.environ.get('LED', 90))


def kelvin(k):
    # perafrim RGB per temperature ngjyre
    t = k / 100.0
    r = 255 if t <= 66 else 329.7 * (t - 60) ** -0.1332
    g = 99.47 * math.log(t) - 161.12 if t <= 66 else 288.12 * (t - 60) ** -0.0755
    b = 255 if t >= 66 else (0 if t <= 19 else 138.52 * math.log(t - 10) - 305.04)
    return tuple(max(0, min(255, c)) / 255 for c in (r, g, b))


def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.render.engine = 'CYCLES'
    sc.cycles.device = 'CPU'
    sc.cycles.samples = SAMPLES
    sc.cycles.use_denoising = True
    sc.render.film_transparent = True
    sc.cycles.film_transparent_glass = True
    sc.cycles.film_transparent_roughness = 0.1
    sc.view_settings.view_transform = 'Standard'
    sc.view_settings.look = 'None'
    sc.render.image_settings.file_format = 'PNG'
    sc.render.image_settings.color_mode = 'RGBA'
    w = bpy.data.worlds.new('W'); sc.world = w
    w.use_nodes = True
    w.node_tree.nodes['Background'].inputs['Color'].default_value = (0.02, 0.014, 0.011, 1)
    w.node_tree.nodes['Background'].inputs['Strength'].default_value = 1.0
    return sc


def img(path, non_color=False):
    im = bpy.data.images.load(path)
    if non_color:
        im.colorspace_settings.name = 'Non-Color'
    return im


def mat_principled(name, color=None, tex=None, rough=0.4, spec=0.5, coat=0.0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; p = nt.nodes['Principled BSDF']
    p.inputs['Roughness'].default_value = rough
    p.inputs['Specular IOR Level'].default_value = spec
    if coat:
        p.inputs['Coat Weight'].default_value = coat
        p.inputs['Coat Roughness'].default_value = 0.08
    if tex is not None:
        t = nt.nodes.new('ShaderNodeTexImage'); t.image = tex
        t.extension = 'EXTEND'
        nt.links.new(t.outputs['Color'], p.inputs['Base Color'])
    elif color is not None:
        p.inputs['Base Color'].default_value = (*color, 1)
    return m


def lathe(name, radii, height, img_half_w_units, segs=64):
    """siperfaqe rrotullimi nga profili i rrezes (rreshti 0 = lart). UV = projeksion frontal."""
    n = len(radii)
    bm = bmesh.new()
    uv = bm.loops.layers.uv.new()
    rings = []
    for i, r in enumerate(radii):
        z = height * (1 - i / (n - 1))
        ring = []
        for s in range(segs):
            a = 2 * math.pi * s / segs
            ring.append(bm.verts.new((r * math.cos(a), -r * math.sin(a), z)))   # -y = drejt kameres
        rings.append(ring)
    def uvof(v):
        return (0.5 + v.co.x / (2 * img_half_w_units), v.co.z / height)
    for i in range(n - 1):
        for s in range(segs):
            f = bm.faces.new((rings[i][s], rings[i][(s + 1) % segs], rings[i + 1][(s + 1) % segs], rings[i + 1][s]))
            for l in f.loops:
                l[uv].uv = uvof(l.vert)
    for ring, rev in ((rings[0], False), (rings[-1], True)):
        f = bm.faces.new(ring[::-1] if rev else ring)
        for l in f.loops:
            l[uv].uv = uvof(l.vert)
    bm.normal_update()
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    for p in me.polygons:
        p.use_smooth = True
    ob = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(ob)
    # normalet e jashtme
    bpy.context.view_layer.objects.active = ob; ob.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.normals_make_consistent(inside=False); bpy.ops.object.mode_set(mode='OBJECT')
    ob.select_set(False)
    return ob


def build_bottle(kind):
    tex = img(os.path.join(A, f'{kind}_tex.png'))
    r_px = np.load(os.path.join(A, f'{kind}_radius.npy'))
    # profil i paster: mediane 31 rreshta (heq gropat nga shkrimi), pastaj buze te rrumbullakosura
    n = len(r_px); k = 15
    pad = np.pad(r_px, k, mode='edge')
    r_px = np.array([np.median(pad[i:i + 2 * k + 1]) for i in range(n)])
    rr = int(n * 0.012)
    for i in range(rr):
        f = math.sqrt(1 - (1 - (i + 0.5) / rr) ** 2)
        r_px[i] = r_px[rr] * (0.85 + 0.15 * f)
        r_px[n - 1 - i] = r_px[n - 1 - rr] * (0.85 + 0.15 * f)
    H = HEIGHT[kind]
    scale = H / len(r_px)                      # njesi per px te fotos
    idx = np.linspace(0, len(r_px) - 1, 260).astype(int)
    radii = np.maximum(r_px[idx] * scale, 0.02)
    # buzet e rrumbullakosura lart/poshte
    half_w = tex.size[0] / 2 * scale
    ob = lathe(kind, list(radii), H, half_w)
    ob.data.materials.append(mat_principled(kind, tex=tex, rough=0.38, spec=0.45, coat=0.15))
    return ob


def build_box():
    tex = img(os.path.join(A, 'box_tex.png'))
    w_px, h_px = tex.size
    H = HEIGHT['box']; W = H * w_px / h_px; D = W * 0.95
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, H / 2))
    ob = bpy.context.active_object; ob.scale = (W, D, H)
    bpy.ops.object.transform_apply(scale=True)
    bpy.ops.object.modifier_add(type='BEVEL'); ob.modifiers['Bevel'].width = 0.012; ob.modifiers['Bevel'].segments = 2
    front = mat_principled('box_front', tex=tex, rough=0.55, spec=0.35)
    side = mat_principled('box_side', color=(0.90, 0.70, 0.46), rough=0.55, spec=0.35)
    ob.data.materials.append(side); ob.data.materials.append(front)
    me = ob.data
    uvl = me.uv_layers.active.data
    for p in me.polygons:
        if p.normal.y < -0.9:                 # faqja perpara (drejt kameres, -y)
            p.material_index = 1
            for li in p.loop_indices:
                v = me.vertices[me.loops[li].vertex_index].co
                uvl[li].uv = (v.x / W + 0.5, v.z / H)
        else:
            p.material_index = 0
    return ob


def build_oil():
    tex = img(os.path.join(A, 'oil_tex.png'))
    w_px, h_px = tex.size                     # 132 x 410, qendra ne mes
    H = HEIGHT['oil']; s = H / h_px
    cap_top, cap_bot, body_bot = 6, 164, 407  # rreshta ne foto (crop nga y=470)
    cap_r = 45.5 * s
    # kapaku i zi me shkelqim
    capH = (cap_bot - cap_top) * s
    bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=cap_r, depth=capH, location=(0, 0, H - cap_top * s - capH / 2))
    cap = bpy.context.active_object; bpy.ops.object.shade_smooth()
    bpy.ops.object.modifier_add(type='BEVEL'); cap.modifiers['Bevel'].width = 0.03; cap.modifiers['Bevel'].segments = 3
    cap.data.materials.append(mat_principled('cap', color=(0.008, 0.008, 0.008), rough=0.12, spec=0.6, coat=0.6))
    # trupi prej xhami (i mbushur me vaj pa ngjyre -> xham i plote)
    bodyH = (body_bot - cap_bot) * s
    r_top, r_bot = 55.0 * s, 61.0 * s
    bpy.ops.mesh.primitive_cone_add(vertices=96, radius1=r_bot, radius2=r_top, depth=bodyH, location=(0, 0, bodyH / 2))
    body = bpy.context.active_object; bpy.ops.object.shade_smooth()
    bpy.ops.object.modifier_add(type='BEVEL'); body.modifiers['Bevel'].width = 0.04; body.modifiers['Bevel'].segments = 3
    m = bpy.data.materials.new('glass'); m.use_nodes = True
    nt = m.node_tree; nt.nodes.clear()
    out = nt.nodes.new('ShaderNodeOutputMaterial')
    glass = nt.nodes.new('ShaderNodeBsdfGlass'); glass.inputs['IOR'].default_value = 1.47; glass.inputs['Roughness'].default_value = 0.01
    ink = nt.nodes.new('ShaderNodeBsdfDiffuse'); ink.inputs['Color'].default_value = (0.01, 0.01, 0.01, 1)
    mix = nt.nodes.new('ShaderNodeMixShader')
    # maska e shkrimit nga foto: pikselet e erreta ne trup
    t = nt.nodes.new('ShaderNodeTexImage'); t.image = tex; t.extension = 'CLIP'
    tc = nt.nodes.new('ShaderNodeTexCoord')
    mp = nt.nodes.new('ShaderNodeMapping')
    # projeksion frontal ne koordinata objekti: u = 0.5 + x/(w), v = (z+bodyH/2+cap..)/H
    mp.inputs['Location'].default_value = (0.5, 0, (bodyH / 2) / H)
    mp.inputs['Scale'].default_value = (1 / (w_px * s), 0, 1 / H)
    nt.links.new(tc.outputs['Object'], mp.inputs['Vector'])
    sep = nt.nodes.new('ShaderNodeSeparateXYZ'); comb = nt.nodes.new('ShaderNodeCombineXYZ')
    nt.links.new(mp.outputs['Vector'], sep.inputs['Vector'])
    nt.links.new(sep.outputs['X'], comb.inputs['X']); nt.links.new(sep.outputs['Z'], comb.inputs['Y'])
    nt.links.new(comb.outputs['Vector'], t.inputs['Vector'])
    rgb2bw = nt.nodes.new('ShaderNodeRGBToBW'); nt.links.new(t.outputs['Color'], rgb2bw.inputs['Color'])
    ramp = nt.nodes.new('ShaderNodeValToRGB')
    ramp.color_ramp.elements[0].position = 0.35; ramp.color_ramp.elements[0].color = (1, 1, 1, 1)
    ramp.color_ramp.elements[1].position = 0.62; ramp.color_ramp.elements[1].color = (0, 0, 0, 1)
    nt.links.new(rgb2bw.outputs['Val'], ramp.inputs['Fac'])
    # vetem faqja e perparme merr shkrimin (y < 0)
    gt = nt.nodes.new('ShaderNodeMath'); gt.operation = 'LESS_THAN'; gt.inputs[1].default_value = 0.0
    nt.links.new(sep.outputs['Y'], gt.inputs[0])
    sepo = nt.nodes.new('ShaderNodeSeparateXYZ'); nt.links.new(tc.outputs['Object'], sepo.inputs['Vector'])
    nt.links.new(sepo.outputs['Y'], gt.inputs[0])
    mul = nt.nodes.new('ShaderNodeMath'); mul.operation = 'MULTIPLY'
    nt.links.new(ramp.outputs['Color'], mul.inputs[0]); nt.links.new(gt.outputs['Value'], mul.inputs[1])
    nt.links.new(mul.outputs['Value'], mix.inputs['Fac'])
    nt.links.new(glass.outputs['BSDF'], mix.inputs[1]); nt.links.new(ink.outputs['BSDF'], mix.inputs[2])
    nt.links.new(mix.outputs['Shader'], out.inputs['Surface'])
    body.data.materials.append(m)
    # tubi i bardhe i pompes
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.035, depth=bodyH * 0.9, location=(-0.08, 0.05, bodyH * 0.5))
    tube = bpy.context.active_object; tube.rotation_euler = (0, math.radians(-6), 0)
    tube.data.materials.append(mat_principled('tube', color=(0.85, 0.85, 0.85), rough=0.3))
    return body


def stage():
    """mur dhe raft si kap-hijesh, dritat e plate-it."""
    sc = bpy.context.scene
    bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 0.9, 0))
    shelf = bpy.context.active_object; shelf.scale = (COL_W, 3.0, 1); shelf.is_shadow_catcher = True
    bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 2.2, PERIOD / 2), rotation=(math.radians(90), 0, 0))
    wall = bpy.context.active_object; wall.scale = (COL_W, PERIOD + 2, 1); wall.is_shadow_catcher = True
    for m_ob in (shelf, wall):
        m_ob.data.materials.append(mat_principled('catch', color=(0.30, 0.22, 0.17), rough=0.6))
    warm = kelvin(3200); key = kelvin(float(os.environ.get('KEYK', 7500)))
    # rripi LED nen buzen e raftit siper (perpara), drejtuar poshte
    bpy.ops.object.light_add(type='AREA', location=(0, -0.9, PERIOD - 0.08))
    led = bpy.context.active_object; led.data.shape = 'RECTANGLE'; led.data.size = COL_W * 0.95; led.data.size_y = 0.05
    led.data.energy = LED; led.data.color = warm
    # shkelqimi poshte prapa (vija e ndritshme ne fund te murit), drejtuar lart
    bpy.ops.object.light_add(type='AREA', location=(0, 1.9, 0.05), rotation=(math.radians(180), 0, 0))
    back = bpy.context.active_object; back.data.shape = 'RECTANGLE'; back.data.size = COL_W * 0.95; back.data.size_y = 0.05
    back.data.energy = 90; back.data.color = warm
    # drite e bute perpara, pak mbi boshtin e kameres
    bpy.ops.object.light_add(type='AREA', location=(0, -9, 4.2))
    k = bpy.context.active_object; k.data.size = 6; k.data.energy = KEY; k.data.color = key
    k.rotation_euler = (math.radians(80), 0, 0)
    # reflektim i ngrohte nga muret anesore champagne
    for sx in (-1, 1):
        bpy.ops.object.light_add(type='AREA', location=(sx * COL_W / 2, 0.3, 2.2), rotation=(0, math.radians(90 * sx), 0))
        s = bpy.context.active_object; s.data.shape = 'RECTANGLE'; s.data.size = 2.5; s.data.size_y = 4.5
        s.data.energy = 60; s.data.color = warm
    # kamera ortografike frontale
    cam_d = bpy.data.cameras.new('cam'); cam_d.type = 'ORTHO'; cam_d.ortho_scale = PERIOD
    cam = bpy.data.objects.new('cam', cam_d); sc.collection.objects.link(cam)
    cam.location = (0, -30, -BELOW + PERIOD / 2); cam.rotation_euler = (math.radians(90), 0, 0)
    sc.camera = cam
    sc.render.resolution_x = int(round(COL_W * PX_PER_UNIT))
    sc.render.resolution_y = int(round(PERIOD * PX_PER_UNIT))
    sc.render.resolution_percentage = 100


def main():
    names = [a for a in sys.argv[1:] if not a.startswith('-')] or ['box', 'oil', 'mask', 'cond']
    for n in names:
        sc = reset()
        stage()
        {'box': build_box, 'oil': build_oil, 'mask': lambda: build_bottle('mask'), 'cond': lambda: build_bottle('cond')}[n]()
        sc.render.filepath = os.path.join(A, f'card_{n}.png')
        bpy.ops.render.render(write_still=True)
        print('ok', n, sc.render.filepath)


main()
