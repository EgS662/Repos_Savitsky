def sort_array_by_parity(nums):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        if nums[left] % 2 != 0 and nums[right] % 2 == 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        elif nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 != 0:
            right -= 1
    
    return nums

nums1 = [3, 1, 2, 4]
result1 = sort_array_by_parity(nums1)
print(f"Output: {result1}")