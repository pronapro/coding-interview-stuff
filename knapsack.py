def knapsack(capacity,n,size,value):
    if n==0 or capacity ==0:
        return 0
    elif size[n-1]>capacity:
        return knapsack(capacity,n-1,size,value)
    else:
        return max(value[n-1]+knapsack(capacity-size[n-1],n-1,size,value),knapsack(capacity,n-1,size,value))

capacity = 16
n = 5
size = [3,4,7,8,9]
value =[4,5,10,11,13]
print(knapsack(capacity,n,size,value))