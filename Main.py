import sys
from ModelCalc import Calc
import noClassCalc

#Program Start
while True:

#  ---===  FIRST LOOP  ===---  #
    # Take user direction
    inputType = ""
    outputType = ""
    outputIteration = 1
    while outputIteration < 3:
        decision = ""
        confirmIn = input("Enter your input number type: 1 = Bin  |  2 = Dec  |  3 = Hex\n" + 
        "Type \"Exit\" to quit.\n")
        if confirmIn.casefold() == "exit":
            noClassCalc.quit()
        elif confirmIn == "1": #Bin
            decision = "bin"
            outputIteration += 1
        elif confirmIn == "2": #Dec
            decision = "dec"
            outputIteration += 1
        elif confirmIn == "3": #Hex
            decision = "hex"
            outputIteration += 1
        else:
            print("Please enter a valid input of 1 - 3, or \"Exit\" to quit.")
        
        #IF BAD STILL RUNS??
        if outputIteration == 2: #first successful iteration
            inputType = decision 
        elif outputIteration == 3:
            outputType = decision #second successful iteration
    
    if outputIteration > 2:
        print("Input is: " + inputType + "\nOutput is: " + outputType)
    else:
        continue

#  ---===  SECOND LOOP  ===---  #
    # Take user input and verify is valid
    # ''''''''''''depending on output type
    userIn = ""
    inputOkay = False
    while inputOkay == False:
        userIn = input("Type \"Exit\" at any time to end the program.\nEnter a number:\n")
        if userIn.casefold() == "exit":
            noClassCalc.quit()
        else:
            inputOkay = noClassCalc.verifyNum(userIn)
    print()


    # Third loop?


