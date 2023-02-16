def singleNumber(nums):
    for i in range(len(nums)):
        if nums.count(nums[i]) > 1:
            i+=1
        else:
            return nums[i]
            
def singleNumber2(nums):
    uniq = 0
    for idx in nums:
        uniq ^= idx
        print(uniq)
    return uniq


leest = [4,1,2,1,2]    
x = singleNumber2(leest)
print(x)


