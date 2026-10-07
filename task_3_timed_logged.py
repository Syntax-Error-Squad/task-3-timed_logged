# Задача №3: декоратор timed_logged
# Реализовать декоратор, который будет:
# Измерять время выполнения функции (в мс).
# Выводить: имя функции, аргументы, результат, время.
# При ошибке — логировать тип и сообщение исключения, не скрывая его.
# Работать с любыми сигнатурами (*args, **kwargs).
# Сохранять метаданные функции (__name__, __doc__) через functools.wraps.

import time
from functools import wraps

def timed_logged(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        t_start = time.perf_counter()
        try:
            result = f(*args, **kwargs)
        except Exception as e:
            print(f"Ошибка: {type(e).__name__} : {e} ")
            raise

        t_end = time.perf_counter()
        print(f"Функция: {f.__name__}, аргументы {args, kwargs}, результат {result}, время {(t_end - t_start)* 1000} мс")
        return result
    return wrapper


@timed_logged
def slow_sum(a, b, delay=0.5):
    """Складывает a и b."""
    time.sleep(delay)
    return a + b
try:
    slow_sum(1, "2", delay=0)
except TypeError:
    print("Поймали ошибку")
slow_sum(1, 2, delay=0.2)

print(slow_sum.__name__)   
print(slow_sum.__doc__)
