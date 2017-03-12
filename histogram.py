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
