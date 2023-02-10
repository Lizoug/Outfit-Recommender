import pandas as pd
import  sys
import pytest
import os
path = os.getcwd()
sys.path.insert(1, path + "//backend")
import create_data

def test_create_dataset():
    # Create a small sample of the dataset to use in the test
    sample_data = {'image_id': [1, 2, 3, 4, 5], 'articleType': ['Shirts', 'Jeans', 'Track Pants', 'Tshirts', 'Casual Shoes'], 
                   'baseColour': ['Navy Blue', 'Blue', 'Silver', 'Black', 'Grey']}
    sample_df = pd.DataFrame(sample_data)
    
    # Pass the sample dataset to the create_dataset function
    result = create_data.create_dataset(sample_df)
    
    # Check if the image_id column is of type int
    assert result['image_id'].dtype == int
    
    # Check if the number of rows in the result is equal to the number of rows in the sample dataset
    assert result.shape[0] == sample_df.shape[0]
    
    # Check if the articleType and baseColour columns only contain values that are in the article_categories and color_names lists
    article_categories = ['Shirts', 'Jeans', 'Track Pants', 'Tshirts', 'Casual Shoes']
    color_names = ['Navy Blue', 'Blue', 'Silver', 'Black', 'Grey']
    assert set(result['articleType'].unique()).issubset(article_categories)
    assert set(result['baseColour'].unique()).issubset(color_names) 
