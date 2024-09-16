n= int(input("Enter a n: "))
if n <= 1:
    print(f"{n} is not a prime number.")
else:
    divisor_count = 0
    for i in range(2, n):
         if (n % i )== 0:
            divisor_count += 1
            break  
    
    for j in range(1):
        if divisor_count == 0:
            print(f"{n} is a prime n.")
        else:
            print(f"{n} is not a prime n.")
