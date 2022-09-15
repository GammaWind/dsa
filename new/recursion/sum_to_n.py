#sum from 1 to n

#Parameterized way
def print_sum(i: int ,sum: int) -> None:

    if i < 0:
        print(sum)
        return

    print_sum(i -1, sum + i)

print_sum(3,0) 
print('\n')

#functional Way

def return_sum(i: int) -> int:
    
    if i == 0:
        return 0

    return i + return_sum(i-1)    

ans = return_sum(3)
print(ans)
     
