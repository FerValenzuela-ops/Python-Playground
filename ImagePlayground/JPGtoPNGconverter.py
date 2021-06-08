import sys
import os
from PIL import Image, ImageFilter

# this works in administrator powersheel, you've gotta put
# python JPGtoPNGconverter.py ./Pokedex ./new


# grab first and second argumkent
image_folder = sys.argv[1] # /Pokedex
output_folder = sys.argv[2] # /New

print(image_folder, output_folder) # Let's see what arguments we gave to the script
#  check if new/ exists if not create it
print(os.path.exists(output_folder)) # Let's checkout if the path exist


if not (os.path.exists(output_folder)): # If /new path doesnt exists, then we are going to create it
    os.makedirs(output_folder)
# loop trough pokedex, and convert images to png
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}/{filename}')
    clean_name = os.path.splitext(filename)[0]
# save them to the new folder
    img.save(f'{output_folder}/{clean_name}.png', 'png')
    print('all done!')


