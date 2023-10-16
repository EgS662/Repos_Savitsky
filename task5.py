def my_pow(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / my_pow(x, -n)
    elif n % 2 == 0:
        half = my_pow(x, n // 2)
        return half * half
    else:
        return x * my_pow(x, n - 1)
x = int(input("Enter x:"))
n = int(input("Enter n:"))
print(my_pow(x, n))    
 
