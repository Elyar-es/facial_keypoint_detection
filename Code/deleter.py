import os

folder_path = "/subed-angles/left-right(lefted)-noBadCrop"

image_files = [file for file in os.listdir(folder_path) if file.__str__()[-8] == 'B' or file.__str__()[-8] == 'T']

for file in image_files:
  print(file.__str__())
  os.remove(os.path.join(folder_path, file))

