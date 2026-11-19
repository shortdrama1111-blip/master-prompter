# Kopje e lëvizjeve të kamerës nga camera-ref.mp4, 1.2–3.0s, zgjatur në ~2.5s.
# 1) fisheye në tokë, ajo ngre këmbën mbi lente  2) plan i gjerë statik  3) punch-in 3 hapa  4) detaj: duart tërheqin xhaketën mbi sup
import bpy, math, sys, os
from mathutils import Vector
OUT=sys.argv[-1]; FPS=24
def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True); s=bpy.context.scene
    s.render.engine='CYCLES'; s.cycles.device='CPU'; s.cycles.samples=4; s.cycles.use_denoising=False; s.cycles.max_bounces=2
    s.render.resolution_x,s.render.resolution_y=720,1280; s.render.fps=FPS; s.render.image_settings.file_format='PNG'
    w=bpy.data.worlds.new('w'); w.use_nodes=True; w.node_tree.nodes['Background'].inputs[0].default_value=(0.8,0.82,0.85,1); s.world=w
    sun=bpy.data.lights.new('sun','SUN'); sun.energy=3; so=bpy.data.objects.new('sun',sun); so.rotation_euler=(math.radians(55),0,math.radians(-35)); bpy.context.collection.objects.link(so)
    return s
def mat(n,rgb):
    m=bpy.data.materials.new(n); m.use_nodes=True; b=m.node_tree.nodes['Principled BSDF']; b.inputs['Base Color'].default_value=(*rgb,1); b.inputs['Roughness'].default_value=0.8; return m
def box(loc,size,m,rot=(0,0,0)):
    bpy.ops.mesh.primitive_cube_add(location=loc,rotation=rot); o=bpy.context.object; o.scale=(size[0]/2,size[1]/2,size[2]/2); o.data.materials.append(m); return o
def cyl(loc,r,d,m,rot=(0,0,0)):
    bpy.ops.mesh.primitive_cylinder_add(radius=r,depth=d,location=loc,rotation=rot); o=bpy.context.object; o.data.materials.append(m); return o
def env():
    g=mat('g',(0.55,0.55,0.56)); kerb=mat('k',(0.45,0.45,0.46)); wall=mat('w',(0.7,0.68,0.64)); sh=mat('sh',(0.38,0.38,0.4))
    box((0,0,-0.05),(30,30,0.1),g); box((0,-1.2,0.05),(30,0.25,0.15),kerb)    # trotuari dhe bordura
    box((0,3.2,4),(30,0.4,8),wall)                                            # muri
    box((0,2.95,1.9),(3.6,0.1,3.8),sh)                                        # qepeni
    for z in range(0,38,2): box((0,2.88,0.1*z+0.05),(3.6,0.04,0.04),wall)     # vijat e qepenit
class Fig:
    def __init__(s):
        body=mat('b',(0.16,0.15,0.17)); skin=mat('s',(0.8,0.68,0.6)); top=mat('t',(0.9,0.9,0.88))
        s.r=bpy.data.objects.new('fig',None); bpy.context.collection.objects.link(s.r)
        def P(o,parent=None): o.parent=parent or s.r; return o
        P(cyl((0,0,1.15),0.17,0.6,top)); P(cyl((0,0,0.88),0.18,0.16,body))
        s.jacket=P(box((0,0,1.18),(0.46,0.3,0.62),body))
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.11,location=(0,0,1.62)); P(bpy.context.object).data.materials.append(skin)
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.07,location=(0,0.1,1.6)); P(bpy.context.object).data.materials.append(body)
        s.L=[];s.A=[]
        for sx in (-1,1):
            p=bpy.data.objects.new('l',None); bpy.context.collection.objects.link(p); p.parent=s.r; p.location=(sx*0.09,0,0.85)
            P(cyl((0,0,-0.42),0.065,0.84,body),p); P(box((0,-0.08,-0.84),(0.09,0.26,0.07),body),p); s.L.append(p)
            a=bpy.data.objects.new('a',None); bpy.context.collection.objects.link(a); a.parent=s.r; a.location=(sx*0.24,0,1.42)
            P(cyl((0,0,-0.3),0.045,0.6,skin),a); s.A.append(a)
    def key(s,f,loc=(0,0,0),yaw=0,legs=(0,0),arms=((0,0,0),(0,0,0))):
        s.r.location=loc; s.r.rotation_euler=(0,0,yaw); s.r.keyframe_insert('location',frame=f); s.r.keyframe_insert('rotation_euler',frame=f)
        for p,v in zip(s.L,legs): p.rotation_euler=(v,0,0); p.keyframe_insert('rotation_euler',frame=f)
        for p,v in zip(s.A,arms): p.rotation_euler=v; p.keyframe_insert('rotation_euler',frame=f)
