from pip._vendor.distlib.compat import raw_input

for i in range(int(input())):
  m=int(input())
  arr=list(map(int, input().split()))
  arr.sort()
  if (len(arr) == 1):
   print('YES')
  else:
    flag = True
    for i in range(len(arr)-1):
       num=abs(arr[i+1] - arr[i])
       if num >1:
           flag=False
    print('YES') if flag else print("NO")

