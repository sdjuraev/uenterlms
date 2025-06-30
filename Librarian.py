from random import randint

from Book import Book
from LibrarySystem import LibrarySystem
from User import User


class Librarian:
    def __init__(self, name, username, password, email, librarySystem):
        self.name = name
        self.username= username
        self.email = email
        self.password = password
        self.librarySystem = librarySystem
    def addBook(self):
        title = input("Enter title: ")
        author = input("Enter author")
        isbn = input("Enter ISBN: ")
        genre = input("Enter category")
        price = input("Enter price")
        year = input("Enter year")
        book = Book(111, title, author, isbn, genre, True, price, year)
        self.librarySystem.addBook(book)

    def removeBook(self, id):
        for book in self.librarySystem.bookList:
            if book.id == id:
                self.librarySystem.bookList.remove(book)
                print("Book removed successfully")

    def showBooks(self):
        for book in self.librarySystem.bookList:
            print(book.title, book.author)

    def randomID(self):
        return randint(100, 999)

    def registerUser(self):
        userID = self.randomID()
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        new_user = User(userID, username, email, password)
        self.librarySystem.addUser(new_user)

    def generateReport(self):
        print("Number of users: ", len(self.librarySystem.userList))
        print("Number of books: ", len(self.librarySystem.bookList))