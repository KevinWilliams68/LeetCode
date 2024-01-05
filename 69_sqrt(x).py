x = 16

def mySqrt(x):
    counter = 0
    i=1
    while i <= x:
        x = x-i
        counter += 1
        i+=2
    print(counter)      
    
mySqrt(x)    

