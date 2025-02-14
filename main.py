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




class CarDealer:
    def __init__(self):
        self.carlist = [] #list that stores all cars
        self.carID = 0
        self.filteredCars = self.carlist


    def addCar(self):
        fORe = input("do you want to add a fuel or electric car? (f/e) ").lower() #check what car needs to be added
        while fORe != "f" and fORe != "e":
            fORe = input("do you want to add a fuel or electric car? (f/e) ").lower()  # check what car needs to be added
        ID = self.carID #give car ID
        self.carID += 1 #add one to car ID so next car has diff
        brand = input("Give me a brand: ")
        model = input("Give me a model: ")

        year = input("Give me a year: ")
        while not year.isdigit(): #stop someone from adding letters
            year = input("Give me a year (only numbers): ")

        price = input("Give me a price: ").replace(",","").replace("$","")
        while not price.isdigit():#stop someone from adding letters
            price = input("Give me a price (only numbers): ").replace(",", "").replace("$", "")

        milage = input("Give me a milage: ").replace(",","")
        while not milage.isdigit():#stop someone from adding letters
            milage = input("Give me a milage (only numbers): ").replace(",", "")

        color = input("What color is the car: ")
        used = input("Was the car used: ")
        moreInfo = input("Any more info about the car: ")
        if fORe == "f": #pick between fuel or electric
            fuelType = input("Give me a fuel type: ")
            self.carlist.append(MakeFcar(ID, brand, model, year, price, milage, color, used, fuelType, moreInfo))
        else:
            chargeTime = input("Give me the charge time: ")
            self.carlist.append(MakeEcar(ID, brand, model, year, price, milage, color, used, chargeTime, moreInfo))


    def save(self,invintory): #save carlist to file
        line = []
        with open(invintory,"w") as file:
            for i in self.carlist:
                if isinstance(i, MakeFcar): #check if it is a fuel car or not, need to add diffrent things to file
                    line.append(f"f,{i.ID},{i.brand},{i.model},{i.year},{i.price},{i.milage},{i.color},{i.used},{i.fuelType},{i.moreInfo}")
                else:
                    line.append(f"e,{i.ID},{i.brand},{i.model},{i.year},{i.price},{i.milage},{i.color},{i.used},{i.chargeTime},{i.moreInfo}")

            file.seek(0) #move curser to first line
            for i in range(len(line)): #write every line to file
                file.write(str(line[i]))
                file.write("\n") #move to next line


    def load(self,invintory): #load file to carlist
        with open(invintory,"r") as file:
            self.carlist = [] #reset carlist
            tempList = []
            amountOfLines = len(file.readlines()) #get amount of lines
            file.seek(0)
            for i in range(amountOfLines): #turn lines to list
                tempList.append(file.readline().splitlines())

            for i in range(len(tempList)):
                tempCar = tempList[i][0].replace("$","").split(",")
                if tempCar[0] == "f":
                    self.carlist.append(MakeFcar(tempCar[1],tempCar[2],tempCar[3],tempCar[4],tempCar[5],tempCar[6],tempCar[7],tempCar[8],tempCar[9],tempCar[10]))
                else: #readd the cars to the list by running it through the
                    self.carlist.append(MakeEcar(tempCar[1],tempCar[2],tempCar[3],tempCar[4],tempCar[5],tempCar[6],tempCar[7],tempCar[8],tempCar[9],tempCar[10]))
            self.filteredCars = self.carlist
            print("Cars have been loaded")

    def displayInfo(self):
        for i in range(len(self.filteredCars)): #print all filtered cars
            self.filteredCars[i].displayInfo()
            print("")


    def filter(self):
        allowedFilters = ["id","price","year","model","brand","vehicle type","vehicle","type","reset"]
        filterBy = input("What do you what to filter by? (ID, price, year, model, brand, vehicle type) or reset filter: ").lower() #get what user wants to change
        while not filterBy in allowedFilters:
            filterBy = input("What do you what to filter by? (ID, price, year, model, brand, vehicle type) or reset filter: ").lower()  # get what user wants to change

        if filterBy == "id": #change id to ID b/c "id" is not part of MakeCar class
            filterBy = "ID"
        if filterBy == "reset":
           self.filteredCars = self.carlist
           return

        filteredCarTemp = [] # make list of sorted cars, if it changed original list, the size would change and it whould be out of index
        if filterBy == "ID" or filterBy == "price" or filterBy == "year": # sorted diffrently if it is a number or not

            lowest = input(f"What is the lowest {filterBy} you want to sort by: ").replace(",","").replace("$","") #get nums to sort by
            while not lowest.isdigit(): #check if user only put numbers
                lowest = input(f"What is the lowest {filterBy} you want to sort by (numbers only): ").replace(",","").replace("$","")
            lowest = int(lowest) #turn to int

            highest = input(f"What is the highest {filterBy} you want to sort by: ").replace(",","").replace("$","") #get nums to sort by
            while not highest.isdigit(): #check if user only put numbers
                highest = input(f"What is the highest {filterBy} you want to sort by (numbers only): ").replace(",","").replace("$","")
            highest = int(highest) #turn to int

            for i in range(len(self.filteredCars)):
                if lowest <= int(getattr(self.filteredCars[i], filterBy)) <= highest: #check if car passes filter
                    filteredCarTemp.append(self.filteredCars[i]) #add to filtered cars


        else:
            sort = input(f"What {filterBy} do you want to sort by: ").lower() #if not a number need to sort differently
            if filterBy == "vehicle type" or filterBy == "vehicle" or filterBy == "type": #if sorting by vehicle type, it sorts by checking what class it is.
                if sort == "fuel":
                    for i in range(len(self.filteredCars)):
                        if isinstance(self.filteredCars[i], MakeFcar):
                            filteredCarTemp.append(self.filteredCars[i])
                else:
                    for i in range(len(self.filteredCars)):
                        if isinstance(self.filteredCars[i], MakeEcar):
                            filteredCarTemp.append(self.filteredCars[i])

            else: #if not sorting by vehicle type it just checks if it is equal to the filter.
                for i in range(len(self.filteredCars)):
                    if getattr(self.filteredCars[i], filterBy).lower() == sort:
                        filteredCarTemp.append((self.filteredCars[i]))
        self.filteredCars = filteredCarTemp.copy() #move filteredCarTemp to filteredCars


    def updatePrice(self):
        updateID = input("What is the ID for the car you want to update the price off: ")
        while not updateID.isdigit():
            updateID = input("What is the ID for the car you want to update the price off (numbers only): ")

        newPrice = input("What is the new price you want: ")
        while not newPrice.isdigit():
            newPrice = input("What is the new price you want (numbers only): ")
        self.carlist[int(updateID)].price = newPrice #update price of car

    def sellCar(self):
        delcar = -1
        carID = input("What is the ID for the car you want to sell: ")
        while not carID.isdigit():
            carID = input("What is the ID for the car you want to sell (numbers only): ")
        carID = int(carID)

        # print(f"Sold car for {self.carlist[carID-1].price}")
        try:
            del self.carlist[carID]
            for i in range(len(self.filteredCars)):
                if int(self.filteredCars[i].ID) == carID:
                    delcar = i
                    break
            try:
                del self.filteredCars[delcar]  # del car after so list does not get shorter
                print("Car has been sold")
            except:
                print("Cant find car ID")
        except:
            print("Cant find car ID")



class Menu(CarDealer):
    def __init__(self):
        super().__init__() #get vars from CarDealership
        self.run = True
        self.file = input("Give me the file name: ")
    def runMenu(self):
        pick = int(input("""
Pick a option
1. Add car
2. Update car price
3. Sell car
4. View cars
5. Filter cars
6. Load cars
7. Save and Exit
option: """))

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

dealershipRun = Menu()
try:
    dealershipRun.load(dealershipRun.file) #load so the cars are added at first
except:
    print("File does not exist making file now")
    open(dealershipRun.file,"w")
    print("File has been made")
while dealershipRun.run:
    dealershipRun.runMenu()
