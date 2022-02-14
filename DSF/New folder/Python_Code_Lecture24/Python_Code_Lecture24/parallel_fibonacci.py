#coding: utf-8

import logging
import threading

from queue import Queue

fibo_dict = {}
shared_queue = Queue()
input_list = [3, 10, 5, 7]  # simulates user input

queue_condition = threading.Condition()


def fibonacci_task(condition):
    with condition:
        while shared_queue.empty():
            print("[%s] - waiting for elements in queue..." %
                  threading.current_thread().name)
            condition.wait()
        else:
            value = shared_queue.get()
            a, b = 0, 1
            for item in range(value):
                a, b = b, a + b
                fibo_dict[value] = a
            shared_queue.task_done()
            print("[%s] fibonacci of key [%d] with result [%d]" %
                  (threading.current_thread().name, value, fibo_dict[value]))


def queue_task(condition):
    print('Starting queue_task...')
    with condition:
        for item in input_list:
            shared_queue.put(item)
        print(
            "Notifying fibonacci_task threads that the queue is ready to consume..")
        condition.notifyAll()


threads = [threading.Thread(
    daemon=True, target=fibonacci_task, args=(queue_condition,)) for i in range(4)]

[thread.start() for thread in threads]

prod = threading.Thread(name='queue_task_thread', daemon=True,
                        target=queue_task, args=(queue_condition,))
prod.start()

[thread.join() for thread in threads]

print("[%s] - Result: %s" % (threading.current_thread().name, fibo_dict))
