import json

with open("example.json","r")as json_file:
    a = json.load(json_file)
print(a)
