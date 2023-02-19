from dataclasses import dataclass

@dataclass
class Person:
    name : str
    age : int
    location : str
    
p1 = Person('Dennis', 42, 'Helsinki')
p2 = Person('Daniel', 35, 'Palma')

print(f"{p2.name} is a nice boy, he is {p2.age} years old and lives in {p2.location}, and he needs to smile more.")