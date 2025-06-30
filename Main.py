from Book import Book
from Loan import Loan
from  LibrarySystem import LibrarySystem
from Librarian import Librarian
from datetime import date

if __name__ == '__main__':
    librarySystem = LibrarySystem()
    book = Book(1222, "Utgan kunlar", "Abdulla Qodiriy",1212,"Drama",True,'','')
    book2 = Book(111,"Something", "Avtor",True)
    librarian = Librarian('jessy',"Jessy", 'pass','email',librarySystem)
    librarySystem.addBook(book)
    librarian.showBooks()
    librarian.addBook()
    librarian.showBooks()


    





