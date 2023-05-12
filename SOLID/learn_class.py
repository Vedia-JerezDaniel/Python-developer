# LEARNING CLASSES
# https://realpython.com/python-classes/#getting-started-with-python-classes

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

