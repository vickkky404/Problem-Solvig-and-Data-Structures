class Student:
    def __init__(self, name, roll, course):
        self.name = name
        self.roll = roll
        self.course = course

    def show_id(self):
        print("----- STUDENT ID CARD -----")
        print("Name   :", self.name)
        print("Roll   :", self.roll)
        print("Course :", self.course)
        print("---------------------------")

s1 = Student("Rahul", 101, "BCA")
s2 = Student("Anita", 102, "BSc")

s1.show_id()
s2.show_id()
