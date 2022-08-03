for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    if not any(arr[i]%arr[0] for i in range(1,n)):
        ans="YES"
    else:
        ans="NO"
    print(ans)