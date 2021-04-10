'''

1)Given a list of non negative integers, arrange them such that they form the largest number.
For example:
Given [3, 30, 34, 5, 9], the largest formed number is 9534330.
Note: The result may be very large, so you need to return a string instead of an integer.
'''

'''
Approach

idea is to sort 2 elemets by comparing them in their string version
ie first = 34 second  = 30

first + second  = "3430"

second + first = "3034"

here first + Second will give bigger value

used custom sort in descending order passong our custom sort function

'''

from functools import cmp_to_key


def customSortLogic(first,second):
    isFirstLarge = str(first) + str(second)
    isSecondLarge = str(second) + str (first)

    if int(isFirstLarge) > int(isSecondLarge):
        return 1
    elif int(isFirstLarge) < int(isSecondLarge):
        return -1
    return 0        
    

def LargestNumber(A):
    A= sorted(A,key=cmp_to_key(customSortLogic),reverse=True)
    return ''.join(str(a) for a in A)

A =  [3, 30, 34, 5, 9]
print(LargestNumber(A))


