# """Stop all threads for 5 seconds if some condition happens."""
# import random
# import threading
# import time

# def safe_write(s, lock=threading.Lock()):
#     with lock:
#         print(s, end="", flush=True)

# def worker(char, started: threading.Event, lock=threading.Lock()):
#     while started.wait():
#         safe_write(char)  # do some work
#         if random.random() < .025:  # if some condition
#             # pause for 5 seconds
#             with lock:  # the pauses are consecutive if the condition
#                 # triggers in more than one thread
#                 started.clear()  # this stops cycles in all threads
#                 try:
#                     safe_write(" wait")
#                     for c in ".....":
#                         safe_write(c)
#                         time.sleep(1)
#                     safe_write("continue\n")
#                 finally:
#                     started.set()  # start the cycles again
#         else:
#             time.sleep(.1)

# started = threading.Event()
# for char in "12345":
#     threading.Thread(target=worker, args=[char, started], daemon=True).start()

# print("Press Enter to exit", flush=True)
# started.set()  # start all cycles
# input()

import time
from threading import Thread

class SetInterval(Thread):
    def __init__(self, func, interval):
        super().__init__()
        self.daemon = True
        self._on = True
        self.func = func
        self.interval = interval
        self.start()

    def run(self):
        while self._on:
            self.func(*args, **kwargs)
            time.sleep(self.interval)

    def stop(self):
        self._on = False

p = lambda: print('Hello')
periodic = SetInterval(func,  ,interval=1)
time.sleep(5.1)
periodic.stop()
time.sleep(2)
print('Main thread has finished work!')

## dopysaty argumenty shchob vyklykalys i *args i **kwargs