def climbStairs(self,n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return (self.climbStairs(n-2) + self.climbStairs(n-1))
#takes a very long time
