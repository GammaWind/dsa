'''

Ath Magical Number
Problem Description

Given three positive integers A, B and C.

Any positive integer is magical if it is divisible by either B or C.

Return the Ath magical number. Since the answer may be very large, return it modulo 109 + 7.



Problem Constraints
1 <= A <= 10^9

2 <= B, C <= 40000



Input Format
The first argument given is an integer A.

The second argument given is an integer B.

The third argument given is an integer C.



Output Format
Return the Ath magical number. Since the answer may be very large, return it modulo 109 + 7.



Example Input
Input 1:

 A = 1
 B = 2
 C = 3
Input 2:

 A = 4
 B = 2
 C = 3


Example Output
Output 1:

 2
Output 2:

 6


Example Explanation
Explanation 1:

 1st magical number is 2.
Explanation 2:

 First four magical numbers are 2, 3, 4, 6 so the 4th magical number is 6.



'''

'''
APPROACH:
here thing to notice is that the range for the number divisible by B or C can start from 1 to 10^9 * min(B,C)
so in this range we can try to find Ath /Nth number divisible by B OR C.

one thing to notice here we will dtermine a mid point and try to determine how many numbers divisible by B or C before our mid exists
and we will keep doing so untill we find the 




'''

from math import gcd

    
def nthMagicalNumber( N, A, B):
        
    MOD = 10**9 + 7
    L = A // gcd(A,B) * B

    def magic_below_x(x):
                    # How many magical numbers are <= x?
        print(x,x // A + x // B - x // L)
        return x // A + x // B - x // L

    lo = 0
    hi = N * min(A, B)
    while lo < hi:
        
        mi = (lo + hi) // 2
        
        if magic_below_x(mi) < N:
            lo = mi + 1
        

        else:
            hi = mi            

    return hi % MOD


N = 4
A = 2
B  = 3
print(nthMagicalNumber(N, A, B))

