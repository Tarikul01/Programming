def solve():
    n,m=getInt()
    s=['B' for i in range(m)]
    check=[0 for i in range(m)]
    arr=getInt()
    for i in range(n):
        first=arr[i-1]
        last=m+1-arr[i-1]
        index=min(first,last)
        if(check[index-1]==1):
            index=max(first,last)
        s[index-1]='A'
        check[index-1]=1
    print("".join(s))


def getInt():
    return list(map(int,input().split()))

for _ in range(int(input())):
    solve()