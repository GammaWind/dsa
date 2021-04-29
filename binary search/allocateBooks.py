'''
Allocate Books
Problem Description

Given an array of integers A of size N and an integer B.

College library has N books,the ith book has A[i] number of pages.

You have to allocate books to B number of students so that maximum number of pages alloted to a student is minimum.

A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.



NOTE: Return -1 if a valid assignment is not possible.



Problem Constraints
1 <= N <= 105
1 <= A[i], B <= 105



Input Format
The first argument given is the integer array A.
The second argument given is the integer B.



Output Format
Return that minimum possible number



Example Input
A = [12, 34, 67, 90]
B = 2


Example Output
113


Example Explanation
There are 2 number of students. Books can be distributed in following fashion : 
        1) [12] and [34, 67, 90]
        Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
        2) [12, 34] and [67, 90]
        Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
        3) [12, 34, 67] and [90]
        Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages
        Of the 3 cases, Option 3 has the minimum pages = 113.
'''
'''

APPROACH:
notice here that we have to allocate contigious pages to the students
so we can derive a middle point which will be the at max number of pages a student can read or study.

so we derive the mid point from the start = 0 to end = sum of elemnts in array
and we verifed if the mid can accomodte the students .
if not them we increased the start to mid + 1 
and if yes then we decreased the end to mid-1 since we are looking for minimum ans here


'''

import sys
#CODE
def canRead(A,B,mid):
    students_required = 1
    curr_sum = 0
    for i in range(len(A)):
        if A[i] > mid:
            return False
        if curr_sum + A[i] <= mid:
            curr_sum += A[i]
        elif curr_sum + A[i] > mid:
            students_required += 1
            curr_sum = A[i]
            if students_required > B:
                return False

    return True
            

        



def allocateBooks(A,B):
    start = 0
    end = sum(A)
    ans = sys.maxsize
    # ATEENTION CORNER CASE if number of students are greater than books
    if len(A) < B:
        return -1

    while start <= end  :
        mid = start + ((end - start)//2)

        if canRead(A,B,mid):
            ans  = min(mid,ans)
            end = mid - 1
        else:
            
            start = mid + 1
    return ans             

        
A = [12, 34, 67, 90]
B = 2

print(allocateBooks(A, B))