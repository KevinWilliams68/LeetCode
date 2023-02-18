def removeDuplicates(nums):
    for num in nums:
        while nums.count(num) > 1:
            nums.remove(num)  
            
    return len(nums)
