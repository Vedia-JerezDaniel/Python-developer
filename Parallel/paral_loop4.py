# SuperFastPython.com
# example of a nested for-loop with a shared process pool
import time
import multiprocessing
 
# third level task
def task3(arg):
    print(f'\t\t>>>task3 {arg}', flush=True)
    time.sleep(1)
 
# second level task
def task2(arg, pool):
    print(f'\t>>task2 {arg}', flush=True)
    time.sleep(1)
    pool.map(task3, range(2))
 
# top level task
def task1(arg, pool):
    print(f'>task1 {arg}', flush=True)
    time.sleep(1)
    args = [(i, pool) for i in range(3)]
    pool.starmap(task2, args)
 
# protect the entry point
if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        with manager.Pool(50) as pool:
            args = [(i, pool) for i in range(5)]
            pool.starmap(task1, args)