class Person:
    def display(self):
        print("I am a Person")

class Student(Person):
    def study(self):
        print("I am studying Python")

obj = Student()
obj.display()
obj.study()