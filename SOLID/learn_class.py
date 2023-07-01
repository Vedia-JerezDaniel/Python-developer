# LEARNING CLASSES
# https://realpython.com/python-classes/#getting-started-with-python-classes

# More easy

# https://realpython.com/python-data-classes/



# n a class body, you can define attributes and methods as needed. As you already learned, attributes are variables that hold the class data, while methods are functions that provide behavior and typically act on the class data.

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)
    
# In this code snippet, you define Circle using the class keyword. Inside the class, you write two methods. The .__init__() method has a special meaning in Python classes. This method is known as the object initializer because it defines and sets the initial values for your attributes. You’ll learn more about this method in the Instance Attributes section.


circle_1 = Circle(42)
circle_2 = Circle(7)

circle_1.radius
circle_1.calculate_area()

circle_2.radius
circle_2.calculate_area()


class SampleClass:
    def __init__(self, value):
        self.__value = value
    def __method(self):
        print(self.__value)

sample_instance = SampleClass("Hello!")
vars(sample_instance)

vars(SampleClass)

sample_instance = SampleClass("Hello!")

# hidden to all __
sample_instance.__value

sample_instance.__method()

dir(sample_instance)
sample_instance._SampleClass__value

sample_instance._SampleClass__method()

# Understanding the Benefits of Using Classes in Python
# Is it worth using classes in Python? Absolutely! Classes are the building blocks of object-oriented programming in Python. They allow you to leverage the power of Python while writing and organizing your code. By learning about classes, you’ll be able to take advantage of all the benefits that they provide. With classes, you can:

# Model and solve complex real-world problems: You’ll find many situations where the objects in your code map to real-world objects. This can help you think about complex problems, which will result in better solutions to your programming problems.

# Reuse code and avoid repetition: You can define hierarchies of related classes. The base classes at the top of a hierarchy provide common functionality that you can reuse later in the subclasses down the hierarchy. This allows you to reduce code duplication and promote code reuse.

# Encapsulate related data and behaviors in a single entity: You can use Python classes to bundle together related attributes and methods in a single entity, the object. This helps you better organize your code using modular and autonomous entities that you can even reuse across multiple projects.

# Abstract away the implementation details of concepts and objects: You can use classes to abstract away the implementation details of core concepts and objects. This will help you provide your users with intuitive interfaces (APIs) to process complex data and behaviors.

# Unlock polymorphism with common interfaces: You can implement a particular interface in several slightly different classes and use them interchangeably in your code. This will make your code more flexible and adaptable.

# In short, Python classes can help you write more organized, structured, maintainable, reusable, flexible, and user-friendly code. They’re a great tool to have under your belt. However, don’t be tempted to use classes for everything in Python. In some situations, they’ll overcomplicate your solutions.

# Instance Attributes

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200
        

toyota_camry = Car("Toyota", "Camry", 2022, "Red")
toyota_camry.make
toyota_camry.model
toyota_camry.color
toyota_camry.speed


class SampleClass:
    class_attr = 100

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr

    def method(self):
        print(f"Class attribute: {self.class_attr}")
        print(f"Instance attribute: {self.instance_attr}")


SampleClass.class_attr

SampleClass.__dict__

SampleClass.__dict__["class_attr"]


instance = SampleClass("Hello!")
instance.instance_attr
instance.method()

instance.__dict__
instance.__dict__["instance_attr"]

instance.__dict__["instance_attr"] = "Hello, Pythonista!"
instance.instance_attr


class Record:
    """Hold a record of data."""
    

john = {
    "name": "John Doe",
    "position": "Python Developer",
    "department": "Engineering",
    "salary": 80000,
    "hire_date": "2020-01-01",
    "is_manager": False,
}


john_record = Record()

for field, value in john.items():
    setattr(john_record, field, value)

john_record.name
john_record.department

john_record.__dict__

class User:
    pass

# Add methods dynamically
def __init__(self, name, job):
    self.name = name
    self.job = job

User.__init__ = __init__
User.__dict__

linda = User("Linda Smith", "Team Lead")
linda.__dict__


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        self._radius = value

    def calculate_area(self):
        return round(math.pi * self._radius**2, 2)
    
# To turn an existing attribute like .radius into a property, you typically use the @property decorator to write the getter method. The getter method must return the value of the attribute. In this example, the getter returns the circle’s radius, which is stored in the non-public ._radius attribute.

# To define the setter method of a property-based attribute, you need to use the decorator @attr_name.setter. In the example, you use @radius.setter. Then you need to define the method itself. Note that property setters need to take an argument providing the value that you want to store in the underlying attribute.

