# retur the fibonacci number at given pos n



def fib_n(i:int) -> int:

    if i <=1:
        return i

    return fib_n(i-1) + fib_n(i-2)


ans  = fib_n(5)
print(ans)

#TIME complexity
'''
Every function calls the recusrion twice and there could be n functions so
complexity would be near 2^n.
This is an exponential time complexity where we are repeatedly calling each function twice again and again'

if there are 3 cakks from n functions every time, the complexity would be 3^n 
need to draw the recursion tree

'''


