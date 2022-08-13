from collections import Counter
def solve():
    n=int(input())
    s=input()
    count=Counter(s)
    ln=len(count)
    sm=sum(count.values())
    print(sm+ln)




def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def getInt():
    return list(map(int,input().split()))

for _ in range(int(input())):
    solve()