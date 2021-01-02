import time

def timer(func):
    def wrapper(s, timer = False):
        if timer:
            start = time.time()
            func(s)
            end = time.time()
            return end - start
        elif not timer:
            output = func(s)
            return output
    return wrapper
