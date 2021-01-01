#####
#swapping app
hold =x
x =y
y = hold
#or
x,y =y,x

######
#Flag variables
""" 
a flag variable can be used to let one part of your program. know when something happens in another part of the program. 
example to determine if number is prime.
"""
num = eval(input("Enter number: "))
flag = 0
for i in range(2,num):
	if num%2 ==0:
		flag  =1
if flag ==1:
	print("not prime")
else:
	print("prime")

#maxes and mins
largest = eval(input("Enter a postive"))
for i in range(9):
	num = eval(input("Enter a positive number"))
	if num >largest:
		largest = num
print(" largest number is: "+ largest)

##########
#stack
############
""" 
the order that they are removed is exactly the reverse of the order that they were placed
the order of insertion is the reverse of the order of removal
##stack operations
s.is_empty()
s.peek()
s.push(True)
S.size()
s.pop()
stack() creates a new  stack that is empty 
"""
class Stack:
	"""docstring for ClassName"""
	def __init__(self):
		self.items =[]
	def is_empty(self):
		return self.items ==[]
	def push(self,item):
		self.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items)-1]
	def size(self):
		return len(self.items)
##########################
#checking parenthesis
########################
def par_checker(symbol_string):
	s =stack()
	balanced =True
	index =0
	while index< len(symbol_string) and balanced:
		symbol =symbol_string[index]
		if symbol == "c":
			s.push(symbol)
		else:
			if s.is_empty():
				balanced =False
			else:
				s.pop()
		index = index+1
	if balanced and s.is_empty():
		return True
	else:
		return False

####################
#Binary
#########################
def divide_by_2(dec_number):
	rem_stack = stack()
	while dec_number>0:
		rem = dec_number%2
		rem_stack.push(rem)
		dec_number = dec_number//2
	bin_string =" "
	while not item_stack.is_empty():
		bin_string =bin_string +str(rem_stack.pop())
	return bin_string
############
#sort stack
############
def sort(input):
	output =stack()
	while(not input.is_empty()):
		temp =input.pop()
		while not (output.is_empty()) and (output.peek(temp)):
			input.push(output.pop())
		output.push(temp)
	return output

#########
#insert(p,x) insert x at position p

s = "1-800-271-828"
s.split("-")


##########
#Queue
#############
""" 
add at back and remove at front
operations
q.is_empty()
q.enqueue()
q.size()
q.queue()
queue() creates a new queue
"""
class Queue:
	def __init__(self):
		self.items =[]
	def is_empty(self):
		return self.items ==[]
	def enqueue(self,item):
		self.items.insert(0,item)
	def dequeue(self):
		return self.item.pop()
	def size(self):
		return len(self.items)

#####################
#Hashing
#####################
"""
mudulo arithmetric (remainder) h(item)= item%11
after values have been computed, we insert each item into the hash table at designated position as shown
note: loop the slots are now occuied . this is referred to as load factor and commonly denoted by n
∫ =no of items
	_____________
	table_size

##folding method
diving number and adding them
##midsquare method
get square of middle point and using modula of missle points

we can create hash functions for character based item such as strings. tje cat can be thought of as sequence of ordinal values
ord('c') =99

######
##hash for the strings
###########

"""
def has(astring,table):
	sum =0
	for pos in range(len(astring)):
		sum =sum+ord(astring[pos])
	return sum%table_size
#############
#implementing the Map Abstract Datatype
################
"""
map() create a new, empty map, it returns an empty map collection
put(key,value) add a new key-value pair to the map. if the key is already in the map then replace the old value with the new value
get(key) given a key return the value stored in the map or none otherwise
del
len() returns the number of the key-value pairs stored in the map

"""
class Hashtable:
	def __init__(self):
		self.size =1
		self.slots =[None]*self.size
		self.data = [None]*self.size

	def put(self,key,data):
		hash_value =self.hash_function(key,len(self.slots))
		if self.slots[hash_value] == None:
			self.slots[hash_value] = key
			self.data[hash_value] =data
		else:
			if self.slots[hash_value]== key:
				self.data[hash_value]= data 
			else:
				next_slot = self.rehash(hash_value, len(self.slots))
				while self.slots[next_slot] != None and self.slots[next_slot] !=key:
					next_slot =self.rehash(next_slot, len(self.slots))
					if self.slots[next_slot] == None:
						self.slots[next_slot] = key
						self.data[next_slot] = data

					else:
						self.data[next_slot] = data
	def hash_function(self, key,size ):
		return key%size
	def rehash(self,old_hash,size):
		return (old_hash+1)%size

	def get(self,key):
		start_slot =self.hash_function(key, len(self.slots))
		data = None
		stop =False
		Found =False
		postion = start_slot
		while self.slots[postion] !=None and not found and not stop:
			if self.slots[position] == key:
				found =True
				data = self.data[postion]
			else:
				position =self.rehash(position,len(self.slots))
				if position ==start_slot:
					stop =True
		return data
	def __getitem__(self,key):
		return self.get(key)
	def __setitem__(self, key,data):
		self.put(key,data)

