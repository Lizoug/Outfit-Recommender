import os 
#what do you think about using the library "global"? It can be used to search for a specific file pattern in a path
#so we could insert a wildcard for the exact image name at the end of the path to the image folder

import glob
from PIL import Image
folder = "/Users/lizak/OneDrive/Desktop/myntradataset/images/"
onlyfiles = []

# Iterate over the files in the specified folder
for filename in glob.glob('path/*.jpg'): #using * as a wildcard for the exact image name
    # Construct the full file path by joining the folder path with the file name
    file_path = os.path.join(folder, f)
    # Check if the file path is a file (and not a directory or symbolic link, etc.)
    if os.path.isfile(file_path):
        onlyfiles.append(f)
