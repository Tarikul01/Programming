def lcs_algo(x,y,m,n):
    l=[[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif x[i-1]==y[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    index=l[m][n]
    lcs_algo=[""]*(index+1)
    lcs_algo[index]=""
    i,j=m,n
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            lcs_algo[index-1]=x[i-1]
            i-=1
            j-=1
            index-=1
        elif l[i-1][j]>l[i][j-1]:
            i-=1
        else:
            j-=1
    print("x  =>"+x+"      y   =>"+y )
    print("LCS =>"+"".join(lcs_algo))
x="AGGTAB"
y="GXTXAYB"

lcs_algo(x,y,len(x),len(y))