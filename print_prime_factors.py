num = int(input('Enter a number: '))

def PrintPrimeFactors(num):
    print_statement = ''
    factors = []
    i = 2
    if num < 2:
        print('There are no prime factors for', num)
    else:
        while i * i < num:
            while num % i == 0:
                num = num / i
                factors.append(i)
            i = i + 1
            
        num = int(num)
        factors.append(num)
    for x in factors:
        print_statement += str(x)
        if x < len(factors):
            print_statement += '*'
    print(print_statement)
PrintPrimeFactors(num)
