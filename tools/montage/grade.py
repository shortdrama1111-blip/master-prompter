import sys, numpy as np
from PIL import Image
im=np.asarray(Image.open(sys.argv[1]).convert('RGB')).astype(np.float32)/255
# 1) lift shadows/midtones (gamma-ish curve, protect highlights)
lum=im.mean(axis=2,keepdims=True)
lift=0.13*(1-lum)**2*np.clip(lum*3,0,1)
im=np.clip(im+lift*(1-im)*1.0,0,1)
# 2) desaturate yellow/orange cast proportional to darkness (shadows got the cast)
import colorsys
r,g,b=im[...,0],im[...,1],im[...,2]
mx=im.max(2); mn=im.min(2); l=(mx+mn)/2
gray=im.mean(2,keepdims=True)
warm=np.clip((r-b)-0.12,0,1)[...,None]   # amount of warm cast beyond cream
k=np.clip(warm*2.2,0,0.55)
im=im*(1-k)+ (gray*np.array([1.06,1.02,0.93]))*k  # pull toward neutral cream
# 3) slight global cool to 5600K neutral
im=im*np.array([0.985,1.0,1.035])
im=np.clip((im-0.03)/0.97,0,1)
Image.fromarray((np.clip(im,0,1)*255).astype(np.uint8)).save(sys.argv[2])
