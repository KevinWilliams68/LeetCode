def addBinary2(a, b):
    return bin(int(a,2) + int(b,2))
    
    
def addBinary(a,b):
    c = d = e = 0
    ans = ""
    for i in range(len(a)):
        c +=  int(a[i]) * 2**(len(a) - 1 - i)
    for i in range(len(b)):
        d +=  int(b[i]) * 2**(len(b) - 1 - i)
    e = c + d 
    if e == 0:
        return "0"
    else:
        while e != 0:
            ans += str(e%2)
            e = e //2
        return ans[::-1]
            
        
a = "1"
b = "0"
x = addBinary(a,b)
print(x)

