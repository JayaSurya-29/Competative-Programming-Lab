dividend=int(input())
divisor=int(input())
if (dividend<0)^(divisor<0):
    sign=-1
else:
    sign=1
dividend=abs(dividend)
divisor=abs(divisor)
low=0
high=dividend
ans=0
while low<=high:
    mid=(low+high)//2
    if mid*divisor<=dividend:
        ans=mid
        low=mid+1
    else:
        high=mid-1
print(sign*ans)
