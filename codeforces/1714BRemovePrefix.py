for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    # ln=len(arr)
    # stack=[]
    # revArr=arr[::-1]

    # for i in range(len(arr)-1,-1,-1):
    #     if(arr[i] not in stack):
    #         stack.append(arr[i])
    #
    #     else:
    #         print(ln - len(stack))
    #         break
    # if(ln==len(stack)):
    #     print(0)
    x=set()
    visited=[]
    for i in range(len(arr)-1,-1,-1):
        x.add(arr[i])
        visited.append(arr[i])
        if len(x) < len(visited):
            break

    print(len(arr) - len(x))



