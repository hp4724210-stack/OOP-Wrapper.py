class Person:

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)



class Employee(Person):

    def __init__(self, name=None, age=None,
                 employee_id=None, salary=0):

        super().__init__(name, age)

        self.__employee_id = employee_id
        self.__salary = salary


    def get_employee_id(self):
        return self.__employee_id

  
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

    def __del__(self):
        pass



class Manager(Employee):

    def __init__(self, name=None, age=None,
                 employee_id=None, salary=0,
                 department=None):

        super().__init__(name, age, employee_id, salary)
        self.department = department

  
    def display(self):
        super().display()
        print("Department:", self.department)



class Developer(Employee):

    def __init__(self, name=None, age=None,
                 employee_id=None, salary=0,
                 programming_language=None):

        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print("Programming Language:",
              self.programming_language)



persons = []
employees = []
managers = []
developers = []


while True:

    print("--- Python OOP Project: Employee Management System ---")

    print("Choose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Create a Developer")
    print("5. Show Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        person = Person(name, age)
        persons.append(person)

        print("Person created successfully!")

    elif choice == "2":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(name, age, emp_id, salary)
        employees.append(employee)

        print("\nEmployee created successfully!")

    elif choice == "3":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(
            name, age, emp_id, salary, department
        )

        managers.append(manager)

        print("\nManager created successfully!")

    elif choice == "4":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        language = input("Enter Programming Language: ")

        developer = Developer(
            name, age, emp_id, salary, language
        )

        developers.append(developer)

        print("Developer created successfully!")

    elif choice == "5":

        print("Choose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        print("4. Developer")

        sub_choice = input("Enter your choice: ")

        if sub_choice == "1":
            for person in persons:
                person.display()

        elif sub_choice == "2":
            for employee in employees:
                employee.display()

        elif sub_choice == "3":
            for manager in managers:
                manager.display()

        elif sub_choice == "4":
            for developer in developers:
                developer.display()

        else:
            print("Invalid choice!")

    elif choice == "6":

        print("Exiting the system.")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")

print("--- Inheritance Checking ---")

print("Is Manager a subclass of Employee?",
      issubclass(Manager, Employee))

print("Is Developer a subclass of Employee?",
      issubclass(Developer, Employee))