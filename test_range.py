def range_contains(element, start, stop, step=1):
    return start <= element < stop and (element - start) % step == 0


range_contains(10,2,45,5)

numbers_as_range = range(10_000_000)
numbers_as_set = set(numbers_as_range)
numbers_as_dict = dict.fromkeys(numbers_as_range)

numbers_as_dict

from timeit import timeit
timeit("50 in numbers_as_dict", globals=globals(), number=100)

# dicts are faster than lists



