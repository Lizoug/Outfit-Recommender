import random

# Categorize the clothing items
jackets = ["Waistcoat", "Rain Jacket",
           "Blazers", "Shrug", "Jackets",
           "Kurtas", "Sarees"]

top = ["Shirts", "Tshirts", "Tops",
       "Sweatshirts", "Innerwear Vests",
       "Sweaters", "Tracksuits", "Jumpsuit",
       "Robe", "Salwar and Dupatta"]

bottom = ["Jeans", "Track Pants",
          "Dresses", "Skirts",
          "Trousers", "Leggings"]

shoes = ["Casual Shoes", "Sandals",
         "Formal Shoes", "Sports Shoes",
         "Heels"]

colors = ["White", "Black", "Red",
          "Green", "Blue", "Yellow",
          "Magenta", "Cyan", "Maroon",
          "Olive", "Navy", "Yellow Green",
          "Purple", "Teal", "Orange",
          "Violet", "Mint Green", "Lime Green",
          "Pink", "Light Blue", "Gray",
          "Light Gray", "Dark Gray",
          "Lavender", "Mustard", "Seafoam",
          "Olive Drab"]


def clothing_item_is_in(clothes_list, clothing_item):
    """ Checks if clothing list already contains the clothing item"""
    # Get the first layer of clothes_list
    for first_layer_clothes_list in clothes_list:
        # Get the second layer of clothes_list
        for second_layer_clothes_list in first_layer_clothes_list:
            # Get each value of clothing item
            for clothing_value in clothing_item:
                # Check if value is in clothing_list
                if clothing_value == second_layer_clothes_list:
                    return True
    return False


def color_in_clothes(clothes_list, color):
    """ Checks if clothes_list already contains the color"""
    for clothes_value in clothes_list:
        if color == clothes_value[1]:
            return True
    return False


def get_clothes(cloth, color):
    """ Returns a set of clothes with colors,
        matching with the clothing item of the user"""
    clothes_list = [[cloth, color]]
    # Execute three times for three clothing items
    for i in range(3):
        # Blue is just our placeholder
        col = "Blue"
        actual_list = []
        # Checks if clothing item is in chothes list and chooses it
        if not clothing_item_is_in(clothes_list, jackets):
            actual_list = jackets
        elif not clothing_item_is_in(clothes_list, top):
            actual_list = top
        elif not clothing_item_is_in(clothes_list, bottom):
            actual_list = bottom
        else:
            actual_list = shoes

        # Setting a random clothing item from choosed category
        random_cloth = actual_list[random.randint(0, len(actual_list)-1)]
        # Continues throwing out random color until the color is not already in clothes
        while color_in_clothes(clothes_list, col):
            col = colors[random.randint(0, len(colors)-1)]
        # Add clothes item and its color to clothes_list
        clothes_list.append([random_cloth, col])
    return clothes_list
