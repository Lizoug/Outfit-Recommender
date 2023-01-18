
#train-test-split
X_train, X_test, y_train, y_test = train_test_split(images_to_numpy,
                                                    lables_one_hot_encoded_to_numpy,
                                                    test_size=0.2,
                                                    random_state=0, shuffle=True,
                                                    metrics=['accuracy'])
