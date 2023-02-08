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

def train_test(path_image):
    df = pd.DataFrame({"lable": lable_article})
    lables_one_hot_encoded = pd.get_dummies(df['lable'])

    images_to_numpy = np.array(images)

    lables_one_hot_encoded_to_numpy = lables_one_hot_encoded.to_numpy()


    #train-test-split
    X_train, X_test, y_train, y_test = train_test_split(images_to_numpy,
                                                        lables_one_hot_encoded_to_numpy,
                                                        test_size=0.2,
                                                        random_state=0, shuffle=True)

    X_train, X_test = X_train / 255.0, X_test / 255.0
    
    return X_train, X_test, y_train, y_test


images = []
lable_article = []
def convert_image_to_array_endlist(path_image, data):
    """ This function takes a single argument "path_image". 
    Within the function, it uses the glob library to get 
    all the jpg images in the given path, enumerates through them,
    #extracts the image id from the filename, uses that id to find
    the corresponding entry in a dataframe, opens the image using
    the Image module and converts it to a numpy array. If the image
    shape is (80,60,3) then it appends the image and the corresponding
    article type to the 'images' and 'lable_article' lists respectively.
    It returns the 'images' and 'lable_article' lists."""

    
    for i,filename in enumerate(glob.glob(f'{path_image}*.jpg')): 

    	# Extract the image id from the filename
        image_id = int(filename.split('\\')[-1].split('.')[0])

        # Use the image id to find the corresponding entry in the 'data' dataframe
        entry_of_dataframe_with_correct_imageid = data[data["image_id"] == image_id]
    
    	# If the entry is empty, continue to the next iteration
        if entry_of_dataframe_with_correct_imageid.empty:
                continue

        # Open the image using the Image module and convert it to a numpy array
        image = Image.open(filename)    
        image = np.array(image)

        if image.shape == (80,60,3): 
            only_entry_of_column_articleType = entry_of_dataframe_with_correct_imageid.iloc[0,2]
            lable_article.append(only_entry_of_column_articleType)
            images.append(image)

    return images, lable_article