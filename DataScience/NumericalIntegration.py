def func(x):
    # Declare the initial function part
    return (1 / (1 + x * x))


def trapezoidal(a, b, n):
    h = (b - a) / n
    s = (func(a) + func(b))
    i = 1
    while i < n:
        s += 2 * func(a + i * h)
        i += 1
    return ((h / 2) * s)
def simpsons_one_third(ll, ul, n):
    h = (ul - ll) / n
    x = list()
    fx = list()
    i = 0
    while i <= n:
        x.append(ll + i * h)
        fx.append(func(x[i]))
        i += 1
    res = 0
    i = 0
    while i <= n:
        if i == 0 or i == n:
            res += fx[i]
        elif i % 2 != 0:
            res += 4 * fx[i]
        else:
            res += 2 * fx[i]
        i += 1
    res = res * (h / 3)
    return res


def simpson_three_eight(a, b, n ):

    interval_size = (float(b - a) / n)
    sum = func(a) + func(b);

    # Calculates value till integral limit
    for i in range(1, n ):
        if (i % 3 == 0):
            sum = sum + 2 * func(a + i * interval_size)
        else:
            sum = sum + 3 * func(a + i * interval_size)

    return ((float( 3 * interval_size) / 8 ) * sum )


def WeedleRule(a, b,n):
    h = (b - a) / n
    sum = 0
    sum = sum + (((3 * h) / 10) * (func(a)
                                   + func(a + 2 * h)
                                   + 5 * func(a + h)
                                   + 6 * func(a + 3 * h)
                                   + func(a + 4 * h)
                                   + 5 * func(a + 5 * h)
                                   + func(a + 6 * h)))

    # Return the final sum
    return sum
x0 = 0
xn = 1
n = 6
print("Value of integral is ", "%.4f" % trapezoidal(x0, xn, n))
print("Value of integral is ", "%.4f" % simpsons_one_third(x0, xn, n))
print("Value of integral is ", "%.4f" % simpson_three_eight(x0, xn, n))
print("Value of integral is ", "%.4f" % WeedleRule(x0, xn, n))

