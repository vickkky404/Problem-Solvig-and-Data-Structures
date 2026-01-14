# creates a bank account object , store account holder name and balance , deposite money , withdraw money ,  show balance

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_details(self):
        print("Account Holder:", self.name)
        print("Balance: ₹", self.balance)


    def deposit(self, amount):
        self.balance += amount
        print("Deposited: ₹", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn: ₹", amount)
        else:
            print("Insufficient balance")


# create bank account object
account1 = BankAccount("Amit", 5000)

account1.show_details()
account1.deposit(2000)
account1.withdraw(200)
account1.show_details()