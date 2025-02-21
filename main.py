from menu import Menu


def main():
    dealershipRun = Menu()
    try:
        dealershipRun.load(dealershipRun.file)  #load so the cars are added at first
    except:
        makeFile = input("File does not exist do you want to make the file (y/n): ").lower()
        while makeFile != "y" and  makeFile != "n":
            makeFile = input("File does not exist do you want to make the file (y/n): ").lower()
        if makeFile == 'y':
            tempFile = open(dealershipRun.file,"w")
            tempFile.close()
            print("File has been made")
        else:
            exit()
    while dealershipRun.run:
        dealershipRun.runMenu()

if __name__ == "__main__":
    main()
