import random

def getrand():
    n =  random.randint(0, 5)
    print(f'returning {n}')
    return n

i = iter(getrand, 3)

print(i)

for one_number in iter(getrand, 3):
    print(one_number)

