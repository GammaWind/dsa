# Spiral Order Matrix II
# Problem Description

# Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.

def spiral(A):
    
    L = 0
    T = 0
    R = A
    B = A
    res = [[0] * A for i in range(A)]
            
    val = 1
            
    while(L<R and T<B):
        for i in range(L,R):
            res[T][i] = val
            val += 1
                    
        T += 1
        for j in range(T,B):
            res[j][R-1]= val
            val += 1
                    
        R -= 1
        for k in range(R-1,L-1,-1):
            res[B-1][k] = val
            val += 1
                    
        B -= 1
        for l in range(B-1,T-1,-1):
            res[l][L] = val
            val += 1
                    
        L += 1
                
    return res    
                           



print(spiral(4))    