s="AB"
# s="ABC"
# s="HACK"
def swap(x,y):
    tmp=x
    a=y
    b=tmp
    return a,b

def permute(str,l,r):
             if l==r:
                   print(str)
             else:
               for j in range(l,r+1):
                        a, b = swap(str[l], str[j])
                        ls = list(str)
                        ls[l] = a
                        ls[j] = b
                        new = "".join(ls)
                        permute(new,l+1,r)



permute(s,0,len(s)-1)