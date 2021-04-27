def bsearch(A,K,start, end):
    if start > end:
        return -1
    mid = start + ((end - start) // 2  )

    if A[mid] == K:
        return mid
    elif A[mid] < K:
        return bsearch(A, K, mid + 1, end)
    else:
        return bsearch(A, K, start, mid - 1)

A = [5,7,9,10,22,55,66]

print(bsearch(A, 8, 0, len(A)-1))
    