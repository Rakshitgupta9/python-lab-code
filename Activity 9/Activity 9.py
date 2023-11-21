class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary:.2f}")


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


emp1 = Employee(1, "John Doe", 50000)
manager1 = Manager(2, "Jane Smith", 70000, "IT")
developer1 = Developer(3, "Bob Johnson", 60000, "Python")


print("Employee Information:")
emp1.display_info()
print("\nManager Information:")
manager1.display_info()
print("\nDeveloper Information:")
developer1.display_info()
