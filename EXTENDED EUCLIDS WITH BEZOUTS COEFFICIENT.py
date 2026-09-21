def egcd(a,b):
    if b==0:
        return 1,0,a
    x,y,d=egcd(b,a%b)
    return y,x-(a//b)*y,d
A,B=map(int,input().split())
x,y,D=egcd(A,B)
print(x,y,D)
