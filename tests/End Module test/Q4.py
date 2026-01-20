import pickle
import re
import os

class Book:
    def __init__(self, book_id, name, author, price):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.book_id} | {self.name} | {self.author} | {self.price}"


class BookManager:
    def __init__(self, filename="books.dat"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        return []

    def save_books(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.books, f)

    # Add Book
    def add_book(self):
        bid = int(input("Enter Book ID: "))
        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        price = float(input("Enter Price: "))

        self.books.append(Book(bid, name, author, price))
        self.save_books()
        print(" Book added successfully")

    #  Update Book
    def update_book(self):
        bid = int(input("Enter Book ID to update: "))
        for book in self.books:
            if book.book_id == bid:
                book.name = input("Enter new name: ")
                book.author = input("Enter new author: ")
                book.price = float(input("Enter new price: "))
                self.save_books()
                print("Book updated successfully")
                return
        print("Book not found")

    # Delete Book
    def delete_book(self):
        bid = int(input("Enter Book ID to delete: "))
        for book in self.books:
            if book.book_id == bid:
                self.books.remove(book)
                self.save_books()
                print(" Book deleted successfully")
                return
        print(" Book not found")

    # Show Specific Data using Regex
    def show_specific(self):
        print("1. Show Names\n2. Show Authors\n3. Show Prices")
        ch = input("Enter choice: ")

        for book in self.books:
            text = str(book)
            if ch == "1":
                print(re.findall(r"\|\s([^|]+)\s\|", text)[0])
            elif ch == "2":
                print(re.findall(r"\|\s[^|]+\s\|\s([^|]+)\s\|", text)[0])
            elif ch == "3":
                print(re.findall(r"\|\s([\d.]+)$", text)[0])

    #  Show All Data
    def show_all(self):
        if not self.books:
            print("No books available")
        for book in self.books:
            print(book)


# -------- Main Program --------
bm = BookManager()

while True:
    print(" Book Management Menu")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. Show Specific Data (Regex)")
    print("5. Show All Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        bm.add_book()
    elif choice == "2":
        bm.update_book()
    elif choice == "3":
        bm.delete_book()
    elif choice == "4":
        bm.show_specific()
    elif choice == "5":
        bm.show_all()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print(" Invalid choice")