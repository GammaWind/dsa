#
'''
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

'''

from typing import List


def combination_sum(i:int, inp: List, ds: list, target:int, ans: List[List[int]]) -> List[List[int]] :

    #base case
    if i == len(inp):
        if target == 0:
            
            ans.append(ds.copy())
            
        return    

   
    if inp[i] <= target:

        ds.append(inp[i])
        combination_sum(i, inp, ds, target - inp[i], ans)
        ds.pop()

        
    
        
    return combination_sum(i+1, inp, ds, target, ans)

ans = []
combination_sum(0, [2,3,6,7], [], 7, ans)
print(ans)            

