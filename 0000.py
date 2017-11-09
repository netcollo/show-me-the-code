#!/usr/bin/env python
import sys

from PIL import Image, ImageDraw, ImageFont
im = Image.open("./img/avatar.jpg")
print(im)
draw = ImageDraw.Draw(im)
font = ImageFont.truetype(font=r"C:\Windows\Fonts\arial.ttf", size=40)

#draw.line((0,0) + im.size, fill=128)
#draw.line((0, im.size[1], im.size[0], 0), fill=128)
draw.text((im.size[0]*0.8, 10), "4", fill="#ff000000",font=font)

im.show()