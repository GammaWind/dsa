#find all the subsequences of a given array
'''
eg. arr = [3,1,2]
ans = [3] [3,1] [3,1,2] [1] [1,2] [2] [] [3,2]
lists can be any order
'''



from typing import List


def get_subsequnce(i:int, ans: List, lst: List, ip: List) -> List:

    if i >= len(ip):
        print(lst)
        return

    #add the number to lst
    lst.append(ip[i])
    get_subsequnce(i+1, ans, lst, ip)

    #remove the number and call
    lst.pop()
    get_subsequnce(i+1, ans, lst, ip)

get_subsequnce(0, [], [], [3,1,2])


#time complexity analysis

"""
for every function call we are calling out 2 new recusions
so for n functions it would be 2^n

"""
print("======================================================")

#all Subsequence with sum equals to k
'''
eg. arr = [3,1,2] k = 3
ans = [3] [1,2]
lists can be any order
'''

def get_subsequence_sum(i: int, inp: List, ans: List, k: int) -> None:

    if i >= len(inp):
        if sum(ans) == k:
            print(ans)
        return

    ans.append(inp[i])
    get_subsequence_sum(i+1, inp, ans, k)

    ans.pop()
    get_subsequence_sum(i+1, inp, ans, k)

get_subsequence_sum(0,[3,1,2],[],3)


#subsequence sum equals to k print/return only first matching subsequence
"""
eg. arr = [3,1,2] k = 3
matching subsequences = [3] [1,2]
ans = [3]
"""

def first_subsequnce_sum(i:int, inp: List, ans: List, k=int):
    
    if i >= len(inp):
        if sum(ans) == k:
            print(ans)
            return True
        else:
            return False

    ans.append(inp[i])
    if first_subsequnce_sum(i+1, inp, ans, k):
        return True
    ans.pop()
    if first_subsequnce_sum(i+1, inp, ans, k):
        return True

print("////////////////////////////////////////////////////////")

print(first_subsequnce_sum(0,[3,1,2], [], 3))
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")


#count of subsequence sum equals to k print/return only first matching subsequence

"""
COUNTS ARE USEFUL IN DP
eg. arr = [3,1,2] k = 3
matching subsequences = [3] [1,2]
ans = 2

here to optimize we will calculate the sum while recursing
"""

def count_subsequence_sum_k(i:int, inp: List, k, su:int) -> int:

    if i >= len(inp):
        if su == k:
            return 1
        else:
            return 0

    su += inp[i]
    first = count_subsequence_sum_k(i+1, inp, k, su)

    su -= inp[i]
    second = count_subsequence_sum_k(i+1, inp, k, su)  

    return first + second 


ans = count_subsequence_sum_k(0,[3,1,2], 3, 0)
print(ans)

