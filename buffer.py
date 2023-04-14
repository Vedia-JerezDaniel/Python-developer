from time import sleep

# overwrites and pre-define print flush to True always
import functools
print = functools.partial(print, flush=True)

# Flush only works for this case
for second in range(3, 0, -1):
    print(f"{second}\n", flush=False)
    sleep(1)
print("Go!")



# Not here
for second in range(3, 0, -1):
    print(second)
    sleep(1)
print("Go!")