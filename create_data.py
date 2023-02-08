import os
import pandas as pd
from tensorflow import keras
import numpy as np
import glob
from PIL import Image
import numpy as np 
from sklearn.model_selection import train_test_split

def create_dataset(path_csv):
    data = pd.read_csv(path_csv+"/styles.csv",error_bad_lines = False)
    
    
    # Issue clean data
    
    data = data.drop(['year','usage', 'productDisplayName', 'masterCategory', 'subCategory'], axis=1)
    
    data = data.rename(columns={'id': 'image_id'})
    
    class_names = ['Shirts', 'Jeans', 'Track Pants', 'Tshirts', 'Casual Shoes', 'Tops',
                   'Sandals', 'Sweatshirts', 'Formal Shoes', 'Waistcoat', 'Sports Shoes', 'Shorts', 
                   'Heels', 'Innerwear Vests', 'Rain Jacket', 'Dresses', 'Skirts', 'Blazers',
                   'Shrug', 'Trousers', 'Jackets', 'Sports Sandals', 'Sweaters', 'Tracksuits', 
                   'Leggings', 'Jumpsuit', 'Robe', 'Salwar and Dupatta', 'Kurtas', 'Sarees']
    
    #delete rows that are not in class_names
    data = data.loc[data["articleType"].isin(class_names)]
    
    data = data.dropna()
    return data 