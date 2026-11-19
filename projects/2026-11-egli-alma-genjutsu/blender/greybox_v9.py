# Grey-box previz v9 (prompt 32): lëvizje reale kamere 1.5 m/s me paralaks, ajo ndryshon pozë vetëm kur kamera lëviz. python3 greybox_v9.py OUTDIR
import bpy, math, sys, os
from mathutils import Vector
OUT = sys.argv[-1]
FPS = 24
W, H = 720, 1280
V = 1.25  # 4.5 km/h

def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    s = bpy.context.scene
    s.render.engine = 'CYCLES'
    s.cycles.device = 'CPU'
    s.cycles.samples = 4
    s.cycles.use_denoising = False
    s.cycles.max_bounces = 2
    s.render.use_motion_blur = False
    s.render.resolution_x, s.render.resolution_y = W, H
    s.render.fps = FPS
    s.render.image_settings.file_format = 'PNG'
    w = bpy.data.worlds.new('w'); w.use_nodes = True
    w.node_tree.nodes['Background'].inputs[0].default_value = (0.8,0.82,0.85,1)
    w.node_tree.nodes['Background'].inputs[1].default_value = 0.8
    s.world = w
    sun = bpy.data.lights.new('sun','SUN'); sun.energy = 3.0
    so = bpy.data.objects.new('sun', sun); so.rotation_euler = (math.radians(50), 0, math.radians(-40)); bpy.context.collection.objects.link(so)
    return s

def mat(name, rgb):
    m = bpy.data.materials.new(name); m.use_nodes = True
    m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (*rgb, 1)
    m.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value = 0.8
    return m

def box(loc, size, m):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    o = bpy.context.object; o.scale = (size[0]/2, size[1]/2, size[2]/2); o.data.materials.append(m); return o

def cyl(loc, r, d, m, rot=(0,0,0)):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=d, location=loc, rotation=rot)
    o = bpy.context.object; o.data.materials.append(m); return o

def env(kind):
    g = mat('ground', (0.55,0.55,0.56)); wall = mat('wall', (0.72,0.70,0.66)); dark = mat('dark', (0.35,0.35,0.37))
    box((0,0,-0.05),(40,120,0.1),g)
    if kind in ('street','boutique'):
        for sx in (-1,1):
            box((sx*5.5,0,8),(1,120,16),wall)
            for y in range(-55,56,4):
                box((sx*4.95,y,3 if kind=='street' else 2), (0.1,1.6,2.6 if kind=='street' else 3.4), dark)
        if kind=='street':
            bpy.ops.mesh.primitive_uv_sphere_add(radius=6, location=(0,60,14)); bpy.context.object.data.materials.append(wall)
    if kind=='portico':
        for y in range(-42,43,3):
            cyl((-1.6,y+0.5,2.6),0.25,5.2,wall)
        box((-1.6,0,5.4),(0.8,90,0.4),wall); box((1.5,0,6.5),(6,90,0.4),wall); box((-6,0,4),(1,90,8),wall); box((14,0,7),(4,90,14),wall)
    if kind=='arno':
        box((3.2,0,0.5),(0.5,120,1.0),wall)   # parapet right
        box((-6,0,5),(1,120,10),wall)
        box((20,40,3),(30,4,1),wall)          # bridge far

class Fig:
    """Kukull gri me ecje të thjeshtë; ecën drejt -Y (drejt kamerës)."""
    def __init__(s):
        body = mat('body',(0.18,0.18,0.2)); skin = mat('skin',(0.8,0.68,0.6))
        s.root = bpy.data.objects.new('fig', None); bpy.context.collection.objects.link(s.root)
        def part(o): o.parent = s.root; return o
        s.torso = part(cyl((0,0,1.15),0.17,0.6,body))
        s.hip = part(cyl((0,0,0.85),0.18,0.12,body))
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.11, location=(0,0,1.62)); s.head = part(bpy.context.object); s.head.data.materials.append(skin)
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.07, location=(0,0.1,1.6)); part(bpy.context.object).data.materials.append(body)  # bun
        s.legs=[]; s.arms=[]
        for sx in (-1,1):
            piv = bpy.data.objects.new('lp',None); bpy.context.collection.objects.link(piv); piv.parent=s.root; piv.location=(sx*0.09,0,0.85)
            l = cyl((0,0,-0.42),0.065,0.84,body); l.parent=piv; s.legs.append(piv)
            ap = bpy.data.objects.new('ap',None); bpy.context.collection.objects.link(ap); ap.parent=s.root; ap.location=(sx*0.22,0,1.42)
            a = cyl((0,0,-0.3),0.045,0.6,skin); a.parent=ap; s.arms.append(ap)
    def key(s, f, pos, phase, walk=1.0, yaw=0.0, arms=None):
        s.root.location = pos; s.root.rotation_euler = (0,0,yaw)
        s.root.keyframe_insert('location', frame=f); s.root.keyframe_insert('rotation_euler', frame=f)
        sw = math.sin(phase)*0.45*walk
        for i,p in enumerate(s.legs):
            p.rotation_euler=(sw*(1 if i else -1),0,0); p.keyframe_insert('rotation_euler', frame=f)
        for i,p in enumerate(s.arms):
            p.rotation_euler=(arms[i] if arms else -sw*0.7*(1 if i else -1),0,0); p.keyframe_insert('rotation_euler', frame=f)

