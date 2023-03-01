# fizzbuzz.py

# Replace numbers that are divisible by 3 with "fizz"
def fizzbuzz(numbers):
    """Implement the Fizz buzz game.

    >>> fizzbuzz([3, 6, 9, 12])
    ['fizz', 'fizz', 'fizz', 'fizz']
    """
    result = []
    for number in numbers:
        if number % 3 == 0:
            result.append("fizz")
        else:
            result.append(number)
    return result