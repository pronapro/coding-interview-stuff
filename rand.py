import random
def winning(Alice,Bob):

    bob_count = 0
    alice_count = 0
    myList = []
    i = 0
    numberOfTosses = 1000000

    while i < numberOfTosses:
        myList.append(random.randint(0,1))
        i += 1

    for i in range (len(myList)):

        if i+2 >= len(myList):
            break

        if myList[i] == Alice[0] and myList[i+1] == Alice[1] and myList[i+2] == Alice[2]:
            alice_count +=1

        if myList[i] == Bob[0] and myList[i+1] == Bob[1] and myList[i+2] == Bob[2]:
            bob_count +=1

    print ('HTT :' ,numberOfTosses, alice_count, numberOfTosses/alice_count)
    print ('HTH :' ,numberOfTosses, bob_count, numberOfTosses/bob_count)

winning((1,1,1),(0,1,1))