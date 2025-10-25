def next_smaller_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n-1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    
    return result

arr = [40, 81, 15, 12, 25]
print("Next Smaller Elements:", next_smaller_element(arr))
arr = [4, 8, 3, 2, 5]
print("Next Smaller Elements:", next_smaller_element(arr))
