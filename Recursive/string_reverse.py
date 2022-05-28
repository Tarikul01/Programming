import  sys
sys.setrecursionlimit(30000)


def string_reverse(s):
    if s=="":
        return s
    else:
     return string_reverse(s[1:])+s[0]
# RecursionError: maximum recursion depth exceeded in comparison occurs when we declared string_reverse(s[1:]+s[0]) but wrong process
s="hello world"
print(string_reverse(s))