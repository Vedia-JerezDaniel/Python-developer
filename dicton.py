"""Sorting a Python Dictionary: Values, Keys, and More

from: https://realpython.com/sort-python-dictionary/
"""

people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

# Sort by key
dict(sorted(people.items()))

# Sort by value
dict(sorted(people.items(), key=lambda item: item[1]))

numbers = [5, 3, 4, 3, 6, 7, 3, 2, 3, 4, 1]
sorted(numbers)

words = ["aa", "ab", "ac", "ba", "cb", "ca"]
sorted(words)

def select_second_character(word):
    return word[1]

sorted(words, key=select_second_character)

numbers.sort(reverse=True) #inplace automatically

people[7] = "Joel"
people.items()

# Sort key
def value_getter(item):
    return item[1]

sorted(people.items(), key=value_getter)
# Or with a lambda function
sorted(people.items(), key=lambda item: item[1])

# Selecting a Nested Value With a Sort Key
data = {
    193: {"name": "John", "age": 30, "skills": {"python": 8, "js": 7}},
    209: {"name": "Bill", "age": 15, "skills": {"python": 6}},
    746: {"name": "Jane", "age": 58, "skills": {"js": 2, "python": 5}},
    109: {"name": "Jill", "age": 83, "skills": {"java": 10}},
    984: {"name": "Jack", "age": 28, "skills": {"c": 8, "assembly": 7}},
    765: {"name": "Penelope", "age": 76, "skills": {"python": 8, "go": 5}},
    598: {"name": "Sylvia", "age": 62, "skills": {"bash": 8, "java": 7}},
    483: {"name": "Anna", "age": 24, "skills": {"js": 10}},
    277: {"name": "Beatriz", "age": 26, "skills": {"python": 2, "js": 4}},
}

def get_relevant_skills(item):
    """Get the sum of Python and JavaScript skill"""
    skills = item[1]["skills"]
    # Return default value that is equivalent to no skill
    return skills.get("python", 0) + skills.get("js", 0)

print(sorted(data.items(), key=get_relevant_skills, reverse=True))

sorted(
    data.items(),
    key=lambda it: (
        it[1]["skills"].get("python", 0) + it[1]["skills"].get("js", 0)
    ), reverse=True,
)

sorted_people = sorted(people.items(), key=lambda it: it[1])

sorted_people_dict = {}
for key, value in sorted_people:
    sorted_people_dict[key] = value

sorted_people_dict


item = ("name", "Guido", 'age', 57)

from operator import itemgetter

getter = itemgetter(1)
getter(item)


fruit_inventory = [("banana", 5), ("orange", 15), ("apple", 3), ("kiwi", 0)]

# Sort by key
sorted(fruit_inventory, key=itemgetter(0))
# Sort by value
sorted(fruit_inventory, key=itemgetter(1))


from timeit import timeit

dict_to_order = {
    1: "requests",
    2: "pip",
    3: "jinja",
    4: "setuptools",
    5: "pandas",
    6: "numpy",
    7: "black",
    8: "pillow",
    9: "pyparsing",
    10: "boto3",
    11: "botocore",
    12: "urllib3",
    13: "s3transfer",
    14: "six",
    15: "python-dateutil",
    16: "pyyaml",
    17: "idna",
    18: "certifi",
    19: "typing-extensions",
    20: "charset-normalizer",
    21: "awscli",
    22: "wheel",
    23: "rsa",
}

sorted_with_lambda = "sorted(dict_to_order.items(), key=lambda item: item[0])"
sorted_with_itemgetter = "sorted(dict_to_order.items(), key=itemgetter(0))"

sorted_with_lambda_time = timeit(stmt=sorted_with_lambda, globals=globals())
sorted_with_itemgetter_time = timeit(
    stmt=sorted_with_itemgetter,  setup="itemgetter", globals=globals(),)

print(
    f"""\
{sorted_with_lambda_time=:.2f} seconds
{sorted_with_itemgetter_time=:.2f} seconds
itemgetter is {(
    sorted_with_lambda_time / sorted_with_itemgetter_time
):.2f} times faster"""
)

# Judging Whether You Want to Use a Sorted Dictionary

# List of tuples
tuople = [
    (3, "Jim"),
    (2, "Jack"),
    (4, "Jane"),
    (1, "Jill"), (5, "Joel")
]

# List of dictionaries
lile = [
    {"id": 3, "name": "Jim"},
    {"id": 2, "name": "Jack"},
    {"id": 4, "name": "Jane"},
    {"id": 1, "name": "Jill"}, {"id": 5, "name": "Joel"}
]


