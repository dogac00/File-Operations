# text file saving

import json

# load method allows you to load data from a file

json_file = open("example.txt", "r", encoding="utf-8")
movie = json.load(json_file)
json_file.close()

print(movie) # will print the example in the dictionary format
print(type(movie)) # you see <class 'dict'> as output
