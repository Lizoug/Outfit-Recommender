import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
import tensorflow as tf
import os

title = st.container()
dataset = st.container()
user_interaction = st.container()
model = st.container()
junk = st.container()

directory = os.getcwd()
path_type = os.path.join(directory+"\Trained_for_Outfits3.h5")
# path_color = os.path.join(directory+"\Trained_for_Outfits4.h5")
model_type = tf.keras.models.load_model(path_type)
# model_color = tf.keras.models.load_model(path_color)
st.write("you are currently in your " + directory + " directory.")
st.write("your current path is " + path_type + ".")
# st.write(path_color)

@st.cache
def get_data(filename):
  data = pd.read_csv(filename)
  return data

col1,col2,col3,col4,col5 = st.columns(5)

if "photo" not in st.session_state:
    st.session_state["photo"]="not done"

def change_photo_state():
    st.session_state["photo"]="done"

with col3:
  with title:
    st.title("Outfit Recommender")

with col1:
    st.title("Introduction")
   
st.write("This project aims to develop an outfit recommendation system using deep learning techniques. The system will take an image from the user as input and suggest a suitable outfit for them. The model will learn to recognize patterns and features in the images, allowing it to make accurate recommendations.")

st.subheader("*Important*")
st.write("Please note the following before uploading your item")
st.markdown("* Rule 1")
st.markdown("* Rule 2")

file_input = st.file_uploader("Please upload a clothing item",on_change=change_photo_state)
camera_input = st.camera_input("Please take a photo!",on_change=change_photo_state)

progress_bar = st.progress(0)
if st.session_state["photo"] == "done":
    for perc_completed in range(100):
        time.sleep(0.01)
        progress_bar.progress(perc_completed + 1)
    st.success("Photo uploaded successfully")
    with st.expander("Click to read more"):
        st.write("here is your photo!")
        if file_input is None:
            st.image(camera_input)
        else:
            st.image(file_input)
st.write(camera_input)
st.download_button(
    label="Download image",
    data=camera_input,
    file_name="test_image.jpg"
)
st.write(type(camera_input))

size = 256, 384
class_article = ['Blazers', 'Casual Shoes', 'Dresses', 'Formal Shoes', 'Heels', 'Innerwear Vests', 'Jackets', 'Jeans',
                   'Jumpsuit', 'Kurtas', 'Leggings', 'Rain Jacket', 'Robe', 'Salwar and Dupatta', 'Sandals', 'Sarees',
                   'Shirts', 'Shorts', 'Shrug', 'Skirts', 'Sports Sandals', 'Sports Shoes', 'Sweaters', 'Sweatshirts',
                   'Tops', 'Track Pants', 'Tracksuits', 'Trousers', 'Tshirts', 'Waistcoat']

# if file_input is given, it opens,resizes,converts to array,and predicts what the file_input is
if file_input is not None:
    # To read image file buffer as a PIL Image:
    image = Image.open(file_input)

    # To convert PIL Image to numpy array:
    new_image = image.resize(size)
    img = np.array(new_image)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(f"PIL shape: {img.shape}")

    i = img[None, :]
    p = model_type.predict(i)
    st.write(class_article[np.argmax(p[0])])
    st.write(np.argmax(p[0]))
    st.write(p[0])

# if camera_input is given, it opens,resizes,converts to array,and predicts what the camera_input is
elif camera_input is not None:
    # To read image file buffer as a PIL Image:
    image = Image.open(camera_input)

    # To convert PIL Image to numpy array:
    new_image = image.resize(size)
    img = np.array(new_image)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(f"PIL shape: {img.shape}")

    i = img[None, :]
    p = model_type.predict(i)
    st.write(class_article[np.argmax(p[0])])
    st.write(np.argmax(p[0]))
    st.write(p[0])
