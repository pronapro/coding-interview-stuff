

#use hash tables 
def permutation(astring,bstring):
    hash1 ={}
    hash2 ={}
    if len(astring) != len(bstring):
        return False    
    for char in astring:
        if char in hash1:
            hash1[char] += 1
        hash1[char] = 1
        
    for char in bstring:
        if char in hash2:
            hash2[char] += 1
        hash2[char] = 1
    return hash1 == hash2

"""
Describe what it means for two strings to be permutations of each other. Now, look at
that definition you provided. Can you check the strings against that definition? 
Two strings that are permutations should have the same characters, but in different
orders. Can you make the orders the same?
Could a hash table be useful? 
There is one solution that is 0 (N log N) time. Another solution uses some space, but
isO(N) time. 

"""
# instead of using hash dict use counter from collections

        
         