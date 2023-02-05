from tensorflow import keras
import numpy as np 
import os
from PIL import Image
import matplotlib.pyplot as plt

#ihr müsst das file zum predicten selbst aussuchen dass kann noch verbessert werden
file = "D:/Ablage/fashion-dataset/images/1165.jpg"
#stimmt so, muss nicht geändert werdeen
model = keras.models.load_model('model/Trained_for_Outfits.h5')

#model.summary()

#Alle bilder müssen resized werden
size = 256, 384

image = Image.open(file)
new_image = image.resize((size))
img = np.array(new_image)

i = img[None, :]

#np.reshape(img, ( 384, 256, 3)) 
p = model.predict(i)

class_names = ['Shirts', 'Jeans', 'Track Pants', 'Tshirts', 'Casual Shoes', 'Tops',
               'Sandals', 'Sweatshirts', 'Formal Shoes', 'Waistcoat', 'Sports Shoes', 'Shorts', 
               'Heels', 'Innerwear Vests', 'Rain Jacket', 'Dresses', 'Skirts', 'Blazers',
               'Shrug', 'Trousers', 'Jackets', 'Sports Sandals', 'Sweaters', 'Tracksuits', 
               'Leggings', 'Jumpsuit', 'Robe', 'Salwar and Dupatta', 'Kurtas', 'Sarees']



print(class_names[np.argmax(p[0])])