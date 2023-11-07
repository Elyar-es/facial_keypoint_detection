import os
import shutil
from PIL import Image

def split_images(input_dir, output_dir, batch_size):  # Splits all the images in the input directory into batches of the specified size

    if not os.path.exists(output_dir):
      
        os.mkdir(output_dir)
  
    image_files = os.listdir(input_dir)
    num_images = len(image_files)
  
    for i in range(0, num_images, batch_size):
      
        batch_files = image_files[i:i + batch_size]
        batch_dir = os.path.join(output_dir, str(i))
        if not os.path.exists(batch_dir):
          
            os.mkdir(batch_dir)
    
        for file in batch_files:
          
            if is_image(file):
              
                image = Image.open(os.path.join(input_dir, file))
                image.save(os.path.join(batch_dir, file))
            
def is_image(filepath):

    extension = filepath.split(".")[-1]
    return extension in ["jpg", "jpeg", "png", "gif"]


if __name__ == "__main__":
    
    input_dir = "/datasets/subed-angles/front-noBadCrop"
    output_dir = "/datasets/data-batched"
    batch_size = 10
  
    split_images(input_dir, output_dir, batch_size)
  
