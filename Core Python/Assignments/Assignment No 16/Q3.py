class Shirt:
    base_price = 1000   

    def __init__(self, sid=0, sname="", stype="", size="small"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.size = size
        self.price = self.calculate_price()

    def calculate_price(self):
        if self.size == "small":
            return Shirt.base_price
        elif self.size == "medium":
            return Shirt.base_price + (Shirt.base_price * 0.10)
        elif self.size == "large":
            return Shirt.base_price + (Shirt.base_price * 0.20)
        elif self.size == "xlarge":
            return Shirt.base_price + (Shirt.base_price * 0.30)
        else:
            return Shirt.base_price

    def showShirt(self):
        print("Shirt ID:", self.sid)
        print("Name:", self.sname)
        print("Type:", self.stype)
        print("Size:", self.size)
        print("Price:", self.price)

    def __del__(self):
        print("Shirt object destroyed")



s1 = Shirt(1, "Raymond", "Formal", "large")
s1.showShirt()