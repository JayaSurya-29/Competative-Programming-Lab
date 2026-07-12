def maxSum(arr):
    curr_sum=arr[0]
    max_sum=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            curr_sum+=arr[i]
        else:
            curr_sum=arr[i]
        max_sum=max(max_sum,curr_sum)
    print(max_sum)       

n=int(input())
arr=list(map(int,input().split()))
maxSum(arr)