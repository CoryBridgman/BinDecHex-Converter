def toBin(n):
#isNumeric(n) -> check if all chars in STRING are numbers
    try:
        n = int(n)
    except:
        try:
            n = float(n)
        except:
            print(type(n))


    if isinstance(n, int) or isinstance(n, float):
        print("Variable " + str(n) + " is a number. " + str(type(n)))
    else:
        print("ERROR: " + str(type(n)) + "NOT A VALID NUMBER")

