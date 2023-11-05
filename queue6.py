from collections import deque

def max_sliding_window(nums, k):
    result = []
    window = deque()
    n = len(nums)

    for i in range(n):
        while window and window[0] <= i - k:
            window.popleft()

        while window and nums[window[-1]] <= nums[i]:
            window.pop()

        window.append(i)

        if i >= k - 1:
            result.append(nums[window[0]])

    return result


nums1 = [1,3,-1,-3,5,3,6,7]
k1 = 3
result1 = max_sliding_window(nums1, k1)
print(result1) 


nums2 = [1]
k2 = 1
result2 = max_sliding_window(nums2, k2)
print(result2) 