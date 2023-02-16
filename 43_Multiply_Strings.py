num1 = "250"
num2 = "10"

def multiplyStrings(num1,num2):
    first,second = 0,0
    for n in num1:
        first = first * 10 + ord(n)-ord('0')
    for p in num2:
        second = second * 10 + ord(p) - ord('0')
        
        
    return str(first*second)
    
    

    
x = multiplyStrings(num1,num2)
print(x)



#works but not allowed! 
#return(str(int(num1)*int(num2)))

def multiply(num1, num2):
    first = converts(num1)
    second = converts(num2)

    return str(first*second)
    
def converts(num):
    p=0
    for n in num:
        p = p * 10 + ord(n) - ord('0')
    return(p)
        