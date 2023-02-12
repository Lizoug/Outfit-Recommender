import pandas as pd
import random

jackets = ['Waistcoat', 'Rain Jacket', 'Blazers', 'Shrug', 'Jackets', 'Kurtas', 'Sarees']

top = ['Shirts', 'Tshirts', 'Tops', 'Sweatshirts', 'Innerwear Vests', 'Sweaters', 
       'Tracksuits', 'Jumpsuit', 'Robe', 'Salwar and Dupatta']

bottom = ['Jeans', 'Track Pants', 'Dresses', 'Skirts', 'Trousers', 'Leggings']

shoes = ['Casual Shoes', 'Sandals', 'Formal Shoes', 'Sports Shoes', 'Heels']

colors =  ["White", "Black", "Red", "Green", "Blue", "Yellow", "Magenta", "Cyan",
           "Maroon", "Olive", "Navy", "Yellow Green", "Purple", "Teal", "Orange",
           "Violet", "Mint Green", "Lime Green", "Pink", "Light Blue", "Gray", 
           "Light Gray", "Dark Gray", "Lavender", "Mustard", "Seafoam", "Olive Drab",]

def is_in(a,b):
    for i in a:
        for j in i:
            for k in b:
                if k == j:
                    return True
    return False

def in_in(a,b):
    for i in a:
        if b == i[1]:
            return True
    return False


def get_clothes(cloth, color):
    clothes = [[cloth,color]]
    for i in range(3):
        col = "Blue"
        actual_list = []
        if not is_in(clothes, jackets):
            actual_list = jackets
        elif not is_in(clothes, top):
            actual_list = top
        elif not is_in(clothes, bottom):
            actual_list = bottom
        else:
            actual_list = shoes
        clothe = actual_list[random.randint(0,len(actual_list)-1)]
        while in_in(clothes, col):
            col = colors[random.randint(0,len(colors)-1)]
        clothes.append([clothe, col])
    return clothes
