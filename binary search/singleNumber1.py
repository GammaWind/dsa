'''
given a sorted list of numbers all the numbers has 2 instances except one number has only one occurance, find the number.

A = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,10]
ans = 10

Approach O(logN):
here the thing to observe is that ideally if there are 2 occurances of all the numbers in the list then the 1st occurance would start at 0th index and 2nd occur. lies at 1st index.
that means 1st occurance at odd pos and 2nd occur at even pos.

so if we try to to a binary search and determine a search space and neglect the non essesntial serch space we can norrow down the number
i.e. whereever there is one occurance of the number starting from there the 1st coccur of the number would be odd and second occur would be at even 








'''

# A Binary search based function to find
# the element that appears only once


def search(arr, low, high):

	# Base cases
	if low > high:
		return None

	if low == high:
		return arr[low]

	# Find the middle point
	mid = low + (high - low)/2

	# If mid is even and element next to mid is
	# same as mid, then output element lies on
	# right side, else on left side
	if mid % 2 == 0:

		if arr[mid] == arr[mid+1]:
			return search(arr, mid+2, high)
		else:
			return search(arr, low, mid)

	else:
		# if mid is odd
		if arr[mid] == arr[mid-1]:
			return search(arr, mid+1, high)
		else:
			return search(arr, low, mid-1)

# Driver Code
# Test Array
arr = [1, 1, 2, 4, 4, 5, 5, 6, 6]

# Function call
result = search(arr, 0, len(arr)-1)

if result is not None:
	print ("The required element is %d") % result
else:
	print ("Invalid Array")
