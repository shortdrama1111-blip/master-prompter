"""Shot 5 v4 (kuadri me afer): kutia DreamDuo bie ne qesen e kuqe. Pjesa Blender: vetem kutia, RGBA.

Plate: refs/shot5-startframe-closer-v2.jpg (1116x2000, logo e korrigjuar nga perdoruesi).
Kamera ortografike, 1 njesi = 100 px te plate-it, x djathtas, z lart (z = (2000 - y_px) / 100).
Kutia: faqja perpara nga foto reale (shot5/assets/dreamduo_front.png, drita e plate-it), materiale emission.
Fizika: renie me graviteti real (qesja 513 px ~ 32 cm -> 1 njesi = 6.24 cm, g = 157 u/s^2),
goditje, dy kercime te vogla, anim 14 -> 0 dhe rrotullim 8 -> 0 gjate renies, lekundje e shuar pas goditjes.

blender -b --factory-startup -P shot5/box_blender.py
Dalja: shot5/box/b####.png + shot5/box/timing.txt (frame-i i goditjes)
"""
import os, math
import bpy

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)
PLATE = os.path.join(PROJ, 'refs', 'shot5-startframe-closer-v2.jpg')
PW, PH = 1116, 2000
FPS, NF = 24, 72

# kutia ne plate (faqja perpara) per teksturen
TEX_BOX = (695, 1255, 960, 1680)          # x0, y0, x1, y1
SIDE_RGB = (0.80, 0.62, 0.53)             # ane e kutise, pak me e erret se perpara
TOP_RGB = (0.93, 0.78, 0.69)

# v4b: faqja perpara nga foto reale e kutise (refs/dreamduo-v2.jpg), e drejtuar dhe me driten e plate-it
FRONT = os.path.join(HERE, 'assets', 'dreamduo_front.png')   # 560x770
BW = 2.8; BH = BW * 770 / 560; BD = 0.95
X_PX = 480.0                              # qendra e kutise mbi qesen
RIM_Y = 678.0                             # buza e qeses te kjo x
SINK = 0.42                               # pjesa e kutise poshte buzes ne fund (titulli mbetet jashte)
G = 157.0
V0 = 3.0
F_DROP = 5


def z_of(y_px):
    return (PH - y_px) / 100.0


def emission(name, rgb=None, img=None, uv_rect=None):
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; nt.nodes.clear()
    out = nt.nodes.new('ShaderNodeOutputMaterial'); em = nt.nodes.new('ShaderNodeEmission')
    nt.links.new(em.outputs['Emission'], out.inputs['Surface'])
    if img is not None:
        t = nt.nodes.new('ShaderNodeTexImage'); t.image = img; t.extension = 'EXTEND'
        nt.links.new(t.outputs['Color'], em.inputs['Color'])
    else:
        em.inputs['Color'].default_value = (*rgb, 1)
    return m


def build_box():
    bpy.ops.mesh.primitive_cube_add(size=1)
    ob = bpy.context.active_object; ob.name = 'dreamduo'
    ob.scale = (BW, BD, BH); bpy.ops.object.transform_apply(scale=True)
    bpy.ops.object.modifier_add(type='BEVEL'); ob.modifiers['Bevel'].width = 0.02; ob.modifiers['Bevel'].segments = 2
    img = bpy.data.images.load(FRONT)
    front = emission('front', img=img); side = emission('side', SIDE_RGB); top = emission('top', TOP_RGB)
    for m in (side, front, top):
        ob.data.materials.append(m)
    me = ob.data; uvl = me.uv_layers.active.data
    x0, y0, x1, y1 = TEX_BOX
    for p in me.polygons:
        if p.normal.y < -0.9:
            p.material_index = 1
            for li in p.loop_indices:
                v = me.vertices[me.loops[li].vertex_index].co
                uvl[li].uv = (v.x / BW + 0.5, v.z / BH + 0.5)
        elif p.normal.z > 0.9:
            p.material_index = 2
        else:
            p.material_index = 0
    return ob


def motion():
    """kthen per cdo frame (z_qendra, anim_y_deg, rrotullim_z_deg) dhe frame-in e goditjes."""
    z_end = z_of(RIM_Y + (SINK - 0.5) * BH * 100)
    z0 = z_of(-BH * 100 / 2 - 25)                  # e gjitha mbi kuadrin
    d = z0 - z_end
    t_fall = (-V0 + math.sqrt(V0 * V0 + 2 * G * d)) / G
    v_imp = V0 + G * t_fall
    # kercimet: lartesi 0.32 u (2 cm) dhe 0.08 u (0.5 cm)
    bounces = []
    for h in (0.32, 0.08):
        tb = 2 * math.sqrt(2 * h / G)
        bounces.append((h, tb))
    out = []
    t_drop = (F_DROP - 1) / FPS
    for f in range(1, NF + 1):
        t = (f - 1) / FPS - t_drop
        if t < 0:
            out.append((z0, 14.0, 8.0)); continue
        if t < t_fall:
            z = z0 - (V0 * t + 0.5 * G * t * t)
            p = t / t_fall
            ease = 1 - (1 - p) ** 2
            out.append((z, 14.0 * (1 - ease), 8.0 * (1 - ease))); continue
        tt = t - t_fall
        z = z_end
        for h, tb in bounces:
            if tt < tb:
                v = math.sqrt(2 * G * h)
                z = z_end + v * tt - 0.5 * G * tt * tt
                break
            tt -= tb
        ta = t - t_fall
        rock = 2.2 * math.exp(-ta / 0.18) * math.sin(2 * math.pi * 5.5 * ta)
        out.append((z, rock, 0.0))
    f_imp = F_DROP + t_fall * FPS
    return out, f_imp, v_imp


def main():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    for eng in ('BLENDER_EEVEE', 'BLENDER_EEVEE_NEXT'):
        try:
            sc.render.engine = eng; break
        except TypeError:
            continue
    sc.render.film_transparent = True
    sc.view_settings.view_transform = 'Standard'; sc.view_settings.look = 'None'
    sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = PW, PH, 100
    sc.render.fps = FPS; sc.frame_start, sc.frame_end = 1, NF
    sc.render.use_motion_blur = True; sc.render.motion_blur_shutter = 0.5
    sc.render.image_settings.file_format = 'PNG'; sc.render.image_settings.color_mode = 'RGBA'
    sc.eevee.taa_render_samples = 16
    w = bpy.data.worlds.new('W'); sc.world = w
    cd = bpy.data.cameras.new('cam'); cd.type = 'ORTHO'; cd.sensor_fit = 'VERTICAL'; cd.ortho_scale = PH / 100
    cam = bpy.data.objects.new('cam', cd); sc.collection.objects.link(cam)
    cam.location = (PW / 200, -20, PH / 200); cam.rotation_euler = (math.radians(90), 0, 0); sc.camera = cam
    box = build_box()
    frames, f_imp, v_imp = motion()
    for f, (z, tilt, yaw) in enumerate(frames, start=1):
        box.location = (X_PX / 100, 0, z)
        box.rotation_euler = (0, math.radians(tilt), math.radians(yaw))
        box.keyframe_insert('location', frame=f); box.keyframe_insert('rotation_euler', frame=f)
    os.makedirs(os.path.join(HERE, 'box'), exist_ok=True)
    with open(os.path.join(HERE, 'box', 'timing.txt'), 'w') as fh:
        fh.write(f'{f_imp:.3f} {v_imp:.2f}\n')
    print('impact frame', round(f_imp, 2), 'v', round(v_imp, 2))
    sc.render.filepath = os.path.join(HERE, 'box', 'b####')
    bpy.ops.render.render(animation=True)


main()
