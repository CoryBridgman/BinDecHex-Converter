# testArray = [("A1\tline 1\nA1\tline 2\nA1\tline 3","A1\tResult: 1 2 3"), ("A2\tline 1\nA2\tline 2\nA2\tline 3", "A2\tResult: 1 2 3")]

calculations = []

def addHistory(n):
  calculations.append(n)

def printAllHistory():
    if len(calculations) == 0:
      print("Calculations array is empty")
    else: 
      indexNum = 0
      for c in calculations:
        print("Index [" + str(indexNum) + "] : " + c[1])
        indexNum += 1

# def printTEST():
#   if len(testArray) == 0:
#       print("Calculations array is empty")
#   else: 
#     index = 0
#     for c in testArray:
#         # while i < 2:
#       print("Index [" + str(index) + "] : " + c[1])
#       index += 1

# printTEST()