# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:19:55 2023

@author: khan0
"""

from webcolors import rgb_to_name
import numpy as np 
import os
from PIL import Image
import matplotlib.pyplot as plt


rl = np.zeros([90, 96])
gl = np.zeros([90, 96])
bl = np.zeros([90, 96])


file = "D:/Ablage/hose.jpg"

size = 256, 384 



def rgb_to_color_name(r, g, b):
    # RGB-Werte normalisieren
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # Farbnamen-Tabelle
    color_names = {
        (1.0, 1.0, 1.0): "Weiß",
        (0.0, 0.0, 0.0): "Schwarz",
        (1.0, 0.0, 0.0): "Rot",
        (0.0, 1.0, 0.0): "Grün",
        (0.0, 0.0, 1.0): "Blau",
        (1.0, 1.0, 0.0): "Gelb",
        (1.0, 0.0, 1.0): "Magenta",
        (0.0, 1.0, 1.0): "Cyan",
        (0.5, 0.0, 0.0): "Bordeauxrot",
        (0.0, 0.5, 0.0): "Olivengrün",
        (0.0, 0.0, 0.5): "Dunkelblau",
        (0.5, 0.5, 0.0): "Senfgelb",
        (0.5, 0.0, 0.5): "Lila",
        (0.0, 0.5, 0.5): "Türkis",
        (1.0, 0.5, 0.0): "Orange",
        (0.5, 0.0, 1.0): "Violett",
        (0.0, 1.0, 0.5): "Mintgrün",
        (0.5, 1.0, 0.0): "Limonengrün",
        (1.0, 0.0, 0.5): "Pink",
        (0.0, 1.0, 1.0): "Hellblau",
        #(0.5, 0.5, 0.5): "Grau",
    }

    # Am nächsten liegenden Farbnamen finden
    min_distance = float("inf")
    nearest_color_name = None
    for color, name in color_names.items():
        distance = ((r - color[0]) ** 2 + (g - color[1]) ** 2 + (b - color[2]) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            nearest_color_name = name

    return nearest_color_name







image = Image.open(file)
new_image = image.resize((size))
img = np.array(new_image)

print(img.shape)
img = img[70:160,80:-80]

print(img.shape)
for i in range(0,90):
    for j in range(0,90):
        #if im[i][j][0] >= 240 and im[i][j][1] >= 240 and im[i][j][2] >= 240:
            rl[i][j] = img[i][j][0]
            gl[i][j] = img[i][j][1]
            bl[i][j] = img[i][j][2]
            
r = int(np.mean(rl))
g = int(np.mean(gl))
b = int(np.mean(bl))

print(r,g,b)
color = rgb_to_color_name(r,g,b)
print(color)