from collections import Counter
def solve():
    n=int(input())
    arr=getInt()
    if(len(arr)==1):
        print("YES")
    else:
       sarr=sorted(arr)
       tmp="YES"
       for i in range(1,n):
           if (sarr[i]<sarr[i-1]) or (sarr[i]==sarr[i-1]):
               tmp="NO"
       print(tmp)










def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def getInt():
    return list(map(int,input().split()))

for _ in range(int(input())):
    solve()