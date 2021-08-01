import random
def winning(Alice,Bob):
    HTH = 0
    HTT = 0
    numberOfTrials = 10000

    for t in range( numberOfTrials ):
        myList = [ random.randint(0,1), random.randint(0,1), random.randint(0,1) ]
        flips = 3
        HTHflips = HTTflips = 0

        while HTHflips == 0 or HTTflips == 0:
            if HTHflips == 0 and myList[flips-3:flips] == [1,0,1]:
                HTHflips = flips
            if HTTflips == 0 and myList[flips-3:flips] == [1,0,0]:
                HTTflips = flips
            myList.append(random.randint(0,1))
            flips += 1

        HTH += HTHflips
        HTT += HTTflips


    print ('HTT :', numberOfTrials, HTT, float(HTT)/numberOfTrials)
    print ('HTH :', numberOfTrials, HTH, float(HTH)/numberOfTrials)

winning("Alice","Bob")