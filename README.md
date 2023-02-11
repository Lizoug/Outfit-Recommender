# *Outfit Recommendation System*
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

## Introduction
This project aims to develop an outfit recommendation system using deep learning techniques. The system will take an image from the user as input and suggest a suitable outfit for them. The model will learn to recognize patterns and features in the images, allowing it to make accurate recommendations. 

## Data
The model will be trained on a dataset of images.

The dataset can be downloaded from Kaggle:<br> 
https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset

Or the smaller dataset:<br>
https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small

## Model
The model will be implemented using deep learning techniques such as convolutional neural networks (CNNs). The CNNs will be used to extract features from the images and the final layers will be trained for the task of outfit recommendation.

## Usage
The system can be used by using this system, users will be able to upload a photo of a clothing and receive outfit suggestions.

## Dependencies<br> 
* Python 3.x<br> 
* TensorFlow 2.x or PyTorch<br> 
* OpenCV<br> 
* Numpy<br> 
* Matplotlib

## Installation
To install the necessary dependencies, run the following command:<br>
`pip install -r requirements.txt`

## How to run the app locally

Before running the code, please make sure you have fulfilled the requirements.
***
1. Python packages<br>

  To do so, run the following code in command prompt:<br>

  `pip install streamlit numpy pandas PIL time tensorflow os-sys`<br>

  (Please be informed that this does take awhile to complete)
***
2. ML Model<br>
  
  To do so, download the model "Trained_for_Oufits3.h5" from the link https://drive.google.com/drive/folders/1jB56j4cuoUvT-hjP-97zoOobCjUQ6tx8<br>
  (alternative link : https://zenodo.org/record/7617914#.Y-a6PXbMIuV)<br>
  
  You can store this model either in Downloads or any other directory you choose, but make sure to open the directory before proceeding to next step.
***
Please follow these step by step otherwise it wont work the way its intended to.<br>

1. Create a dummy folder on your desktop

2. Click the folder and left click to git bash into the folder<br> 
   "Git Bash here"

3. Clone this repository by running this code:<br>
   `git clone https://github.com/Lizoug/Outfit-Recommender.git`

4. You can now close the bash terminal and open the command prompt

5. Enter the frontend directory by running this code :<br>
   `cd Desktop/dummy_folder_name/Outfit-Recommender/frontend/streamlit`<br>
   (Remember to replace dummy_folder_name with your actual dummy folder name)

6. Run our application website locally by running this code :<br>
   `streamlit run draft.py`

## Note
Please make sure you have a dataset before running the training and evaluation command.

## Contribution
Feel free to open a pull request or an issue if you have any suggestions for improvements.

## Licence
This project is licensed under the terms of the MIT license.


