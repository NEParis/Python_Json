import json

#read data from file
with open("people.json", "r") as peopleFile:
    peopleCollection = json.load(peopleFile)

    print(peopleCollection)