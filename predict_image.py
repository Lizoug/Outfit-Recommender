from tensorflow import keras
import numpy as np 
import os
from PIL import Image
import matplotlib.pyplot as plt

file = "D:/Ablage/3920.jpg"
model = keras.models.load_model('C:/VM/HSD/Outfit-Recommender/model/Trained_for_Outfits3.h5')

#model.summary()

size = 256, 384



# wo ihr die daten extrahiert habt... normalerweise unter Downloads 
start_path = "D:/Ablage/fashion-dataset/images"


image = Image.open(file)
new_image = image.resize((size))
img = np.array(new_image)

i = img[None, :]

p = model.predict(i)

class_names = ['Blazers', 'Casual Shoes', 'Dresses', 'Formal Shoes', 'Heels', 'Innerwear Vests', 'Jackets', 'Jeans', 'Jumpsuit', 'Kurtas', 'Leggings', 'Rain Jacket', 'Robe', 'Salwar and Dupatta', 'Sandals', 'Sarees', 'Shirts', 'Shorts', 'Shrug', 'Skirts', 'Sports Sandals', 'Sports Shoes', 'Sweaters', 'Sweatshirts', 'Tops', 'Track Pants', 'Tracksuits', 'Trousers', 'Tshirts', 'Waistcoat']
print(class_names[np.argmax(p[0])])
print(np.argmax(p[0]))
print(p[0])