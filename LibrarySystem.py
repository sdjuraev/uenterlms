from Loan import Loan
from MainMenu import Menu
from datetime import date, timedelta


class LibrarySystem:
    def __init__(self):
        self.librarians = []
        self.bookList = []
        self.userList = []
        self.loans = []

    def addLibrarian(self, library):
        self.librarians.append(library)

    def addBook(self, book):
        self.bookList.append(book)

    def addUser(self, new_user):
        for user in self.userList:
            if user.email == new_user.email:
                print("User already exists")
                return False
        self.userList.append(new_user)
        return True

    def printUsers(self):
        for user in self.userList:
            print(user.id, user.email, user.password)

    def login(self, username, password):
        for lib in self.librarians:
            if lib.username == username and lib.password == password:
                print("Logged in successfully")
                return True
        print("Invalid username or password")
        return False

    def loginUser(self, email, password):
        for user in self.userList:
            if user.email == email and user.password == password:
                print("Logged in successfully")
                return user
        print("Invalid username or password")
        return None

    def addLoan(self, new_loan):
        self.loans.append(new_loan)

    def search(self, title):
        for book in self.bookList:
            if book.title == title:
                return book
        return None

    def search2(self, year):
        for book in self.bookList:
            if book.year == year:
                return book
        return None

    def search3(self, id):
        for book in self.bookList:
            if book.id == id:
                return book
        return None

    def printBorrowedBooks(self):
        for loan in self.loans:
            print(loan.issueDate, loan.dueDate, loan.Book.title, loan.Book.author + loan.User.email)
    def returnBorrowedBooks(self, title, User):
        book = self.search(title)
        for loan in self.loans:
            if loan.Book==book and loan.User == User and loan.dueDate < date.today():
                print("You have fine")
                timedelta =date.today() - loan.dueDate
                print("You need to pay",timedelta * 10000 )
