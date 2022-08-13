def solve():
    n=int(input())
    showKey=getInt()
    for i in range(n):
        keyPress=input()
        x,y=keyPress.split()
        U=y.count('U')
        D=y.count('D')
        showKey[i]=(showKey[i]+D-U)%10
    print(*showKey,sep=" ")



def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def getInt():
    return list(map(int,input().split()))

for _ in range(int(input())):
    solve()