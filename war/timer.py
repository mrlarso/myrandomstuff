
import time

def timer(x):
    def get_time(func):
        def timeit():
            print "limit = {}".format(x)
            start = time.time()
            print "Starting"
            func()
            print "Stopping"

            if time.time() - start <= x:
                return True
            else:
                return False

        return timeit

    return get_time

@timer(1)
def hello():
    time.sleep(1.2)

print hello()
"""

import time
def timer(limit):
    def dec(f):
        def wrapper(*args, **kwargs):
            start = time.time()
            f(*args, **kwargs)
            end = time.time()
            return end - start < limit
        return wrapper
    return dec

@timer(1)
def foo():
    time.sleep(1.1)

print foo()
"""
