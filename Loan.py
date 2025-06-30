import datetime


class Loan(object):
    def __init__(self, loan_ID, issueDate, dueDate, returnDate):
        self.loanID = loan_ID
        self.issueDate = issueDate
        self.dueDate = dueDate
        self.returnDate = returnDate


    def isOverDue(self, dueDate, returnDate):
        if dueDate < returnDate:
            return returnDate - dueDate

        else:
            return 0



