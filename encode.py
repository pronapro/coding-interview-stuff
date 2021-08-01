vowels = "AEIOU"
def convert(char):
    n = int(ord(char))
    encoded_char = chr(n+4)
    return encoded_char

def encode_word(word):
    result = ""
    for i in range(len(word)):
        if i ==0 or i ==len(word)-1:
            result +=convert(word[i])
        elif word[i] not in vowels:
            result += convert(word[i])
    return result 


    #print(result)
    
#encode_word("is")
#encode_word("cOmE")

# encode string 
def encode_string(my_string):
    result_list = []
    result =""
    for word in my_string.split():

        result_list.append(encode_word(word))
    
    encoded_result = " ".join(result_list) 
    return encoded_result 

astring =  """
 A SUBSET OF MACHINE LEARNING IS CLOSELY RELATED TO COMPUTATIONAL STATISTICS
         WHICH FOCUSES ON MAKING PREDICTIONS USING COMPUTERS.
"""



print(encode_string(astring))







