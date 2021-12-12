# def f(a):
#     global b
#     print(a)
#     print(b)
#     b = 3
#
#
# b = 2
# f(1)
# print(b)

# def main_func():
#     def inner_func():
#         print('Hello my friend')
#     inner_func()
#
# main_func()

# def main_func():
#     def inner_func():
#         print('Hello my friend')
#     return inner_func
#
# a = main_func()
# print(a)

# Замыканием называется ситуация когда вложенная
# функция пользуется переменными которые не объявлены в
# её теле.
# def main_func():
#     name = 'Ivan'
#     def inner_func():
#         print('Hello my friend', name)
#     return inner_func
#
# a = main_func()
# print(a)

# Как использовать:
# def main_func(value):
#     name = value
#     def inner_func():
#         print('Hello my friend', name)
#     return inner_func
#
#
# a = main_func('Misha')
# a()
# b = main_func('Vasia')
# b()

# пример счётчика
# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#
#     return inner
#
#
# q = counter()
# q()
# q()
# q()