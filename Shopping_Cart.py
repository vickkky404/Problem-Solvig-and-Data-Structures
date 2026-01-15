class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)
        print("Product added to cart")

    def view_cart(self):
        if not self.cart:
            print("Cart is empty")
        else:
            print("\n--- Your Cart ---")
            for p in self.cart:
                print(p.name, "- ₹", p.price)

    def remove_product(self, name):
        for p in self.cart:
            if p.name == name:
                self.cart.remove(p)
                print("Product removed")
                return
        print("Product not found")

    def total_price(self):
        total = 0
        for p in self.cart:
            total += p.price
        print("Total Amount: ₹", total)

cart = ShoppingCart()

while True:
    print("\n--- Shopping Menu ---")
    print("1. Add Product")
    print("2. View Cart")
    print("3. Remove Product")
    print("4. Total Price")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter product name: ")
        price = int(input("Enter product price: "))
        cart.add_product(Product(name, price))

    elif choice == "2":
        cart.view_cart()

    elif choice == "3":
        name = input("Enter product name to remove: ")
        cart.remove_product(name)

    elif choice == "4":
        cart.total_price()

    elif choice == "5":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice")
