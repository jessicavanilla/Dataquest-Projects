#! /usr/bin/env python3

import requests
import os

url = 'http://localhost/upload/'
images_folder = 'supplier-data/images/'

for image in os.listdir(images_folder):
  if image.endswith('.jpeg'):
    with open('/home/student-04-eb1ddd53a3f1/supplier-data/images/' + image, 'rb') as file:
      r = requests.post(url, files={'file': file})
