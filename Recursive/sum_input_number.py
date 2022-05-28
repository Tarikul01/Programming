def sum_input(n):
    if n<=1:
        return n
    else:
        return n+sum_input(n-1)
print(sum_input(10))