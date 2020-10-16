import sys

binNums = ['0', '1']
decNums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
hexNums = ['0','1','2','3','4','5','6','7','8','9','A','a','B','b','C','c','D','d','E','e','F','f']

# Verify the input value is appropriate for the datatype
def verifyInput(inputNum, numType):
    inputOkay = False
    for i in inputNum:
        # print(i)
        if numType.casefold() == "bin":
            if i in binNums:
                inputOkay = True
            else:
                print("ERROR: The value entered is not Binary. The character \""+i+"\" is invalid.")
                inputOkay = False
                break
        elif numType.casefold() == "dec":
            if i in decNums:
                inputOkay = True
            else:
                print("ERROR: The value entered is not a Decimal. The character \""+i+"\" is invalid.")
                inputOkay = False
                break
        elif numType.casefold() == "hex":
            if i in hexNums:
                inputOkay = True
            else:
                print("ERROR: The value entered is not Hexadecimal. The character \""+i+"\" is invalid.")
                inputOkay = False
                break
        else:
            print("ERROR: input type is not bin, dec, or hex")
            inputOkay = False
    return inputOkay



# Exit the program
def quit():
    print("\n  ---===|  Goodbye  |===---  \n")
    sys.exit()
