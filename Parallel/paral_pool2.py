# SuperFastPython.com
# example of a nested for-loop to use a single shared thread pool with a queue unbounded
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
    global task_queue, counter
    print(f'\t>>task2 {arg}')
    time.sleep(1)
    for i in range(2):
        task_queue.put((task3, (i,)))
    counter.release(n=2)
 
# top level task
def task1(arg):
    global task_queue, counter
    print(f'>task1 {arg}')
    time.sleep(1)
    for i in range(3):
        task_queue.put((task2, (i,)))
    counter.release(n=3)
 
# callback on all tasks in the thread pool
def callback(arg):
    global counter
    counter.acquire()
 
# protect the entry point
if __name__ == '__main__':
    global task_queue
    task_queue = queue.Queue()
    for i in range(5):
        task_queue.put((task1, (i,)))
    global counter
    counter = threading.Semaphore(5)
    with multiprocessing.pool.ThreadPool(30) as pool:
        while True:
            with counter._cond:
                if not counter._value:
                    break
            try:
                task, args = task_queue.get(timeout=1)
            except queue.Empty:
                continue
            async_result = pool.apply_async(task, args, callback=callback)
        pool.close()
        pool.join()