def solve():
    n=int(input())
    arr=[ i for i in range(1,n+1)]
    ln=len(arr)
    if ln==1:
        print(arr[0])
    else:

        if ln%2==0:
            for i in range(0, ln - 1, 2):
                a, b = swap(arr[i], arr[i + 1])
                arr[i] = a
                arr[i + 1] = b
            print(*arr,sep=" ")
        else:
            temp = arr[ln - 2]
            arr[ln - 2] = arr[ln-1]
            arr[ln-1] = temp
            for i in range(0, ln - 1, 2):
                a, b = swap(arr[i], arr[i + 1])

                arr[i] = a
                arr[i + 1] = b

            print(*arr,sep=" ")

def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def getInt():
    return list(map(int,input().split()))

for _ in range(int(input())):
    solve()