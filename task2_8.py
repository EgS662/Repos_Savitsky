def valid_mountain_array(arr):
    n = len(arr)
    
    if n < 3:
        return False

    peak = max(arr)
    peak_index = arr.index(peak)
    
    if peak_index == 0 or peak_index == n - 1:
        return False
    
    for i in range(peak_index):
        if arr[i] >= arr[i+1]:
            return False
    
    for i in range(peak_index, n-1):
        if arr[i] <= arr[i+1]:
            return False
    
    return True


arr1 = [2, 1]
result1 = valid_mountain_array(arr1)
print(f"Output: {result1}")

arr2 = [3, 5, 5]
result2 = valid_mountain_array(arr2)
print(f"Output: {result2}")

arr3 = [0, 3, 2, 1]
result3 = valid_mountain_array(arr3)
print(f"Output: {result3}")