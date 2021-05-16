'''
Strange Equality
Problem Description

Given an integer A.
Two numbers X and Y are defined as follows:

X is the greatest number smaller than A such that XOR sum of X and A is the same as the sum of X and A.
Y is the smallest number greater than A such that XOR sum of Y and A is the same as the sum of Y and A.
Find and return the XOR of X and Y.

NOTE 1: XOR of X and Y is defined as X ^ Y where '^' is the BITWISE XOR operator.

NOTE 2: Your code will be run against a maximum of 100000 Test Cases.



Problem Constraints
1 <= A <= 109



Input Format
First and only argument is an integer A.



Output Format
Return an integer denoting the XOR of X and Y.



Example Input
A = 5


Example Output
10


Example Explanation
The value of X will be 2 and the value of Y will be 8. The XOR of 2 and 8 is 10.



×
You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified. Still have a doubt? Checkout Sample Codes for more details.

'''


'''
APPROACH : THE PROBLEM IS BASED IN A FORMULA WHICH IS STATED AS BELOW AS
 
A + B  = (A ^ B) + 2 * (A & B)

SO if we want to find the numbers where A + B == A ^ B then the part (A & B) should be zero
so simply if and of 2 numbers is zero the their sum will be equal to their XOR value.

BUT BUT BUT, we can simply start from given A to its left until we find A & i == 0 and to its right untill A & y == 0

this solution can take more time will give TLE hence we need to come up with constatant time.

to do so new problem is we want to find the closset number which gives 0 when performed AND
so how do we find the nearest smller than A ??
well find the unset bits and turn them into set also turn set bits into unset


how to we find greater nearest of A.
well count the number of contributing bits in A and take its next 2s power i.e. 1 << numberofcontributingbtsinA

to calculate number of bits contributing we used formula numOFbits = int(math.log(A,2) + 1)






'''
import math
def solve( A):
    numOFbits = int(math.log(A,2) + 1)  #formula to calculate the number of bits contributing in a given number
    x = 0
        
    for i in range(numOFbits):
        if not A & (1 << i):
            x += (1 << i)
                
    y = 1 << numOFbits # grater power of 2 than the number of bits in A
    return x ^ y


A = 5
print(solve(A))    