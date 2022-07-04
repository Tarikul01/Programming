import sys
sys.setrecursionlimit(10000)

def pathval(a,b,n,m):
    return ((a-1)*m)+b

def recur(n,m,x,y,sum):
    if n>=2:
        # print(n,m)
        sum+=pathval(n,m,x,y)
        return recur(n-1,m,x,y,sum)
    if m>=1:
        # print(n,m)
        sum += pathval(n, m, x, y)
        return recur(n,m-1,x,y,sum)
    return sum

# for i in range(int(input())):
#     n,m=list(map(int,input().split()))
#     sum=0
#     for i in range(1,m+1):
#         # print(i)
#         sum+=i
#     for i in range(2,n+1):
#         # print(m*i)
#         sum+=m*i
#     print(sum)

t = int(input())

for _ in range(int(input())):
	n, m = map(int, input().split())
	print(m*(m-1 + n*(n+1))//2)
