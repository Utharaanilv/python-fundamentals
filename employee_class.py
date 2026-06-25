class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)

emp = Employee("Rahul", 35000)
emp.details()