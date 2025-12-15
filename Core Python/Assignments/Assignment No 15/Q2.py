class Product:
    def __init__(self, pid, pname, price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
    
    def getData(self):
        data = 'PRODUCT ID:'+str(self.pid)+'\n'
        data += 'PRODUCT NAME:'+self.pname+'\n'
        data += 'PRICE:'+str(self.price)+'\n'
        data += 'QUANTITY:'+str(self.quantity)+'\n'
        return data

p1 = Product(1,'Pen', 500, 100)
p2 = Product(2,'Notebook', 300, 12)

print(p1.getData())
print(p2.getData())