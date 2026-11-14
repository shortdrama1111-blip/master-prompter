# Grafika "mission passed" në stilin e lojës së 2013: brez i errët i tejdukshëm, tekst i artë me kontur të zi të trashë,
# emri i misionit poshtë me të bardhë. PNG 1080x1920 me alfa. Përdorim: python3 make_mission_v.py <dalja.png> "<emri i misionit>"
import sys, os
from PIL import Image, ImageDraw, ImageFont
OUT, NAME = sys.argv[1], sys.argv[2]; W, H = 1080, 1920; D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')
im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
CY = 640
d.rectangle((0, CY-150, W, CY+150), fill=(0, 0, 0, 120))
F = ImageFont.truetype(os.path.join(D, 'TitanOne-Regular.ttf'), 140)
while d.textlength("mission passed", font=F) > 960: F = ImageFont.truetype(os.path.join(D, 'TitanOne-Regular.ttf'), F.size-4)
d.text((W/2, CY-30), "mission passed", font=F, fill=(214, 172, 58, 255), anchor='mm', stroke_width=12, stroke_fill=(0, 0, 0, 255))
S = ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Regular.otf', 52)
d.text((W/2, CY+95), NAME, font=S, fill=(245, 245, 245, 255), anchor='mm', stroke_width=3, stroke_fill=(0, 0, 0, 200))
im.save(OUT)
