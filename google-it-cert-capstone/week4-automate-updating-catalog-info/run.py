#! /usr/bin/env python3

import requests
import os
from os import path

images_path = 'supplier-data/images'
images = os.listdir(images_path)
text_path = 'supplier-data/descriptions'
files = os.listdir(text_path)
keys = ['name', 'weight', 'description', 'image_name']
text_list = []

for description in files:
  with open(os.path.join(text_path, description), 'r') as text:
    reader = text.readlines()
    i = 0
    text_dict = {}
    for line in reader:
      if i == 1:
        text_dict[keys[i]] = int(line.replace(' lbs', ''))
      else:
        text_dict[keys[i]] = line.strip()
      i += 1
  fruit_id = path.splitext(path.basename(description))[0]
  text_dict[keys[3]] = fruit_id + '.jpeg'  
  text_list.append(text_dict)

for text in text_list:
  response = requests.post('http://localhost/fruits/', data=text)
  if not response.ok:
    print('Error code: {}'.format(response.status_code))
