from tensorflow import keras
import numpy as np 
import os
from PIL import Image
import matplotlib.pyplot as plt

def predict(file):
    """ Prediction of the clothing items of the images."""

    # Loading the model from keras
    model = keras.models.load_model('../model/Trained_for_Outfits.h5')
    
    # Set the sizes for our prediction
    size = 256, 384
    
    # Resize the image
    image = Image.open(file)
    # Resize the image
    new_image = image.resize((size))
    # Convert image to numpy array
    img = np.array(new_image)
    # Setting the array to the shape of our model
    i = img[None, :]
    
    # Return predictions for image
    p = model.predict(i)
    
    class_names = ['Blazers', 'Casual Shoes', 'Dresses', 'Formal Shoes', 'Heels', 'Innerwear Vests', 'Jackets', 'Jeans', 'Jumpsuit', 'Kurtas', 'Leggings', 'Rain Jacket', 'Robe', 'Salwar and Dupatta', 'Sandals', 'Sarees', 'Shirts', 'Shorts', 'Shrug', 'Skirts', 'Sports Sandals', 'Sports Shoes', 'Sweaters', 'Sweatshirts', 'Tops', 'Track Pants', 'Tracksuits', 'Trousers', 'Tshirts', 'Waistcoat']
    # Returns the value which was predicted with class_names
    return class_names[np.argmax(p[0])]
