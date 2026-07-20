def check(n,k):
    if n&(1<<k)!= 0:
        return 1
    else:
        return 0
n=int(input())
k=int(input())        
print(check(n,k))
