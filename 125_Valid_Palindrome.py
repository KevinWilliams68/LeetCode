s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    s = ''.join(ch for ch in s if ch.isalnum()).lower()
    a = s[::-1]
    if a == s:
        print(True)
    else:
        print(False)
    
isPalindrome(s)