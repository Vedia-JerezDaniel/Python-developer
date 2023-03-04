# SuperFastPython.com
# example of a nested for-loop to use a single shared process pool with a queue unbounded
import time
import queue
import multiprocessing
import multiprocessing.managers
 
# custom counter class
class SafeCounter():
    def __init__(self, count):
        self._lock = multiprocessing.Lock()
        self._value = count
    def is_zero(self):
        with self._lock:
            return self._value == 0
    def increment(self, value=1):
        with self._lock:
            self._value += value
    def decrement(self, value=1):
        with self._lock:
            self._value -= value
 
# custom manager to support custom classes
class CustomManager(multiprocessing.managers.BaseManager):
    pass
 
# third level task
def task3(arg, task_queue, counter):
    print(f'\t\t>>>task3 {arg}', flush=True)
    time.sleep(1)
    counter.decrement()
 
# second level task
def task2(arg, task_queue, counter):
    print(f'\t>>task2 {arg}', flush=True)
    time.sleep(1)
    for i in range(2):
        task_queue.put((task3, (i,task_queue,counter)))
        counter.increment()
    counter.decrement()
 
# top level task
def task1(arg, task_queue, counter):
    print(f'>task1 {arg}', flush=True)
    time.sleep(1)
    for i in range(3):
        task_queue.put((task2, (i,task_queue,counter)))
        counter.increment()
    counter.decrement()
 
# protect the entry point
if __name__ == '__main__':
    CustomManager.register('SafeCounter', SafeCounter)
    CustomManager.register('Queue', multiprocessing.Queue)
    # create manager
    with CustomManager() as manager:
        task_queue = manager.Queue()
        counter = manager.SafeCounter(5)
        for i in range(5):
            task_queue.put((task1, (i,task_queue,counter)))
        # create a process pool, local to the main thread/process
        with multiprocessing.Pool(50) as pool:
            # loop over all known tasks
            while not counter.is_zero():
                try:
                    task, args = task_queue.get(timeout=1)
                except queue.Empty:
                    continue
                async_result = pool.apply_async(task, args)
            pool.close()
            pool.join()