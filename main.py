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
    # str=input()
    # arr=[]
    # tmp=0
    # for i in range(n):
    #     if len("".join(set(str[:i+1])))<i+1:
    #         tmp=i
    #         break
    # print(len("".join(set(str[:tmp])))+len("".join(set(str[tmp:]))))

    # if n==1:
    #     print(1)
    #     return
    # elif n==0:
    #     print(0)
    #     return
    #
    # l=0
    # r=len(str)-1
    # while (str[l]=='0' and str[r]=='1' and l<=r) or (str[l]=='1' and str[r]=='0' and l<=r):
    #     l=l+1
    #     r=r-1
    # print(len(str[l:r+1]))





    # u=0
    # r=0
    # for  i in range(n):
    #
    #     if str[i]=="U":
    #         u=u+1
    #     elif str[i]=="D":
    #         u=u-1
    #     elif str[i]=="R":
    #         r=r+1
    #     elif str[i]=="L":
    #         r=r-1
    #
    #     if u == 1 and r == 1:
    #         print("YES")
    #         return
    # print("NO")

    # str="codeforces"
    # ch=input()
    # if ch in str:
    #     print("YES")
    # else:
    #     print("NO")
    # sm=sum(arr)
    arr=li()
    check=0
    check1=0
    sm=sum(arr)
    for i in range(n-1):
        if arr[i]==-1 and arr[i]==arr[i+1]:
            check=1
        if arr[i]==-1:
            check1=1
    if arr[n-1]==-1:
        check1=1
    if check==1:
        print(sm+4)
    elif check1==1:
        print(sm)
    else:
        print(sm-4)







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









