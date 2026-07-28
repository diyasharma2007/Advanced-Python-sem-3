from datetime import datetime


def logger(func):

    def wrapper():
        print("Function Name:", func.__name__)
        print("Time:", datetime.now())
        func()

    return wrapper


@logger
def greet():
    print("Hello Diya")


greet()
