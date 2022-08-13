def solve():
    n,m=getInt()
    a=input()
    b=input()
    aln=len(a)
    bln=len(b)
    x=1-m
    if aln<bln:
        ans="NO"
    elif a==b:
        ans="YES"
    elif m==1:
        if(b in a):
            ans="YES"
        else:
            ans="NO"
    else:
        if (a[x:]==b[1:]) and (b[0] in a[:x]):
            ans="YES"
        else:
            ans="NO"
    print(ans)

    # ans="NO"
    # while i<aln:
    #     if a[i]==b[j]:
    #         j+=1
    #     if j==bln:
    #         ans="YES"
    #         break
    #
    #     i+=1
    # print(ans)










def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def getInt():
    return list(map(int,input().split()))

for _ in range(int(input())):
    solve()
