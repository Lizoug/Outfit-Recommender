import pandas as pd
from feature_lable import lable_article, images
import numpy as np

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