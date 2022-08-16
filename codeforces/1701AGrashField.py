from collections import Counter
def solve():
    a1=getInt()
    a2=getInt()
    c1=a1.count(1)
    c2=a2.count(1)
    if((c1+c2)==0):
        print(0)
    elif((c1+c2)==4):
        print(2)
    else:
        print(1)








def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def getInt():
    return list(map(int,input().split()))

for _ in range(int(input())):
    solve()