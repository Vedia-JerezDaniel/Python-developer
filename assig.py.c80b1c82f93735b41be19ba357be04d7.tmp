# https://realpython.com/python-assignment-operator/

counter = 0
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32
user_template = {"id": None, "name": "", "permissions": ("r",)}
welcome_message = "Welcome to Real Python!"
is_empty = False

user_template

letter_counter = word_counter = 0
id(letter_counter) == id(word_counter)

n = 300
m = 300
id(n) == id(m)

x = y = 300
id(x) == id(y)

from platform import python_version

interning = [x for x, y in zip(range(5), range(15)) if x == y]

print(f"Interning interval for Python {python_version()} is: "f" [{interning[0]} to {interning[-1]}]")


letters = ["A", "b", "c", "D"]
letters[1:3] = ["B", "C"]
letters

letters[3:] = ("F", "G")
letters

letters[3:3] = ["D"]
letters

letters[1::2] = ["b", "d", "g"]
letters

inventory = {"apple": 100, "orange": 80, "banana": 120}
inventory

inventory["orange"] = 140
inventory

a,v,b, = [],[],[]


from math import sqrt

a, b, c = 2.0, -1.0, -4.0

x1, x2 = ((-b - sqrt(b**2 - 4 * a * c)) / (2 * a),
    (-b + sqrt(b**2 - 4 * a * c)) / (2 * a),)

f"{x1=}, {x2=}"



def bubble_sort_list(a_list):
    n = len(a_list)
    for i in range(n):
        is_sorted = True
        for j in range(n - i - 1):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                is_sorted = False
        if is_sorted:
            break
    return a_list


a = bubble_sort_list([1, 3, 2, 4, 7, 6, 3, 8, 9, 1])

a

head, *bo, tail = a
print(head,*bo)

*_, last = a


class User:
    pass

users: list[User] = []
users

"""Now you’re clearly communicating that users will hold a list of User instances. Using type hints in assignment statements that initialize variables to empty collection data types—such as lists, tuples, or dictionaries—allows you to provide more context about how your code works. This practice will make your code more explicit and less error-prone.
"""

class Point:

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
        except ValueError:
            raise ValueError('"x" must be a number') from None

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        try:
            self._y = float(value)
        except ValueError:
            raise ValueError('"y" must be a number') from None


# from point import Point

point_1 = Point()
point_1.x = 1
point_1.y = 2
point_1.x, point_1.y

point_2 = Point()
point_2.x = "one"


from collections import UserDict

class LowerCasedDict(UserDict):
    def __setitem__(self, key, value):
        key = key.lower()
        super().__setitem__(key, value)


numbers = LowerCasedDict()
numbers["ONE"] = 1
numbers["Two"] = 2
numbers["Three"] = 3

numbers


def greet(name):
   print(id(name))
   print(f"Hello, {name}!")

greet

id(greet)

fellow = "Pythonista"
greet(fellow)

id(fellow)



