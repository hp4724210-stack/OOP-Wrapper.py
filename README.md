# Employee Management System

## 1. Project Title

**Python OOP Project: Employee Management System**

---

## 2. Project Description

The Employee Management System is a simple Python project based on **Object-Oriented Programming (OOP)** concepts.

This project allows the user to create and manage different types of objects:

- Person
- Employee
- Manager
- Developer

The program uses a menu-driven system where the user can select an operation, enter details, and display the stored information.

This project demonstrates important Python OOP concepts such as:

- Classes and Objects
- Constructors
- Inheritance
- Encapsulation
- Polymorphism
- Method Overriding
- Getter and Setter Methods
- Destructor
- `super()` Function
- `issubclass()` Function

---

# 3. Requirements

To run this project, you need:

- Python 3.x
- Any Python IDE or code editor

Examples:

- VS Code
- PyCharm
- IDLE

No external libraries are required.

---

# 4. How to Run the Project

### Step 1: Save the Python File

Save the program with a name such as:

```text
employee_management.py
```

### Step 2: Open Terminal

Open the terminal in the project folder.

### Step 3: Run the Program

Use the following command:

```text
python employee_management.py
```

The Employee Management System menu will appear on the screen.

---

# 5. Project Structure

The project contains the following main classes:

```text
Person
   |
   └── Employee
          |
          ├── Manager
          |
          └── Developer
```

This structure shows the inheritance relationship between the classes.

---

# 6. Class Details

## 6.1 Person Class

The `Person` class is the parent or base class.

It stores basic information about a person.

### Attributes

- `name`
- `age`

### Methods

#### Constructor

```python
def __init__(self, name=None, age=None):
```

The constructor initializes the name and age of a person.

#### Display Method

```python
def display(self):
```

This method displays the person's name and age.

### Example

```python
person = Person("Harshil", 20)
person.display()
```

### Output

```text
Name: Harshil
Age: 20
```

---

## 6.2 Employee Class

The `Employee` class inherits from the `Person` class.

It contains all the information from the Person class and adds employee-specific information.

### Attributes

- Name
- Age
- Employee ID
- Salary

### Private Variables

The Employee ID and Salary are declared as private variables:

```python
self.__employee_id
self.__salary
```

The double underscore (`__`) represents private variables.

This demonstrates the concept of **Encapsulation**.

### Getter Methods

Getter methods are used to access private variables.

```python
def get_employee_id(self):
    return self.__employee_id
```

```python
def get_salary(self):
    return self.__salary
```

### Setter Methods

Setter methods are used to update private variables.

```python
def set_employee_id(self, employee_id):
    self.__employee_id = employee_id
```

```python
def set_salary(self, salary):
    self.__salary = salary
```

### Using super()

The Employee class uses:

```python
super().__init__(name, age)
```

This calls the constructor of the parent `Person` class.

---

## 6.3 Manager Class

The `Manager` class inherits from the `Employee` class.

A manager has all the details of an employee and one additional detail.

### Additional Attribute

- Department

### Constructor

The constructor calls the Employee class constructor using:

```python
super().__init__(name, age, employee_id, salary)
```

### Display Method

The `display()` method is overridden.

First, it displays employee details using:

```python
super().display()
```

Then, it displays the department.

### Example

```python
manager = Manager(
    "Rahul", 30, "M101", 50000, "Sales"
)

manager.display()
```

---

## 6.4 Developer Class

The `Developer` class also inherits from the `Employee` class.

A developer has all employee details and one additional detail.

### Additional Attribute

- Programming Language

### Example

```python
developer = Developer(
    "Amit", 25, "D101", 40000, "Python"
)

developer.display()
```

The program displays:

- Name
- Age
- Employee ID
- Salary
- Programming Language

---

# 7. Menu Options

When the program starts, the following menu is displayed:

```text
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit
```

---

## Option 1: Create a Person

The user enters:

- Name
- Age

A `Person` object is created and stored in the `persons` list.

```python
persons.append(person)
```

---

## Option 2: Create an Employee

The user enters:

- Name
- Age
- Employee ID
- Salary

An `Employee` object is created and stored in the `employees` list.

```python
employees.append(employee)
```

---

## Option 3: Create a Manager

The user enters:

- Name
- Age
- Employee ID
- Salary
- Department

A `Manager` object is created and stored in the `managers` list.

```python
managers.append(manager)
```

---

## Option 4: Create a Developer

The user enters:

- Name
- Age
- Employee ID
- Salary
- Programming Language

A `Developer` object is created and stored in the `developers` list.

