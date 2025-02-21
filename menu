from carDealer import CarDealer
class Menu(CarDealer):
    def __init__(self):
        super().__init__() #get vars from CarDealership
        self.run = True
        self.file = input("Give me the file name: ")
    def runMenu(self):
        pick = ""
        while not pick.isdigit():
            pick = input("""
Pick a option
1. Add car
2. Update car price
3. Sell car
4. View cars
5. Filter cars
6. Load cars
7. Save and Exit
option: """)
        pick= int(pick)
        if pick == 1:
            self.addCar()
        if pick == 2:
            self.updatePrice()
        if pick == 3:
            self.sellCar()
        if pick == 4:
            self.displayInfo()
        if pick == 5:
            self.filter()
        if pick == 6:
            self.load(self.file)
        if pick == 7:
            self.save(self.file)
            print("Saved and Exited")
            self.run = False
