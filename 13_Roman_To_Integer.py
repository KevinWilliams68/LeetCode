s = "MCMXCIV"

roman = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1 }
#roman = {"I":1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M":1000}
def romanToInt(s):
    add = 0
    x=0
    while(x < len(s)): #cannot increment x in forloop
        #error checking for length and checking adjacent elements
        if(x+1 < len(s) and roman[s[x]] < roman[s[x+1]]): 
            #subtracting next element to previous
            add += (roman[s[x+1]] - roman[s[x]])
            #incrementing x by 2
            x+=2
        else:
            #adding current element in string to variable
            add += roman[s[x]]
            #single step increment
            x+=1    

    print(add)
    
romanToInt(s)


    
