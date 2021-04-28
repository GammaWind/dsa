'''
Special Integer
Problem Description

Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with sum of elements greater than B.



Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10^9

1 <= B <= 10^9



Input Format
The first argument given is the integer array A.

The second argument given is integer B.



Output Format
Return the maximum value of K (sub array length).



Example Input
Input 1:

A = [1, 2, 3, 4, 5]
B = 10
Input 2:

A = [5, 17, 100, 11]
B = 130


Example Output
Output 1:

 2
Output 2:

 3


Example Explanation
Explanation 1:

Constraints are satisfied for maximal value of 2.
Explanation 2:

Constraints are satisfied for maximal value of 3.



Approach O(NlogN):
    here we try to find if all the subarrays of a chosen size satiesfies condition
    and to our surprise we can use binary search herebut how ?,

    lets say we have array of size 5 we can start with mid ie. 2 
    if 2 satiesfies our req. then we try to push by elements greater than 2 we eliminate the search space untill 2 since it will satisfy our req but will not give max K.

    in similar order if chosen K doesnt satisfy the consition e.i. sum of subarray should be less than given target sum then we can try to reduce the searchspace here searching the k in the range lesser than current one.
    
    logN to find the correct K and for each step we will find the sum of all subarrays which will cost us O(N)
    so TC is NlogN


lets code !!!
'''

def splInteger(A,B):
    if len(A) == 2:
        return 1
    
    prefix = []
    ans = 0
        
    summ = 0
    prefix.append(0)
    for i in A:
        summ += i
        prefix.append(summ)

    start  = 1
    end  = len(prefix) -1

    while start <= end :

        mid  = start + ((end -start)//2)
        sumofSubarray = 0
        count = 0
        for i in range(mid,len(prefix) ):
            sumofSubarray = 0
            sumofSubarray = prefix[i] - prefix[count]
            count += 1
            if sumofSubarray > B:
                break

        if sumofSubarray > B :
            end = mid -1
        elif sumofSubarray < B : 
            start  = mid + 1
            ans  = mid        

    return ans



A = [5, 17, 100, 11]
B = 130
print(splInteger(A, B))






