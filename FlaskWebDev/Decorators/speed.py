import time


def speed_calc_decorator(function):
    def wrapper_function():
        start = time.time()
        function()
        end = time.time()
        print(f"Function {function.__name__} ran in {end - start} seconds")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()