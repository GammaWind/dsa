'''
Aggressive cows
Problem Description

Farmer John has built a new long barn, with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall, and an integer B which represent the number of cows.

His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?



Problem Constraints
2 <= N <= 100000
0 <= A[i] <= 109
2 <= B <= N



Input Format
The first argument given is the integer array A.
The second argument given is the integer B.



Output Format
Return the largest minimum distance possible among the cows.



Example Input
Input 1:

A = [1, 2, 3, 4, 5]
B = 3
Input 2:

A = [1, 2]
B = 2


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 
John can assign the stalls at location 1,3 and 5 to the 3 cows respectively.
So the minimum distance will be 2.
Explanation 2:

 
The minimum distance will be 1.


APPROACH: notice here we need to apply binary search over the answer space,
so we try to calculate the atlest distance using binary search and see if we can fit all the cows given to us

if we are able to fit then we can increase the distance or else if we are not able to fit all given cows then we reduce the atleast distance between 2 cows


instead of trying the burte force way all the possible distances we are calculating using binary search






'''
def canFitAll(A,B,mid):

    i = 0
    point  = 0
    B -=1
    while i < len(A):
        print(mid,A[i],A[point] + mid,B)
        if A[i] >= A[point] + mid:
            point = i
            B -= 1
        i += 1
    if A[i-1] >= A[point] + mid:
        B -= 1  
    print(B)      
    if B <= 0:
        return True
    return False        


    






def canAccomodateCows(A,B):
    start  = A[0]
    end  = A[-1]
    ans  = 0
    while start <= end: 
        mid = start + ((end-start)//2)
        

        if canFitAll(A,B,mid):
            
            ans  = max(ans,mid)
            start = mid + 1
        else:
            end = mid - 1
    return ans 


A = [1, 2, 3, 4, 5]
B = 3
print(canAccomodateCows(A, B))        
        





