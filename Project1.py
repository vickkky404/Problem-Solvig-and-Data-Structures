class ATM:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Current Balance: ₹", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited: ₹", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn: ₹", amount)
        else:
            print("Insufficient balance")

user = ATM("Rahul", 5000)

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user.check_balance()

    elif choice == "2":
        amt = int(input("Enter amount to deposit: "))
        user.deposit(amt)

    elif choice == "3":
        amt = int(input("Enter amount to withdraw: "))
        user.withdraw(amt)

    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")
