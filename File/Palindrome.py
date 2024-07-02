def is_palindrome(s):
    if(s == s[::-1]):
        return "Palindrome"
    else:
        return "Not Palindrome"


print(is_palindrome("aba"))