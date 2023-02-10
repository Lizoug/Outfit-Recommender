Here's how you run the app locally from your PC:

***
Before running the code, please make sure you have fulfilled the requirements.
***
1. Python packages<br>

  To do so, run the following code in command prompt:<br>

  pip install streamlit numpy pandas PIL time tensorflow os-sys

  (Please be informed that this does take awhile to complete)
***
2. ML Model<br>
  
  To do so, download the model "Trained_for_Oufits3.h5" from the link https://drive.google.com/drive/folders/1jB56j4cuoUvT-hjP-97zoOobCjUQ6tx8
  (alternative link : https://zenodo.org/record/7617914#.Y-a6PXbMIuV)<br>
  
  You can store this model either in Downloads or any other directory you choose, but make sure to open the directory before proceeding to next step.
***
Please follow these step by step otherwise it wont work the way its intended to.<br>

1. Create a dummy folder on your desktop

2. Click the folder and left click to git bash into the folder 
   "Git Bash here"

3. Clone this repository by running this code:
   git clone https://github.com/Lizoug/Outfit-Recommender.git

4. You can now close the bash terminal and open the command prompt

5. Enter the frontend directory by running this code :
   cd Desktop/dummy_folder_name/Outfit-Recommender/frontend/streamlit

6. Run our application website locally by running this code :
   streamlit run draft.py
