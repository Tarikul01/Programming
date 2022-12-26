def unset(num, pos):
    # Second Step: Bitwise AND this number with the given number
    num &= (~(1 << pos))
    print(num)


num, pos = 7, 1

unset(num, pos)