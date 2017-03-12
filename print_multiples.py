def PrintMultiples(start, end, multiple):
    if multiple <= 0:
        print('Input multiple must be greater than 0')
    if multiple > 0:
        multiple_count = 0
        for num in range(start, end + 1):
            if num % multiple == 0:
                print(num)
                multiple_count += 1
        if multiple_count == 0:
                print("There are no multiples of", multiple,
                      "in the range of", start, "to", end)


start = int(input('Enter start number: '))
end = int(input('Enter end number: '))
multiple =  int(input('Enter the multiple: '))


PrintMultiples(start, end, multiple)
