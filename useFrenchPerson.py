from tryClasses.frenchPerson import FrenchPerson


p1 = FrenchPerson("Erik","France", 45)
print(p1.LastName)
print(p1.Age)
print(p1.FirstName)
print(p1.FullName)

print("\n")

p2 = FrenchPerson("Justyn", "France", 19)
numberToAdd = 5

print(p2.FullName)
print("Original Age:", p2.Age)

i=1
while (i<=5):
    print("Additional " + str(i) + " years:", p2.Age_ByYears(i))
    i+=1