# Inside the setter method, you use a conditional to check whether the input value is an integer or a floating-point number. You also check if the value is less than or equal to 0. If either is true, then you raise a ValueError with a descriptive message about the actual issue. Finally, you assign value to ._radius, and that’s it. Now, .radius is a property-based attribute.


circle_1 = Circle(100)
circle_1.radius

circle_1.radius = 500
circle_1.radius = 0

circle_1.calculate_area()


import math


class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = name
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    def __set__(self, instance, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        instance.__dict__[self._name] = value

class Circle:
    radius = PositiveNumber()
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return round(math.pi * self.radius**2, 2)

class Square:
    side = PositiveNumber()
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
        return round(self.side**2, 2)
    
    
circle = Circle(100)
circle.radius

circle.radius = 500
circle.radius

square = Square(200)
square.side

square.side = 300
square.side

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

    def start(self):
        print("Starting the car...")
        self.started = True

    def stop(self):
        print("Stopping the car...")
        self.started = False

    def accelerate(self, value):
        if not self.started:
            print("Car is not started!")
            return
        if self.speed + value <= self.max_speed:
            self.speed += value
        else:
            self.speed = self.max_speed
        print(f"Accelerating to {self.speed} km/h...")

    def brake(self, value):
        if self.speed - value >= 0:
            self.speed -= value
        else:
            self.speed = 0
        print(f"Braking to {self.speed} km/h...")
    
    def __str__(self):
        return f"{self.make}, {self.model}, {self.color}: ({self.year})"

    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f'(make="{self.make}", '
            f'model="{self.model}", '
            f"year={self.year}, "
            f'color="{self.color}")'
        )
        

x3 = Car("BMw", "X3", 2005, "Black")
x3.start()

x3.accelerate(100)

x3.brake(50)

x3.brake(80)

x3.stop()

x3.accelerate(100)

x3.__str__()
x3.__repr__()

# The .__str__() method provides what’s known as the informal string representation of an object. This method must return a string that represents the object in a user-friendly manner. You can access an object’s informal string representation using either str() or print().

# The .__repr__() method is similar, but it must return a string that allows you to re-create the object if possible. So, this method returns what’s known as the formal string representation of an object. This string representation is mostly targeted at Python programmers, and it’s pretty useful when you’re working in an interactive REPL session.

str(x3)
repr(x3)

# Python protocols are another fundamental topic that’s closely related to special methods. Protocols consist of one or more special methods that support a given feature or functionality. Common examples of protocols include:

# Protocol	Provided Feature	Special Methods
# Iterator	Allows you to create iterator objects	.__iter__() and .__next__()
# Iterable	Makes your objects iterable	.__iter__()
# Descriptor	Lets you write managed attributes	.__get__() and optionally .__set__(), .__delete__(), and .__set_name__()
# Context manager	Enables an object to work on with statements	.__enter__() and .__exit__()

# Getter and Setter Methods vs Properties

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()
        

jane = Person("Jane")
jane.name

jane.name = "Jane Doe"
jane.name


# Exploring Specialized Classes From the Standard Library

from dataclasses import dataclass


@dataclass
class ThreeDPoint:
    x: int | float
    y: int | float
    z: int | float

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)

    @staticmethod
    def show_intro_message(name):
        print(f"Hey {name}! This is your 3D Point!")


from dataclasses import astuple

point_1 = ThreeDPoint(1.0, 2.0, 3.0)
point_1

astuple(point_1)

point_2 = ThreeDPoint(2, 3, 4)
point_1 == point_2


point_3 = ThreeDPoint(1, 2, 3)
point_1 == point_3


# Enumerations
# An enumeration, or just enum, is a data type that you’ll find in several programming languages. Enums allow you to create sets of named constants, which are known as members and can be accessed through the enumeration itself.

from enum import Enum


class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    
    @classmethod
    def favorite_day(cls):
        return cls.FRIDAY

    def __str__(self):
        return f"Current day: {self.name}"
    
list(WeekDay)

# Dot notation
WeekDay.MONDAY
# Call notation
WeekDay(2)
# Dictionary notation
WeekDay["WEDNESDAY"]

for day in WeekDay:
    print(day.name, "->", day.value)

WeekDay.favorite_day()

print(WeekDay.FRIDAY)

# Simple Inheritance
# When you have a class that inherits from a single parent class, then you’re using single-base inheritance or just simple inheritance. To make a Python class inherit from another, you need to list the parent class’s name in parentheses after the child class’s name in the definition.

