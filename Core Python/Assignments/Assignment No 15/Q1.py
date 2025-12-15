class Book:
    def __init__(self, bid, bname, price, author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
    
    def getData(self):
        data = 'BOOK ID:'+str(self.bid)+'\n'
        data += 'BOOK NAME:'+self.bname+'\n'
        data += 'PRICE:'+str(self.price)+'\n'
        data += 'AUTHOR:'+self.author+'\n'
        return data

b1 = Book(1,'Wings of fire', 270, 'Dr.a.p.j.kalam')
b2 = Book(2,'Wise & Otherwise', 300, 'Sudha Murthy')

print(b1.getData())
print(b2.getData())