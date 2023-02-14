append later:
-only use jpeg, there is a link on the website
-don't worry about the error messages you get while installing, the programm should work never the less
-on the webpage, click "browse photo" to select a photo (jpeg) from your computer
-click [..] to get photo analyzed

-change description, so that user knows which steps to perform (and which not) to use the programm


# *Outfit Recommendation System*
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![.github/workflows/my first ci](https://github.com/Lizoug/Outfit-Recommender/actions/workflows/my_first_ci.yaml/badge.svg)](https://github.com/Lizoug/Outfit-Recommender/actions/workflows/my_first_ci.yaml)



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

First be sure to have your image in .jpg format ready.<br>
Convert it online with the following link :<br>
https://convertio.co/jpeg-jpg/
***
### Requirements
Before running the code, please make sure you have fulfilled the requirements.<br>
1. Anaconda installed and Anaconda prompt ready<br>
  
  You can download Anaconda here :<br>
  https://www.anaconda.com/
  
  
2. Additional Python packages<br>

  To do so, run the following code in Anaconda prompt:<br>

  `pip install streamlit webcolors`<br>

  (Please be informed that this does take awhile to complete)
***
### Manual
Please follow these step by step otherwise it wont work the way its intended to.<br>

1. Create a dummy folder on your desktop

2. Click the folder and left click to git bash into the folder<br> 
   "Git Bash here"

3. Clone this repository by running this code:<br>
   `git clone https://github.com/Lizoug/Outfit-Recommender.git`

4. You can now close the bash terminal and open Anaconda prompt

5. Enter the frontend directory by running this code :<br>
   `cd Desktop/dummy_folder_name/Outfit-Recommender`<br>
   (Remember to replace dummy_folder_name with your actual dummy folder name)

6. If you haven't already, install requirements with the following code :<br>
   `pip install -r requirements.txt`<br>
   (This will take awhile and you may see some errors but it should still work fine)
   
7. Enter the code directory with the following code : <br>
   `cd code`<br>
   
8. Run the code :<br>
   `streamlit run main.py`<br>
   (The website should be launched from your browser with the given IP Address)

## Note
Please make sure you have a dataset before running the training and evaluation command.

## Contribution
Feel free to open a pull request or an issue if you have any suggestions for improvements.

## Licence
This project is licensed under the terms of the MIT license.


