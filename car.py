class Car:
    def __init__(self, ID, brand, model, year, price, milage, color ,used, moreInfo):
        self.ID = ID
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.milage = milage
        self.color = color
        self.used = used
        self.moreInfo = moreInfo



class MakeFcar(Car):
    def __init__(self, ID, brand, model, year, price, milage, color, used, fuelType, moreInfo):
        super().__init__(ID, brand, model, year, price, milage, color, used, moreInfo) #get peramiter that every car needs.
        self.fuelType = fuelType #add what only fuel car needs


    def displayInfo(self):
        nicePrice = "{:,}".format(int(float(self.price)))
        niceMilage = "{:,}".format(int(float(self.milage)))
        print(f"ID: {self.ID} | Type: Fuel | Brand: {self.brand} | Model: {self.model} | Year: {self.year} | Price: ${nicePrice} | Milage: {niceMilage} | Color: {self.color} | Used: {self.used} | Fuel Type: {self.fuelType} | More Info: '{self.moreInfo}'")



class MakeEcar(Car):
    def __init__(self, ID, brand, model, year, price, milage, color, used, chargeTime, moreInfo):
        super().__init__(ID,brand, model, year, price, milage, color, used, moreInfo) #get peramiter that every car needs.
        self.chargeTime = chargeTime #add what only electric car needs

    def displayInfo(self):
        nicePrice = "{:,}".format(int(float(self.price)))
        niceMilage = "{:,}".format(int(float(self.milage)))
        print(f"ID: {self.ID} | Type: Electric | Brand: {self.brand} | Model: {self.model} | Year: {self.year} | Price: ${nicePrice} | Milage: {niceMilage} | Color: {self.color} | Used: {self.used} | Charge Time: {self.chargeTime} | More Info: '{self.moreInfo}'")


class MakeHcar(Car):
    def __init__(self, ID, brand, model, year, price, milage, color, used, fuelType, chargeTime, moreInfo):
        super().__init__(ID,brand, model, year, price, milage, color, used, moreInfo) #get peramiter that every car needs.
        self.fuelType = fuelType #add both fuel and electric
        self.chargeTime = chargeTime

    def displayInfo(self):
        nicePrice = "{:,}".format(int(float(self.price)))
        niceMilage = "{:,}".format(int(float(self.milage)))
        print(f"ID: {self.ID} | Type: Hybrid | Brand: {self.brand} | Model: {self.model} | Year: {self.year} | Price: ${nicePrice} | Milage: {niceMilage} | Color: {self.color} | Used: {self.used} | Fuel Type: {self.fuelType} | Charge Time: {self.chargeTime} | More Info: '{self.moreInfo}'")
