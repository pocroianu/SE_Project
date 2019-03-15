import sys
import os
import Rules

flag_R2 = False
flag_R3 = False
flag_R4 = False

def NewCarWanted():
    print("-------------------------------------")
    print("You choose a new car ")
    print("Now you need to customize your car")
    print("Please tell us your preferences")
    print("First select your desire colour:")
    print('Colour available: Red, Blue, White, Black')
    desireColour = input("Write here your desire colour: ")

    global flag_R2
    R2 = Rules.Ruless2(desireColour)
    if R2 == True: 
        print("Desire colour accepted ")
    elif R2 != True:
        print("Desire colour not accepted! Please choose again!")
        R2 = Rules.Ruless2(desireColour)
    flag_R2 = True
        
def BodyCar():
    print("-------------------------------------")
    print("Please tell us your preferences")
    print('Body car  available: SmallCar, SportCar, SUV, VAN')
    desireBodyCar = input("Write here your desire Body Car: ")
    global flag_R3
    R3 = Rules.Ruless3(desireBodyCar)
    if R3 == True: 
        print("Desire Body Car accepted ")
    elif R3 != True:
        print("Desire Body Car not accepted! Please choose again!")
        R3 = Rules.Ruless3(desireBodyCar)
    flag_R3 = True


def FuelTypeInterface():
    print("-------------------------------------")
    print("Please tell us your preferences")
    print('Body car  available: Petrol,Diesel,Electric,Gas')
    desiredFuelType = input("Write here your desire Fuel type: ")
    global flag_R4
    R4 = Rules.Ruless4(desiredFuelType)
    if R4 == True: 
        print("Desire Fuel Type accepted ")
    elif R4 != True:
        print("Desire Fuel Type not accepted! Please choose again!")
        R4 = Rules.Ruless4(desiredFuelType)
    flag_R4 = True




def OldCarWanted():
    print('oldCarWanted')



ans=True
while ans:
    SelectMode = input("Press 1 to choose a car or 2 for EXIT : ")
    if SelectMode == '1' and flag_R2 == False:
        Rules.Ruless1(SelectMode)

    if flag_R2 == True:
        BodyCar()

    if flag_R3 == True:
        FuelTypeInterface()  

    elif SelectMode == '2': 
        print("Exit")
        ans = False
    


