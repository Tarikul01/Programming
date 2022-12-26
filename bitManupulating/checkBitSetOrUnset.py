def at_position(num, pos):
    bit = num & (1 << pos)
    return bit


num = 5
pos = 0
bit = at_position(num, pos)
print(bit)