from tensorflow import keras
import numpy as np 
import os
from PIL import Image
import matplotlib.pyplot as plt

# forexample
#file = "D:/Ablage/13702.jpg"

def predict(file:)
    #is correct
    model = keras.models.load_model('../model/Farbe_model.h5')
    
    #model.summary()
    
    #Alle bilder müssen resized werden
    size = 60, 80
    
    image = Image.open(file)
    new_image = image.resize((size))
    img = np.array(new_image)
    
    i = img[None, :]
    
    #np.reshape(img, ( 384, 256, 3)) 
    p = model.predict(i)
    
    class_names = ['Navy Blue', 'Blue', 'Silver', 'Black', 'Grey', 'Green', 'Purple', 'White',
     'Beige', 'Brown', 'Bronze', 'Teal', 'Copper', 'Pink', 'Off White', 'Maroon',
     'Red', 'Khaki', 'Orange', 'Coffee Brown', 'Yellow', 'Charcoal', 'Gold', 'Steel',
     'Tan', 'Multi', 'Magenta', 'Lavender', 'Sea Green', 'Cream', 'Peach', 'Olive',
     'Skin', 'Burgundy', 'Grey Melange', 'Rust', 'Rose', 'Lime Green', 'Mauve',
     'Turquoise Blue', 'Metallic', 'Mustard', 'Taupe', 'Nude', 'Mushroom Brown',
     'Fluorescent Green']
    
    
    print(class_names[np.argmax(p[0])])
    
    print(p.shape)