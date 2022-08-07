def solve():
    n=int(input())
    n=abs(n)
    if(n==1):
        print(2)
    elif(n%3==1):
        print(((n//3)-1)+2)
    elif(n%3==2):
        print((n//3)+1)
    else:
        print(n//3)





def getInt():
    return list(map(int,input().split()))

for _ in range(int(input())):
    solve()