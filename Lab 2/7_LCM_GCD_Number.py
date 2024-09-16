def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b, gcd):
    return (a * b) // gcd

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = calculate_gcd(num1, num2)
lcm = calculate_lcm(num1, num2, gcd)

print(f"The GCD of {num1} and {num2} is: {gcd}")
print(f"The LCM of {num1} and {num2} is: {lcm}")
