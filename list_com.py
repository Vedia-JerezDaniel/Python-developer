# Python List Comprehensions Are More Powerful Than You Might Think

# from https://betterprogramming.pub/python-list-comprehensions-are-more-powerful-than-you-might-think-3363a90e5bb0

values = [True, False, True, None, True]

print(['yes' if v is True else 'no' if v is False else 'unknown' for v in values])
# ['yes', 'no', 'yes', 'unknown', 'yes']

# Above is equivalent to:
result = []
for v in values:
    if v is True:
        result.append('yes')
    elif v is False:
        result.append('no')
    else:
        result.append('unknown')

print(result)
# ['yes', 'no', 'yes', 'unknown', 'yes']


print([i for i in range(200) if i > 10 if i < 20 if i % 2])

result = [i for i in range(200) if i > 10 and i < 20 and i % 2]
print(result)
# [11, 13, 15, 17, 19]
print([i for i in range(20) if i % 2])

def func(val):
    return val > 4

values = [1, 4, 3, 5, 12, 9, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,5,78,484,64]
print([func(x) for x in values if func(x)]) 

print([y for y in (func(x) for x in values) if y])

print([y for x in values if (y := func(x))])


def catch(f, *args, handle=lambda e: e, **kwargs):
    try:
        return f(*args, **kwargs)
    except Exception as e:
        return handle(e)


values = [1, "text", 2, 5, 1, "also-text"]
print([catch(int, value) for value in values])
print([catch(lambda: int(value)) for value in values])  # Alternative syntax

# Breaking the Loop

print(list(iter(iter(range(10)).__next__, 4)))

from itertools import takewhile
print(list(takewhile(lambda x: x < 4, range(10))))

import datetime
import more_itertools

dates = [
    datetime.datetime(2020, 1, 15),
    datetime.datetime(2020, 1, 16),
    datetime.datetime(2020, 1, 17),
    datetime.datetime(2020, 2, 1),
    datetime.datetime(2020, 2, 2),
    datetime.datetime(2020, 2, 4)
]

groups = [list(group) for group in more_itertools.consecutive_groups(dates, ordering=lambda d: d.toordinal())]

groups


from itertools import accumulate

data = [4, 5, 12, 8, 1, 10, 21]
cumulative = list(accumulate(data, initial=100))
print(cumulative)
# [100, 104, 109, 121, 129, 130, 140, 161]
print([y - x for x, y in more_itertools.pairwise(cumulative)])


# Only returns boolean, not the values
print(any(data > 10 for data in data))  # True
print(all(data < 10 for data in data))  # False

any((value := data) > 8 for data in data)
a = [value]
print(value,a)  # 12

any((counter_example := data) < 8 for data in data)  # False
print(counter_example)  # 12