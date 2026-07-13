n,m=map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a=sorted(a1+a2)
length=len(a)
if length%2==1:
    print(a[length//2])
else:
    median=(a[length//2-1]+a[length//2])/2
    print(f"{median:.1f}")
