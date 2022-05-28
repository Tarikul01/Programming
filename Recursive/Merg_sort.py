
def merg(arr,l,p,r):
    n1=p-l+1
    n2=r-p
    L=[0]*(n1)
    R=[0]*(n2)
    for i in range(0,n1):
        L[i]=arr[l+i]
    for j in range(0,n2):
        R[j]=arr[p+1+j]
    k=l
    i=0
    j=0
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1
def merg_sort(arr,l,r):
    if l<r:
        p=l+(r-l)//2
        merg_sort(arr,l,p)
        merg_sort(arr,p+1,r)
        merg(arr,l,p,r)


arr=[1,4,3,4]
n=len(arr)
merg_sort(arr,0,n-1)
print(arr)
