
# def myFunc(func):
#     def wrapper(func):
#         print("Start")
#         func()
#         print("end")
#     return wrapper

# def say_hello():
#     print("hello")

# myFunc(say_hello)(say_hello)

def myFunc(func):
    def wrapper():
        print("Start")
        func()
        print("end")
    return wrapper

@myFunc  # <---- A decorator
def say_hello():
    print("hello")

say_hello()