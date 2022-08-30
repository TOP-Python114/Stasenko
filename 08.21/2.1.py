from time import time_ns, perf_counter, perf_counter_ns


def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        start_time1 = perf_counter_ns()
        func(*args, **kwargs)
        print(f'Функция работала: {perf_counter() - start_time} сек.\nИли: {perf_counter_ns() - start_time1} наносек.')
    return wrapper

@decorator
def rand_func():
    start_time2 = time_ns()
    while True:
        if time_ns() > start_time2:
            break

rand_func()
