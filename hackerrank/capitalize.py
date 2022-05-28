s="hello world"
new=s.split(' ')
fs=new[0][0].upper()+new[0][1:len(new[0])]
snd=new[1][0].upper()+new[1][1:len(new[1])]
str=fs+" "+snd
print(str)