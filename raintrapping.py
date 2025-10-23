
                       # Two Pointer approach 

def trap(height):
    left,right=0 , len(height)-1
    left_max=0
    right_max=0
    water=0
    while left<=right:
        if height[left]<=height[right]:
            if height[left]>=left_max:
                left_max=height[left]
            else:
                water+=left_max-height[left]
            left+=1
        else:
                if height[right]>=right_max:
                    right_max=height[right]
                else:
                    water+=right_max-height[right]
                right-=1
    return water 
print("no. of columns in which we can store water if the array is [4,0,1,5,0,4] : ",trap([4,0,1,5,0,4]))
print("no. of columns in which we can store water if the array is [1,0,0,8,0,2] : ",trap([1,0,0,8,0,2]))
print("no. of columns in which we can store water if the array is [4,0,1,0,5,0,5] : ",trap([4,0,1,0,5,0,5]))










