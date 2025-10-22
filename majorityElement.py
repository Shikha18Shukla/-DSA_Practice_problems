#complexity O(n^2)
def majorityElement(arr):
    n = len(arr)

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1                                 
        if count > n // 2:   
            return arr[i]
    return -1
arr=[1,2,3,3,3,4,3]
print("majorityElement:",majorityElement(arr))






#complexity O(n)
#Boyer–Moore Voting Algorithm


from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate