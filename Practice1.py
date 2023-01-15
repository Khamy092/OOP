# Practice 1
# my first OOP-based python program. Wish myself luck!

class Student:

    def __init__(self, name, age, year, gpa, eligibleHonour, grades): # self does not need to be passed in as an argument.
        self.name = name
        self.age = age
        self.year = year
        self.gpa = gpa
        self.eligibleHonour = eligibleHonour
        self.grades = grades


    def get_grades(self):
        overallGrade = sum(self.grades) / len(self.grades)
        if overallGrade >= 90:
            return "High Distinction"
        elif overallGrade >= 80:
            return "Distinction"
        elif overallGrade >= 70:
            return "Credit"
        elif overallGrade >= 60:
            return "Pass"
        else:
            return "Fail"

    def get_eligibleHonour(self):

        if self.gpa >= 5:
            self.eligibleHonour = "Yes"
            return self.eligibleHonour
        else:
            self.eligibleHonour = "No"
            return self.eligibleHonour
    

khamy092 = Student("Taqi", 24, "Second", 3.8, eligibleHonour="N/A", grades=[90, 89, 79, 55, 76, 91, 72, 87])

print("Student:" ,khamy092.name)
print("Age:" ,khamy092.age)
print("Year:" ,khamy092.year)
print("GPA:" ,khamy092.gpa)
print("Eligible for Honours:" ,khamy092.get_eligibleHonour())
print("Overall Grade:" ,khamy092.get_grades())

print("------------------------------------")

james1010 = Student("James", 25, "Third", 6.12, eligibleHonour="N/A", grades=[68, 70, 100, 100, 73, 100, 100, 90])

print("Student:" ,james1010.name)
print("Age:" ,james1010.age)
print("Year:" ,james1010.year)
print("GPA:" ,james1010.gpa)
print("Eligible for Honours:" ,james1010.get_eligibleHonour())
print("Overall Grade:" ,james1010.get_grades())

print()
input("Press Enter to exit...")


# I did it!