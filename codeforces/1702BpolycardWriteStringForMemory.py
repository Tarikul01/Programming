for i in range(int(input())):
    s = input()
    k = 0
    T = set()
    N = len(s)
    for i in range(N):
        T.add(s[i])
        if len(T)>3:
            k+=1
            T = {s[i]}
    print(k+1)