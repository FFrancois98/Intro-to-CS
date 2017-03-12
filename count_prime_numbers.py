def IsNumberPrime(num):       
    if num < 2:
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
    return prime

nums = [4, 7, 8, 11, 17]
def CountPrimeNumbers(nums):
    count = 0
    for i in nums:
        if IsNumberPrime(i)== True:
            count += 1
    print(count)

CountPrimeNumbers(nums)
        
