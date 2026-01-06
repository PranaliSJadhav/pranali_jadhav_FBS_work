class Television:
    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0

    def input_data(self):
        try:
            self.model_number = int(input("Enter model number: "))
            self.screen_size = int(input("Enter screen size: "))
            self.price = int(input("Enter price: "))

            if(self.model_number > 9999):
                raise ValueError("Invalid model number")

            if(self.screen_size < 12 or self.screen_size > 70):
                raise ValueError("Invalid screen size")

            if(self.price < 0 or self.price > 5000):
                raise ValueError("Invalid price")

        except Exception as e:
            print("Exception:", e)
            self.model_number = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print("Model Number:", self.model_number)
        print("Screen Size:", self.screen_size)
        print("Price:", self.price)


if(__name__ == "__main__"):
    tv = Television()
    tv.input_data()
    tv.display()
