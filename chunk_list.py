# https://realpython.com/how-to-split-a-python-list-into-chunks/#split-a-python-list-into-a-fixed-number-of-chunks

import numpy as np
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

np.split(numbers, 2)

np.split(numbers, 3)

np.array_split(numbers, 3)

numbers

np.array_split(numbers, [3, 6, 9])


def split_with_numpy(numbers, chunk_size):
    indices = np.arange(chunk_size, len(numbers), chunk_size)
    return np.array_split(numbers, indices)

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

split_with_numpy(numbers, 3)
split_with_numpy(numbers, 4)
split_with_numpy(numbers, 5)

import sys
from itertools import islice, zip_longest

# ...

def split_into_pairs(iterable, fill_value=None):
    iterator = iter(iterable)
    return zip_longest(iterator, iterator,fillvalue=fill_value)

def split_drop_last(iterable, chunk_size):
    return zip(*[iter(iterable)] * chunk_size)

def split_sequence(sequence, chunk_size):
    for i in range(0, len(sequence), chunk_size):
        yield sequence[i: i + chunk_size]

for chunk in split_drop_last("ABCDEFGHIJ", 4):
    print(chunk)
    
for chunk in split_drop_last("ABCDEFGHIJ", 3):
    print(chunk)
    
for chunk in split_sequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4):
    print(chunk)



numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

a =np.array_split(numbers, 2)

from itertools import cycle, zip_longest

def split_round_robin(iterable, num_chunks):
    chunks = [[] for _ in range(num_chunks)]
    index = cycle(range(num_chunks))
    for value in iterable:
        chunks[next(index)].append(value)
    return chunks

for chunk in zip_longest(*split_round_robin("ABCDEFGHIJ", 4)):
    print(chunk)
    
    # spatial_splitting.py

from math import floor, sqrt

def find_divisors(number):
    divisors = {1, number}
    for divisor in range(2, floor(sqrt(number)) + 1):
        factor, remainder = divmod(number, divisor)
        if remainder == 0:
            divisors.add(divisor)
            divisors.add(factor)
    return divisors

find_divisors(25)

def get_slices(length, num_chunks):
    chunk_size, remaining = divmod(length, num_chunks)
    for i in range(num_chunks):
        begin = i * chunk_size + min(i, remaining)
        end = (i + 1) * chunk_size + min(i + 1, remaining)
        yield slice(begin, end)
        
for _ in get_slices(10, 3):
    print(_)