from collections import Counter
def solve():
    arr=[]
    for i in range(9):
        arr.append(input())
    for i in range(1,9):
        if(arr[i].count("R")==8):
            print("R")
            return
    print("B")













def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
def getInt():
    return list(map(int,input().split()))

for _ in range(int(input())):
    solve()