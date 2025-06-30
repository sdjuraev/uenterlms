from Loan import Loan
from MainMenu import Menu
from datetime import  date

class LibrarySystem:
    def __init__(self):
        self.librarians = []
        self.bookList = []
        self.userList = []
        self.loans = []
        menu = Menu()
        self.lpt = menu.menu_show()

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

    def addLoan(self, userID, days):
        new_loan = Loan(self, userID, date.today(),date.today()+days, NULL)
        self.loans.append(new_loan)
        return new_loan