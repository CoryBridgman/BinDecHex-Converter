import sys
import ResultStorage

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

#Math string builder
# toBin
# toDec
# toHex
    # if input = dec do:
    # if input = bin do:


#  ---===|  Print History  |===---  #

def printHistory():
    print("\t-=| Select an option to display calculation history |=-\n" +
    "1: View entire calclation histroy\n" +
    "2: View a specific calculation, with math process details\n"+
    "3: Delete specific calculation from history\n"+
    "4: Delete entire calculation history")
    histIn = input("Enter your selection: ")
    if histIn == '1':
        ResultStorage.printAllHistory()
        #view all
    elif histIn == '2':
        pass
        #view one
    elif histIn == '3':
        pass
        #delete one
    elif histIn == '4':
        pass
        #delete all
    else:
        print("\"" + histIn + "\" is not a valid entry.")

# Exit the program
def quit():
    print("\n  ---===|  Goodbye  |===---  \n")
    sys.exit()
