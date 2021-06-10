'''
Find the first repeating element in an array of integers
Difficulty Level : Easy
Last Updated : 10 May, 2021
Given an array of integers, find the first repeating element in it. We need to find the element that occurs more than once and whose index of first occurrence is smallest. 

Examples: 

Input:  arr[] = {10, 5, 3, 4, 3, 5, 6}
Output: 5 [5 is the first element that repeats]

Input:  arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
Output: 6 [6 is the first element that repeats]

Approach 1 : two pointer compare start and end , start + 1 and end also start and end + 1 keep loop untill start < end
TC O(N)
SC = O(1)

Approach 2:  use hash map put all elements in map with freq and then trverse all array and find if element has 2 nstances then return true
TC O(N)
SC O(N)

'''


A = [10, 5, 3, 4, 3, 6]
def solve(A):
    start  = 0 # star
    end  = len(A) - 1

    while start < end:
        if A[start] == A[end]:
            return A[start]
        start += 1
        if A[start] == A[end]:
            return A[start]
        end -=1
        if A[end] == A[start]:
            return A[end]
    return None            
                
print(solve(A))                


