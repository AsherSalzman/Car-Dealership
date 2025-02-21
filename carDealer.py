from car import MakeFcar, MakeEcar, MakeHcar
class CarDealer:
    def __init__(self):
        self.carlist = [] #list that stores all cars
        self.carID = 1
        self.filteredCars = self.carlist


    def addCar(self):
        fORe = input("do you want to add a fuel, electric or hybrid car or exit? (f/e/h): ").lower() #check what car needs to be added
        if fORe != "exit":
            while fORe != "f" and fORe != "e" and fORe != "h":
                fORe = input("do you want to add a fuel, electric or hybrid car? (f/e/h): ").lower()  # check what car needs to be added
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
            elif fORe == "e":
                chargeTime = input("Give me the charge time: ")
                self.carlist.append(MakeEcar(ID, brand, model, year, price, milage, color, used, chargeTime, moreInfo))
            elif fORe == "h":
                fuelType = input("Give me a fuel type: ")
                chargeTime = input("Give me the charge time: ")
                self.carlist.append(MakeHcar(ID, brand, model, year, price, milage, color, used, fuelType, chargeTime, moreInfo))


    def save(self,invintory): #save carlist to file
        line = []
        with open(invintory,"w") as file:
            for i in self.carlist:
                if isinstance(i, MakeFcar): #check if it is a fuel car or not, need to add diffrent things to file
                    line.append(f"f,{i.ID},{i.brand},{i.model},{i.year},{i.price},{i.milage},{i.color},{i.used},{i.fuelType},{i.moreInfo}")
                elif isinstance(i, MakeEcar):
                    line.append(f"e,{i.ID},{i.brand},{i.model},{i.year},{i.price},{i.milage},{i.color},{i.used},{i.chargeTime},{i.moreInfo}")
                elif isinstance(i, MakeHcar):
                    line.append(f"h,{i.ID},{i.brand},{i.model},{i.year},{i.price},{i.milage},{i.color},{i.used},{i.fuelType},{i.chargeTime},{i.moreInfo}")


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
                elif tempCar[0] == "e":
                    self.carlist.append(MakeEcar(tempCar[1],tempCar[2],tempCar[3],tempCar[4],tempCar[5],tempCar[6],tempCar[7],tempCar[8],tempCar[9],tempCar[10]))
                elif tempCar[0] == "h":
                    self.carlist.append(MakeHcar(tempCar[1],tempCar[2],tempCar[3],tempCar[4],tempCar[5],tempCar[6],tempCar[7],tempCar[8],tempCar[9],tempCar[10],tempCar[11]))
            self.filteredCars = self.carlist
            print("Cars have been loaded")


    def displayInfo(self):
        if len(self.filteredCars) != 0:
            for i in range(len(self.filteredCars)): #print all filtered cars
                self.filteredCars[i].displayInfo()
                print("")
            print(f"There are {len(self.filteredCars)} that match your filters")
        else:
            print("\nNo cars have been found that match your filters")


    def filter(self):
        allowedFilters = ["id","price","year","model","brand","vehicle type","vehicle","type","reset","used"]
        filterBy = input("What do you what to filter by? (ID, price, year, model, brand, used, vehicle type (fuel/electric/hybrid) or reset/exit filter: ").lower() #get what user wants to change
        if filterBy != "exit":
            while not filterBy in allowedFilters:
                filterBy = input("What do you what to filter by? (ID, price, year, model, brand, used, vehicle type (fuel/electric/hybrid) or reset filter: ").lower()  # get what user wants to change


            if filterBy == "id": #change id to ID b/c "id" is not part of MakeCar class
                filterBy = "ID"
            if filterBy == "reset":
               self.filteredCars = self.carlist
               return


            filteredCarTemp = [] # make list of sorted cars, if it changed original list, the size would change and it whould be out of index
            if filterBy == "ID" or filterBy == "price" or filterBy == "year": # sorted diffrently if it is a number or not

                lowest = input(f"What is the lowest {filterBy}  you want to sort by: ").replace(",","").replace("$","") #get nums to sort by
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
                if filterBy == "used": #if user picked used then the else statement won't make sense
                    sort = input("Has the car been used (yes/no): ")
                else:
                    sort = input(f"What {filterBy} do you want to sort by: ").lower() #if not a number need to sort differently
                if filterBy == "vehicle type" or filterBy == "vehicle" or filterBy == "type": #if sorting by vehicle type, it sorts by checking what class it is.
                    if sort == "fuel":
                        for i in range(len(self.filteredCars)):
                            if isinstance(self.filteredCars[i], MakeFcar): #check if fuel car
                                filteredCarTemp.append(self.filteredCars[i]) #if yes add to filtered cars
                    elif sort == "electric":
                        for i in range(len(self.filteredCars)):
                            if isinstance(self.filteredCars[i], MakeEcar):
                                filteredCarTemp.append(self.filteredCars[i])
                    elif sort == "hybrid":
                        for i in range(len(self.filteredCars)):
                            if isinstance(self.filteredCars[i], MakeHcar):
                                filteredCarTemp.append(self.filteredCars[i])

                else: #if not sorting by vehicle type it just checks if it is equal to the filter.
                    for i in range(len(self.filteredCars)):
                        if getattr(self.filteredCars[i], filterBy).lower() == sort.lower():
                            filteredCarTemp.append((self.filteredCars[i]))
            self.filteredCars = filteredCarTemp.copy() #move filteredCarTemp to filteredCars
            print("cars have been filtered")


    def updatePrice(self):
        updateID = input("What is the ID for the car you want to update the price off (exit to cancel): ")
        if updateID == "exit":
            print("\nExit")
        else:
            while not updateID.isdigit():
                updateID = input("What is the ID for the car you want to update the price off (numbers only): ")

            newPrice = input("What is the new price you want: ")
            while not newPrice.isdigit():
                newPrice = input("What is the new price you want (numbers only): ")
            self.carlist[int(updateID)].price = newPrice #update price of car


    def sellCar(self):
        delcar = -1
        carID = input("What is the ID for the car you want to sell (exit to cancel): ")
        if carID == "exit":
            print("\nExit")
        else:
            while not carID.isdigit():
                carID = input("What is the ID for the car you want to sell (numbers only): ")
            carID = int(carID)

            try:
                for i in self.carlist:
                    if i.ID == carID:
                        del i
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
