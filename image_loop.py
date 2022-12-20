import os 

folder = "/Users/lizak/OneDrive/Desktop/myntradataset/images/"
onlyfiles = []

# Iterate over the files in the specified folder
for f in os.listdir(folder):
    # Construct the full file path by joining the folder path with the file name
    file_path = os.path.join(folder, f)
    # Check if the file path is a file (and not a directory or symbolic link, etc.)
    if os.path.isfile(file_path):
        onlyfiles.append(f)
