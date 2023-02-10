import pandas as pd
import sys
import os
path = os.getcwd()
sys.path.insert(1, path + "//backend")
import create_data


def test_create_dataset():
    path_csv = "test.csv"
    test_df = pd.DataFrame({'id': [1, 2, 3, 4],
                            'articleType': ['Shirts', 'Jeans',
                                            'Tshirts', 'Tops'],
                            'baseColour': ['Navy Blue', 'Silver',
                                           'Black', 'Green'],
                            'year': [2010, 2011, 2012, 2013],
                            'usage': ['Casual', 'Formal',
                                      'Party', 'Sports'],
                            'productDisplayName': ['Test1', 'Test2',
                                                   'Test3', 'Test4'],
                            'masterCategory': ['Clothing', 'Clothing',
                                               'Clothing', 'Clothing'],
                            'subCategory': ['Topwear', 'Bottomwear',
                                            'Topwear', 'Topwear']})
    test_df.to_csv(path_csv, index=False)

    result = create_data.create_dataset(path_csv)
    expected_df = pd.DataFrame({'image_id': [1, 2, 3, 4],
                                'articleType': ['Shirts', 'Jeans',
                                                'Tshirts', 'Tops'],
                                'baseColour': ['Navy Blue', 'Silver',
                                               'Black', 'Green']})
    assert result.equals(expected_df), f"Expected {expected_df} but got {result}"
    os.remove(path_csv)
