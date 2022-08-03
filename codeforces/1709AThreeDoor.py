def solve():
    key=int(input())
    door=list(map(int,input().split()))
    count=1
    while(door[key-1] != 0):
        key=door[key-1]
        count+=1
    if(count==3):
        print('YES')
    else:
        print('NO')
for _ in range(int(input())):
    solve()
