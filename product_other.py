"""
Given an array of integers, return a new array such 
that each element at index i of the new array is the
product of all the numbers in the original array except 
the one at i. For example, ifour input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24]. Ifourinputwas [3, 2, 1],
the expected output would be [2, 3, 6].
"""

#O(n)
def product(nums):
    prefix_product =[]
    suffix_product =[]
    for num in nums:
        if prefix_product:
            prefix_product.append(prefix_product[-1]*num)
        else:
            prefix_product.append(num)
    for num in reversed(nums):
        if suffix_product:
            suffix_product.append(suffix_product[-1]*num)
        else:
            suffix_product.append(num)
    suffix_product =list(reversed(suffix_product))
    #print(suffix_product)
    #print(prefix_product)
    result =[]
    for i in range(len(nums)):
        
        if i ==0:
            result.append(suffix_product[i+1])
        elif i == len(nums)-1:
            result.append(prefix_product[i-1])
        else:
            result.append(
                prefix_product[i-1]*suffix_product[i+1]
            )
    return result


print(product([1, 2, 3, 4, 5]))


#solution two



