#Method 1
'''
This method is more efficent than the
second one.
'''

nums = []

def PrintHistogram(nums):
    num_asterisk = 0
    store_x = []
    store_ast = []
    for x in nums:
        num_asterisk = nums.count(x)
        if x not in store_x:
            store_x.append(x)
            store_ast.append(num_asterisk)

    for ran in range(len(store_ast)):
        print(store_x[ran], ':', '*' * store_ast[ran])

PrintHistogram(nums)

#Method 2

'''
This was my original code for
print_histogram before PA 3 was changed.
It works for both sort and unsorted lists
but it doesn't print the histogram in order.
'''

nums = []

def PrintHistogram(nums):
    while nums != []:
        for num in nums:
            num_asterisk = []
            while num in nums:
                num_asterisk.append(num)
                nums.remove(num)
            print(num, ':', '*' * len(num_asterisk))

PrintHistogram(nums)
