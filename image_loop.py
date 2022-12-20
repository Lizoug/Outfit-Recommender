import os 

folder = "/Users/lizak/OneDrive/Desktop/myntradataset/images/"
onlyfiles = []
for f in os.listdir(folder):
    file_path = os.path.join(folder, f)
    if os.path.isfile(file_path):
        onlyfiles.append(f)
