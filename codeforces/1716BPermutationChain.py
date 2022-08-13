def solve():
    n=int(input())
    arr=[ i for i in range(1,n+1)]
    print(n)
    print(*arr,sep=" ")
    ln=len(arr)
    for i in range(ln-1):
        a,b=swap(arr[i],arr[i+1])
        arr[i]=a
        arr[i+1]=b
        print(*arr,sep=" ")










def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def getInt():
    return list(map(int,input().split()))

for _ in range(int(input())):
    solve()