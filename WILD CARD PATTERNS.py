s=input().strip()
p=input().strip()
i=j=0
star=-1
k=0
while i<len(s):
    if j<len(p) and (p[j]==s[i] or p[j]=='?'):
        i+=1
        j+=1
    elif j<len(p) and p[j]=='*':
        star=j
        k=i
        j+=1
    elif star!=-1:
        j=star+1
        k+=1
        i=k
    else:
        print(0)
        break
else:
    while j<len(p) and p[j]=='*':
        j+=1
    if j==len(p):
        print(1)
    else:
        print(0)
