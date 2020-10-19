# testArray = [("A1\tline 1\nA1\tline 2\nA1\tline 3","A1\tResult: 1 2 3"), ("A2\tline 1\nA2\tline 2\nA2\tline 3", "A2\tResult: 1 2 3")]

# tesing gitIgnore

calculations = []

def addHistory(n):
  calculations.append(n)

def removeHistory(n):
  pass

def clearHistory():
  calculations.clear()

def printHistory(n):
  i = 0
  n = int(n)
  print("\n\t-=|  Calculating [input , type] to [type]  |=-\n")
  while i < len(calculations[0]):
    if i < 1:
      print(calculations[n][i])
    else:
      print("Result: " + calculations[n][i])
    i += 1

def printAllHistory():
    if len(calculations) == 0:
      print("Calculations array is empty")
    else: 
      indexNum = 0
      for c in calculations:
        print("Index [" + str(indexNum) + "] : " + c[1])
        indexNum += 1

# -----
            # Input: 1234 dec
            # Answer: 1a2b hex
            # ID number: 3
            # -----
            # Input: ...




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