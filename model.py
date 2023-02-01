import pandas as pd
from feature_lable import lable_article, images
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt

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

#used dimensions of all used vectors except for batch size
inputs = keras.Input(shape=X_train.shape[1:])
#conv2D is convertional layer
#used rather small number for filters for trial if code works
dense_layer = keras.layers.Conv2D(50, (3, 3), activation='relu')(inputs)
dense_layer = keras.layers.MaxPooling2D((2, 2))(dense_layer)
dense_layer = keras.layers.Conv2D(50, (3, 3), activation='relu')(dense_layer)
dense_layer = keras.layers.MaxPooling2D((2, 2))(dense_layer)
dense_layer = keras.layers.Flatten()(dense_layer)
dense_layer = keras.layers.Dense(50, activation='relu')(dense_layer)
#training on 30 output lables
output_layer = keras.layers.Dense(30, activation="softmax")(dense_layer)

model = keras.Model(inputs=inputs, outputs=output_layer, name="cifar_model_small")

model.summary()


model.compile(optimizer='adam',
              loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

#only used 10 epochs for trial if code works
history = model.fit(X_train, y_train, epochs=10)