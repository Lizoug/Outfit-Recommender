import os 
import glob
from PIL import Image

folder = "/Users/lizak/OneDrive/Desktop/myntradataset/images/"
onlyfiles = []

# Iterate over the files in the specified folder
for filename in glob.glob('path/*.jpg'): #using * as a wildcard for the exact image name
    # Check if the file path is a file (and not a directory or symbolic link, etc.)
   im = Image.open(filename) 
   onlyfiles.append(im)
