n=10

# Returns index of target in nums array if present, else -1 
def binary_search(nums, left, right, target):   
    # Base case 
    if right >= left: 
        mid = int((left + right)/2)
        # If target is present at the mid, return
        if nums[mid] == target: 
            return mid 
        # Target is smaller than mid search the elements in left
        elif nums[mid] > target: 
            return binary_search(nums, left, mid-1, target) 
        # Target is larger than mid, search the elements in right
        else: 
            return binary_search(nums, mid+1, right, target) 
    else: 
        # Target is not in nums 
        return -1
nums = [1,2,3,4,5,6,7,8,9]
print(binary_search(nums, 0, len(nums)-1,7))