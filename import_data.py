import os
import pandas as pd
from tensorflow import keras

#path = os.getcwd()
        
path_csv = "/Users/lizak/OneDrive/Desktop/myntradataset"
path_image = "/Users/lizak/OneDrive/Desktop/myntradataset/images/"

print(os.listdir(path_csv))

data = pd.read_csv(path_csv+"/styles.csv",error_bad_lines = False)
