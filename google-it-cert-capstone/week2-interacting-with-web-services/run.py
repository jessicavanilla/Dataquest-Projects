#! /usr/bin/env python3
import os
import requests

path = '/data/feedback'
reviews = os.listdir(path)
entries_list = []
keys = ['title', 'name', 'date', 'feedback']

for review in reviews:
        with open (os.path.join(path, review), 'r') as file:
                reader = file.readlines()
                i = 0
                entry_dict = {}
                for line in reader:
                        entry_dict[keys[i]] = reader[i].strip()
                        i += 1
        entries_list.append(entry_dict)

for entry in entries_list:
        response = requests.post("http://34.16.137.225/feedback/", data=entry)
        if not response.ok:
                print(f"Error code: {response.status_code}")