###################
#sorting algorithms
#######################
##########
##bubble sort
#############
def bubble_sort(a_list):
	for pass_num in range(len(a_list-1,0,-1)):
		for i in range(pass_num):
			if a_list[i]>a_list[i+1]:
				temp =a_list[i]
				a_list[i] = a_list[i+1]
				a_list[i+1] = temp

################
#selection sort
#################
"""looks at largest value as it makes a pass"""
def selection_sort(a_list):
	for fill_slot in range(len(a_list)-1,0,-1):
		pos_of_max =0
		for location in range(1,fill_slot+1):
			if a_list[location]>a_list[pos_of_max]:
				pos_of_max = location
		temp = a_list[fill_slot]
		a_list[fill_slot] = a_list[pos_of_max]
		a_list[pos_of_max] = temp

##################
#insertion sort
#####################
def insertion_sort(a_list):
	for index in range(1,len(a_list)):
		current_value = a_list[index]
		position = index
		while position> 0 and a_list[position]>current_value:
			a_list[position] = a_list[position-1]
			position =position-1
		a_list[position] = current_value

####
#shell sort
########


##################
#the merge sort
################

#######
#quick sort
##############
def sort(array):
	less =[]
	equal =[]
	greater =[]
	if len(array)>1:
		pivot =array[random.rand.int(o,len(array)-1)]
		for x in array:
			if x<pivot:
				less.append(x)
			if x==pivot:
				equal.append(x)
			if x>pivot:
				greater.append(x)
				return sort(less)+equal+sort(greater)
	else:
		return array







#checking execution time
def time_execution(code):
	start = time.clock()
	result = eval(code)
	run_time = time.clock()-start
	return result, run_time

###############
#set
##############
class Set:
	def __init__(self):
		self._the_elements =list()
	def __len__(self):
		return len(self._the_elements)
	def __contains__(self,elements):
		return elements in self._the_elements
	def remove(self,elements):
		assert element in self
		self._the_elements.remove(item)
	def __eq__(self,setB):
		if len(self)!=len(setB):
			return False
		else:
			return self.isSubsetof(setB)
	def isSubsetof(self,setB):
		for element in self:
			if element not in setB:
				return False
		return True
	def union(self,setB):
		newset =set()
		newset._the_elements.extent(self._the_elements)
		for elements in setB:
			if elements not in self:
				newset._the_elements.append(element)
		return newset


###############################################
##LIST
##############################################
""" 
the node class
1. data field
2.
"""
class Node:
	def __init__(self,init_data):
		self.data = init_data
		self.next = None
	def get_data(self):
		return self.data
	def get_next(self):
		return self.next
	def set_data(self, new_data):
		self.data =new_data
	def set_next(self,new_next):
		self.next =new_next

"""
List is a collection of 
start head = None
is empty

"""
class UnorderedList:
	def __init__(self):
		self.head =None
	def is_empty(self):
		return self.head ==None
	def add(self,item):
		temp =Node(item)
		emp.set_next(self.head)
		self.head =temp
	def size(self):
		current =self.head
		count =0
		while current !=None:
			count =count+1
			current = current.get_next()
		return count

	def search(self,item):
		current =self.head
		found =False
		while current !=None and not found:
			if current.get_data() ==item:
				found =True
			else:
				current =current.get_next()
		return found

	def remove(self,item):
		current =self.head
		previous =None
		found =False 
		while not found:
			if current.get_data() ==item:
				found =True
			else:
				previous =current
				current = current.get_next()
			if previous ==None:
				self.head =current.get_next()
			else:
				previous = set_next(current.get_next())


##################################
#searching algorithm complexity = O(n)
##################################
def search_list(a_item, i_list):
	pos = 0
	found = False
	while pos<len(i_list) and not found:
		if i_list[pos] ==a_item:
			found =True
		else:
			pos +=1
	return found

