def replace_elements(arr):
    n = len(arr)
    
    max_element = -1 
    
    for i in range(n-1, -1, -1):
        current_element = arr[i]
        arr[i] = max_element  
        max_element = max(max_element, current_element)  
    
    return arr

arr1 = [17, 18, 5, 4, 6, 1]
result1 = replace_elements(arr1)
print(f"Output: {result1}")