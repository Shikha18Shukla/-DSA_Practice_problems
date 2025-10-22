#find kth smallest and largest element in an  array
def kth_smallest(arr,k):
    arr_sort=arr.sort()
    return arr_sort[k-1]
def kth_largest(arr,k):
    arr_sort=arr.sort()                 #wrong answer 
    return arr_sort[-k]

arr=[7,0,9,4,1,6]
k1=2
k2=3
print("second smallest element :",kth_smallest(arr,k1))
print("third largest element :",kth_largest(arr,k2))