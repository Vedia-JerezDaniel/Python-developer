def mysum(*args):
    total = 0
    for one_number in args:
        total += one_number
    return total


mysum(10, 20, 30)

# Again: args will always be a tuple. And it'll contain the positional arguments that didn't otherwise have a place to go. In this particular case, where there were no other parameters, all of the positional arguments were assigned to args. But we can have functions in which we do have other parameters:
    
def myfunc(a, b, *args):
    return f'{a=}, {b=}, {args=}'

myfunc(10, 20, 30, 40, 50, 60)

# When should you use *args? Whenever you aren't sure how many values you'll get, obviously. But here are some specific examples:
# You've written a method that adds any number of objects to a container
# You've written a function that works with any number of files
# You want to retrieve data from any number of URLs

def myfunc(a, b=999, *args):
    return f'{a=}, {b=}, {args=}'

myfunc(10)
myfunc(10,20)

def myfunc(a, b, **kwargs):
    return f'{a=}, {b=}, {kwargs=}'

myfunc(10, 20, x=30, y=40, z=50)
# kwargs is a dictionary 