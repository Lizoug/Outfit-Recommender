from data_cleaned import data
import glob
from PIL import Image
import numpy as np 
from import_data import path_image

images = []
lable_article = []
lable_color = []

def convert_image_to_array_endlist(path_image):
    """This function takes a single argument "path_image". 
    Within the function, it uses the glob library to get 
    all the jpg images in the given path, enumerates through them,
    #extracts the image id from the filename, uses that id to find
    the corresponding entry in a dataframe, opens the image using
    the Image module and converts it to a numpy array. If the image
    shape is (80,60,3) then it appends the image and the corresponding
    article type to the 'images' and 'lable_article' lists respectively.
    It returns the 'images' and 'lable_article' lists."""
  
    
    for i, filename in enumerate(glob.glob(f'{path_image}*.jpg')):
      
        # Extract the image id from the filename
        image_id = int(filename.split('\\')[-1].split('.')[0])
        
        # Use the image id to find the corresponding entry in the 'data' dataframe 
        entry_of_dataframe_with_correct_imageid = data[data["image_id"] == image_id]
        
        # If the entry is empty, continue to the next iteration
        if entry_of_dataframe_with_correct_imageid.empty:
            continue
        
        # Open the image using the Image module and convert it to a numpy array
        im=Image.open(filename)
        im = np.array(im)

        if im.shape == (80,60,3): 
            colors_entry = entry_of_dataframe_with_correct_imageid.iloc[0,3]
            articleType_entry = entry_of_dataframe_with_correct_imageid.iloc[0,2]
            lable_article.append(articleType_entry)
            lable_color.append(colors_entry)
            images.append(im)

    return images, lable_article

convert_image_to_array_endlist(path_image)
