s = 120

def reverse(x):
    s = str(x)
    new_string = ""
    length = len(s)
    if s[0] == '-':
        s = s.replace('-', '')
        reverse=s[length::-1]
        integ = int(reverse)
        if integ > (2**31 - 1):
            return 0
        else:
            print(integ*-1)
    else:
        reverse=s[length::-1]
        integ = int(reverse)
        if integ > (2**31 - 1):
            return 0
        else:
            print(integ)

                
reverse(s)

#if it goes outside 32 bit integer range, return 0
#huh?????
#1534236469 should return 0
#was accepted on leetcode