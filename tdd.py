# Build a Hash Table in Python With TDD
# Real Python

https://realpython.com/python-hash-table/

glossary = {"BDFL": "Benevolent Dictator For Life"}
glossary["GIL"] = "Global Interpreter Lock"  # Add
glossary["BDFL"] = "Guido van Rossum"  # Update
del glossary["GIL"]  # Delete
glossary["BDFL"]  # Search

glossary


import string
text = string.ascii_uppercase * 50

text[:50]  # Show the first 50 characters

len(text)

text[0]  # The first element
text[len(text) // 2]  # The middle element
text[-1]  # The last element, same as text[len(text) - 1]

hash(2.0001)
id(2.0001)
hash('Hola Daniel''Bienvenido a la clase de Python')

def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])

def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")
        
from string import printable
from collections import Counter

plot(distribute(printable, 10))

def hash_function(text):
    return sum(ord(character) for character in repr(text))

hash_function("Hola Daniel")
hash_function("Hola Dan")


def hash_function(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key).lstrip("'"), start=1))
    
hash_function("Tiny")
hash_function("This has a somewhat medium length.")
hash_function("This is very long and slow!" * 1_000_000)

plot(distribute(printable, 10, hash_function))


def test_should_always_pass():
    assert 2 == 20, "This is just a dummy test"
    

class HashTable:
    def __init__(self, capacity):
        self.values = capacity * [None]
    def __len__(self):
        return len(self.values)
    def __setitem__(self, key, value):
        self.values.append(value)
    
def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None
    
test_should_create_hashtable()

def test_capacity():
    assert len(HashTable(capacity=100)) == 100
    
test_capacity()

def test_should_insert_key_value_pairs():
    hash_table = HashTable(capacity=100)

    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True

    assert "hello" in hash_table.values
    assert 37 in hash_table.values
    assert True in hash_table.values
    
test_should_insert_key_value_pairs()