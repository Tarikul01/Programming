n=int(input())
for i in range(n):
    m=int(input())
    arr=list(map(int,input().split()))
    mn=sum(arr)/m
    print("YES" if mn in arr else "NO")

