def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

def count_numbers_with_even_digits(nums):
    
    even_count = 0
    
    for num in nums:
        if count_digits(num) % 2 == 0:
            even_count += 1
    
    return even_count


print(count_numbers_with_even_digits([555, 901, 482, 1771]))