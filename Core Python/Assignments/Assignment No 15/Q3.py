class Shirt:
    def __init__(self, sid, sname, type, price, size):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
    
    def getData(self):
        data = 'SHIRT ID:'+str(self.sid)+'\n'
        data += 'SHIRT NAME:'+self.sname+'\n'
        data += 'SHIRT TYPE:'+self.type+'\n'
        data += 'PRICE:'+str(self.price)+'\n'
        data += 'SIZE:'+self.size+'\n'
        return data

s1 = Shirt(1,'formal shirt', 'Cotton', 2300, 'M')
s2 = Shirt(2,'Casual', 'Polyster', 2500, 'L')

print(s1.getData())
print(s2.getData())