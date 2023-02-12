import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
import tensorflow as tf
import os
import save
import return_clothes


title = st.container()
dataset = st.container()
user_interaction = st.container()
model = st.container()
junk = st.container()

@st.cache
def get_data(filename):
  data = pd.read_csv(filename)
  return data

col1,col2,col3,col4,col5 = st.columns(5)

clothing = None
clothes_l = False

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
st.markdown("* The files need to be jpg files")
st.markdown("* On the pictures the clothing should take the entire place")

file_input = st.file_uploader("Please upload a clothing item:", type="jpg", on_change=change_photo_state)
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


if camera_input is not None:
    clothing, cloth_color = save.save_data(camera_input)
if file_input is not None:
    clothing, cloth_color = save.save_data(file_input)
    
def get_clothes_for_list():
    return True

if clothing is not None:
    if cloth_color is not None:
        st.write(clothing)
        st.write(cloth_color)
        clothes_l = st.button(label="return fitting clothes", on_click=get_clothes_for_list, type="secondary", disabled=False) 

if clothes_l:
    clothes_list = return_clothes.get_clothes(clothing, cloth_color)
    st.write(f"With your {clothes_list[0][1]} {clothes_list[0][0]}")
    st.write(f"a {clothes_list[1][1]} {clothes_list[1][0]} would fit perfectly.")
    st.write(f"Then you could ad {clothes_list[2][1]} {clothes_list[2][0]}")
    st.write(f"and on top of that a {clothes_list[3][1]} {clothes_list[3][0]}.")