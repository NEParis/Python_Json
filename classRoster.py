import json

## Initialize
classesCollection = {}


## Read data from file
with open("class_rosters.json", "r") as rosterFile:
    classesCollection = json.load(rosterFile)
    # print(classesCollection)

# ## Access specific value
# print(classesCollection['classes'][0]['students'][1]['lastName'])


# ## Access one stuedent
# student = classesCollection['classes'][0]['students'][1]
# print(student)


## Iterate collection
for classes in classesCollection['classes']:
    print("==============================")
    print(classes['className'],"students:")
    print("==============================")
    
    for student in classes['students']:
        print("First Name: " + student['firstName'])
        print("Last Name: " + student['lastName'])
        print("Age: " + student['age'])
        print("Gender: " + student['gender'])
        print("-------------------")

    ## Create spacing before next class
    print("\n")