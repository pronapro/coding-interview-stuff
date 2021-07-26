import math
def isprime(n):
    # all numbers less than 2 are not primes
    if n < 2:
        return False
    # loop from 2 to sqrt(n)
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        # check if (n mod i) is equal to 0, if so then there are # two numbers, a and b, that can multiply to give n
        if n % i == 0:
            return False

     
    return True