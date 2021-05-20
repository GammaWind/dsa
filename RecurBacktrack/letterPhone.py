'''
Letter Phone
Problem Description

Given a digit string A, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



The digit 0 maps to 0 itself. The digit 1 maps to 1 itself.

NOTE: Make sure the returned strings are lexicographically sorted.



Problem Constraints
1 <= |A| <= 10



Input Format
The only argument is a digit string A.



Output Format
Return a string array denoting the possible letter combinations.



Example Input
Input 1:

 A = "23"
Input 2:

 A = "012"


Example Output
Output 1:

 ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
Output 2:

 ["01a", "01b", "01c"]


Example Explanation
Explanation 1:

 There are 9 possible letter combinations.
Explanation 2:

 Only 3 possible letter combinations.

 APPROACH/INTUTION:
 TRY TO THINK IT IN BRUTEFORCE/ ITERATIVE WAY FIRST

 THEN  you can esily think that this can be solved using backtracking
 as for each number provided to you you need to put/try all the corresponding letters for that number eg. for 2 you need to put a,b,c

 but once you put "a" and filled your current array you need to replace that a with b and c later so how do you do that

 you simply backtrack!!!
 first you put a then backtack then you put b then backtrack then c
 simply iterate over the given letters for the number and put them call recursion and then backtrack 

 here the parameters we re passing to aur recursion function are : A , index of A, current array, answer final array

 so what do we do for base case
 if the lenth of currarray is len(A) or our idx == len(A)
 then we add our current ans to array and return

 else for index idx we catch the letters form lookup array and for the catched string we run a loop adding each char to current string and then call recursively our function with in dex + 1
 and then remove that added char 
 again add next char , call recur , backtack

 '''


def letterCombinations( A):
	    
	lookup = ['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
	ans = []
	def genText(A, idx, lookup, curr, ans):
	    if idx == len(A):
	        ans.append(curr)
	        return
	    getLettersAtNum = lookup[int(A[idx])]
	        
	        
	        
	    for i in range(len(getLettersAtNum)):
	            
	        curr += getLettersAtNum[i]
	            
	        genText(A , idx +1, lookup, curr, ans)
	            
	        curr = curr[:-1]
	        
	genText(A, 0, lookup, '', ans)
	
	    
	return ans
	    

A = "23"
print(letterCombinations(A))

