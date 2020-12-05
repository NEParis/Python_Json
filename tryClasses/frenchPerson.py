class FrenchPerson:

    def __init__(self, FirstName, LastName, Age):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age


    @property
    def FullName(self):
        return self.FirstName + " " + self.LastName


    def Age_ByYears(self, number):
        return self.Age + number

    