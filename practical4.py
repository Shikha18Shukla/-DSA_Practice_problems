# array containing 0s,1s, and 2s , sort in linear time  O(n)
arr=[1,2,1,0,0,1,2,1]
low=arr[0]
high=arr[n]-1
mid=arr[0]
while mid<= high:
    if arr[mid]==0:           # not completed question 
        arr[low],arr[mid]=arr[mid],arr[low]
        low+=1
        mid+=1
    elif arr[mid]==1:
        mid+=1
    else:
        arr[mid],arr[high]=arr[high],arr[mid]
        high-=1
arr=[2,3,5,7,8,12,14,22,15]
n=len(arr)






