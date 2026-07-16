def countingSort(arr):
    n=len(arr)
    max_val=max(arr)
    count=[0]*(max_val+1)
    for i in arr:
        count[i]+=1
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    output=[0]*n
    for i in range(n-1,-1,-1):
        a=arr[i]
        b=count[a]-1
        output[b]=a
        count[a]-=1
    return output
    
n=int(input())
arr=list(map(int,input().split()))
print(countingSort(arr))