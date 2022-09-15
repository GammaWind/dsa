# Print numbers from 1 to n

#normal approach
def print_n(i: int,n: int) -> None:
    
    if i > n:
        return
    print(i)

    print_n(i + 1, n)

print_n(1, 4)


#backtracking
def print_n_bt(i: int, n: int) -> None:
    
    if i < 1:
        return

    print_n_bt(i - 1, n)

    print(i)    

    
print_n_bt(4,4)