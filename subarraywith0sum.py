#sub array with zero sum 
#the task is to find if there is a subarray (of size at least one) with 0 sum.

def subArrayExists(arr, N):
    n_sum = 0
    s = set()

    for i in range(N):
        n_sum += arr[i]
        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)
    return False

if __name__ == '__main__':
    arr = [-3, 2, 3, 1, 6]
    N = len(arr)

    if subArrayExists(arr, N) == True:
        print("Found a subarray with 0 sum")
    else:
        print("No Such sub array exits!")