##################
#binary search complexity = O(log n)
##################
def binary_search(alist,item):
	if len(alist) ==0:
		return False
	else:
		midpoint =len(alist)//2
		if alist[midpoint] ==item:
			return True
		else:
			if item <alist[midpoint]:
				return binary_search(alist[:midpoint],item)
			else:
				return binary_search(alist[midpoint:],item)

def is_isomorphic(x,y):
	if len(x) !=len(y):
		return False
	char_mapping ={ }
	for i in xrange(0,len(x)):
		if x[i] in char_mapping:
			if char_mapping.get(x[i])!=y[i]:
				return False
			else:
				if y[i] in char_mapping.value():
					return False
				char_mapping[x[i]] ==y[i]
	return True


################################
#reverse string
#################################
def(string)
	result =""
	index =len(string)-1
	for i in range(len(string)):
		result +=string[index]
		index -=1
	return result

###########################
#antivowel
###########################
def anti_vowel(text):
	ans =" "
	for char in text:
		if char.lower() not in "aeiou":
			ans+ =char
	return ans

####################
#triangle check if shape is a triangle
#########################
class Triangle:
	num_of_sides =3
	def __init__(self,angle1,angle2,angle3):
		self.angle1 =angle1
		self.angle2 = angle2
		self.angle3 =angle3
	def check_angles(self):
		sum =self.angle1+self.angle2+self.angle3
		if sum ==180:
			return True
		else:
			return False
########################
#factorial
########################
def factorial(x):
	if x ==1:
		return 1
	else:
		ans =x
		while x>1:
			ans *=x-1
			x -=1
	return ans

################################
#LONGEST COMMON SUBSTRING
###############################
def lcs(a,b):
	maximum =0
	dp =[[0 for i in b] for i in a]
	for i in range(len(a)):
		for j in range(len(b)):
			if a[i]==b[i]:
				if i ==0 or j==0:
					dp[i][j] =1
				else:
					dp[i][j] =1+dp[i-1][j-1]
					maximum =max(maximum,dp[i][j])
		return maximum

"""
given an array of integers, return indices of the two number such that they add up to a specific target
"""
def two_sum(nums,target):
	d ={}
	for i,num in enumerate(nums):
		if target-num in d:
			return [d[target-num],1]
		else:
			d[num] =i
##########
#add 3 elements n get zero
##################
def three_sum(self,nums):
	res =[]
	sorted_list =sorted(nums)
	for left in xrange(0,len(nums)-2):
		left =0
		right =len(nums)-1
		mid =left+1
		right =len(nums)-1
		while mid <right:
			new_list =[sorted_list[left],sorted_list[mid],sorted_list[right]]
			s =sum(new_list)
			if s>0:
				right -=1
			elif s<0:
				mid +=1
			else:
				if new_list not in res:
					res.append(new_list)
					mid +=1
		return res

##########
#adding digits until 1
###########################
def add_digits(num):
	if num ==0:
		return 0
	else:
		return (1+(num-1)%9)

##############################
#pascal's triangle
#####################
def generate_pascal(numrows):
	triangle =[]
	for i in xrange(0,numrows):
		new_row =[1]*(i*1):
		for j in xrange(1,i):
			new_row[j] =triangle[i-1][j-1]+triangle[i-1][j]
			triangle.append(new_row)
	return triangle

################################
#find the common elements of 2 int arrays
#################################
def find_common(array1,array2):
	hash_table =dict()
	shared_elements =set()
	for element in array1:
		if element not in hash_table:
			hash_table[element] =True
	for element in array2:
		if element in hash_table:
			shared_elements.add(element)
	return shared_elements

#########
##########
def find_single_occurance(self):
	hash_table =dict()
	#add all elements into hastable
	for element in array:
		if element not in hash_table:
			hash_table[element] =1
		else:
			hash_table[element] +=1
		#find element that occurs once
	for key in hash_table.keys():
		if hastable[key] is 1:
	return key
#################
#fibonnacci
####################
def fibonnacci_recursive(index):
	if index <=0:
		return 0
	if index<2:
		return 1
	if index not in hastable:
		hastable[index] =fibonnacci_recursive(index-2)+fibonnacci_recursive(index)


##############
#array pair sum
######################
#nlogn
def mid_find_pair_sum(int_arr,target):
	pairs =[]
	#sort array
	int_arr.sort()
	for i in range(len(int_arr)):
		x =int_arr[i]
		compliment =target-x
		#find compliment with binary search
		found_compliment = _bisearch(array,compliment)
		if found_compliment:
			y = int_arr[found_compliment]
			pairs.append(i,found_compliment,x,y)
	return pairs