class Parent:
    # Parent's definition goes here...
    pass

class Child(Parent):
    # Child definitions goes here...
    pass


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._started = False

    def start(self):
        print("Starting engine...")
        self._started = True

    def stop(self):
        print("Stopping engine...")
        self._started = False
        
        
class Car(Vehicle):
    def __init__(self, make, model, year, num_seats):
        super().__init__(make, model, year)
        self.num_seats = num_seats

    def drive(self):
        print(f'Driving my "{self.make} - {self.model}" on the road')

    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_seats} seats'
    

tesla = Car("Tesla", "Model S", 2022, 5)
tesla.start()
tesla.drive()
tesla.stop()
print(tesla)

class Animal:
    def __init__(self, name, sex, habitat):
        self.name = name
        self.sex = sex
        self.habitat = habitat

class Mammal(Animal):
    unique_feature = "Mammary glands"

class Bird(Animal):
    unique_feature = "Feathers"

class Fish(Animal):
    unique_feature = "Gills"

class Dog(Mammal):
    def walk(self):
        print("The dog is walking")

class Cat(Mammal):
    def walk(self):
        print("The cat is walking")

class Eagle(Bird):
    def fly(self):
        print("The eagle is flying")

class Penguin(Bird):
    def swim(self):
        print("The penguin is swimming")

class Salmon(Fish):
    def swim(self):
        print("The salmon is swimming")

class Shark(Fish):
    def swim(self):
        print("The shark is swimming")
        
# Extended vs Overridden Methods

class Aircraft:
    def __init__(self, thrust, lift, max_speed):
        self.thrust = thrust
        self.lift = lift
        self.max_speed = max_speed

    def show_technical_specs(self):
        print(f"Thrust: {self.thrust} kW")
        print(f"Lift: {self.lift} kg")
        print(f"Max speed: {self.max_speed} km/h")

class Helicopter(Aircraft):
    def __init__(self, thrust, lift, max_speed, num_rotors):
        super().__init__(thrust, lift, max_speed)
        self.num_rotors = num_rotors

    def show_technical_specs(self):
        super().show_technical_specs()
        print(f"Number of rotors: {self.num_rotors}")

sikorsky_UH60 = Helicopter(1490, 9979, 278, 2)
sikorsky_UH60.show_technical_specs()


class Worker:
    def __init__(self, name, address, hourly_salary):
        self.name = name
        self.address = address
        self.hourly_salary = hourly_salary

    def show_profile(self):
        print("== Worker profile ==")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Hourly salary: {self.hourly_salary}")

    def calculate_payroll(self, hours=40):
        return self.hourly_salary * hours
    
class Manager(Worker):
    def __init__(self, name, address, hourly_salary, hourly_bonus):
        super().__init__(name, address, hourly_salary)
        self.hourly_bonus = hourly_bonus

    def calculate_payroll(self, hours=40):
        return (self.hourly_salary + self.hourly_bonus) * hours
    

class Vehicle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start(self):
        print("Starting the engine...")

    def stop(self):
        print("Stopping the engine...")

    def show_technical_specs(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")

class Car(Vehicle):
    def drive(self):
        print("Driving on the road...")

class Aircraft(Vehicle):
    def fly(self):
        print("Flying in the sky...")

class FlyingCar(Car, Aircraft):
    pass

space_flyer = FlyingCar("Space", "Flyer", "Black")
space_flyer.show_technical_specs()

space_flyer.start()

space_flyer.drive()

space_flyer.fly()

space_flyer.stop()


# Benefits of Using Inheritance
# Inheritance is a powerful tool that you can use to model and solve many real-world problems in your code. Some benefits of using inheritance include the following:

# Reusability: You can quickly inherit and reuse working code from one or more parent classes in as many subclasses as you need.
# Modularity: You can use inheritance to organize your code in hierarchies of related classes.
# Maintainability: You can quickly fix issues or add features to a parent class. These changes will be automatically available in all its subclasses. Inheritance also reduces code duplication.
# Polymorphism: You can create subclasses that can replace their parent class, providing the same or equivalent functionality.
# Extensibility: You can quickly extend an exiting class by adding new data and behavior to its subclasses.


class Stack:
    def __init__(self, items=None):
        self._items = [] if items is None else list(items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._items})"
    

stack = Stack([1, 2, 3])
stack

stack.push(4)
stack

stack.pop()
stack.pop()
stack

dir(stack)


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2
    
    def get_perimeter(self):
        return 2 * pi * self.radius
    
    
circle = Circle(100)
circle.radius

circle.get_area()
circle.get_perimeter()