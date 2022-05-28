



def lengthOfLongestSubstring(s):
    start=0
    end=0
    lent=0
    dc={}
    while end <len(s):
        if s[end] in dc and dc[s[end]]>=start:
            start=dc[s[end]]+1
        lent=max(lent,end-start+1)
        dc[s[end]]=end
        end+=1
    return lent
s='pwwkew'
print(lengthOfLongestSubstring(s))