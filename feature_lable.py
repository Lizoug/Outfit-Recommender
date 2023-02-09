import glob
from PIL import Image
import numpy as np 
from import_data import path_image, data


images = []
lable_article = []

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
            only_entry_of_column_articleType = entry_of_dataframe_with_correct_imageid.iloc[0,2]
            lable_article.append(only_entry_of_column_articleType)
            images.append(im)

    return images, lable_article

<<<<<<< HEAD:feature_lable.py
if __name__ == '__main__':
    images, lable_article = convert_image_to_array_endlist('path_to_your_images')

=======
convert_image_to_array_endlist(path_image)
>>>>>>> fc096d6da094c6a231ec50383f8e621f30186835:feature_lable_color.py
