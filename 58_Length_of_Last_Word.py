def lengthOfLastWord(s):
    s = list(s.split())
    return len(s[len(s) - 1])
