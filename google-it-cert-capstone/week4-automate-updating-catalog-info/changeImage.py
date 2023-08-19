#! /usr/bin/env python3

from PIL import Image
import os

images_path = 'supplier-data/images/'

new_size = (600, 400)

for image in os.listdir(images_path):
  if image.endswith('.tiff'):
    im = Image.open(os.path.join(images_path, image))
    im.resize(new_size).convert('RGB').save(os.path.join(images_path, image).replace('.tiff', '.jpeg'), 'JPEG')
