from functools import wraps
count = {}


def counter(func):
    """Cчитает и печатает количество вызовов декорируемой функции."""
    # Создаём запись в словаре с ключом в виде имени декорируемой функции
    # В качестве ключа используем имя функции, полученное из магического метода
    count[func.__name__] = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        # При вызове добавили к счётчику единицу
        count[func.__name__] += 1
        return func(*args, **kwargs)

    return wrapper


def dealer(func):
    """Делает что-то полезное до и после вызова декорируемой функции."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Полезная работа декоратора до вызова функции {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Полезная работа декоратора после вызова функции {func.__name__}')
        return result

    return wrapper


@counter
@dealer
def first():
    print('Вызвана first')


@dealer
@counter
def second():
    print('Вызвана second')


first()
second()
second()
print(count)

# def mydeco(func):
#     def wrapper(*args, **kwargs):
#         return f'{func(args, **kwargs)}!!!'
#     wrapper.__name__ = func.__name__
#     wrapper.__doc__ = func.__doc__
#     return wrapper