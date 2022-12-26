def set(num, pos):
    # First step = Shift '1'
    # Second step = Bitwise OR
    num |= (1 << pos)
    print(num)


num, pos = 4, 1

set(num, pos)
print(1<<4)
print(4<<1)