s=input().strip()
if s:
    n=len(s)
    for p in range(1,n):
        if s[p:]==s[:n-p]:
            print(p)
            exit()
    print(n)