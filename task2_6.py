def remove_duplicates(nums):
    if not nums:
        return 0
    
    k = 1  
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]  
            k += 1
    
    return k, nums[:k] + ['_'] * (len(nums) - k) 


nums1 = [1, 1, 2]
result1, modified_nums1 = remove_duplicates(nums1)
print(f"Output: {result1}, nums = {modified_nums1}")
