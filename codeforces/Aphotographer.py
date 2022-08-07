def solve():
    n,x=getInt()
    arr=getInt()
    arr.sort()
    ans="YES"
    for i in range(n):
        if(arr[i+n]-arr[i]<x):
            ans="NO"
            break

    print(ans)




def getInt():
    return list(map(int,input().split()))

for _ in range(int(input())):
    solve()