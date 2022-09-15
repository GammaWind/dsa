#return factorial of a number

def get_factorial(i: int) -> int:
    
    if i == 1:
        return 1

    return i * get_factorial(i -1)

ans = get_factorial(4)
print(ans)