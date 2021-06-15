'''
MAX Area of rectangle between any two nodes

Approach : 2  pointer  approach , we will try to get maximum area so we will go with approach

start a pointer at start and from end and calculate between 2

now move the smaller pointer !! why ??? bcoz area is calculated using the minimum of both start end end. if you keep smaller then  there would be no difference between are so

what if both start and end are same,,,, then we can move either of them or both

moving both would be optimal

TC = O(N)
Auxilary Space = O(1)



'''

A = [2,5,9,7,2,5,10,5,7]



def maxAreaOf(A):
    start = 0
    end  = len(A) - 1
    maxArea = 0
    while start < end:
        area = min(A[start],A[end]) * (end - start)
        maxArea = max(area, maxArea)

        if A[start] < A[end]:
            start += 1
        elif A[start] > A[end]:
            end  -= 1

        else:
            start +=1 
            end -= 1

    return  maxArea              

print(maxAreaOf(A))





