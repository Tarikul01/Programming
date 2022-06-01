t=int(input())
def solve():
    x=int(input())
    arr=list(map(int,input().split()))
    ans=0
    i=0
    while(i<len(arr)-1):
        if(arr[i]>arr[i+1]):
            ans+=1
            i+=2
        else:
            i+=1
    print(ans)
for i in range(t):
    solve()
