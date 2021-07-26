""" You are given a string with the symbols ( and ) and 
you need to write a function that will determine if the parenthsis 
are correctly nested in the string which means every opening 
( has a closing )
True
()
(())
()()()
False
((()()))
(()
((((
())()
()()())
"""
def check(astring):
    holder = 0
    open ="("
    close =")"
    for i in astring:
        if i ==open:
            holder +=1
        elif  i ==close:
            holder -=1
    if holder== 0:
        return True
    else:
        return False
  

print(check("((()()))"))