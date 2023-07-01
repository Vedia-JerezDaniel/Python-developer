# FROM https://realpython.com/python-iterators-iterables/

class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration
        item = self._sequence[self._index]
        self._index += 1
        return item
    
for item in SequenceIterator([1, 2, 3, 4]):
    print(item)
    
sequence = SequenceIterator([1, 2, 3, 4])
# Get an iterator over the data
iterator = sequence.__iter__()
while True:
    try:
        # Retrieve the next item
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

class SquareIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration
        square = self._sequence[self._index] ** 2
        self._index += 1
        return square
    
class FibonacciIterator:
    def __init__(self, stop=10):
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= self._stop:
            raise StopIteration
        self._index += 1
        fib_number = self._current
        self._current, self._next = (
            self._next, self._current + self._next,)
        return fib_number
    
for fib_number in FibonacciIterator():
    print(fib_number)
    
def fibonacci_generator(stop=10):
    current_fib, next_fib = 0, 1
    index = 0
    while True:
        if index == stop:
            return
        index += 1
        fib_number = current_fib
        current_fib, next_fib = next_fib, current_fib + next_fib
        yield fib_number
    
list(fibonacci_generator(15))

# Returning Iterators Instead of Container Type
def square_list(sequence):
    return [item**2 for item in sequence]

numbers = [1, 2, 3, 4, 5]
square_list(numbers)

def to_square(numbers):
    return (number**2 for number in numbers)
def to_cube(numbers):
    return (number**3 for number in numbers)
def to_even(numbers):
    return (number for number in numbers if number % 2 == 0)
def to_odd(numbers):
    return (number for number in numbers if number % 2 != 0)
def to_string(numbers):
    return (str(number) for number in numbers)

sample = range(20)

list(to_string(to_square(to_even(range(20)))))
list(to_string(to_cube(to_odd(range(20)))))

## Understanding Some Constraints of Python Iterators
numbers_iter = SequenceIterator([1, 2, 3, 4])

for number in numbers_iter:
    print(number)

#* esto ya no corre porque el iterador ya se agoto
for number in numbers_iter:
    print(number)

numbers_iter = SequenceIterator([1, 2, 3, 4,5,6,7])

for number in numbers_iter:
    if number == 4:
        break
    print(number)

next(numbers_iter)
next(numbers_iter)
next(numbers_iter)

# es reusable pero no vale la pena
class ReusableRange:
    def __init__(self, start=0, stop=10, step=1):
        if stop is None:
            stop, start = start, 0
        self._range = range(start, stop, step)
        self._iter = iter(self._range)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self._iter)
        except StopIteration:
            self._iter = iter(self._range)
            raise

numbers = ReusableRange(5)
list(numbers)
