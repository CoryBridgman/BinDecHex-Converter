#Performs calculations on user input, returns string on calculations performed

numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = [('a',10),('b',11),('c',12),('d',13),('e',14),('f',15)]

  # To do:
# dec to bin DONE
# hex to bin DONE
# bin to dec
# hex to dec
# bin to dec
# bin to hex

print("TESTING")

### TEST AREA ###

# testInput = input("Enter a number: ")
# DEC TO BIN
# decToBin(int(testInput))

# a = float(int(float(12.3456789)*100))/100
# print( " "+ str(len(str(a))-1) + "hi")

# try:
#     #method as int
# except:
#     try:
#         #method as float
#     except:
#         print("\nInvalid Input.\n")

### TEST AREA ###


#Convert Decimal to Binary
def decToBin(inputBin):
    binOut = ""
    mathOutBin = ""

    while inputBin > 1:
        if inputBin%2 == 0:
            binOut = '0'+binOut
            mathOutBin = mathOutBin + str(inputBin) + "/2 = " + str(int(inputBin/2)) + " Remainder: 0\n"
        else:
            binOut = '1'+binOut
            mathOutBin = mathOutBin + str(inputBin) + "/2 = " + str(int(inputBin/2)) + " Remainder: 1\n"

        inputBin = int(inputBin/2)
        # print(inputBin)

    if inputBin == 1:
        binOut = '1'+ binOut
        mathOutBin = mathOutBin + "1/2 = 0 Remainder: 1\n"

    # print(mathOutBin)
    # print("Binary Output: " + binOut)
    # print()
    return mathOutBin, binOut

# Convert Hexadecimal to Binary
def hexToBin(inputHex):
    binOut = ""
    mathOutBin = "Convert \"" + inputHex + "\" from Hex to Bin:\n"

    for i in inputHex:
        iNum = "default iNum"
        for a in letters:
            if i in numbers:
                iNum = int(i)
                break
            elif i.casefold() == a[0]:
                iNum = a[1]
                break
            else:
                pass
        
        # If the returning binary is shorter than 4 digits, 
        # add a 0 until it is 4 digits long
        binReturn = str(decToBin(iNum)[1])
        while len(binReturn) < 4:
            binReturn = "0" + binReturn
        mathOutBin += str(iNum) + "hex\t=\t" + str(binReturn) + "bin\n"
        binOut += binReturn
    mathOutBin += "RESULT: " + binOut
    # print(mathOutBin + "RESULT: " + binOut)
    return mathOutBin, binOut

hexToBin("AB5C")

# bin to dec
def binToDec(inputBin):
    
    pass


# hex to dec
# bin to dec
# bin to hex