# FROM https://realpython.com/solid-principles-python/

from pathlib import Path
from zipfile import ZipFile

# Single-Responsibility Principle (SRP)
# The single-responsibility principle (SRP) comes from Robert C. Martin, more commonly known by his nickname Uncle Bob, who’s a well-respected figure in the software engineering world and one of the original signatories of the Agile Manifesto. In fact, he coined the term SOLID.


class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
            
# The concept of responsibility in this context may be pretty subjective. Having a single responsibility doesn’t necessarily mean having a single method. Responsibility isn’t directly tied to the number of methods but to the core task that your class is responsible for, depending on your idea of what the class represents in your code. However, that subjectivity shouldn’t stop you from striving to use the SRP.

# Open-Closed Principle (OCP)

# Having to make these changes to create new shapes means that your class is open to modification. That violates the open-closed principle. How can you fix your class to make it open to extension but closed to modification? Here’s a possible solution:

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2
    

# Liskov Substitution Principle (LSP)

# In practice, this principle is about making your subclasses behave like their base classes without breaking anyone’s expectations when they call the same methods. To continue with shape-related examples, say you have a Rectangle class like the following:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["height"] = value
            

square = Square(5)
vars(square)

square.width = 7
vars(square)

square.height = 9
vars(square)

square.calculate_area()


def get_total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)

get_total_area([Rectangle(10, 5), Square(5)])

# Interface Segregation Principle (ISP)

# Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, not to hierarchies.

# In this case, clients are classes and subclasses, and interfaces consist of methods and attributes. In other words, if a class doesn’t use particular methods or attributes, then those methods and attributes should be segregated into more specific classes.

from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")
        
# Dependency Inversion Principle (DIP)

# The dependency inversion principle (DIP) is the last principle in the SOLID set. This principle states that:

# Abstractions should not depend upon details. Details should depend upon abstractions.

# To fix the issue, you can apply the dependency inversion principle and make your classes depend on abstractions rather than on concrete implementations like BackEnd. In this specific example, you can introduce a DataSource class that provides the interface to use in your concrete classes:


from abc import ABC, abstractmethod


class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):
        return "Data from the API"
    
# In this redesign of your classes, you’ve added a DataSource class as an abstraction that provides the required interface, or the .get_data() method. Note how FrontEnd now depends on the interface provided by DataSource, which is an abstraction.

# Then you define the Database class, which is a concrete implementation for those cases where you want to retrieve the data from your database. This class depends on the DataSource abstraction through inheritance. Finally, you define the API class to support retrieving the data from the REST API. This class also depends on the DataSource abstraction.

db_front_end = FrontEnd(Database())
db_front_end.display_data()

api_front_end = FrontEnd(API())
api_front_end.display_data()