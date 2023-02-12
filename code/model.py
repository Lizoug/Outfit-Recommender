from tensorflow import keras


def cnn_clothing_type(X_train, y_train, X_test, y_test):
    """trains a cnn to determine which type of clothing
    item is given into to neural network"""

    # all dimensions are used except for batch size
    inputs = keras.Input(shape=X_train.shape[1:])

    # conv2D is convolutional layer
    # in the convolutional layer, single attributed are recognized (like lines, edges or shapes)
    # first number in brackets is the number of used neurons, the numbers in the next bracket define the kernel-size
    dense_layer = keras.layers.Conv2D(64, (3, 3), activation='relu')(inputs)
    # in the maxpooling layer, the size of feature maps are reduced while the characteristic
    # attributes are kept
    # the numbers in the brackets define the pooling-window
    dense_layer = keras.layers.MaxPooling2D((2, 2))(dense_layer)
    dense_layer = keras.layers.Conv2D(64, (3, 3), activation='relu')(dense_layer)
    dense_layer = keras.layers.MaxPooling2D((2, 2))(dense_layer)
    dense_layer = keras.layers.Conv2D(64, (3, 3), activation='relu')(dense_layer)
    dense_layer = keras.layers.MaxPooling2D((2, 2))(dense_layer)
    dense_layer = keras.layers.Conv2D(64, (3, 3), activation='relu')(dense_layer)
    dense_layer = keras.layers.MaxPooling2D((2, 2))(dense_layer)

    # in the flatten layer, high dimensional data is converted into one vector
    dense_layer = keras.layers.Flatten()(dense_layer)

    # dense layers are used to learn high-level features from input data
    # used for processing dense, flat input data like vectors
    dense_layer = keras.layers.Dense(128, activation='relu')(dense_layer)
    # training on 30 output lables
    output_layer = keras.layers.Dense(30, activation="softmax")(dense_layer)

    # the model defines the neural network in keras and makes it ready for training and prediction
    model = keras.Model(inputs=inputs, outputs=output_layer, name="cifar_model_small")

    model.summary()

    model.compile(optimizer='adam',
                  loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    # training of the model
    history = model.fit(X_train, y_train,
                        validation_data=(X_test, y_test),
                        epochs=10)
