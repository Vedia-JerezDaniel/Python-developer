# https://superfastpython.com/parallel-nested-for-loops-in-python/

# SuperFastPython.com
# example of a nested for-loop to use a single shared thread pool
import time
import multiprocessing.pool
 
def task3(arg):
    print(f'\t\t>>>task3 {arg}')
    time.sleep(1)
 
def task2(arg):
    global pool
    print(f'\t>>task2 {arg}')
    time.sleep(1)
    pool.map(task3, range(2))
 
def task1(arg):
    global pool
    print(f'>task1 {arg}')
    time.sleep(1)
    pool.map(task2, range(3))
 
if __name__ == '__main__':
    global pool
    pool = multiprocessing.pool.ThreadPool(50)
    pool.map(task1, range(5))
    pool.close()