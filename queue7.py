def max_subsequence_sum(nums, k):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]

    for i in range(1, n):
        dp[i] = max(dp[j] + nums[i] for j in range(max(0, i-k), i))

    return max(dp)


nums1 = [10,2,-10,5,20]
k1 = 2
result1 = max_subsequence_sum(nums1, k1)
print(result1)  


nums2 = [-1,-2,-3]
k2 = 1
result2 = max_subsequence_sum(nums2, k2)
print(result2)  


nums3 = [10,-2,-10,-5,20]
k3 = 2
result3 = max_subsequence_sum(nums3, k3)
print(result3) 