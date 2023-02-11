import predict_image as image
import return_color as color
import pandas as pd

def save_data(filename):
    file = f"../data/images/{filename}.jpg"
    clothing = image.predict(file)
    cloth_color = color.get_color(file)
    d = {'ID': [filename], 'clothing': [clothing], 'color': [cloth_color]}
    df = pd.DataFrame(data=d)
    df.to_csv('../data/data.csv', sep=';', mode='a', header=False, index=False)
    