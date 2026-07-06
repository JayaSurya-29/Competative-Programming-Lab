def max_subarray(a):
    current_sum=a[0]
    max_sum=a[0]
    for i in range(1,len(a)):
        current_sum=max(a[i],current_sum+a[i])
        max_sum=max(max_sum,current_sum)
    return max_sum
 
n=int(input())       
a=list(map(int,input().split()))
print(max_subarray(a))
