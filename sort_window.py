"""
Given an array of integers that are out of order, determine the bounds of the smallest
window that must be sorted in order for the entire array to be sorted. For example, 
given[3, 7, 5, 6, 9],youshouldreturn(1, 3).
"""
#0(nlogn)
def window(nums):
    left,right =None,None
    a =sorted(nums)
    for i in range(len(nums)):
        if nums[i]!=a[i] and left is None:
            left =i
        elif nums[i] !=a[i]:
            right =i 
    return left,right
print(window([3, 7, 5, 6, 9]))
        