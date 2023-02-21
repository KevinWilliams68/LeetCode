from functools import reduce
def addDigits(self, num):
    if len(str(num)) > 1:
        res = [int(x) for x in str(num)]
        sum = reduce((lambda x, y: x + y), res)
        return self.addDigits(sum)
    else:
        return num