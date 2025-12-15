class Book:
    count = 0   

    def __init__(self, bid=0, bname="", price=0.0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1

    def showBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

    def __del__(self):
        Book.count -= 1
        print("Book object destroyed")


b1 = Book(1, "Python Basics", 450, "Guido")
b2 = Book()

b1.showBook()
print("Total Book Objects:", Book.count)