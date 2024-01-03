
def twoSum(nums, target):
    for i in range(0,len(nums)):
        for j in  range(i+1,len(nums)):
            if nums[i] + nums[j] ==target:
                return i,j
            

def two_sum(nums, target):
    hash = {}

    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in hash:
            return [hash[difference],i]
        else:
            hash[nums[i]] = i

