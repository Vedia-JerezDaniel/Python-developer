# class Person:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.name = f"{self.first} {self.last}"

#     def set_first(self, first):
#         self.first = first
#         self.name = f"{self.first} {self.last}"

#     def set_last(self, last):
#         self.last = last
#         self.name = f"{self.first} {self.last}"


import datetime as dt


class Person:
    def __init__(self, first, last, birthdate):
        self.first = first
        self.last = last
        self.birthdate = birthdate

    @property
    def age(self):
        today = dt.date.today()
        current_year = today.year
        # Will the person still celebrate their birthday this current year?
        will_celebrate = self.birthdate.replace(year=current_year) > today
        return current_year - self.birthdate.year - will_celebrate

    @property
    def name(self):
        return f"{self.first} {self.last}"

john = Person("John", "Doe")


john.first = "Charles"
john.last = 'Doe'

john.get_name()


# When should I use a property?
# There is no hard rule for when you should use a property attribute versus a getter
# method. There seems to be some consensus, however, on some indicators of times 
# when it might be a good idea to use a property:

# the value can be computed fast (it would look weird to use dot notation to access 
# an attribute and then it takes a long time to return the value);
# the value is a piece of data intrinsically associated with the instance we are 
# talking about; and
# the value is a simple piece of data. (There is nothing against it, but it is not
# very common to see a property that returns a list of dictionaries whose keys are 
# strings and that map into triples of integers, Booleans, and file paths. 
# Properties tend to be relatively simple pieces of data.)
# The more you study and read code from others, the better your appreciation 
# will be for when to use properties. Don't be afraid to try them out, 
# and rest assured that it is not the end of the world if you use a property 
# in a place where you “shouldn't”.

# On top of the rules of thumb listed above, if you realise you need any of 
# the functionalities that will be listed next, then that might be an excellent 
# indicator of your need for a property.


class Person:
    def __init__(self, first):
        self._first = first

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, first_name):
        self._first = first_name.strip().capitalize()

    @first.deleter
    def first(self):
        del self._first
        

john = Person("John")
john.first
john.first = "CHArles"
john.first
del john.first

john.first