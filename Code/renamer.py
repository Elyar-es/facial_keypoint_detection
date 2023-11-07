import os
import sys

def change_character_in_image_names(folder, index, character):   # Changes the character at the specified index in the names of the images in the specified folder to the specified character.


  for image in os.listdir(folder):
    if image.endswith(".jpg"):
      current_name = os.path.basename(image)
      new_name = current_name[:index] + character + current_name[index + 1:]
      os.rename(os.path.join(folder, image), os.path.join(folder, new_name))

if __name__ == "__main__":
  folder = sys.argv[3]
  index = int(sys.argv[2])
  character = sys.argv[1]

  change_character_in_image_names(folder, index, character)

  print("changed the char at index {} in the names of the images in the folder {} to {}".format(index, folder, character))



