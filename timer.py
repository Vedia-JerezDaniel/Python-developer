snippet_1 = """
def traditional_loop():
    numbers = range(10)

    output = []
    for one_number in numbers:
        output.append(one_number ** 2)
    return output
traditional_loop()
"""

snippet_2 = """
def comprehension():
    numbers = range(10)

    return [one_number ** 2
            for one_number in numbers]
comprehension()
"""

import timeit

timeit.timeit(snippet_1, number=1_000_000,setup="""numbers=range(100)""")

timeit.timeit(snippet_2, number=1_000_000,setup="""numbers=range(100)""")



