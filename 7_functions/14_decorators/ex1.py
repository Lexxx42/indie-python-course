# Напишите декоратор text_decor, который оборачивает вызов декорированной функции фразами «Hello» и «Goodbye!»: фраза «Hello» печатается до вызова, фраза «Goodbye!» - после
#
# @text_decor
# def simple_func():
#     print('I just simple python func')
#
# simple_func()
#
# # Вывод
# Hello
# I just simple python func
# Goodbye!
# @text_decor
# def multiply(num1, num2):
#     print(num1 * num2)
#
# multiply(3, 5)
#
# # Вывод
# Hello
# 15
# Goodbye!

def text_decor(func, *args, **kwargs):
    def inner(*args, **kwargs):
        print('Hello')
        func(*args, **kwargs)
        print('Goodbye!')

    return inner
