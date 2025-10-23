def findLargest(arr):
    if not arr:
        return None 

    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest


arr = [3, 7, 2, 9, 5, 1]
print(findLargest(arr)) 
