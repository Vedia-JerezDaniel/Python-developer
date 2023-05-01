(42).__class__
"Hello, World!".__class__
[1, 2, 3].__class__


class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

john = Student("John", "Computer Science")
type(john)

john.__class__ = Person
type(john)

john.name
john.major

# INMUTABLE

letters = "a", "b", "c", "d"
type(letters)

# Mutable Built-in Data Types 
numbers = [1, 2, 314]
numbers[2] = 3  # Mutation
numbers

# Regular operator
numbers = [1, 2, 3] + [4, 5, 6]
numbers

# Augmented operator
numbers = [1, 2, 3]
numbers += [4, 5, 6]

numbers


inventory = {"apple": 100, "orange": 80, "banana": 120}
inventory

inventory["orange"] = 140  # Change
inventory

inventory["lemon"] = 200  # Add
inventory

del inventory["banana"]  # Remove
inventory


# Operation	Description
# a_dict.clear()	Removes all key-value pairs from a_dict.
# a_dict.pop(key[, default])	Removes the key-value pair 
# under key and returns the value, or default if the key doesn’t exist.
# a_dict.popitem()	Removes and returns the most recently added key-value
# pair as a tuple like (key, value).
# a_dict.setdefault(key[, default])	Inserts a new key-value pair with 
# default as its value and key as its key if key doesn’t exist. 
# Then returns the value associated with key.
# a_dict.update([other])	Updates the dictionary with the key-value 
# pairs from other, overwriting existing keys and creating new keys for missing ones.

## SETS
# Operation	Description
# a_set.add(element)	Adds element to a_set.
# a_set.update(*others)	Updates a_set, adding elements from one or more 
# sets unpacked from others. Equivalent to a_set |= other_1 | other_2 | ... | other_n.
# a_set.remove(element)	Removes element from a_set, raising a KeyError
# if element doesn’t exist.
# a_set.discard(element)	Removes element from a_set, skipping the KeyError
# if element doesn’t exist.
# a_set.pop()	Removes and returns an arbitrary element from a_set,
# raising a KeyError if the set is empty.
# a_set.clear()	Removes all elements from a_set.

fruits = {"apple", "orange", "banana"}
fruits.add("lemon")

fruits.add("orange")

fruits.update({"grape", "orange"})
fruits

fruits.remove("apple")
fruits

fruits.remove("mango")
fruits.discard("mango")
fruits

fruits.pop()

fruits


# Method	Description
# a_set.intersection_update(*others)	Updates a_set in place, 
# keeping only elements found in it and all others
# a_set.difference_update(*others)	Updates a_set in place, 
# removing elements found in others
# a_set.symmetric_difference_update(other)	Updates a_set in place, 
# keeping only elements found in either set but not in both

# Regular operators
{"apple", "orange"} | {"banana"}  # Union

f = {"apple", "orange"} & {"apple"}  # Intersection

{"apple", "orange"} - {"apple", "banana"}  # Difference
{"apple", "orange"} ^ {"apple", "banana"}  # Symmetric difference

# Augmented operators
fruits = {"apple", "orange"}

fruits |= {"banana"}  # Augmented union

fruits = {"apple", "orange"}
fruits &= {"apple"}  # Augmented intersection
fruits


number = 42
another_number = number
number += 1
number
another_number

fruits = ["apple"]
another_fruits = fruits
fruits += ["banana"]
fruits
another_fruits


def squares_of(numbers):
    return [number ** 2 for number in numbers]

sample = [2, 3, 4]
squares_of(sample)

counter = 0

def increment():
    global counter
    counter += 1

increment()
counter


def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target

append_to(1)
append_to(2)
append_to(3)


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    def __repr__(self):
        return f"{type(self).__name__}(x={self.x}, y={self.y})"


point = Point(21, 42)
point.x
point.y


class Coordinate:
    def __set_name__(self, owner, name):
        self._name = name
    def __get__(self, instance, owner):
        return instance.__dict__[f"_{self._name}"]
    def __set__(self, instance, value):
        raise AttributeError(f"can't set attribute '{self._name}'")

class Point:
    x = Coordinate()
    y = Coordinate()

    def __init__(self, x, y):
        self._x = x
        self._y = y
    def __repr__(self):
        return f"{type(self).__name__}(x={self.x}, y={self.y})"
    
    
point = Point(21, 42)
point.x
point.y

import math
from collections import namedtuple


class Point(namedtuple("Point", "x y")):
    __slots__ = ()

    def distance(self, other: "Point") -> float:
        return math.dist((self.x, self.y), (other.x, other.y))
    
origin = Point(0, 0)
point = Point(4, 3)
point.distance(origin)


from dataclasses import dataclass


@dataclass
class Color:
    red: int
    green: int
    blue: int

color = Color(255, 0, 0)
color

color.green = 128
color

color



