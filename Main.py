from Book import Book
from Loan import Loan
from  LibrarySystem import LibrarySystem
from Librarian import Librarian
from datetime import date, timedelta
from User import  User


if __name__ == '__main__':
    librarySystem = LibrarySystem()
    librarian = Librarian("Alex", 'alex','pass','email@com', librarySystem)
    user = User(2222,'john',"john",'pass')
    book = Book(111, "Alice in Wonderland","Duma",True)
    librarySystem.addBook(book)
    librarySystem.addLibrarian(librarian)
    librarySystem.addUser(user)
    print("Welcome to Library Management System!")
    print("Select user")
    print("1. Librarian")
    print("2. User")
    select = int(input(""))
    if select == 1:
        print("Librarian")
        login = input("Enter your username: ")
        password = input("Enter your password: ")
        if librarySystem.login(login, password):
                print("Login successful")
                while select != 0:
                    print("1. Add books")
                    print("2. Delete books")
                    print("3. Issue books")
                    print("4. Receive Books")
                    print("5. Register User")
                    print("6. Generate Report")
                    print("7. Display Books")
                    print("0. Exit")
                    select = int(input(""))
                    if select == 1:
                        librarian.addBook()
                    if select == 2:
                        id = int(input("Enter ID of book: "))
                        librarian.removeBook(id)
                    if select == 5:
                        librarian.registerUser()
                    if select == 6:
                        librarian.generateReport()
                    if select == 7:
                        librarian.showBooks()

    if select==2:
        email = input("Enter email:")
        password = input("Enter password:")

        if librarySystem.loginUser(email.strip(), password.strip()):
            print("Login successful")
            while select != 0:
                print("1. Search Book")
                print("2. Borrow Book")
                print("3. Return Book")
                print("4. Renew Book")
                print("5. Reserve Book")
                print("0. Exit")
                select = int(input("Enter your choice: "))
                if select == 1:
                    title = input("Enter Book Title")
                    book = librarySystem.search(title)
                    if book is not None:
                        print(book.title, book.author, book.status)
                if select == 2:
                    title = input("Enter Book Title You want to borrow")
                    book = librarySystem.search(title)
                    if book is not None:
                        if book.status:
                            day = int(input("How many days would you like to borrow?"))
                            book.status = False
                            today = date.today()
                            dueDate = date.today() + timedelta(days=day)
                            borrowBooks = Loan(1, today, dueDate, None, book)
                            librarySystem.addLoan(borrowBooks)
                            librarySystem.printBorrowedBooks()

                        else:
                            print("You can't borrow this book")
                if select == 3:
                    title = input("Enter Book Title You want to Return")
                    book = librarySystem.search(title)
                    if book is not None:
                        book.status = True








    





