'''
Anagrams
Problem Description

Given an array A of N strings, return all groups of strings that are anagrams.

Represent a group by a list of integers representing the index(1-based) in the original list. Look at the sample case for clarification.

NOTE: Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp'.



Problem Constraints
1 <= N <= 104

1 <= |A[i]| <= 104

Each string consists only of lowercase characters.

Sum of length of all the strings doesn't exceed 107



Input Format
Single Argument A which is an array of strings.



Output Format
Return a two-dimensional array where each row describes a group.

Note:

Ordering of the result :
You should not change the relative ordering of the strings within the group suppose within a group containing A[i] and A[j], A[i] comes before A[j] if i < j.



Example Input
Input 1:

 A = [cat, dog, god, tca]
Input 2:

 A = [rat, tar, art]


Example Output
Output 1:

 [ [1, 4],
   [2, 3] ]
Output 2:

 [ [1, 2, 3] ]


Example Explanation
Explanation 1:

 "cat" and "tca" are anagrams which correspond to index 1 and 4 and "dog" and "god" are another set of anagrams which correspond to index 2 and 3.
 The indices are 1 based ( the first element has index 1 instead of index 0).
Explanation 2:

 All three strings are anagrams.
'''

'''
Approach : here we can simply hash the given words after sorting each of them. so hashing and increasing count would give us the number of indexes

map would be  hmap[word] = [indexes]

but here we are sorting the word so it would add extra TC of O(Klog(K)) where k is longest word in the list provided

Approach 2 :
        here we can thing of something, we can convert words in array/list/tuple.

        so for each word we will create a count array of size 26, initalize with 0.
        and add mappaing with its askii value so that 0 maps to a, 1 maps to b, 2 maps to 3......


        and then we can hash this count arrray as key , but hold on we cannot hash a list in python, so we will convert list to touple and the hash
        its say if we found that same count array exits in key we will add the index of cuureent to value of the key

        at the end we can return all the values in hashmpas which would have pairs so anagrams in each value

'''

import collections

def anagrams( A):
	hmap = collections.defaultdict(list)
	    
	for i in range(len(A)):
	    count = [0] * 26
	        
	    for j in A[i]:
	            
	        count[ord(j) - ord('a')] += 1
	        
	    hmap[tuple(count)].append(i + 1)
	        
	ans = []
	for k in hmap.keys():
	    ans.append(hmap[k])
	return ans     
	            
A = ['cat', 'dog', 'god', 'tca']
print(anagrams(A))


