t_b = 99

for i in range(99, -1, -1):
    if i == 1:
        print(i, 'bottle of beer on the wall,', i,'bottle of beer.',
        'Take one down, pass it around, no more bottles of beer on the wall...')
    elif i == 0:
        print('No more bottles of beer on the wall, no more bottles of beer.',
        'Go to the store and buy some more,', t_b,
         'bottles of beer on the wall...')
    else:
        print(i, 'bottles of beer on the wall,', i, 'bottles of beer.',
        'Take one down, pass it around,', i - 1,
        'bottles of beer on the wall...')
