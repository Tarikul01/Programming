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
    n=int(input())
    arr=getInput()
    sum=0
    for i in range(len(arr)-1):
        arr[i+1]=arr[i]*arr[i+1]
        arr[i]=1
    print((arr[len(arr)-1]+len(arr)-1)*2022)
    # sum=0
    #
    # for i in range(1,n+1):
    #     if i==n:
    #         sum+=i*i
    #     else:
    #         sum+=i*i
    #         sum+=i*(i+1)
    # print((sum*2022)%1000000007)






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









