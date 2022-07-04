for _ in range(int(input())):
    a=int(input())
    n=input()
    if(n[0]=='9'):
        print(int('1'*(a+1))-int(n))
    else:
        print(int('9' * (a)) - int(n))

# for _ in range(int(input())):
#     n=int(input())
#     s=input()
#     if s[0]=='9':
#         print(int('1'*(n+1))-int(s))
#     else:
#         print(int('9'*n)-int(s))
