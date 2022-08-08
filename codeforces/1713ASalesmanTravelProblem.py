def solve():
    n=int(input())
    left=right=up=down=0
    while n:
        x,y=getInt()
        if x>0:
            right=max(right,x)
        elif x<0:
            left=max(left,abs(x))
        elif y>0:
            up=max(up,y)
        else:
            down=max(down,abs(y))
        n=n-1
    print((left+right+up+down)*2)





def getInt():
    return list(map(int,input().split()))

for _ in range(int(input())):
    solve()