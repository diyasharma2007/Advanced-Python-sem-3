def counter(func):

    count = 0

    def wrapper():

        nonlocal count
        count += 1

        print("Called", count, "time(s)")
        func()

    return wrapper


@counter
def welcome():
    print("hey!whats up?")

welcome()
welcome()
welcome()