from collections import Counter
def solve():
    a,b,c=sorted(getInt())
    if a+b==c:
        print("YES")
    else:
        print("NO")










def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def getInt():
    return list(map(int,input().split()))

for _ in range(int(input())):
    solve()