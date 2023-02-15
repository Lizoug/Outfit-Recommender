import numpy as np
from PIL import Image


def rgb_to_color_name(r, g, b):
    """ Gets what color the rgb values are"""
    # RGB-values get normalized
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # Color table
    color_list = {
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
        # (0.5, 0.5, 0.5): "Gray", We threw it out because it causes errors
        (0.65, 0.65, 0.65): "Light Gray",
        (0.25, 0.25, 0.25): "Dark Gray",
        (0.6, 0.2, 0.8): "Lavender",
        (0.8, 0.6, 0.2): "Mustard",
        (0.2, 0.8, 0.6): "Seafoam",
        (0.4, 0.4, 0.0): "Olive Drab",
    }

    # Find the most similar color of table list
    # Set a float variable
    min_distance = float("inf")
    most_similar_color = None
    # Redo for every color in color_names
    for rgb_value, color_item in color_list.items():
        # Calculate how similar the RGB value fits to our colors in color_list
        similarity = ((r - rgb_value[0]) ** 2 + (g - rgb_value[1]) ** 2 + (b - rgb_value[2]) ** 2) ** 0.5
        # Check if similarity of value is higher and change the value or of its lower and let the value be
        if similarity < most_similarity:
            most_similarity = similarity
            most_similar_color = color_item

    return most_similar_color


def get_color(file):
    """ Gets the RGB value of clothes and derives theis color"""
    # sets arrays for RGBs we want to get
    rl = np.zeros([90, 96])
    gl = np.zeros([90, 96])
    bl = np.zeros([90, 96])
    # Set the sizes for our IMAGE
    size = 256, 384

    # Load the image
    image = Image.open(file)
    # Resize the image
    new_image = image.resize((size))
    # Convert image to numpy array
    img = np.array(new_image)
    # chooses the coordinates in the image, where we want to get the RGB values from
    img = img[70:160, 80:-80]

    # gets separate lists for R, G and B
    for i in range(0, 90):
        for j in range(0, 90):
                rl[i][j] = img[i][j][0]
                gl[i][j] = img[i][j][1]
                bl[i][j] = img[i][j][2]

    # Calculates the mean to get only one last number for each list
    r = int(np.mean(rl))
    g = int(np.mean(gl))
    b = int(np.mean(bl))

    # Gets what color the rgb values are
    color = rgb_to_color_name(r, g, b)
    return color
