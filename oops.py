# # Write a class Car with attributes brand and year. Create an object of this class and display its attributes.#
# class Car:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
# my_car = Car("Toyota", 2020)
# print(my_car.brand)  
# print(my_car.year)  
# # Create a Rectangle class with methods to calculate area and perimeter.
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
#     def perimeter(self):
#         return 2 * (self.length + self.width)
# rect = Rectangle(5, 3)
# print(rect.area())
# print(rect.perimeter()) 
# #Demonstrate the difference between class attributes and instance attributes in a Dog class.
# class Dog:
#     species = "Canine" 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Max", 5)
# print(dog1.species)  # Output: Canine
# print(dog2.name)
# #Write a Python class that represents a car with attributes like model, year, and method to display details.
# class Car:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#     def display_details(self):
#         print(f"Model: {self.model}, Year: {self.year}")
# car = Car("Tesla", 2023)
# car.display_details()
# #How do you create an instance of a class and access its attributes in Python?
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# person = Person("Alice", 25)
# print(person.name, person.age)
# #What is method overriding in Python? Demonstrate with an example.
# class Animal:
#     def sound(self):
#         print("Animal Sound")
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
# dog = Dog()
# dog.sound()
# #How do you create a class that inherits from another class in Python?
# class Parent:
#     def __init__(self, name):
#         self.name = name
# class Child(Parent):
#     def greet(self):
#         print(f"Hello, {self.name}")
# child = Child("John")
# child.greet()
# #What is a class method in Python and how is it different from an instance method?
# class MyClass:
#     class_attr = "Class Attribute"
#     def __init__(self, name):
#         self.name = name
#     @classmethod
#     def display_class_attr(cls):
#         print(cls.class_attr)
# obj = MyClass("Object1")
# obj.display_class_attr()
# #Create a Python class that represents a bank account with methods to deposit and withdraw money.
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("Insufficient balance")
# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(300)
# print(account.balance)
# #Write a Python class with a property that gets the value of an attribute but prevents setting it directly.
# class MyClass:
#     def __init__(self, value):
#         self._value = value
#     @property
#     def value(self):
#         return self._value
# obj = MyClass(10)
# print(obj.value)
# #Write a Python program to demonstrate the use of multiple inheritance.
# class ClassA:
#     def method_a(self):
#         print("Method A from Class A")
# class ClassB:
#     def method_b(self):
#         print("Method B from Class B")
# class ClassC(ClassA, ClassB):
#     pass
# obj = ClassC()
# obj.method_a()
# obj.method_b()
# #Write a Python program to demonstrate the concept of abstraction using an abstract class.
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
# circle = Circle(5)
# print(circle.area())






# class parent():
#     def method1(self):
#         print("im parent")
# class child(parent):
#     def method2(self):
#         print("i m child")
# child1 = child()
# child1.method2()
# child1.method1()
# parent1 = parent()
# parent1.method2( )
# class father():
#     def method1(self):
#         print("i m father")
# class mother():
#     def method2(self):
#         print("i m mother")
# class child(father,mother):
#     def method3(self):
#         print("i m child")
# child1 = child()
# child1.method2()
# child1.method1()
# child1.method3()
# print(child.__mro___)
class grandparent():
    def method1(self):
        print("i m father")
class parent(grandparent):
    def method2(self):
        print("i m mother")
class child(grandparent):
    def method3(self):
        print("i m child")
child1 = child()
print(child.__mro__)
