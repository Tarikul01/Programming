from collections import Counter, defaultdict
from math import gcd


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    s = set()
    for i, v in enumerate(a):
        d[v] = i
        s.add(v)
    ans = -1
    for i in s:
        for j in s:
            if gcd(i, j) == 1:
                ans = max(ans, d[i] + d[j] + 2)
    print(ans)

# def coprime(a, b) :
#     return (gcd(a, b) == 1)
# def gcd(a, b):
#     # Everything divides 0
#     if (a == 0 or b == 0):
#         return False
#
#     # base case
#     if (a == b):
#         return a
#
#     # a is greater
#     if (a > b):
#         return gcd(a - b, b)
#
#     return gcd(a, b - a)
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def getInt():
    return list(map(int,input().split()))

for _ in range(int(input())):
    solve()