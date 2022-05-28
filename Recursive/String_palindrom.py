def palidrom(s):
    if len(s)==0 or len(s)==1:
        return True
    if s[0]==s[len(s)-1]:
        return palidrom(s[1:len(s)-2])
    return False
s="abbb"
print(palidrom(s))