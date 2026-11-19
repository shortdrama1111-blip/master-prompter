"""Shot 5 final render: gift pyramid with the red holiday bags, DreamDuo and Hair Oil; a small gift drops on top.

Layout, drop and camera follow previz.py shot5 (1.67 s, 40 frames, FOV 34, push-in 15 cm); look from
final_common.py. Products are only the client's references: red bag (print from the photo), DreamDuo
box, Hair Oil bottle and box. The wrapped gifts are set dressing in cream, champagne and soft gold
paper with red satin ribbon, as in the brief.
  Blender -b --factory-startup --python shot5_final.py -- OUTDIR [still|test|full]
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import final_common as F
from final_common import bpy, Vector

N = 40


def paper(name, rgb, rough, metal=0.0, sheen=0.0):
    """Wrapping paper: fine fibre bump so it reads as paper, not plastic."""
    m, bsdf, nt = F.principled(name)
    bsdf.inputs["Base Color"].default_value = (*rgb, 1)
    bsdf.inputs["Roughness"].default_value = rough
    bsdf.inputs["Metallic"].default_value = metal
    try:
        bsdf.inputs["Sheen Weight"].default_value = sheen
    except Exception:
        pass
    noise = nt.nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 900.0
    noise.inputs["Detail"].default_value = 6.0
    bump = nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.12
    bump.inputs["Distance"].default_value = 0.0004
    nt.links.new(noise.outputs["Fac"], bump.inputs["Height"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    return m


PAPERS = [paper("paper_cream", (0.86, 0.82, 0.76), 0.70),            # cool cream so it stays cream under 3200K
          paper("paper_champagne", (0.62, 0.50, 0.34), 0.38, metal=0.55),
          paper("paper_gold", (0.70, 0.52, 0.28), 0.32, metal=0.75)]
M_DROP = paper("paper_drop", (0.88, 0.85, 0.80), 0.65)

F.box("floor", (8, 8, 0.02), (0, 0, -0.01), F.M_ROOM)
F.box("backwall", (8, 0.02, 4.0), (0, 1.6, 2.0), F.M_ROOM)


def soft_box(name, size, loc, mat, parent, bevel=0.004):
    """Box with rounded edges: wrapped corners catch a thin highlight instead of a hard CG edge."""
    bm = F.bmesh.new()
    F.bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co = Vector((v.co.x * size[0], v.co.y * size[1], v.co.z * size[2]))
    F.bmesh.ops.bevel(bm, geom=list(bm.edges), offset=bevel, segments=3, profile=0.5, affect="EDGES")
    for f in bm.faces:
        f.smooth = True
    o = F.mesh_obj(name, bm, mat, parent, smooth_sides=False)
    o.location = loc
    try:
        o.data.shade_auto_smooth()
    except Exception:
        pass
    return o


def bow(parent, z, size=1.0):
    """Satin bow: two flat ribbon loops and two short tails, knot in the middle."""
    for a in (30, -150):
        pts = []
        for i in range(25):
            t = 2 * math.pi * i / 24
            pts.append((0.045 * size * (1 - math.cos(t)) / 2, 0, z + 0.028 * size * math.sin(t) * 0.9 + 0.004))
        lp = F.ribbon_strip(pts, 0.03 * size, F.M_SATIN_RED, parent, "bow_loop")
        lp.rotation_euler = (math.radians(18), 0, math.radians(a))
        lp.location.z = 0
    for a in (60, -120):
        pts = [(0.05 * size * i / 6, 0, z - 0.0005 * i) for i in range(7)]
        tl = F.ribbon_strip(pts, 0.026 * size, F.M_SATIN_RED, parent, "bow_tail")
        tl.rotation_euler = (0, 0, math.radians(a))
    soft_box("bow_knot", (0.022 * size, 0.022 * size, 0.014 * size), (0, 0, z + 0.006), F.M_SATIN_RED, parent, 0.004)


def gift(size, base, mat, rz=0.0):
    """Wrapped gift on its base, crossed with red satin ribbon and a satin bow on top."""
    w, d, h = size
    e = F.link(bpy.data.objects.new("gift", None))
    e.location, e.rotation_euler = base, (0, 0, math.radians(rz))
    soft_box("paper", (w, d, h), (0, 0, h / 2), mat, e)
    soft_box("ribbon_x", (0.032, d + 0.003, h + 0.003), (0, 0, h / 2), F.M_SATIN_RED, e, 0.002)
    soft_box("ribbon_y", (w + 0.003, 0.032, h + 0.003), (0, 0, h / 2), F.M_SATIN_RED, e, 0.002)
    bow(e, h + 0.002, min(1.0, max(0.6, w / 0.2)))
    return e


# pyramid sized for 9:16: the previz pile was 1.3 m wide and only 0.6 m fits the vertical frame, so
# the gifts shrink to about 60% and the real products (true size) come forward and read larger.
for i, (x, w, d, rz) in enumerate([(-0.22, 0.22, 0.22, -4), (0.02, 0.24, 0.24, 3), (0.25, 0.20, 0.22, -2)]):
    gift((w, d, 0.20), (x, 0, 0), PAPERS[i % 3], rz)
for i, (x, w, rz) in enumerate([(-0.11, 0.20, 6)]):
    gift((w, 0.18, 0.17), (x, 0.02, 0.20), PAPERS[(i + 1) % 3], rz)
gift((0.16, 0.15, 0.14), (0.0, 0.03, 0.37), PAPERS[2], -7)
b1 = F.bag(0.5)
b1.location, b1.rotation_euler = (0.14, 0.02, 0.20), (0, 0, math.radians(10))   # second-row right, beside the top gift
b2 = F.bag(0.7)
b2.location, b2.rotation_euler = (-0.26, -0.25, 0), (0, 0, math.radians(-16))
dd = F.duo_box()
dd.location, dd.rotation_euler = (0.0, -0.22, 0.095), (math.radians(-10), 0, math.radians(6))
F.oil_box((0.12, -0.24, 0), None)
oe = F.link(bpy.data.objects.new("oil_e", None))
oe.location = (0.19, -0.33, 0)
F.oil_bottle((0, 0, 0), oe)
drop = gift((0.10, 0.10, 0.08), (0.0, 0.03, 0.51), M_DROP, 12)
rest_z = drop.location.z

F.area("Key", (-1.0, -1.8, 1.0), (0.0, -0.1, 0.30), 1.6, 90, F.KEY)
F.area("TopWash", (0.0, -0.4, 2.4), (0.0, 0.0, 0.5), 2.0, 70, F.LED)
F.area("WallGlow", (0.0, 1.0, 0.3), (0.0, 1.6, 1.2), 1.5, 30, F.LED)
F.area("Rim", (1.3, 0.6, 1.2), (0.0, 0.0, 0.5), 1.0, 40, F.LED)


def update(t):
    if t < 0.40:
        s = t / 0.40
        drop.location.z = rest_z + 0.30 * (1 - s * s)
    else:
        drop.location.z = rest_z + 0.012 * math.exp(-12 * (t - 0.40)) * abs(math.sin(25 * (t - 0.40)))
    s = min(max(t / 1.667, 0), 1)
    s = s * s * (3 - 2 * s)
    F.aim((0.0, -1.75 + 0.15 * s, 0.36), (0.0, 0, 0.30), 34)


F.render(update, N, "shot5")
