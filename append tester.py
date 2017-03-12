def IsNumberPrime(num):       
    if num > 1:
        prime = False
        if num == 2:
            prime = True
        p_c = 0            # p_c is the 'not a prime number' count
        for i in range(2, num):
            if num % i == 0:
                p_c += 1
        if p_c > 0:
            prime = False
        else:
            prime = True
    else:
        prime = False
    return prime

nums = []
max_nums_list = 5
while len(nums) < max_nums_list:
    digits = int(input('Enter a number into the list: '))
    nums.append(digits)
def CountPrimeNumbers(nums):
    count = []
    for i in nums:
        if IsNumberPrime(i)== True:
            count.append(i)
    print(count)

CountPrimeNumbers(nums)
        
