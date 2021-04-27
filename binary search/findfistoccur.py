'''
finf the fist occurance of the given number else return -1 if not present. 
TIP: Array is already sorted


A = [1,2,2,2,5,6,9,10]
K = 2
ans  = 1

here the first instance of 2 (K) is at index 1 thats why 1 is ans

Approaches : 
O(N) - search linearly untill u find element then retrn

O(N) - binary search an element untill u find it if you find K then linearly search to its left unill its K.


O(log N):
    in ordrt to find first coour in log N cost we need to continue the search even if we fidn element.
    lets say we found K at some index then we would reduce the search space to its left side untill base condition is hit

    





'''


ans  = -1

def fistOccur( A, K, start, end): 
    global ans 
    if start > end :
        return
    mid = start + ((end - start)//2)

    if A[mid] == K:
          ans  = mid
          return fistOccur(A, K, start, mid - 1)

    elif A[mid] < K:
        return fistOccur(A, K, mid + 1, end)        
    else:
        return fistOccur(A, K, start, mid- 1)



A = [1,5,6,9,10]
fistOccur(A, 2, 0, len(A)-1)
print(ans)
