# SuperFastPython.com
# example of a nested for-loop with separate thread pools
import time
import multiprocessing.pool
 
def task3(arg):
    print(f'\t\t>>>task3 {arg}')
    time.sleep(1)
 
# second level task
def task2(arg):
    print(f'\t>>task2 {arg}')
    time.sleep(1)
    with multiprocessing.pool.ThreadPool(3) as pool:
        pool.map(task3, range(2))
 
# top level task
def task1(arg):
    print(f'>task1 {arg}')
    time.sleep(1)
    with multiprocessing.pool.ThreadPool(3) as pool:
        pool.map(task2, range(3))
 
# protect the entry point
if __name__ == '__main__':
    with multiprocessing.pool.ThreadPool(5) as pool:
        pool.map(task1, range(5))
