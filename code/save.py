import predict_image as image
import return_color as color
import pandas as pd

def save_data(file):
    clothing = image.predict(file)
    cloth_color = color.get_color(file)
    return clothing, cloth_color
    