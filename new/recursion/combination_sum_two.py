'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

https://leetcode.com/problems/combination-sum-ii/

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
'''


from typing import List


def combination_sum_two(i:int, inp: List, target:int, ds: List, ans: List) -> List:

   
    if target == 0:
        print(ds)
        ans.append(ds.copy())
        return


    for j in range(i, len(inp)):
        if j > i and inp[j] == inp[j-1]:
            continue

        if inp[j] > target:
            break

        
        
        ds.append(inp[j])
        combination_sum_two(j+1, inp, target - inp[j], ds, ans)

        ds.pop()


candidates = [10,1,2,7,6,1,5]
target = 8
#SORTING THE ARRAY IS NECESSARY
candidates.sort()
ans = []
combination_sum_two(0, candidates, target, [],ans)
print(ans)