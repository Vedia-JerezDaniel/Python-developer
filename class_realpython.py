# Python Class Constructors: Control Your Object Instantiation
# Real Python

https://realpython.com/python-class-constructor/


class Point:
    def __new__(cls, *args, **kwargs):
        print("1. Create a new instance of Point.")
        return super().__new__(cls)

    def __init__(self, x, y):
        print("2. Initialize the new instance of Point.")
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x}, y={self.y})"
    
    
p = Point(1, 2)
p

p1 =p.__init__(3, 4)
p2 = p.__new__(Point, 5, 6)
print(p)

p1 =p2.__init__(5, 46)
print(p2)



class A:
    def __init__(self, a_value):
        print("Initialize the new instance of A.")
        self.a_value = a_value

class B:
    def __new__(cls, *args, **kwargs):
        print(*args, **kwargs)

    def __init__(self, b_value):
        print("Initialize the new instance of B.")
        self.b_value = b_value

b = B(45,88,5,8,9)

b.__init__(45)

c = B.__init__(A, 555)
A.b_value


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rectangle = Rectangle(21, 42)
rectangle.width
rectangle.height


class Rectangle:
    def __init__(self, width, height):
        if not (isinstance(width, (int, float)) and width > 0):
            raise ValueError(f"positive width expected, got {width}")
        self.width = width
        if not (isinstance(height, (int, float)) and height > 0):
            raise ValueError(f"positive height expected, got {height}")
        self.height = height

rectangle = Rectangle(15.8, 42)
rectangle.width
rectangle.height


class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

class Employee(Person):
    def __init__(self, name, birth_date, position):
        super().__init__(name, birth_date)
        self.position = position

john = Employee("John Doe", "2001-02-07", "Python Developer")

john.name
john.birth_date
john.position


class Greeter:
    def __init__(self, name, formal=False):
        self.name = name
        self.formal = formal

    def greet(self):
        if self.formal:
            print(f"Good morning, {self.name}!")
        else:
            print(f"Hello, {self.name}!")
       
           
informal_greeter = Greeter("Pythonista")
informal_greeter.greet()

formal_greeter = Greeter("Pythonista", formal=True)
formal_greeter.greet() 


class SomeClass:
    def __init__(self, value):
        self.value = value

some_obj = SomeClass(42)
some_obj

some_obj.value


class Distance(float):
    def __new__(cls, value, unit):
        instance = super().__new__(cls, value)
        instance.unit = unit
        return instance

in_miles = Distance(42.0, "Miles")
in_miles

in_miles.real
in_miles.unit
in_miles + 42.0

dir(in_miles)


from random import choice

class Pet:
    def __new__(cls):
        other = choice([Dog, Cat, Python])
        instance = super().__new__(other)
        print(f"I'm a {type(instance).__name__}!")
        return instance

class Dog:
    def communicate(self):
        print("woof! woof!")
class Cat:
    def communicate(self):
        print("meow! meow!")
class Python:
    def communicate(self):
        print("hiss! hiss!")
        
        
pet = Pet()
pet.communicate()

isinstance(pet, Pet)
isinstance(pet, Dog)

another_pet = Pet()
another_pet.communicate()


class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


first = Singleton('a')
second = Singleton()
first is second


from operator import itemgetter

def named_tuple_factory(type_name, *fields):
    num_fields = len(fields)

    class NamedTuple(tuple):
        __slots__ = ()

        def __new__(cls, *args):
            if len(args) != num_fields:
                raise TypeError(
                    f"{type_name} expected exactly {num_fields} arguments,"
                    f" got {len(args)}")
            cls.__name__ = type_name
            for index, field in enumerate(fields):
                setattr(cls, field, property(itemgetter(index)))
            return super().__new__(cls, args)

        def __repr__(self):
            return f"""{type_name}({", ".join(repr(arg) for arg in self)})"""

    return NamedTuple


Point = named_tuple_factory("Point", "x", "y")

point = Point(21, 42)
point

point.x
point.y

point[0]
point[1]

point.x = 84
dir(point)