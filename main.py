import os
import re
# from turtle import  *
from collections import defaultdict, namedtuple, OrderedDict, Counter,deque
from datetime import datetime
from enum import unique
from itertools import combinations, combinations_with_replacement, groupby, permutations, starmap, product
from time import ctime, time, gmtime, localtime, mktime, strptime, strftime
from pip._vendor.distlib.compat import raw_input

import cmath
import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

def solution():
    n = int(input())
    s = input()
    cnt = [0] * len(s)
    curr = set()
    for i in range(len(s)):
        curr.add(s[i])
        cnt[i] = len(curr)
    curr2 = set()
    ans = 0
    for i in reversed(range(1, len(s))):
        curr2.add(s[i])
        ans = max(ans, len(curr2) + cnt[i - 1])
    print(ans)








for i in range(int(input())):
    solution()




# End  library and  litteral
# def sortcheck(ar):
#     flag=0
#     ar1=ar[:]
#     ar.sort()
#     if arr==ar1:
#         return True
#     else:
#         return False
# def reversecheck(ar):
#     ar1=ar[:]
#     ar.sort(reverse=True)
#     if ar==ar1:
#         return True
#     else:
#         return False









