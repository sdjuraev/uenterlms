class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.list_books=[]
    def search(self, book_list, title):
        for book in book_list:
            if book.title == title:
                return book
        return None
    def search2(self, book_list, year):
        for book in book_list:
            if book.year == year:
                return book
        return None
    def search3(self, book_list, id):
        for book in book_list:
            if book.id == id:
                return book
        return None

    def borrow(self, book_list, id):
        book = self.search3(book_list, id)
        if book != None:
            if book.status==True:
                self.list_books.append(book)
                book.status=False
                print("Book borrowed successfully")
            else:
                print("Book not borrowed successfully")




