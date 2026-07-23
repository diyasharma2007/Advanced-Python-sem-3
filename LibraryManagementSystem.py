class Book:
    def __init__(self, title):
        self.title = title
        self.status = "Available"


class Patron:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self):
        t = input("Enter book name: ")
        b = Book(t)
        self.books.append(b)
        print("Book Added")

    def add_user(self):
        n = input("Enter user name: ")
        p = Patron(n)
        self.users.append(p)
        print("User Registered")

    def borrow(self):
        book = input("Enter book name: ")

        for i in self.books:
            if i.title == book:
                if i.status == "Available":
                    i.status = "Borrowed"
                    print("Book Borrowed")
                else:
                    print("Book Already Borrowed")
                return

        print("Book Not Found")

    def return_book(self):
        book = input("Enter book name: ")

        for i in self.books:
            if i.title == book:
                i.status = "Available"
                print("Book Returned")
                return

        print("Book Not Found")

    def show_books(self):
        print("\nBooks:")
        for i in self.books:
            print(i.title, "-", i.status)


lib = Library()

while True:
    print("\n1.Add Book")
    print("2.Register User")
    print("3.Borrow Book")
    print("4.Return Book")
    print("5.Show Books")
    print("6.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        lib.add_book()

    elif ch == 2:
        lib.add_user()

    elif ch == 3:
        lib.borrow()

    elif ch == 4:
        lib.return_book()

    elif ch == 5:
        lib.show_books()

    elif ch == 6:
        print("Program Ended")
        break

    else:
        print("Wrong Choice")