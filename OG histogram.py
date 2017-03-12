nums = [-2, -2, -2, -3]

def PrintHistogram(nums):
    while nums != []:
        for num in nums:
            num_asterisk = []
            while num in nums:
                num_asterisk.append(num)
                nums.remove(num)
            print(num, ':', '*' * len(num_asterisk))

PrintHistogram(nums)
