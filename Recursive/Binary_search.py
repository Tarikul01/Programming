def binary_search(arr,l,r,x):
    if r<=l:
        return -1
    else:
        mid=l+(r-l)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,l,mid-1,x)
        else:
            return binary_search(arr,mid+1,r,x)
arr=[2,3,1,4,5,7,6,9,11,10]
print(binary_search(arr,0,len(arr)-1,7))