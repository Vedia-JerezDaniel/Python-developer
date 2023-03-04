# SuperFastPython.com
# example of a nested for-loop to use a single shared thread pool with a queue

import time
import threading
import multiprocessing.pool
import queue
 
# third level task
def task3(arg):
    print(f'\t\t>>>task3 {arg}')
    time.sleep(1)
 
# second level task
def task2(arg):
    global queue
    print(f'\t>>task2 {arg}')
    time.sleep(1)
    for i in range(2):
        queue.put((task3, (i,)))
 
# top level task
def task1(arg):
    global queue
    print(f'>task1 {arg}')
    time.sleep(1)
    for i in range(3):
        queue.put((task2, (i,)))
 
 
if __name__ == '__main__':
    global queue
    queue = queue.Queue()
    for i in range(5):
        queue.put((task1, (i,)))
    total_tasks = 50
    with multiprocessing.pool.ThreadPool(total_tasks) as pool:
        for _ in range(total_tasks):
            task, args = queue.get()
            pool.apply_async(task, args)
        pool.close()
        pool.join()
        
# global queue
# queue = queue.Queue()
# for i in range(5):
#     queue.put((task1, (i,)))
# total_tasks = 50
# with multiprocessing.pool.ThreadPool(total_tasks) as pool:
#     for _ in range(total_tasks):
#         task, args = queue.get()
#         pool.apply_async(task, args)
#     pool.close()
#     pool.join()