def cam(fov_v):
    c = bpy.data.cameras.new('c'); c.sensor_fit='VERTICAL'; c.angle_y = math.radians(fov_v); c.clip_start=0.02
    o = bpy.data.objects.new('cam', c); bpy.context.collection.objects.link(o); bpy.context.scene.camera=o; return o

def look(o, target):
    d = Vector(target) - o.location
    o.rotation_euler = d.to_track_quat('-Z','Y').to_euler()

def render_shot(name, kind, dur, fn):
    s = reset(); env(kind); fig = Fig(); n = round(dur*FPS)
    c = cam(47)
    for i in range(n):
        t = i/FPS; f = i+1
        fn(t, f, fig, c)
        c.keyframe_insert('location', frame=f); c.keyframe_insert('rotation_euler', frame=f)
        c.data.keyframe_insert('lens', frame=f)
    s.frame_start, s.frame_end = 1, n
    s.render.filepath = os.path.join(OUT, name, 'f_')
    bpy.ops.render.render(animation=True)
    return n

def fov(c, deg): c.data.angle_y = math.radians(deg)
def walkpos(y0, t, v=V): return (0, y0 - v*t, 0)
PH = 2*math.pi/1.1   # një cikël ecjeje = 1.1 s (hapi 0.55 s)

# ---- SHOTS ----  ajo qëndron te (0,0) me fytyrë drejt -Y; kamera në -Y
def ease(u): u=min(1,max(0,u)); return u*u*(3-2*u)
def take(t,f,fig,c,kind):
    # kohët brenda take-it 8 s: 0–1.5 close, 1.5–3.5 tërhiqet, 3.5–5 wide, 5–6.5 afrohet poshtë, 6.5–8 mesatar
    d1,d2,d3=1.0,4.5,1.8
    h1,h2=(1.6,1.35); h3=0.95 if kind=='boutique' else 0.6
    if t<1.5: d,x,h,pose=d1,0,h1,0
    elif t<3.5: u=ease((t-1.5)/2); d,x,h,pose=d1+(d2-d1)*u,-1.0*u,h1+(h2-h1)*u,u
    elif t<5.0: d,x,h,pose=d2,-1.0,h2,1
    elif t<6.5: u=ease((t-5)/1.5); d,x,h,pose=d2+(d3-d2)*u,-1.0+0.8*u,h2+(h3-h2)*u,1+u
    else: d,x,h,pose=d3,-0.2,h3,2
    # pozat: 0 drejt, 1 e mbështetur (anon), 2 boutique=përkulet përpara / portico=ulur
    if pose<=1: z=0; tilt=-0.12*pose; arms=(-0.4*(1-pose),-0.2)
    else:
        k=pose-1
        if kind=='boutique': z=0; tilt=-0.12+0.5*k; arms=(-0.6*k,-0.3)
        else: z=-0.55*k; tilt=-0.12+0.3*k; arms=(-0.9*k,-1.2*k)
    fig.key(f,(0,0,z),0,0.0,arms=arms); fig.root.rotation_euler=(tilt,0,0); fig.root.keyframe_insert('rotation_euler',frame=f)
    fov(c,63*0+54); c.location=(x,-d,h); look(c,(0,0,max(0.5,h-0.05+z*0.5)))
def fg(kind):
    m=mat('fg',(0.5,0.5,0.52))
    if kind=='boutique':
        box((0,0.35,3),(8,0.3,6),mat('wallb',(0.62,0.6,0.57))); box((-1.0,-1.2,2),(0.6,0.6,4),m)   # mur + shtylla para
    else:
        cyl((0.35,0.2,2.6),0.25,5.2,m); cyl((-1.0,-2.0,2.6),0.25,5.2,m)                      # kolona e saj + kolona më afër
def outfit2(t,f,fig,c): take(t,f,fig,c,'boutique')
def outfit3(t,f,fig,c): take(t,f,fig,c,'portico')
SHOTS=[('o2','boutique',8.0,outfit2),('o3','portico',8.0,outfit3)]
_orig_env=env
def env(kind): _orig_env(kind); fg(kind)
only=os.environ.get('ONLY')
for name,kind,dur,fn in SHOTS:
    if only and name not in only.split(','): continue
    render_shot(name,kind,dur,fn)
