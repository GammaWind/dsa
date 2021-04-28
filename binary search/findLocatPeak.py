'''

given an unsorted array  find any loacl peak
local peak eg. 3,8,5
here 8 is a peak since 8 is greater than both 3 nd 5

O(logN):
    find mid 

    if mid is greater than or equal to both of its neighbour elemnts then mid is ans

    but if mid is not the largest the we reduce the searchspace to the the larger number

    A = [1,3,5,9,7,5,4,6]
    ans = 9|6





'''


def findLocalPeak(A,start,end):
    while start <= end:
        mid  = start + ((end - start)//2)

        if mid != len(A)-1 and mid != 0 and A[mid] >= A[mid-1] and A[mid] >= A[mid+ 1]:
            return A[mid]

        elif mid == len(A)-1 and A[mid] >= A[mid-1]:  #Corner case
            return A[mid]
        elif mid == 0 and A[mid] >=  A[0]: #corner Case
            return A[mid]

        elif A[mid] < A[mid+ 1]:
            start = mid + 1
        elif A[mid] < A[mid+-1]:
            end = mid  -1

    return -1

A = [11,5,2,15,5,1]
print(findLocalPeak(A, 0, len(A)-1))


