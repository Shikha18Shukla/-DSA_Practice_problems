

def prefix_sum(arr):
    n=len(arr)
    prefix=[0]*n
    prefix[0]=arr[0]
    for i in range(1,n):
        prefix[i]=prefix[i-1] + arr[i]
    return prefix

arr=[1,3,4,5,6,7]
print("Original Array:",arr)
print("prefix sum :",prefix_sum(arr))