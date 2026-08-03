# Class
class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Object creation
student1 = Student("Sofia", 20)
student2 = Student("Anna", 21)

# Calling the method
student1.display()
student2.display() 