from import_data import data

#Github Issue clean data

#drop columns that aren't relevant for the model training
data = data.drop(['year','usage', 'productDisplayName', 'masterCategory', 'subCategory'], axis=1)

data= data.rename(columns={'id': 'image_id'})
#selected rows that have the labels we want to keep for our training
selected_lables = ['Shirts', 'Jeans', 'Track Pants', 'Tshirts', 'Casual Shoes', 'Tops',
               'Sandals', 'Sweatshirts', 'Formal Shoes', 'Waistcoat', 'Sports Shoes', 'Shorts', 
               'Heels', 'Innerwear Vests', 'Rain Jacket', 'Dresses', 'Skirts', 'Blazers',
               'Shrug', 'Trousers', 'Jackets', 'Sports Sandals', 'Sweaters', 'Tracksuits', 
               'Leggings', 'Jumpsuit', 'Robe', 'Salwar and Dupatta', 'Kurtas', 'Sarees']

#delete rows that are not in selected_lables
data = data.loc[data["articleType"].isin(selected_lables)]

data = data.dropna()
