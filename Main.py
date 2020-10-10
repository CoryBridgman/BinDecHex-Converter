import sys
from ModelCalc import Calc
# from noClassCalc import toBin
import noClassCalc

print("running Main")

Converter = Calc()

Converter.classTest()
#test

#toBin(input("Enter a number"))

userIn = ""

while True:

    #Take user input
    userIn = ""
    inputOkay = False
    while inputOkay == False:
        userIn = input("Type \"Exit\" at any time to end the program.\nEnter a number:\n")
        if userIn.casefold() == "exit":
            noClassCalc.quit()
        else:
            inputOkay = noClassCalc.toBin(userIn)

    print()
    #Take user direction
    inputConfirm = False
    while inputConfirm == False:
        confirmIn = input("Enter \"Redo\" to start over with a new number.\n"
        + "Enter your input number type: 1 = Bin  |  2 = Dec  |  3 = Hex\n")
        if confirmIn.casefold() == "exit":
            noClassCalc.quit()
        elif confirmIn.casefold() == "redo":
            break
        elif confirmIn == "1": #Bin

            inputConfirm = True
        elif confirmIn == "2": #Dec

            inputConfirm = True
        elif confirmIn == "1": #Hex
            
            inputConfirm = True
        else:
            print("Please enter a valid input of 1 - 3, or \"Redo\" to start over")

    print()
    #Third loop?    
    restartPgm = False
    while inputConfirm == True and restartPgm == False:
        print("\n Third loop works \n")
        break

