s = 1994

#roman = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1 }
number = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C",
          90:"XC" , 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
def intToRoman(s):
    strings = ""
    for val in number:
        div = s // val
        if div == 0:
            val+=1
        else:
            num = div*val
            strings += number[num]
            s -= num
    print(strings)
        
    
intToRoman(s)

#in this program, i forgot the idea of floor division and stood with modulus for a while


#helped a lot
#https://leetcode.com/problems/integer-to-roman/discuss/1642886/Python-Quick-and-Readable-Solution-w-Dictionary