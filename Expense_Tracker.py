"""
    Concpet of Expense Tracker
    class
    Object
    constructor
    Instance variables
    Instance Methods
"""
"""
    *Create expense Object
    *store amount and category
    *Display Expenses
    *calculate total expenses
"""

# create the expense class
class Expense:
    def __init__(self,amount,category):
        self.amount = amount
        self.category = category


        # add a display method
    def show_expense(self):
        print("Category: ", self.category)
        print("Amount: ₹", self.amount)
        print("-------------------")


        # create expense objects
e1 = Expense(1500,"Food")
e2 = Expense(2000,"Transport")
e3 = Expense(500,"Entertainment")


        # calculate total expense
total = e1.amount + e2.amount + e3.amount
print("Total Expense: ₹", total)
