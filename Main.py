# import sys
# import ModelCalc
import AuxFunctions
import Calculator
import ResultStorage

# tesing gitIgnore

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
            selectString = "\t-=| Select the INPUT datatype |=-\n"
        else:
            selectString = "\t-=| Select the OUTPUT datatype |=-\n"
        
        confirmIn = input("Command Menu:\n\"Redo\" to start over\n\"History\" to bring up previous calculations\n\"Exit\" to end the program\n\n"+selectString+"\t1 = Bin  |  2 = Dec  |  3 = Hex\n")

        # /// MOVE TO MODEL CLASS \\\
        if confirmIn.casefold() == "exit":
            AuxFunctions.quit()
        elif confirmIn.casefold() == "redo":
            outputIteration = 1
            continue
        elif confirmIn.casefold() == "history":
            # print("HISTORY CALL")
            AuxFunctions.printHistory()
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
        print("\n\t-=| Conversions Selected |=-\nInput is: " + inputType + "\nOutput is: " + outputType + "\n")
    else:
        continue


#  ---===|  Input Validation: SECOND LOOP  |===---  #
    
    inputOkay = False
    while inputOkay == False: #while input ok?

        userIn = input("Command Menu:\n\"Redo\" to start over\n\"History\" to bring up previous calculations\n\"Exit\" to end the program\n\n\t -=| Please enter a number |=-\n")
        if userIn.casefold() == "exit":
            AuxFunctions.quit()
        elif userIn.casefold() == "redo":
            outputIteration = 1
            break
        elif userIn.casefold() == "history":
            # print("HISTORY CALL")
            AuxFunctions.printHistory()
        else:
            inputOkay = AuxFunctions.verifyInput(userIn, inputType)

    if inputOkay == True:
        print("User input is: \"" + userIn + "\"\n"
            + "Input type is: " + inputType + "\n"
            + "Output type is: " + outputType + "\n")


#  ---===|  Perform Calculations  |===---  #

    skipMath = False

    try:
        if float(userIn) == 0:
            print("You have entered a value of Zero.\nYour return value is also Zero.\nThere is no conversion to perform.")
            skipMath = True
        else:
            pass
    except:
        pass

    if skipMath:
        print("Result: 0")
    else:
        finalResult = Calculator.calculate(userIn, inputType, outputType)
        print(finalResult[0] + "\nResult:\t" + finalResult[1])
        # Send info to storage
        # ResultStorage.calculations += finalResult
        ResultStorage.addHistory(finalResult)


