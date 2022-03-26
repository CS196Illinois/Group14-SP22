class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def getName(self):
        return self.name
    def getYear(self):
        return self.year
    def setYear(self,new_year):
        self.year = new_year
    student1 = Student("Hector", "2025")
    print(student1.getname())