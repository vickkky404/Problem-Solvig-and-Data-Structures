# online library management systems....
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def show_books(self):
        if not self.books:
            print("No books available")
        else:
            for book in self.books:
                status = "Available" if book.available else "Borrowed"
                print(f"{book.title} by {book.author} - {status}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book borrowed successfully!")
                return
        print("Book not available")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print("Book returned successfully!")
                return
        print("Invalid book title")

library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(Book(title, author))

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        title = input("Enter book title to borrow: ")
        library.borrow_book(title)

    elif choice == "4":
        title = input("Enter book title to return: ")
        library.return_book(title)

    elif choice == "5":
        print("Exiting Library System")
        break

    else:
        print("Invalid choice")
