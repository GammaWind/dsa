# check if given string is palindrome

def check_palindrome(i:int, s:str) -> bool:

    if i >= len(s)//2:
        return True

    if s[i] != s[len(s) - 1 - i]:
        return False

    return check_palindrome(i+1, s)

ans = check_palindrome(0, 'MADAM')
print(ans)
ans2 = check_palindrome(0, 'MADIAM')
print(ans2)


