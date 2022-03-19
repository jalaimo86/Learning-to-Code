def hex_output(hexnum):
    total = 0
    for index, one_digit in enumerate(reversed(hexnum)):
#        print(f'{one_digit} * 16 ** {index}')             #debugging line
        total += int(one_digit, 16) * 16 ** index
        print(total)
hex_output('ff')
