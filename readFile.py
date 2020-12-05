import json

## Initialize
peopleCollection = {}


## Read data from file
with open("people.json", "r") as peopleFile:
    peopleCollection = json.load(peopleFile)
    # print(peopleCollection)


## Act
print(peopleCollection)