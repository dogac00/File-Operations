import json

value = """
        {"title": "Abcd",
          "composer": "Fghfd",
          "release_year": "1897",
          "budget": 1500000,
          "actors": null,
          "won_oscar": false
          }
          """
obj = json.loads(value)

print(obj) # will print a valid python dictionary

# true, false will be True, False
# null will be None
