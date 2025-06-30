class Book(object):
    def __init__(self, id, title, author, status):
        self.id = id
        self.title = title
        self.author = author
        self.status = status

    def print_information(self):
        print(f"ID:{self.id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {self.status}")

    def is_available(self):
        return self.status
    def reserve(self):
        if self.status:
            self.status = False
            return  True
        else:
            return False

    def return_book(self):
        self.status = True
    

