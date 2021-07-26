def unique(astring):
    for i in range(len(astring)):
        for j in range(i+1,len(astring)):
            if astring[i] == astring[j]:
                return False
    return True
#print(unique("unique"))
#print(unique("astring"))
#print(unique("n"))

#check if length is greater than 128

def is_unique_chars(string):
 
    if len(string) > 128:
        return False

    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True

#use set or bits for improvements
#Try a hash table. 
#Could a bit vector be useful? 
#Can you solve it in O(N log N) time? What might a solution like that look like? 

