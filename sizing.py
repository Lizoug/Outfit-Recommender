# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:42:30 2022

@author: khan0
"""

import os
from PIL import Image

# wo ihr die daten extrahiert habt... normalerweise unter Downloads 
start_path = "D:/Ablage/fashion-dataset/images"
#wo es hin kommt damit man es pushen kann

start_file = os.listdir(start_path)

size = 256, 384

for infile in start_file:
    print(infile)
    found = "D:/Ablage/fashion-dataset/images/%s"%infile
    place = "D:/Ablage/fashion-set/images/%s"%infile
    image = Image.open(found)
    print(image)
    new_image = image.resize((size))
    new_image.save(place)