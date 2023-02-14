from tensorflow import keras
import numpy as np
from PIL import Image


def predict(file):
    """ Prediction of colors.
        This code is for further purposes, since we
        are not predicting colors at the moment"""

    # Loading the model from keras
    model = keras.models.load_model('../model/color_model.h5')

    # Set the sizes for our prediction
    size = 60, 80

    # Load the image
    image = Image.open(file)
    # Resize the image
    new_image = image.resize((size))
    # Convert image to numpy array
    img = np.array(new_image)
    # Setting the array to the shape of our model
    i = img[None, :]

    # Return predictions for image
    p = model.predict(i)

    class_names = ['Navy Blue', 'Blue', 'Silver', 'Black', 'Grey', 'Green',
                   'Purple', 'White', 'Beige', 'Brown', 'Bronze', 'Teal',
                   'Copper', 'Pink', 'Off White', 'Maroon', 'Red', 'Khaki',
                   'Orange', 'Coffee Brown', 'Yellow', 'Charcoal', 'Gold',
                   'Steel', 'Tan', 'Multi', 'Magenta', 'Lavender', 'Sea Green',
                   'Cream', 'Peach', 'Olive', 'Skin', 'Burgundy',
                   'Grey Melange', 'Rust', 'Rose', 'Lime Green', 'Mauve',
                   'Turquoise Blue', 'Metallic', 'Mustard', 'Taupe', 'Nude',
                   'Mushroom Brown', 'Fluorescent Green']

    # Returns the value
    return class_names[np.argmax(p[0])]
