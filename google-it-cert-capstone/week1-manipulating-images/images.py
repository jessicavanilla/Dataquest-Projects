#!/usr/bin/env python3

from PIL import Image
import os

save_path = '/opt/icons/'
images_folder = 'images/'

for image in os.listdir(images_folder):
  if image != '.DS_Store':
    im = Image.open(os.path.join(image_folder, image))
    im.rotate(-90).resize(128, 128).convert('RGB').save(os.path.join(save_path, image))
