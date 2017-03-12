nums = []

def GetSecondLargestNumber(nums):
    if len(nums)<= 1:
        return
    else:
        largest = max(nums)
        while largest in nums:
            nums.remove(largest)
        if len(nums) == 0:
            return
        largest_2nd = max(nums)
        return largest_2nd

print(GetSecondLargestNumber(nums))
