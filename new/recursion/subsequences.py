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



