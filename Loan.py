import datetime
from Book import Book
from User import User
class Loan(object):
    def __init__(self, loan_ID, issueDate, dueDate, returnDate, Book, User):
        self.loanID = loan_ID
        self.issueDate = issueDate
        self.dueDate = dueDate
        self.returnDate = returnDate
        self.Book = Book
        self.User = User


    def isOverDue(self, dueDate, returnDate):
        if dueDate < returnDate:
            return returnDate - dueDate

        else:
            return 0



