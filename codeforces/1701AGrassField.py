for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    c,d=list(map(int,input().split()))
    if a==1:
        if c==0 and b==0:
            print(1)
        else:
            print(2)

    else:
        if b==0 and c==0:
            print(0)
        else:
            print(1)