```python
developers.append(developer)
```

---

## Option 5: Show Details

The user can select which type of details to display:

```text
1. Person
2. Employee
3. Manager
4. Developer
```

The program uses a `for` loop to display all objects stored in the selected list.

Example:

```python
for employee in employees:
    employee.display()
```

---

## Option 6: Exit

When the user selects option 6, the program displays:

```text
Exiting the system.
Goodbye!
```

The `break` statement stops the `while` loop and exits the program.

---

# 8. Lists Used in the Project

The project uses four lists to store objects.

```python
persons = []
employees = []
managers = []
developers = []
```

### Purpose of Each List

| List Name | Stores |
|---|---|
| `persons` | Person objects |
| `employees` | Employee objects |
| `managers` | Manager objects |
| `developers` | Developer objects |

---

# 9. OOP Concepts Used

## 9.1 Class

A class is a blueprint for creating objects.

Example:

```python
class Person:
```

---

## 9.2 Object

An object is an instance of a class.

Example:

```python
person = Person("Harshil", 20)
```

Here, `person` is an object of the `Person` class.

---

## 9.3 Inheritance

Inheritance allows a child class to use the properties and methods of a parent class.

In this project:

```text
Person → Employee
Employee → Manager
Employee → Developer
```

Example:

```python
class Employee(Person):
```

This means the Employee class inherits from the Person class.

---

## 9.4 Encapsulation

Encapsulation is the process of hiding data and controlling access to it.

In this project:

```python
self.__employee_id
self.__salary
```

These are private variables.

Getter and Setter methods are used to access and modify them.

---

## 9.5 Polymorphism

Polymorphism means the same method name can have different behavior.

In this project, all classes use a method named:

```python
display()
```

However, each class displays different information.

---

## 9.6 Method Overriding

Method overriding happens when a child class provides its own version of a parent class method.

Example:

```python
def display(self):
    super().display()
    print("Department:", self.department)
```

The Manager class overrides the Employee class `display()` method.

---

## 9.7 Constructor

A constructor is a special method that is automatically called when an object is created.

In Python:

```python
def __init__(self):
```

The project uses constructors to initialize object data.

---

## 9.8 Destructor

A destructor is a special method that can run when an object is destroyed.

In this project:

```python
def __del__(self):
    pass
```

The `pass` statement means no specific action is performed.

---

## 9.9 super() Function

The `super()` function is used to call methods from the parent class.

Example:

```python
super().__init__(name, age)
```

It calls the constructor of the parent class.

Another example:

```python
super().display()
```

It calls the parent class display method.

---

# 10. Inheritance Checking

At the end of the program, the `issubclass()` function checks the inheritance relationship.

Example:

```python
issubclass(Manager, Employee)
```

This checks whether `Manager` is a subclass of `Employee`.

Another example:

```python
issubclass(Developer, Employee)
```

This checks whether `Developer` is a subclass of `Employee`.

Both results should return:

```text
True
```

---

# 11. Sample Output

```text
--- Python OOP Project: Employee Management System ---

Choose an operation:

1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

Enter your choice: 2

Enter Name: Harshil
Enter Age: 20
Enter Employee ID: E101
Enter Salary: 25000

Employee created successfully!
```

### Display Example

```text
Employee Details:
Name: Harshil
Age: 20
Employee ID: E101
Salary: 25000.0
```

---

# 12. Advantages of This Project

- Easy to understand
- Uses basic Python OOP concepts
- Menu-driven system
- Stores multiple objects
- Demonstrates inheritance
- Demonstrates encapsulation
- Demonstrates polymorphism
- Easy to expand with new features

---

# 13. Future Improvements

The following features can be added in the future:

- Search an employee by Employee ID
- Update employee information
- Delete employee information
- Store data in a file
- Add a database
- Add input validation
- Create a graphical user interface (GUI)

---

# 14. Conclusion

The **Employee Management System** is a Python project created using Object-Oriented Programming concepts.

The project demonstrates how different classes can work together using inheritance. The `Person` class is the base class, while `Employee` inherits from it. The `Manager` and `Developer` classes further inherit from the `Employee` class.

The project also demonstrates encapsulation by using private variables for Employee ID and Salary. Getter and Setter methods are used to access and modify these values.

Overall, this project helps in understanding important Python OOP concepts such as **Class, Object, Inheritance, Encapsulation, Polymorphism, Method Overriding, Constructor, Destructor, and the super() function**.

This project is simple, structured, and suitable for Python practicals, assignments, and OOP learning.
