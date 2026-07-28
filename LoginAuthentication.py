# lets say in this case the user is logged in
user_logged_in = True

# Decorator for authentication


def login_check(func):

    def wrapper():
        if user_logged_in:
            func()
        else:
            print("Access denied! Please sign in first.")

    return wrapper


@login_check
def dashboard():
    print("Welcome! You can now access your dashboard.")


dashboard()
