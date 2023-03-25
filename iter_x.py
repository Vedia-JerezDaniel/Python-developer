def outer():
    counter = 0
    def inner():
        nonlocal counter
        counter += 1
        return counter
    return inner

func = outer()
i = iter(func, 5)

next(i)

def next_word(s):
    index = 0

    def wrapper():
        nonlocal index
        output = ''
        while index < len(s):
            current = s[index]
            index += 1
            if current == ' ':
                break
            output += current
        return output
    return wrapper

func = next_word('abcd ef ghij')
i = iter(func, '')
next(i)