from Book import Book
from Loan import Loan
from  LibrarySystem import LibrarySystem
from Librarian import Librarian
from datetime import date

if __name__ == '__main__':
    librarySystem = LibrarySystem()
    librarian = Librarian("Alex", 'alex','pass','email@com', librarySystem)
    book = Book(111, "Alice in Wonderland","Duma",True)
    librarySystem.addBook(book)
    librarySystem.addLibrarian(librarian)
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
                print("1. Add books")
                print("2. Delete books")
                print("3. Issue books")
                print("4. Receive Books")
                print("5. Register User")
                print("6. Generate Report")
                print("7. Display Books")
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




    





