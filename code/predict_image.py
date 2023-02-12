from tensorflow import keras
import numpy as np 
import os
from PIL import Image
import matplotlib.pyplot as plt

# for example:
# file = "D:/Ablage/3920.jpg"

def predict(file):
    #directory = os.getcwd()
    model = keras.models.load_model('../model/Trained_for_Outfits.h5')
    
    #model = keras.models.load_model(directory)
    
    size = 256, 384
    
    image = Image.open(file)
    new_image = image.resize((size))
    img = np.array(new_image)
    
    i = img[None, :]
    
    p = model.predict(i)
    
    class_names = ['Blazers', 'Casual Shoes', 'Dresses', 'Formal Shoes', 'Heels', 'Innerwear Vests', 'Jackets', 'Jeans', 'Jumpsuit', 'Kurtas', 'Leggings', 'Rain Jacket', 'Robe', 'Salwar and Dupatta', 'Sandals', 'Sarees', 'Shirts', 'Shorts', 'Shrug', 'Skirts', 'Sports Sandals', 'Sports Shoes', 'Sweaters', 'Sweatshirts', 'Tops', 'Track Pants', 'Tracksuits', 'Trousers', 'Tshirts', 'Waistcoat']
    
    return class_names[np.argmax(p[0])]