import sys
import ModelCalc
import auxFunctions
import Calculator


#  ---===|  PROGRAM START  |===---  #
print("\n\t ---===|   Program Start   |===---")
while True:

#  ---===| Datatype Selection: FIRST LOOP  |===---  #
    userIn = ""
    inputType = ""
    outputType = ""
    outputIteration = 1
    decision = ""
    while outputIteration < 3:
        print("\n")
        if outputIteration == 1:
            print("Select the datatype for your INPUT:\n")
        else:
            print("Select the datatype for your OUTPUT:\n")
        
        confirmIn = input("1 = Bin  |  2 = Dec  |  3 = Hex\n" + 
        "Type \"Redo\" to start over, or \"Exit\" to quit.\n")

        # /// MOVE TO MODEL CLASS \\\
        if confirmIn.casefold() == "exit":
            auxFunctions.quit()
        elif confirmIn.casefold() == "redo":
            outputIteration = 1
            continue
        elif confirmIn == "1" or confirmIn.casefold() == "bin": #Bin
            decision = "bin"
            outputIteration += 1
        elif confirmIn == "2" or confirmIn.casefold() == "dec": #Dec
            decision = "dec"
            outputIteration += 1
        elif confirmIn == "3" or confirmIn.casefold() == "hex": #Hex
            decision = "hex"
            outputIteration += 1
        else:
            print("Please enter a valid input of 1 - 3, or \"Exit\" to quit.")
        
        # /// MOVE TO MODEL CLASS \\\

        #If invalid input will still execute. Okay because decision value will remain
        if outputIteration == 2: #first successful iteration
            inputType = decision 
        elif outputIteration == 3:
            if decision.casefold() == inputType.casefold(): #if the input matches the output (nothing to convert)
                print("\n!!!  ERROR: Input and Output types cannot match. Please select a different output.  !!!")
                outputIteration = 2
            else:
                outputType = decision #second successful iteration
    
    if outputIteration > 2:
        print("Input is: " + inputType + "\nOutput is: " + outputType)
    else:
        continue


#  ---===|  Input Validation: SECOND LOOP  |===---  #
    
    inputOkay = False
    while inputOkay == False: #while input ok?

        userIn = input("Type \"Exit\" at any time to end the program.\nEnter a number:\n")
        if userIn.casefold() == "exit":
            auxFunctions.quit()
        elif confirmIn.casefold() == "redo":
            outputIteration = 1
            break
        else:
            inputOkay = auxFunctions.verifyInput(userIn, inputType)

    if inputOkay == True:
        print("User input is: \"" + userIn + "\"\n"
            + "Input type is: " + inputType + "\n"
            + "Output type is: " + outputType + "\n")


#  ---===|  Perform Calculations  |===---  #
    finalResult = Calculator.calculate(userIn, inputType, outputType)
    print(finalResult[0], finalResult[1])
    # Send info to storage