###########
#O(n)
def best_find_pair_sum(int_arr,target):
	pairs =[]
	hastable =dict()
	#add all of items into a hashtable
	for item in int_arr:
		hashtable[item] =True
	for i in range(len(int_arr)):
		x =int_arr
		compliment =target-x
		#look up compliment in hashtable if it exists
		found_compliment =None
		if compliment in hashtable:
			found_compliment =compliment
		if found_compliment and x is not found_compliment:
			pairs.append(x,found_compliment)
	return pairs

def is_substring(array1,array2):
	i =0
	for i in array1:
		if is not array2[i]:
			i =0
		if i is len(array2)-1:
			return True
			i+=1
	return False
######
#check if a string is composed of all unique character
#############################################

def check_all_unique(string):
	hashtable =dict()
	#add all chars to hashtable for their frequency
	for char in string:
		if char not in hashtable:
			hashtable[char] =1
		else:
			hashtable[char]+=1
	#check if all chars only occured once
	for char in hashtable.keys():
		if hashtable[char] is not 1:
			return False
	return True
###
#Anagram: words that are same but differnt arrangement
#
def check_anagram(str1,str2):
	if len(str1) is not len(str2):
		return False
		hashtable1 =dict()
		hashtable2 =dict()
	#add all of strings 1 and string2 char frequences to hashtable
	for i in range(len(str1)):
		char1 =str1[i]
		char2 =str2[i]
		#add char1 to hashtable 1
		if char1 not in hashtable1:
			hashtable1[char1] =1
		else:
			hashtable1[char1]+=1
		if char2 not in hashtable2:
			hashtable2[char2] =1
		else:
			hashtable2[char2]+=1	
	return hashtable1 ==hashtable2

#check palindrome
def check_palindrome(string):
	string =string.replace(" "," ").lower()
	for i in range(len(string)):
		if string[i] is not string[len(string)-1]:
			return False
	return True

#find the first non repeated character in string
def find_non_repeat(string):
	hashtable =dict()
	#add all chars into hashtable with their frequencies
	for char in string:
		if char not in hashtable:
			hashtable[char]+=1
		else:
			hashtable[char]+=1
	for char in string:
		if hashtable[char] is 1:
			return char
	return None



#######################
#reverse string
######################
#iteratively
def reverse_iteratively(string):
	new_string =str()
	for char in reversed(string):
		new_string +=char
	return new_string
#recursively
def reverse_recursively(string):

	length =len(string)
	if length ==1:
		return string
	return string[length-1]+ reverse_recursively(string[-1])

#if one is a permutation of another
def check_permutation(first_string,second_string):
	if len(first_string) !=len(second_string):
		return False
	count_dictionary ={}
	for char in first_string:
		if char in count_dictionary:
			count_dictionary[char]+=1
		else:
			count_dictionary[char] =1
	for char in second_string:
		if char in count_dictionary and count_dictionary[char] !=0:
			count_dictionary[char] -=1
		else:
			return False
	return True

#remove duplicates
def remove_duplicate(duplicate):
	final_list =[]
	for num in duplicate:
		if num not in final_list:
			final_list.append(num)
	return final_list


#########################################
#binary search
#########################################
def binary_tree(r):
	return [r,[],[]]
def insert_left(root,new_branch):
	t =root.pop(1)
	if len(t)>1:
		root.insert(1,[new_branch,t,[]])
	else:
		root.insert(1,[new_branch,[],[]])
	return root
def insert_right(root,new_branch):
	t =root.pop(2)
	if len(t)>1:
		root.insert(2,[new_branch,t])
	else:
		root.insert(2,[new_branch,[],[]])
	return root
def get_root_val(root):
	return root[0]
def set_root_val(root,new_val):
	root[0] =new_val
def get_left_child(root):
	retrurn root[1]
def get_rigt_child(root):
	return root[2]


#binary tree using nodes and references

class binary_tree(self,root):
	self.key =root
	self.left_child =None
	self.right_child =None

	def insert_left(self,new_node):
		if self.left_child ==None:
			self.left_child =binary_search(new_node)
		else:
			t = binary_search(new_node)
			t.left_child =self.left_child
			self.left_child =t

	def insert_right(self,new_node):
		if self.right_child ==None:
			self.right_child =binary_search(new_node)
		else:
			t = binary_search(new_node)
			t.right_child =self.right_child
			self.right_child =t

	def get_right_child(self):
		return self.right_child
	def get_left_child(self):
		return self.left_child
	def set_root_val(self,obj):
		self.key = obj
	def get_root_val(self):
		return self.key





































































































