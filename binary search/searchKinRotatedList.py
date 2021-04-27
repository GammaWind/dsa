'''
given a list containing non duplicate and the list is clockwise rotated. find element index

A = [40,45,48,2,4,9,13]
 K = 4

ans=> 4

approach :

if we are able to find the pivot here we can run binary search on both parts of the list on O(logN)
but how do we find the pivot ????
here the pivot is index 3 i.e. element 2

idea is to determine the pivot point of the list comparing the mid with first and last element so that we can guess if we are in first part or second part of the list 

so there are 3 cases

if A[mid] > A[end] this means we are in the first part of the list
so here we can skip the left search space by setting start = mid + 1

another condition 
A[mid] <= A[end]
this means we are in the second part of the list 

if we find the pivot in O(logN) the we can run binary search again on both parts of the list seperately






'''


def bSearch(A,K,start,end):
    #run loop untill
    while start <= end:

        #can use mid if we have overflow issues
        mid = (start + end)//2

        if A[mid] == K:
            return mid
        elif A[mid] < K:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def searchInRotatedList(A,K):
    start = 0
    end = len(A)-1
    getmid = -1

    while start <= end:
        mid  = (start + end)//2

        if A[mid] > A[len(A)-1]:
            start = mid  +1
        elif A[mid] <= A[len(A)-1]:
            end = mid - 1
            getmid = mid
    ans = 0
    if K > A[len(A)-1]:
        ans = bSearch(A, K, 0, getmid-1)     
    else:
        ans  = bSearch(A, K, getmid, len(A)-1)

    return ans     

    
A = [40,45,48,2,4,9,13]
K = 13

print(searchInRotatedList(A, K))