# Palindrome Integer
# Determine whether an integer is a palindrome. Do this without extra space.

# A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed. Negative numbers are not palindromic.

# Example :

# Input : 12121
# Output : True

# Input : 123
# Output : False

def isPalindrome(self, A):
	res = 0
	temp  = A
	while A > 0:
	    res = (res * 10) + (A%10)
        A = A // 10
    if res == temp :
        return 1
    
    return 0    


print(isPalindrome(12121))   