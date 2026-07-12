def majority_elements(arr):
    count = 1
    arr.sort()

    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            count += 1
        else:
            count = 1

        if count > len(arr)//2:
            return arr[i]

    return -1


n = int(input())
arr = list(map(int, input().split()))
print(majority_elements(arr))