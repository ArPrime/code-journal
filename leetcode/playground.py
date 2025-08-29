def binary_search_recursive(nums, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
        return binary_search_recursive(nums, target, left, right)
    else:
        right = mid - 1
        return binary_search_recursive(nums, target, left, right)
    
print(binary_search_recursive(nums=[-1,0,3,5,9,12], target = 9, left=0, right=5))