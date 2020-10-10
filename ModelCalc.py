class Calc:

    def classTest(self):
        print("Class test working")

    def isANumber(self, n):
        if n == int or float or complex:
            print(str(n) + " is a number!")
        else:
            print(str(n) + " is not a number :(")
