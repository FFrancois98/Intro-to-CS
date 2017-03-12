nums = [2, 4, 6, 5, 3, 1, 5, 4]
n = 10
def GetNthLargestNumber(nums, n):
    distinct = []
    for num in nums:
        if num not in distinct:
            distinct.append(num)
    if len(nums)<= 1:
        return
    elif n > len(distinct):
        return
    elif n == 1:
        largest = max(distinct)
        return largest
    else:
        for i in range(n - 1):
            largest = max(distinct)
            distinct.remove(largest)
        if len(distinct) == 0:
            return
        largest_nth = max(distinct)
        return largest_nth

print(GetNthLargestNumber(nums, n))
