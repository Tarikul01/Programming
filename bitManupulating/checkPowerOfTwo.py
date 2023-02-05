def isPowerOfTwo(x):
    # First x in the below expression
    # is for the case when x is 0
    return (x and (not (x & (x - 1))))