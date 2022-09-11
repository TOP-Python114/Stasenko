from time import time_ns, perf_counter, perf_counter_ns


# ИСПРАВИТЬ: любые имена должны быть значащими — что такое decorator?
def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        start_time1 = perf_counter_ns()
        # ДОБАВИТЬ: а если декорируемая функция что-то возвращает?
        func(*args, **kwargs)
        # ИСПОЛЬЗОВАТЬ: лучше сначала сделать отсечку таймеров, а потом уже считать и выводить
        end_time = perf_counter()
        end_time1 = perf_counter_ns()
        # ИСПОЛЬЗОВАТЬ: с помощью f-строк возможно быстро округлять дробные значения — и не только, изучите синтаксис f-строк, там очень много полезных и мощных возможностей
        print(f'Функция работала в течение: '
              f'{end_time - start_time:.6f} с '
              f'({end_time1 - start_time1} нс)')
    return wrapper


@decorator
def rand_func():
    start_time2 = time_ns()
    while True:
        if time_ns() > start_time2:
            break


rand_func()


# ДОБАВИТЬ: после кода под комментарием stdout закомментированный вывод примера выполнения
# stdout:


# ИТОГ: хорошо! — 5/6
