# def my_decorator(func):
#
#     def wrapper():
#         print("Перед выполнением функции")
#         func()
#         print("После выполнением функции")
#
#         return wrapper
#
# @my_decorator
# def hello():
#     print("Привет!!!")
#

# Декораторы с аргументами



# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for i in range(n):
#                 func()
#         return wrapper
#     return decorator
#
# amount = int(input("Введите число"))
#
#
# @repeat(amount)
# def greet():
#     print("Привет!!!")
#
#
# greet()


def class_decorator(cls):

    class NewClass(cls):
        pass
    return NewClass


def old_method():
    return "Старый метод!!!"


class Myclass(object):

    def new_method(self):
        pass


object = Myclass()
print(object.new_method())
print(old_method())
