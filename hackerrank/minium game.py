
s="AABCAAADA"
k=3
def rmvch(s):
    list=[]
    for i in range(len(s)):
        if s[i] not in list:
           list.append(s[i])
    return "".join(list)
sln=len(s)
x=int(sln/k)
y=sln/k
sln=k*(x+1) if x<y else k*x
for i in range(0,sln,k):
     newst=s[i:i+k]
     print(rmvch(newst))
