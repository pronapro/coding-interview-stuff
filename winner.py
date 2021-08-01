import random
def winning(Alice,Bob):
    alice_wins = 0
    bob_wins = 0
    numberOfTrials = 10000

    for t in range( numberOfTrials ):
        myList = [ random.randint(0,1), random.randint(0,1), random.randint(0,1) ]
        flips = 3
        bob_count =alice_count = 0

        while alice_count == 0 or bob_count == 0:
            if alice_count == 0 and myList[flips-3:flips] == Alice:
                alice_count = flips
            if bob_count == 0 and myList[flips-3:flips] == Bob:
                bob_count = flips
            myList.append(random.randint(0,1))
            flips += 1

        alice_wins += alice_count
        bob_wins += bob_count
    number_of_wins = bob_wins+alice_wins
    alice_prob =alice_wins/number_of_wins
    bob_prob =bob_wins/number_of_wins


    print ('Alice wins :', alice_wins,"Alice probability", alice_prob)
    print ('Bob wins :', bob_wins, "lice probability",bob_prob)
    return((alice_wins,alice_prob),(bob_wins,bob_prob))

print(winning([1,0,1],[1,1,1]))