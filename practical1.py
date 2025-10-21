def find_min_max(arr):
    minimum = arr[0]
    maximum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    return minimum, maximum

arr = [5, 2, 9, 1, 7]
print("Min and Max:", find_min_max(arr))
