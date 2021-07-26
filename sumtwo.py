def sum_two(nums,s):
    hashtable ={}
    for num in nums:
        value = s-num 
        if value in hashtable:
            return(value,num)
        else:
            hashtable[num] = 1

#print(sum_two([3,3],6))

#return index
def sum_two_index(nums,s):
    hashtable ={}
    index = []
    for i,num  in enumerate(nums):
        value = s-num 
        if value in hashtable:
            index.append(hashtable[value])
            index.append(i)
        else:
            hashtable[num] = i
    return index

#print(sum_two_index([2,7,11,15],9))


#better structure 
def twoSum2(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable ={}

        for i,num  in enumerate(nums):
            value = target-num 
            if value in hashtable:
                return[hashtable[value],i]

            else:
                hashtable[num] = i

print(twoSum2([2,7,11,15],9))