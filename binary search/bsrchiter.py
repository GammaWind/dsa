
def bsearh(A,K,start,end):

    while start <= end:
        mid = start + ((end - start) // 2)

        if A[mid] == K:
            return mid
        elif A[mid] < K:
            start = mid + 1
        else:
            end = mid - 1
    return -1


A = [2,5,6,9,10,15,17]
print(bsearh(A,25,0,len(A)-1))
