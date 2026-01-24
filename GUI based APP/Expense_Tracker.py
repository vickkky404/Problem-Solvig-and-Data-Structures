# Desktop app

# tkinter is a module that helps build desktop apps

# importing tkinter as tk 
import tkinter as tk
# the (as) is allias..

class ExpenseTracker:
    def __init__(self, root):
        self.total = 0
        self.expenses = []

        root.title("Expense Tracker")
        root.geometry("350x400")

        tk.Label(root, text="Expense Tracker", font=("Arial", 16)).pack(pady=10)

        tk.Label(root, text="Amount").pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        tk.Label(root, text="Category").pack()
        self.category_entry = tk.Entry(root)
        self.category_entry.pack()

        tk.Button(root, text="Add Expense", command=self.add_expense).pack(pady=10)

        self.result_label = tk.Label(root, text="Total Expense: ₹0")
        self.result_label.pack()

        self.expense_list = tk.Label(root, text="", justify="left")
        self.expense_list.pack()

    def add_expense(self):
        amount = int(self.amount_entry.get())
        category = self.category_entry.get()

        self.expenses.append((category, amount))
        self.total += amount

        text = ""
        for c, a in self.expenses:
            text += f"{c} - ₹{a}\n"

        self.expense_list.config(text=text)
        self.result_label.config(text=f"Total Expense: ₹{self.total}")

        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)

root = tk.Tk()
app = ExpenseTracker(root)
root.mainloop()
