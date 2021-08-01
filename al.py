import random

HTH = 0
HTT = 0
myList = []
i = 0
numberOfTosses = 1000000

while i < numberOfTosses:
    myList.append(random.randint(0,1))
    i += 1

for i in range (len(myList)):

    if i+2 >= len(myList):
        break

    if myList[i] == 1 and myList[i+1] == 0 and myList[i+2] == 1:
        HTH +=1

    if myList[i] == 1 and myList[i+1] == 0 and myList[i+2] == 0:
        HTT +=1

print ('HTT :' ,numberOfTosses, HTT, numberOfTosses/HTT)
print ('HTH :' ,numberOfTosses, HTH, numberOfTosses/HTH)