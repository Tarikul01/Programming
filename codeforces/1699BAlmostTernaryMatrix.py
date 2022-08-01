for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    for i in range(n):
        for j in range(m):
            print(((i//2+j//2)&1),end=" ")
            # print(((i%4<=1)!=(j%4<=1)&1),end=" ")
        print()