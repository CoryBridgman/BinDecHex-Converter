from ModelCalc import Calc
from noClassCalc import toBin

print("running Main")

Converter = Calc()

Converter.classTest()
#test

#toBin(input("Enter a number"))

userIn = ""

while True:
    userIn = input("Type \"Exit\" to end the program.\nEnter a number: ")

    if userIn.casefold() == "exit":
        break
    else:
        print(userIn.casefold())