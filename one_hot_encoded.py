df = pd.DataFrame({"lable": lable_article})
lables_one_hot_encoded = pd.get_dummies(df['lable'])

images_to_numpy = np.array(images)

lables_one_hot_encoded_to_numpy = lables_one_hot_encoded.to_numpy()
