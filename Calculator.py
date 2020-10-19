#Performs calculations on user input, returns string on calculations performed

numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = [('a',10),('b',11),('c',12),('d',13),('e',14),('f',15)]

def calculate(inputNum, inputType, outputType):
    # print(inputNum)
    # print(inputType)
    # print(outputType)

    finalResult = []
    if inputType.casefold() == 'bin':
        if outputType.casefold() == 'dec':
            finalResult = binToDec(inputNum)
        elif outputType.casefold() == 'hex':
            finalResult = binToHex(inputNum)
    elif inputType.casefold() == 'dec':
        if outputType.casefold() == 'bin':
            finalResult = decToBin(inputNum)
        elif outputType.casefold() == 'hex':
            finalResult = decToHex(inputNum)
    elif inputType.casefold() == 'hex':
        if outputType.casefold() == 'bin':
            finalResult = hexToBin(inputNum)
        elif outputType.casefold() == 'dec':
            finalResult = hexToDec(inputNum)

    return finalResult

#Convert Decimal to Binary
def decToBin(inputDec):
    binOut = ""
    mathOutBin = ""

    while float(inputDec) > 1:
        if float(inputDec)%2 == 0:
            binOut = '0'+binOut
            mathOutBin = mathOutBin + str(inputDec) + "/2 = " + str(int(inputDec)/2) + " Remainder: 0\n"
        else:
            binOut = '1'+binOut
            mathOutBin = mathOutBin + str(inputDec) + "/2 = " + str(int(float(inputDec)/2)) + " Remainder: 1\n"

        inputDec = str(int(float(inputDec)/2))
        # print(inputDec)

    if int(inputDec) == 1:
        binOut = '1'+ binOut
        mathOutBin = mathOutBin + "1/2 = 0 Remainder: 1\n"

    # print(mathOutBin)
    # print("Binary Output: " + binOut)
    # print()
    return mathOutBin, binOut

# Convert Hexadecimal to Binary
def hexToBin(inputHex):
    binOuthex = ""
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
        

        print(str(iNum) + " " + str((type(iNum))))
        # If the returning binary is shorter than 4 digits, 
        # add a 0 until it is 4 digits long
        binReturn = (decToBin(iNum)[1])
        # binReturn = str(decToBin(iNum)[1])


        while len(binReturn) < 4:
            binReturn = "0" + str(binReturn)

        mathOutBin += str(iNum) + "hex\t=\t" + str(binReturn) + "bin\n"
        binOuthex += binReturn
    # END OF FOR EACH
    print(binOuthex)
    # mathOutBin += "RESULT: " + binOuthex
    # print(mathOutBin + "RESULT: " + binOuthex)
    return mathOutBin, binOuthex


# Convert Binary to Decimal
def binToDec(inputBin):
    decOut = 0
    mathOutDec = "Converting " + inputBin + "bin to Decimal:\n"
    binPower = 0

    for i in reversed(inputBin):
        decOut += (int(i))*(2**binPower)
        mathOutDec += i + "* (2 to the power of " + str(binPower) + ") = " + str((int(i))*(2**binPower)) + "\n"
        binPower += 1
    
    # print(mathOutDec + str(decOut))
    return mathOutDec, str(decOut)
    

# Convert Hexadecimal to Decimal
def hexToDec(inputHex):
    decOut = 0
    mathOutDec = "Converting " + inputHex + "hex to Decimal:\n"
    binPower = 0
    iNum = 0

    for i in reversed(inputHex):
        for a in letters:
            if i in numbers:
                iNum = int(i)
                break
            elif i.casefold() == a[0]:
                iNum = a[1]
                break

        decOut += iNum*(16**binPower)
        mathOutDec += str(iNum) + "* (16 to the power of " + str(binPower) + ") = " + str(iNum*(16**binPower)) + "\n"
        binPower += 1
    
    # print(mathOutDec + str(decOut))
    return mathOutDec, str(decOut)

# Convert Binary to Hexadecimal
def binToHex(inputBin):
    hexOut = ""
    mathOutHex = "Converting " + inputBin + " to Hexadecimal:\n"
    binPower = 0
    iterationNum = 0
    hexBlock = 0
    currentBin = ""

    for i in reversed(inputBin):

        if iterationNum < 4:
            currentBin = i + currentBin
            hexBlock += (int(i))*(2**binPower)
            iterationNum += 1
            binPower += 1
        else:
            # print("ELSE")
            for a in letters:
                if hexBlock == a[1]:
                    hexOut = a[0].upper() + hexOut
                    mathOutHex += currentBin + " converts to " + str(a[1]) + "dec, which in hex = " + a[0] + "\n"
            for a in numbers:
                if hexBlock == int(a):
                    hexOut = a + hexOut
                    mathOutHex += currentBin + " converts to " + a + "dec, which in hex = " + a + "\n"
            binPower = 0
            currentBin = i
            hexBlock = (int(i))*(2**binPower)
            iterationNum = 1
            binPower += 1

    # print("IterationNum: "+str(iterationNum)+".\tFinal hexblock is " + str(hexBlock))
    if iterationNum < 5:
        for a in letters:
            if hexBlock == a[1]:
                hexOut = a[0].upper() + hexOut
                mathOutHex += currentBin + " converts to " + str(a[1]) + "dec, which in hex = " + a[0] + "\n"
        for a in numbers:
            if hexBlock == int(a):
                if a == '0':
                    pass
                else:
                    hexOut = a + hexOut
                    mathOutHex += currentBin + " converts to " + a + "dec, which in hex = " + a + "\n"

    # print(mathOutHex + hexOut)
    return mathOutHex, hexOut
         

# binToHex("00111011111000001011111")
#8FAE


# dec to hex
def decToHex(inputDec):
    hexOut = ""
    mathOutHex = "Converting " + inputDec + " to Hexadecimal:\n"
    hexHolder = 0

    while int(inputDec) > 15:
        inputDec = float(inputDec)/16
        hexHolder = int(((inputDec) - (int(inputDec)))*16)
        
        if hexHolder < 10:
            for a in numbers:
                if hexHolder == int(a):
                    hexOut = a + hexOut
                    mathOutHex += a + " goes into hex as " + a + "\n"
        else:
            for a in letters:
                if hexHolder == a[1]:
                    hexOut = a[0].upper() + hexOut
                    mathOutHex += str(a[1]) + " goes into hex as " + a[0] + "\n"

    if int(inputDec) < 10:
        for a in numbers:
            if int(inputDec) == int(a):
                hexOut = a + hexOut
                mathOutHex += a + " goes into hex as " + a + "\n"
    else:
        for a in letters:
            if int(inputDec) == a[1]:
                hexOut = a[0].upper() + hexOut
                mathOutHex += str(a[1]) + " goes into hex as " + a[0] + "\n"

    # print(mathOutHex + hexOut + " hex")
    return mathOutHex, hexOut

