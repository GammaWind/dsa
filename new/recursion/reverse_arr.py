#reverse the gievn array using recursion


from typing import List

def rev_arr(start: int, stop: int, arr: List) -> List:
    if start >= stop:
        return arr

    arr[start] , arr[stop] = arr[stop], arr[start]

    return rev_arr(start + 1, stop -1, arr)

ar = [1,2,3,4,5]
ans = rev_arr(0, len(ar) - 1, ar)
print(ar)

#rev using 1 variable only

def rev_arr_one(pos: int, arr: List) -> List:
    
    if pos >= len(arr)//2:
        return arr

    arr[pos] , arr[len(arr) - 1 - pos] = arr[len(arr) - 1 - pos] , arr[pos]

    return rev_arr_one(pos + 1, arr)

print('\n')
ar = [1,2,3,4,5]
ans1 = rev_arr_one(0, ar)
print(ans1)