dictionary_of_dictionaries = {
    1: {"first_name": "Dorthea", "last_name": "Emmanuele", "age": 29},
    2: {"first_name": "Evelina", "last_name": "Ferras", "age": 91},
    3: {"first_name": "Frederica", "last_name": "Livesay", "age": 99},
    4: {"first_name": "Murray", "last_name": "Linning", "age": 36},
    5: {"first_name": "Annette", "last_name": "Garioch", "age": 93},
    6: {"first_name": "Rozamond", "last_name": "Todd", "age": 36},
    7: {"first_name": "Tiffi", "last_name": "Varian", "age": 28},
    8: {"first_name": "Noland", "last_name": "Cowterd", "age": 51},
    9: {"first_name": "Dyana", "last_name": "Fallows", "age": 100},
    10: {"first_name": "Diahann", "last_name": "Cutchey", "age": 44},
    11: {"first_name": "Georgianne", "last_name": "Steinor", "age": 32},
    12: {"first_name": "Sabina", "last_name": "Lourens", "age": 31},
    13: {"first_name": "Lynde", "last_name": "Colbeck", "age": 35},
    14: {"first_name": "Abdul", "last_name": "Crisall", "age": 84},
    15: {"first_name": "Quintus", "last_name": "Brando", "age": 95},
    16: {"first_name": "Rowena", "last_name": "Geraud", "age": 21},
    17: {"first_name": "Maurice", "last_name": "MacAindreis", "age": 83},
    18: {"first_name": "Pall", "last_name": "O'Cullinane", "age": 79},
    19: {"first_name": "Kermie", "last_name": "Willshere", "age": 20},
    20: {"first_name": "Holli", "last_name": "Tattoo", "age": 88}
}

list_of_dictionaries = [
    {"id": 1, "first_name": "Dorthea", "last_name": "Emmanuele", "age": 29},
    {"id": 2, "first_name": "Evelina", "last_name": "Ferras", "age": 91},
    {"id": 3, "first_name": "Frederica", "last_name": "Livesay", "age": 99},
    {"id": 4, "first_name": "Murray", "last_name": "Linning", "age": 36},
    {"id": 5, "first_name": "Annette", "last_name": "Garioch", "age": 93},
    {"id": 6, "first_name": "Rozamond", "last_name": "Todd", "age": 36},
    {"id": 7, "first_name": "Tiffi", "last_name": "Varian", "age": 28},
    {"id": 8, "first_name": "Noland", "last_name": "Cowterd", "age": 51},
    {"id": 9, "first_name": "Dyana", "last_name": "Fallows", "age": 100},
    {"id": 10, "first_name": "Diahann", "last_name": "Cutchey", "age": 44},
    {"id": 11, "first_name": "Georgianne", "last_name": "Steinor", "age": 32},
    {"id": 12, "first_name": "Sabina", "last_name": "Lourens", "age": 31},
    {"id": 13, "first_name": "Lynde", "last_name": "Colbeck", "age": 35},
    {"id": 14, "first_name": "Abdul", "last_name": "Crisall", "age": 84},
    {"id": 15, "first_name": "Quintus", "last_name": "Brando", "age": 95},
    {"id": 16, "first_name": "Rowena", "last_name": "Geraud", "age": 21},
    {"id": 17, "first_name": "Maurice", "last_name": "MacAindreis", "age": 83},
    {"id": 18, "first_name": "Pall", "last_name": "O'Cullinane", "age": 79},
    {"id": 19, "first_name": "Kermie", "last_name": "Willshere", "age": 20},
    {"id": 20, "first_name": "Holli", "last_name": "Tattoo", "age": 88}
]

sorting_list = "sorted(list_of_dictionaries, key=lambda item:item['age'])"
sorting_dict = """
dict(sorted(dictionary_of_dictionaries.items(), key=lambda item: item[1]['age']))"""

sorting_list_time = timeit(stmt=sorting_list, globals=globals())
sorting_dict_time = timeit(stmt=sorting_dict, globals=globals())

print(
    f"""\
{sorting_list_time=:.2f} seconds
{sorting_dict_time=:.2f} seconds
list is {(sorting_dict_time/sorting_list_time):.2f} times faster"""
)

# Comparing the Performance of Lookups

lookups = [15, 18, 19, 16, 6, 12, 5, 3, 9, 20, 2, 10, 13, 17, 4, 14, 11, 7, 8]

list_setup = """
def get_key_from_list(key):
    for item in list_of_dictionaries:
        if item["id"] == key:
            return item
"""

lookup_list = """
for key in lookups:
    get_key_from_list(key)
"""

lookup_dict = """
for key in lookups:
    dictionary_of_dictionaries[key]
"""

lookup_list_time = timeit(stmt=lookup_list, setup=list_setup, globals=globals())
lookup_dict_time = timeit(stmt=lookup_dict, globals=globals())

print(
    f"""\
{lookup_list_time=:.2f} seconds
{lookup_dict_time=:.2f} seconds
dict is {(lookup_list_time / lookup_dict_time):.2f} times faster"""
)


for key in lookups:
    dictionary_of_dictionaries[key]
    
    
def get_key_from_list(key):
    for item in list_of_dictionaries:
        if item["id"] == key:
            return item
for key in lookups:
    get_key_from_list(key)