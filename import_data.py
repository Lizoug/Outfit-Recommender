import os
import pandas as pd
from tensorflow import keras
from feature_lable_type import lable_article, images
import numpy as np


#path = os.getcwd()

# load data
path_csv = "/Users/lizak/OneDrive/Desktop/myntradataset"
path_image = "/Users/lizak/OneDrive/Desktop/myntradataset/images/"

def create_dataset(path_image, path_csv):

    data = pd.read_csv(path_csv+"/styles.csv",error_bad_lines = False)
    
    #Github Issue clean data
    
    #drop columns that aren't relevant for the model training
    data = data.drop(['year','usage', 'productDisplayName', 'masterCategory', 'subCategory'], axis=1)
    
    data= data.rename(columns={'id': 'image_id'})
    #selected rows that have the labels we want to keep for our training
    selected_lables = ['Shirts', 'Jeans', 'Track Pants', 'Tshirts', 'Casual Shoes', 'Tops',
                   'Sandals', 'Sweatshirts', 'Formal Shoes', 'Waistcoat', 'Sports Shoes', 'Shorts', 
                   'Heels', 'Innerwear Vests', 'Rain Jacket', 'Dresses', 'Skirts', 'Blazers',
                   'Shrug', 'Trousers', 'Jackets', 'Sports Sandals', 'Sweaters', 'Tracksuits', 
                   'Leggings', 'Jumpsuit', 'Robe', 'Salwar and Dupatta', 'Kurtas', 'Sarees']
    
    #delete rows that are not in selected_lables
    data = data.loc[data["articleType"].isin(selected_lables)]
    
    data = data.dropna()
    
    df = pd.DataFrame({"lable": lable_article})
    lables_one_hot_encoded = pd.get_dummies(df['lable'])

    images_to_numpy = np.array(images)

    lables_one_hot_encoded_to_numpy = lables_one_hot_encoded.to_numpy()

    from sklearn.model_selection import train_test_split

    #train-test-split
    X_train, X_test, y_train, y_test = train_test_split(images_to_numpy,
                                                        lables_one_hot_encoded_to_numpy,
                                                        test_size=0.2,
                                                        random_state=0, shuffle=True)

    X_train, X_test = X_train / 255.0, X_test / 255.0
    
    return X_train, X_test, y_train, y_test
