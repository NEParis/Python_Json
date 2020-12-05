import json

## Initialize
peopleCollection = {}


## Read data from file
with open("people.json", "r") as peopleFile:
    peopleCollection = json.load(peopleFile)
    # print(peopleCollection)


## Act
# print(peopleCollection)


## Act II
# print(peopleCollection['people'])


# ## Only 1st Person
# print("Working with first person")
# firstPerson = peopleCollection['people'][0]

# print("First Name: " + firstPerson['firstName'])
# print("Last Name: " + firstPerson['lastName'])
# print("Age: " + firstPerson['age'])
# print("Gender: " + firstPerson['gender'])


# ## Only 2nd Person
# print("Working with second person")
# firstPerson = peopleCollection['people'][1]

# print("First Name: " + firstPerson['firstName'])
# print("Last Name: " + firstPerson['lastName'])
# print("Age: " + firstPerson['age'])
# print("Gender: " + firstPerson['gender'])



## Iterate collection
for person in peopleCollection['people']:
    print("-------------------")
    print("First Name: " + person['firstName'])
    print("Last Name: " + person['lastName'])
    print("Age: " + person['age'])
    print("Gender: " + person['gender'])
    print("-------------------")