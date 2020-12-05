import json

#Create json data within code
data = { 
        "people": [ 
                {"firstName": "Jim", "lastName":"Smith", "gender":"male", "age":"41"},
                {"firstName": "Mary", "lastName":"Johnson", "gender":"female", "age":"34"}
            ] 
        }


#Write data to file
with open("people.json", "w") as peopleFile:
    json.dump(data, peopleFile, indent = 4, sort_keys = True, separators = ("," , ": " ))