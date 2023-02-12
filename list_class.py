# https://realpython.com/inherit-python-list/
# Custom Python Lists: Inheriting From list vs UserList

# string_list.py

class StringList(list):
    def __init__(self, iterable):
        super().__init__(str(item) for item in iterable)

    def __setitem__(self, index, item):
        super().__setitem__(index, str(item))

    def insert(self, index, item):
        super().insert(index, str(item))

    def append(self, item):
        super().append(str(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(str(item) for item in other)
            

"""
.__init__ initializes all the class’s new instances.
.__setitem__() allows you to assign a new value to an existing item using the item’s index, 
like in a_list[index] = item.
.insert() allows you to insert a new item at a given position in the underlying list 
using the item’s index.
.append() adds a single new item at the end of the underlying list.
.extend() adds a series of items to the end of the list.
"""

data = StringList([1, 2, 2, 4, 5])
data

data.append(6)
data

data.insert(0, 0)
data

data.extend([7, 8, 9])
data

data[3] = 3
data


from collections import UserList

class StringList(UserList):
    def __init__(self, iterable):
        super().__init__(str(item) for item in iterable)

    def __setitem__(self, index, item):
        self.data[index] = str(item)

    def insert(self, index, item):
        self.data.insert(index, str(item))

    def append(self, item):
        self.data.append(str(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(str(item) for item in other)
            
        
data = StringList([1, 2, 2, 4, 5])
data

data.append(6)
data

data.insert(0, 0)
data

data.extend([7, 8, 9])
data

data[3] = 3
data        


# A List That Accepts Numeric Data Only

class NumberList(UserList):
    def __init__(self, iterable):
        super().__init__(self._validate_number(item) for item in iterable)

    def __setitem__(self, index, item):
        self.data[index] = self._validate_number(item)

    def insert(self, index, item):
        self.data.insert(index, self._validate_number(item))

    def append(self, item):
        self.data.append(self._validate_number(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(self._validate_number(item) for item in other)

    def _validate_number(self, value):
        if isinstance(value, (int, float, complex)):
            return value
        raise TypeError(f"numeric value expected, got {type(value).__name__}")

"""To validate the input data, you use a helper method called ._validate_number(). This method uses the built-in isinstance() function to check if the current input value is an instance of int, float, or complex, which are the built-in classes representing numeric values in Python.
"""        

numbers = NumberList([1.1, 2, 3j])
numbers

numbers.append("4.2")

numbers.append(4.2)
numbers

numbers.insert(0, "0")

numbers.insert(0, 0)
numbers

numbers.extend(["5.3", "6"])

numbers.extend([5.3, 6])
numbers


# A List With Additional Functionality

"""_summary_
.join() concatenates all the list’s items in a single string.
.map(action) yields new items that result from applying an action() callable to each item in the underlying list.
.filter(predicate) yields all the items that return True when calling predicate() on them.
.for_each(func) calls func() on every item in the underlying list to generate some side effect.
"""

class CustomList(list):
    def join(self, separator=" "):
        return separator.join(str(item) for item in self)

    def map(self, action):
        return type(self)(action(item) for item in self)

    def filter(self, predicate):
        return type(self)(item for item in self if predicate(item))

    def for_each(self, func):
        for item in self:
            func(item)


words = CustomList([
        "Hello,",
        "Pythonista!",
        "Welcome",
        "to",
        "Real",
        "Python!" ])

words.join()

words.map(str.upper)

words.filter(lambda word: word.startswith("Py"))

words.for_each(print)

