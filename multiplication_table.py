num_1 = int(input('Enter 1st number: '))
num_2 = int(input('Enter 2nd number: '))

def PrintMultiplicationTable(num_1, num_2):
    for i in range(1, num_1 + 1):
        for x in range(1, num_2 +1):
            product = i * x
            print(i, 'x', x, '=', product)

table = PrintMultiplicationTable(num_1, num_2)
