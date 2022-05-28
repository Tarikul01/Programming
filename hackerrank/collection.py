a=int(input())
size=list(map(int,input().split(" ")))
customer=int(input())
totalearn=0
csize=[]
cprize=[]
for i in range(customer):
    a,b=input().split(" ")
    csize.append(a)
    cprize.append(b)
for i in range(len(csize)):
    csize[i]=int(csize[i])
    if csize[i] in size:
        totalearn +=int(cprize[i])
        size.remove(csize[i])
print(totalearn)



# csize=['6', '6', '6', '4', '18', '10']
# cprize=['55', '45', '55', '40', '60', '50']
# print(size)
# mx=max(size)
# mn=min(size)
# sizecnt=[]
# arra1=insertionSort(size)
# print(arra1)
# for i in range(len(size)):
#     for j in range(len(size)):
#         if size[i]==size[j]:
#             sizecnt[i]=sizecnt[i]+1
