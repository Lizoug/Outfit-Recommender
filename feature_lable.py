images = []
lable_article = []
def convert_image_to_array_endlist(path_image):
    counter = 0
    
    for filename in enumerate(glob.glob(f'{path_image}*.jpg')): 
    
        image_id = int(filename.split('\\')[-1].split('.')[0])
    
        entry_of_dataframe_with_correct_imageid = data[data["image_id"] == image_id]
    
        if entry_of_dataframe_with_correct_imageid.empty:
                continue
    
        image = Image.open(filename)    
        image = np.array(image)

        if image.shape == (80,60,3): 
            only_entry_of_column_articleType = entry_of_dataframe_with_correct_imageid.iloc[0,2]
            lable_article.append(only_entry_of_column_articleType)
            images.append(image)
        else:
            counter += 1

    return images, lable_article