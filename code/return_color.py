

from webcolors import rgb_to_name
import numpy as np 
import os
from PIL import Image
import matplotlib.pyplot as plt

# for example:
# file = "D:/Ablage/hose.jpg"

def rgb_to_color_name(r, g, b):
    # RGB-Werte normalisieren
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # Farbnamen-Tabelle
    color_names = {
        (1.0, 1.0, 1.0): "White",
        (0.0, 0.0, 0.0): "Black",
        (1.0, 0.0, 0.0): "Red",
        (0.0, 1.0, 0.0): "Green",
        (0.0, 0.0, 1.0): "Blue",
        (1.0, 1.0, 0.0): "Yellow",
        (1.0, 0.0, 1.0): "Magenta",
        (0.0, 1.0, 1.0): "Cyan",
        (0.5, 0.0, 0.0): "Maroon",
        (0.0, 0.5, 0.0): "Olive",
        (0.0, 0.0, 0.5): "Navy",
        (0.5, 0.5, 0.0): "Yellow Green",
        (0.5, 0.0, 0.5): "Purple",
        (0.0, 0.5, 0.5): "Teal",
        (1.0, 0.5, 0.0): "Orange",
        (0.5, 0.0, 1.0): "Violet",
        (0.0, 1.0, 0.5): "Mint Green",
        (0.5, 1.0, 0.0): "Lime Green",
        (1.0, 0.0, 0.5): "Pink",
        (0.0, 1.0, 1.0): "Light Blue",
        #(0.5, 0.5, 0.5): "Gray",
        (0.65, 0.65, 0.65): "Light Gray",
        (0.25, 0.25, 0.25): "Dark Gray",
        (0.6, 0.2, 0.8): "Lavender",
        (0.8, 0.6, 0.2): "Mustard",
        (0.2, 0.8, 0.6): "Seafoam",
        (0.4, 0.4, 0.0): "Olive Drab",
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


def get_color(file):
    rl = np.zeros([90, 96])
    gl = np.zeros([90, 96])
    bl = np.zeros([90, 96])
    size = 256, 384 
    
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
    
    #print(r,g,b)
    color = rgb_to_color_name(r,g,b)
    return color