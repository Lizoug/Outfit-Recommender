from backend.create_data import train_test
from backend.create_data import convert_image_to_array_endlist, create_dataset


def test_train_test():
    path_csv = '/Users/lizak/OneDrive/Desktop/myntradataset/styles.csv'
    path_image = "/Users/lizak/OneDrive/Desktop/myntradataset/images/"
    data = create_dataset(path_csv)
    # Test case 1: Article labels
    images, lable_article = convert_image_to_array_endlist(path_image,
                                                           data, "article")
    X_train, X_test, y_train, y_test = train_test(images,
                                                  lable_article, 'article')

    # Number of training images and labels should be equal
    assert X_train.shape[0] == y_train.shape[0]
    # Number of test images and labels should be equal
    assert X_test.shape[0] == y_test.shape[0]

    # Maximum pixel value should be 1.0
    assert X_train.max() <= 1.0
    assert X_test.max() <= 1.0


test_train_test()
