# Week 9 Yelyzaveta Tymofieieva

"""

1. Write a Program to create a class by name Students, and initialize attributes
like name, age, and grade while creating two instances of Students and print them.
"""
# create a class Student and initialize attributes
class Students:
    def __init__(self, name, age, grade):
        self.name =name
        self.age =age
        self.grade =grade
student1 = Students("Raj", 16, 11)
student2 = Students("Joe", 17, 11)

print(student2.name)
print(student1.age)


"""
2. Write a program to create a child class Teacher that will inherit the properties of Parent class Staff.  
Staff has attributes name, department, role, salary. 
Teacher has an additional attribute age.  Create two instances of Teacher and print them.
"""
# create a parent class Staff and initialize attributes
class Staff:
    def __init__(self, name, department, role, salary):
        self.name = name
        self.department = department
        self.role = role
        self.salary = salary

# create a subclass teacher that inherits the attributes of Staff
class Teacher(Staff):
    def __init__(self, name, age,  department, role, salary):
        # use super().__init__ to make sure the class inherits Staff class attributes
        super().__init__(name, department, role, salary)
        # add an additional attribute 'age'
        self.age = age

# use __str__ function to return a readable output instead of printing an instance of a class
    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, Department: {self.department}, "
                f"Role: {self.role}, Salary: {self.salary}")

# create instances of the class 'Teacher'
teacher1 = Teacher("Raj",20, "Science", "Teacher", 40000)
teacher2 = Teacher("Joe", 58, "Science", "Teacher", 80000)

print(teacher1)
print(teacher2)

"""
3. Write a Python class Square and define two methods that return 
the square area and perimeter given the length of a side.
"""

class Square:
    def __init__(self, side):
        self.side = side
    # define area method, round the result to max 2 decimal places
    def area(self):
        return round(self.side ** 2, 2)

    # define perimeter method, round the result to max 2 decimal places
    def perimeter(self):
        return round(self.side * 4, 2)

# use __str__ method to return a readable output
    def __str__(self):
        return (f"The side of the square is: {self.side}, \n "
                f"the perimeter is: {self.perimeter()} \n"
                f"the area is: {self.area()}.")

square1 = Square(7.25)
square2 = Square(10)
print(square1)

