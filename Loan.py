import datetime
from Book import Book

class Loan(object):
    def __init__(self, loan_ID, issueDate, dueDate, returnDate, Book):
        self.loanID = loan_ID
        self.issueDate = issueDate
        self.dueDate = dueDate
        self.returnDate = returnDate
        self.Book = Book


    def isOverDue(self, dueDate, returnDate):
        if dueDate < returnDate:
            return returnDate - dueDate

        else:
            return 0



