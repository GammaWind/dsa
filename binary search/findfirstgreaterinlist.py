'''
finf the fist greater element  of the given number if not present else return K index if present
TIP: Array is already sorted


A = [1,2,2,2,5,6,9,10]
K = 3
ans  = 4

here given k is 3, 3 is not in list hence first greater element is 5 so index of 5 is 4 hence and is 4.

Approaches : 



O(log N):
    in ordrt to find first coour in log N cost we need to continue the search even if we fidn element.
    lets say we found K at some index then we would reduce the search space to its left side untill base condition is hit

    if we dont find element then we need to consier the last mid our search function formed and compare its left and right.







'''




def fistOccur( A, K, start, end): 
    mid = 0
    ans  = -1
    while start <= end : 
        mid = start + ((end -  start) // 2)

        if A[mid] == K:
            ans  = mid 
            end  = mid - 1
        elif A[mid] < K :
            start = mid + 1
        else:
            end  = mid - 1
    
    
    if ans == -1:
       
        if A[mid] < K:
            ans  = mid + 1
        elif A[mid] > K:
            return mid    
        else:
            ans = mid - 1
    return ans
    

A = [1,1,1,1,1,5,5,5,5,5,6,9,10]
print(fistOccur(A, 10, 0, len(A)-1))

