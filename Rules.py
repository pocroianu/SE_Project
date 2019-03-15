
def Ruless1(SelectMode):
    from Interface import NewCarWanted,OldCarWanted 
    if SelectMode == '1':
        WantedCar = input("What kind of car you want? Please type new / old : ")
    if WantedCar == 'new' or WantedCar == 'old':
        if WantedCar == 'new':
            NewCarWanted()
        elif WantedCar =="old":
            OldCarWanted()

def Ruless2(desireColour):
    if desireColour == "Red" or desireColour == "Blue" or desireColour == "White" or desireColour == "Black":
        return True

def Ruless3(desireBodyCar):
    if desireBodyCar == "SmallCar" or desireBodyCar == "SportCar" or desireBodyCar == "SUV" or desireBodyCar == "VAN":
        return True

def Ruless4(desiredFuelType):
    if desiredFuelType == "Petrol" or desiredFuelType == "Diesel" or desiredFuelType == "electric" or desiredFuelType == "Gas":
        return True








