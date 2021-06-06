'''
Maximum Frequency stack
Problem Description

You are given a matrix A which represent operations of size N x 2. Assume initially you have a stack-like data structure you have to perform operations on it.

Operations are of two types:

1 x: push an integer x onto the stack and return -1

2 0: remove and return the most frequent element in the stack.

If there is a tie for the most frequent element, the element closest to the top of the stack is removed and returned.

A[i][0] describes the type of operation to be performed. A[i][1] describe the element x or 0 corresponding to the operation performed.



Problem Constraints
1 <= N <= 100000

1 <= A[i][0] <= 2

0 <= A[i][1] <= 109



Input Format
The only argument given is the integer array A.



Output Format
Return the array of integers denoting answer to each operation.



Example Input
Input 1:

A = [
            [1, 5]
            [1, 7]
            [1, 5]
            [1, 7]
            [1, 4]
            [1, 5]
            [2, 0]
            [2, 0]
            [2, 0]
            [2, 0]  ]
Input 2:

 A =  [   
        [1, 5]
        [2 0]
        [1 4]   ]


Example Output
Output 1:

 [-1, -1, -1, -1, -1, -1, 5, 7, 5, 4]
Output 2:

 [-1, 5, -1]


Example Explanation
Explanation 1:

 Just simulate given operations
Explanation 2:

 Just simulate given operations



Approach : here we are tracking the frequency of each elemt simultaniously we are tracking a Maxfreq variable on each step depending on the frequency of the elements in the elements
also we will have a hashmap to store the key as frequency and value as actual stacks generated for that frequency by pushing the elements

so when we push an element we increase its frequency if frequency is the new Maxfreq then we create a new stack append the element in to it and store in hashmap with key as freq and value as stacks generated

while popping we will start with maxfreq element we will find the  value of maxfreq elemet from the hashmap and pop the elements from the stacks
if stack is empty we will reduce the value of maxfreq
'''


import collections
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    
    
    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0
    
    
    
    def push(self, x):
        
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x) 
        return -1
        
    
    def pop(self):
        
        getmaxval = self.group[self.maxfreq].pop()
        self.freq[getmaxval] -= 1
        
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return getmaxval    
        
        
        
    def solve(self, A):
        ans = []
        for i in A:
            
            if i[0] == 1:
                
                tmp  = self.push(i[1])
                ans.append(tmp)
                
            
            elif i[0] == 2:
                
                tmp2 = self.pop()
                ans.append(tmp2)
                
        return ans
        

A = [
            [1, 5],
            [1, 7],
            [1, 5],
            [1, 7],
            [1, 4],
            [1, 5],
            [2, 0],
            [2, 0],
            [2, 0],
            [2, 0]  ]
sol = Solution()
print(sol.solve(A))