def setcam(c,kind,fov=47,lens_fish=180):
    if kind=='fish':
        c.data.type='PANO'
        try: c.data.panorama_type='FISHEYE_EQUISOLID'
        except Exception: c.data.cycles.panorama_type='FISHEYE_EQUISOLID'
        try: c.data.fisheye_fov=math.radians(lens_fish); c.data.fisheye_lens=10.5
        except Exception: pass
    else:
        c.data.type='PERSP'; c.data.sensor_fit='VERTICAL'; c.data.angle_y=math.radians(fov)
def look(o,t): o.rotation_euler=(Vector(t)-o.location).to_track_quat('-Z','Y').to_euler()

s=reset(); env(); fig=Fig()
cd=bpy.data.cameras.new('c'); cd.clip_start=0.01; c=bpy.data.objects.new('cam',cd); bpy.context.collection.objects.link(c); s.camera=c
DUR=2.5; N=round(DUR*FPS)
# kohët (s): fisheye 0–0.85 · gjerë 0.85–1.35 · punch-in 1.35–1.53–1.71–1.9 · detaj 1.9–2.5
markers=[]
for i in range(N):
    t=i/FPS; f=i+1
    if t<0.85:   # 1) fisheye në tokë; ajo afrohet, pastaj ngre këmbën e djathtë lart mbi lente
        setcam(c,'fish'); c.location=(0.05,-0.15,0.07); look(c,(0,0.9,1.5))
        y=max(0.45,1.5-1.6*t); k=max(0,(t-0.3)/0.55); kick=-math.sin(min(1,k)*math.pi*0.85)*2.0
        fig.key(f,(0,y,0),0,legs=(0.25*math.sin(t*9),kick),arms=((0.3,0,0.2),(0.3,0,-0.2)))
    elif t<1.35:  # 2) plan i gjerë statik, kamera në lartësi gjuri, ajo qëndron para qepenit
        setcam(c,'p',47); c.location=(0.05*math.sin(t*5),-3.6,0.6); look(c,(0,1.6,1.05))
        fig.key(f,(0,1.6,0),0)
    elif t<1.9:   # 3) punch-in: tre hapa në të njëjtin aks
        st=0 if t<1.53 else (1 if t<1.71 else 2)
        fov,dist,h,tz=[(47,3.6,0.6,1.05),(29,3.0,0.75,1.1),(18,2.6,0.9,1.25)][st]
        setcam(c,'p',fov); c.location=(0,1.6-dist,h); look(c,(0,1.6,tz))
        fig.key(f,(0,1.6,0),0,arms=((0.1,0,0.1),(0.1,0,-0.1)))
    else:         # 4) detaj: kamera në dorë afër supit; duart tërheqin xhaketën mbi sup
        setcam(c,'p',29); k=(t-1.9)/0.6
        c.location=(0.45+0.02*math.sin(t*9),1.6-0.95,1.42+0.015*math.sin(t*13)); look(c,(0.12,1.6,1.45))
        fig.key(f,(0,1.6,0),math.radians(-15),arms=((-2.4*min(1,k*1.5),0,0.3),(-2.0*min(1,k*1.5),0,-0.4)))
    c.keyframe_insert('location',frame=f); c.keyframe_insert('rotation_euler',frame=f)
    if c.data.type=='PERSP': c.data.keyframe_insert('lens',frame=f)
FISH_END=round(0.85*FPS)
for a,b,kind in [(1,FISH_END,'fish'),(FISH_END+1,N,'p')]:
    setcam(c,kind)
    s.frame_start,s.frame_end=a,b; s.render.filepath=os.path.join(OUT,'f_')
    bpy.ops.render.render(animation=True)
