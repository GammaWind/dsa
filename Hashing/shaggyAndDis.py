'''
Shaggy and distances
Problem Description

Shaggy has an array A consisting of N elements. We call a pair of distinct indices in that array as a special pair if elements at that index in the array are equal.

Shaggy wants you to find a special pair such that distance between that pair is minimum. Distance between two indices is defined as |i-j|. If there is no special pair in the array then return -1.



Problem Constraints
1 <= |A| <= 105



Input Format
First and only argument is the array A.



Output Format
Return one integer corresponding to the minimum possible distance between a special pair.



Example Input
Input 1:

A = [7, 1, 3, 4, 1, 7]
Input 2:

A = [1, 1]


Example Output
Output 1:

 3
Output 2:

 1


Example Explanation
Explanation 1:

Here we have 2 options:
1. A[1] and A[4] are both 1 so (1,4) is a special pair and |1-4|=3.
2. A[0] and A[5] are both 7 so (0,5) is a special pair and |0-5|=5.
Therefore the minimum possible distance is 3. 
Explanation 2:

Only possibility is choosing A[1] and A[2].

APPROACH : TC O(N)
sc : O(DISTINCT ELEMENTS) ~ O(N)

here we need to find 2 nearest indexes such that their values are same.
we can store each element in list to hashmap along with its index but when again the same key appeares we can calculate the diff between 2 indexes 
also one thing to keep in mind, we need to update the index pos of the elements once we calculate the diffeence as we meed minimum diff not maximum
'''


import sys

def solve(A):
    minDistance = sys.maxsize
    hMap = dict()
    for i in range(len(A)):
        if A[i] not in hMap:
            hMap[A[i]] = i
            
        elif A[i] in hMap:
            diff  = i - hMap[A[i]]
            hMap[A[i]] = i
            minDistance = min(diff, minDistance)
        
    if  minDistance == sys.maxsize:
        return -1
    return minDistance        

A = [7, 1, 3, 4, 1, 7]
print(solve(A))