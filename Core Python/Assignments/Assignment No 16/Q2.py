class Product:
    discount = 10   

    def __init__(self, pid=0, pname="", price=0.0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def applyDiscount(self):
        discount_amount = self.price * Product.discount / 100
        self.price -= discount_amount

    def __del__(self):
        print("Product object destroyed")


p1 = Product(101, "Laptop", 50000, 2)
p1.applyDiscount()
p1.showProduct()