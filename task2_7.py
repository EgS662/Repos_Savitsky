def check_double(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n):
            if i != j and arr[i] == 2 * arr[j]:
                return True
    
    return False


arr1 = [10, 2, 5, 3]
result1 = check_double(arr1)
print(f"Output: {result1}")