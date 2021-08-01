vowels = "AEIOU"
def convert(char):
    n = int(ord(char))
    encoded_char = chr(n-4)
    return encoded_char

def decode_word(word):
    result = ""
    for i in range(len(word)):
        result += convert(word[i])
    return result 


    #print(result)
    


# decode string 
def decode_string(my_string):
    result_list = []
    result =""
    for word in my_string.split():

        result_list.append(decode_word(word))
    
    encoded_result = " ".join(result_list) 
    return encoded_result 

astring =  """
E PRK XQI EKS MR E KP\] JV JV E[]222
"""



print(decode_string(astring))







