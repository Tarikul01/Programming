from collections import Counter
from itertools import combinations, permutations


def solve():
   # n,m=getInt()
   # for i in range(m):
   #     x,y=getInt()
   # if n>m:
   #     print("YES")
   # else:
   #     print("NO")

   # n=int(input())
   # monster=getInt()
   # spell=getInt()
   # spell.sort()
   # print(sum(monster)+sum(spell[0:len(spell)-1]))

   n=int(input())
   arr=getInt()
   arr1=sorted(arr)
   val=arr1[len(arr)-1]
   ind=arr.index(val)
   if len(arr)==1:
       print(arr[0])
       return
   if(val>=val-ind+1):
       print(val)
   else:
       print(0)





def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def getInt():
    return list(map(int,input().split()))

for _ in range(int(input())):
    solve()