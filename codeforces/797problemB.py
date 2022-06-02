# n=int(input())
# a=list(map(int,input().split()))
a=[-2,2,-3,1];
s,en=0,10001

for x in a:
    if x>0:
        s+=x
        # print(x)
    if x%2!=0:
        en=min(en,abs(x))
if s%2==0: s-=en
print(s)