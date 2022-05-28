# def aModm(s,mod):
#     number=0
#     for i in  range(len(s)):
#         number=(number*10 +int(s[i]))
#         number=number%mod
#
#     return number
# def BigMod(a,b,m):
#     ans=aModm(a,m)
#     mul=ans
#     for i in range(1,b):
#         ans=(ans*mul)%m
#     return ans
# a = "7"
# b, m = 37, 9
# print(BigMod(a, b, m))
def bigmod(base,pow,mod):
    if pow==0:
        return 1
    elif pow%2==0:
        p1=bigmod(base,pow/2,mod)
        return (p1*p1)%mod
    elif pow%2==1:
        p1=base%mod
        p2=bigmod(base,pow-1,mod)
        return  (p1*p2)%mod
print(bigmod(2,30,11))
