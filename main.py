import os
import re
# from turtle import  *
from collections import defaultdict, namedtuple, OrderedDict, Counter,deque
from datetime import datetime
from enum import unique
from itertools import combinations, combinations_with_replacement, groupby, permutations, starmap, product
from time import ctime, time, gmtime, localtime, mktime, strptime, strftime
from pip._vendor.distlib.compat import raw_input

# Assainament
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
#Read Student Grades .csv file and divide the data into dependent and independent variables.
# data = pd.read_csv('Student_Grades_Data.csv')
# data.head()

import cmath
# ath,calendar
# import sys
# sys.setrecursionlimit(10**20)


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

# t0=time()
# t0=time()
# for _ in range(int(input())):
#     a = int(input()) + 0.99
#     print(a)
#     print(a**.5)
#     print(a**(1/3))
#     print(a**(1/6))
#     print(int(a ** 0.5) + int(a ** (1 / 3)) - int(a ** (1 / 6)))
# s="abcabcbb"
# charset=set()
# l=0;
# res=0
# for i in range(len(s)):
#     while(s[i] in charset):
#         print(l)
#         charset.remove(s[l])
#         print(charset)
#         l+=1
#
#     charset.add(s[i])
#     print(charset)
#     res=max(res,i-l+1)
# print(res)
# n=3;
# m=3;
# need=[];
# for i in range(n):
#     need.append(list(map(int,input().split(' '))))
# print(need);
# lst=list(map(int,input().split(' ')));
# print(lst);
# n=int(input("Number of process:"))
# m=int(input("Number of Resources:"))
# alloc=[[int(input()) for i in range(n)] for i in range(m)];
# print(alloc)




def numberOfPaths(m, n):
    # If either given row number is first
    # or given column number is first
    if (m == 1 or n == 1):
        return 1

    # If diagonal movements are allowed
    # then the last addition
    # is required.
    print(n,m)
    return numberOfPaths(m - 1, n) + numberOfPaths(m, n - 1)
x=int(input())
y=int(input())
print(numberOfPaths(x,y))


