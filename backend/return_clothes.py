import pandas as pd
import random

jackets = ['Waistcoat', 'Rain Jacket', 'Blazers', 'Shrug', 'Jackets', 'Kurtas', 'Sarees']

top = ['Shirts', 'Tshirts', 'Tops', 'Sweatshirts', 'Innerwear Vests', 'Sweaters', 
       'Tracksuits', 'Jumpsuit', 'Robe', 'Salwar and Dupatta']

bottom = ['Jeans', 'Track Pants', 'Dresses', 'Skirts', 'Trousers', 'Leggings']

shoes = ['Casual Shoes', 'Sandals', 'Formal Shoes', 'Sports Shoes', 'Heels']

def get_clothes(name):
    df = pd.read_csv('../data/data.csv', sep=';', header=None, index_col=None)
    df.columns = ['ID', 'clothing', 'color']
    clothes = []
    
    for i in range(3):
        actual_list = []
        actual_cloth = df['clothing'][df['ID'] == name].iloc[0]
        actual_color = df['color'][df['ID'] == name].iloc[0]
        actual_name = df[df['ID'] == name]
        
        df.drop(actual_name.index, inplace = True, errors='ignore')
        df.drop(df[df['color'] == actual_color].index, inplace = True, errors='ignore')
        
        if actual_cloth in jackets:
            actual_list = jackets
        elif actual_cloth in top:
            actual_list = top
        elif actual_cloth in bottom:
            actual_list = bottom
        else:
            actual_list = shoes
            
            
        for v in actual_list:
            df.drop(df[df['clothing'] == v].index, inplace = True, errors='ignore')
    
        if not df.empty:
            r = random.randint(0,len(df)-1)
            clothes.append(df['ID'].iloc[r])
            name = df['ID'].iloc[r]
            
        else:
            print("not enough data please put in more images")
            break
    return clothes

x = get_clothes('hose')

print(x)