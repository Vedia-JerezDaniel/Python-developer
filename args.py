# *args and **kwargs
# *args in the function definition

def add(*numbers):  
    sum = 0
    for number in numbers:
        sum += number
    return sum

# * in the function call

def add(number_1, number_2, number_3):
    return number_1 + number_2 + number_3

my_list = [1, 2, 3]
add(*my_list)

# Constructing lists
my_list_1 = [1, 2, 3]
my_list_2 = [10, 20, 30]

some_value = 42
merged_list = [*my_list_1, some_value, *my_list_2]
merged_list

social_media_details = {'twitter': 'bascodes'}
contact_details = {'email': 'blog@bascodes.example.com'}
user_dict = {'username': 'bas', **social_media_details, **contact_details}

user_dict

# Destructuring lists
# You might already know, that you can split elements of a list to multiple variables like so:

my_list = [1, 2, 3]
a, b, c = my_list
print(a, b, c)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a, *b, c = my_list
print(a, b, c)

