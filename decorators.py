def decorator(func):
    print('До')
    result = func()
    print("После")
    return result


@decorator
def func():
    print('Вызов функции func')

func()
decorator(func)

# # Классический декоратор
# def decorator(func):
#     def wrapper():
#         print('До')
#         result = func()
#         print("После")
#         return result
#     return wrapper
#
#
# @decorator
# def func():
#     print('Вызов функции func')
#
# func()
# decorator(func)


# # *args, **kwargs
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('До')
#         print('*args:', args)
#         print('**kwargs:', kwargs)
#         result = func(*args, **kwargs)
#         print('После')
#         print('-----------')
#         return result
#     return wrapper
#
#
# @decorator
# def func(a, b):
#     print(a + b)
#
#
# func(1, 1)
# func(2, b=1)
# func(a=2, b=2)


# # Хранение данных
# def decorator(func):
#     print('Декоратор')
#     series = []
#     count = 1
#     print(id(series))
#
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         result = func(*args, **kwargs)
#         series.append(result)
#         count += 1
#         print(id(series))
#         print('-----------')
#         return result
#
#     return wrapper
#
#
# @decorator
# def func(a, b):
#     return a + b
#
#
# func(1, 1)
# func(2, b=1)
# func(a=2, b=2)


# for i, freeval in enumerate(func.__code__.co_freevars):
#     print(freeval, '=', func.__closure__[i].cell_contents)


# # Декораторы с параметрами
# def make_decorator(start_counter):
#     def decorator(func):
#         series = []
#         count = start_counter
#
#         def wrapper(*args, **kwargs):
#             nonlocal count
#             result = func(*args, **kwargs)
#             series.append(result)
#             count += 1
#             return result
#
#         return wrapper
#
#     return  decorator
#
#
# @make_decorator(10)
# def func(a, b):
#     return a + b
#
#
# @make_decorator(50)
# def func2(a, b):
#     return a * b
#
#
# func(1, 1)
# func(2, b=1)
# func(a=2, b=2)
#
# func2(1, 1)
# func2(2, b=1)
# func2(a=2, b=2)
#
# for i, freeval in enumerate(func.__code__.co_freevars):
#     print(freeval, '=', func.__closure__[i].cell_contents)
#
# print()
#
# for i, freeval in enumerate(func2.__code__.co_freevars):
#     print(freeval, '=', func2.__closure__[i].cell_contents)
