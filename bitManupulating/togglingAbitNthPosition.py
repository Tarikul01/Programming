def toggle(num, pos):
    # First Step: Shifts '1'
    # Second Step: XOR num
    num ^= (1 << pos)
    print(num)


num, pos = 4, 1

toggle(num, pos)