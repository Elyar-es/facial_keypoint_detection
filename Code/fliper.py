import os
from PIL import Image

folder_path = "/all/temp"

for file in os.listdir(folder_path):

  if file.endswith(".jpg") or file.endswith(".png"):

    image = Image.open(os.path.join(folder_path, file))
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    image.save(os.path.join(folder_path, file))

