def D_T_B(n,s):
    if n==0:
        return s
    else:
        s+=str(n%2)
        return D_T_B(n//2,s)

print(D_T_B(233,""))