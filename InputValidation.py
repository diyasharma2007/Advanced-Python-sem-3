def check(func):

    def wrapper(*args):

        for i in args:
            if i <= 0 or type(i) != int:
                print("Invalid Input")
                return

        func(*args)

    return wrapper


@check
def add(a, b):
    print("Sum =", a + b)


add(5, 10)
add(78, -1)
