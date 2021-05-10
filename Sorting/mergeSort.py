'''
Famous Merge Sort

'''


        
     

    


arr = [5,1,2,9,15,50,45,24,63]
def mSort(A):
    # global arr
    # print(arr)
    if len(A) > 1:
        mid = len(A)// 2
        A1 = A[:mid]
        B1 = A[mid:]
        # print(A1,B1)
        mSort(A1)
        mSort(B1)
        

        i,j = 0, 0
        k = 0
        while i < len(A1) and j < len(B1):
            if A1[i] <= B1[j]:
                A[k] = A1[i]
                
                i += 1
            else:
                A[k] = B1[j]
                j += 1
            k += 1

        
        while i < len(A1):
            A[k] = A1[i]
            i += 1
            k += 1    
       
        while j < len(B1):
            A[k] = B1[j]
            j += 1
            k += 1

        # print(A1,B1,A)    

    return



mSort(arr)
print(arr)



