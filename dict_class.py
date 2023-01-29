import contextlib

class UpperCaseDict(dict):
    def __init__(self, mapping=None, /, **kwargs):
        if mapping is not None:
            mapping = {
                str(key).upper(): value for key, value in mapping.items()
            }
        else:
            mapping = {}
        if kwargs:
            mapping |= {str(key).upper(): value for key, value in kwargs.items()}
        super().__init__(mapping)

    def __setitem__(self, key, value):
        key = key.upper()
        super().__setitem__(key, value)


from collections import UserDict

class UpperCaseDict(UserDict):
    def __setitem__(self, key, value):
        key = key.upper()
        super().__setitem__(key, value)
        
        
numbers = UpperCaseDict({"one": 1, "two": 2})

numbers["three"] = 3
numbers.update({"four": 4})
numbers.setdefault("five", 5)

numbers

        """The .__setitem__() method will allow you to always store keys in American English.
        The .__getitem__() method will make it possible to retrieve the value associated with a given key, whether it’s spelled in American or British English.
        """

from collections import UserDict
import contextlib

UK_TO_US = {"colour": "color", "flavour": "flavor", "behaviour": "behavior"}

class EnglishSpelledDict(UserDict):
    def __getitem__(self, key):
        with contextlib.suppress(KeyError):
            return self.data[key]
        with contextlib.suppress(KeyError):
            return self.data[UK_TO_US[key]]
        raise KeyError(key)

    def __setitem__(self, key, value):
        with contextlib.suppress(KeyError):
            key = UK_TO_US[key]
        self.data[key] = value
        
# Alternative solution avoiding the use of .data()
# class EnglishSpelledDict(UserDict):
#     def __getitem__(self, key):
#         with contextlib.suppress(KeyError):
#             return super().__getitem__(key)
#         with contextlib.suppress(KeyError):
#             return super().__getitem__(UK_TO_US[key])
#         raise KeyError(key)

#     def __setitem__(self, key, value):
#         with contextlib.suppress(KeyError):
#             key = UK_TO_US[key]
#         super().__setitem__(key, value)
        
likes = EnglishSpelledDict({"color": "blue", "flavour": "vanilla"})
likes

likes["flavour"]
likes["flavor"]

likes["behaviour"] = "polite"
likes

likes.get("colour")
likes.get("color")

likes.update({"behaviour": "gentle"})
likes

# A Dictionary That Accesses Keys Through Values

class ValueDict(dict):
    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k
        raise ValueError(value)

    def keys_of(self, value):
        for k, v in self.items():
            if v == value:
                yield k
                

inventory = ValueDict()
inventory["apple"] = 2
inventory["banana"] = 3
inventory.update({"orange": 2})

inventory

inventory.key_of(2)
inventory.key_of(3)

list(inventory.keys_of(2))

class ExtendedDict(dict):
    def apply(self, action):
        for key, value in self.items():
            self[key] = action(value)

    def remove(self, key):
        del self[key]

    def is_empty(self):
        return len(self) == 0
    
numbers = ExtendedDict({"one": 1, "two": 2, "three": 3})
numbers

numbers.apply(lambda x: x**2)
numbers

numbers.remove("two")
numbers

numbers.is_empty()

class ExtendedDict_UserDict(UserDict):
    def apply(self, action):
        for key, value in self.items():
            self[key] = action(value)

    def remove(self, key):
        del self[key]

    def is_empty(self):
        return len(self) == 0
    
    """The only difference between these two classes is that ExtendedDict_dict subclasses dict, and ExtendedDict_UserDict subclasses UserDict.

To check their performance, you can start by timing core dictionary operations, such as class instantiation. Run the following code in your Python interactive session:
        """    
    
import timeit

init_data = dict(zip(range(10000), range(10000)))

dict_initialization = min(
    timeit.repeat(
        stmt="ExtendedDict(init_data)",
        number=10000,
        repeat=5,
        globals=globals(),    ))

user_dict_initialization = min(
    timeit.repeat(
        stmt="ExtendedDict_UserDict(init_data)",
        number=10000,
        repeat=5,
        globals=globals(),    ))

print(
    f"UserDict is {user_dict_initialization / dict_initialization:.3f}",
    "times slower than dict",)