nu = (1, 'F')


from typing import Callable

def add_one(i: int) -> int:
    return i + 1

def multiply_with(x: int, y: int) -> int:
    return x * y

def as_pixels(i: int) -> str:
    return f"{i}px"

def calculate(i: int, action: Callable[..., int], *args: int) -> int:
    return action(i, *args)

# Works:
calculate(1, add_one)
calculate(1, multiply_with, 3)

# Use ellipsis to slice in Numpy

import numpy as np

dimensions = 3
items_per_dimension = 4
max_items = items_per_dimension**dimensions
axes = np.repeat(items_per_dimension, dimensions)
arr = np.arange(max_items).reshape(axes)
arr

arr[:,:,2]

