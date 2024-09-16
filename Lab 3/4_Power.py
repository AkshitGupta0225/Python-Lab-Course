x=int(input("Enter the lower coefficient"))
n=int(input("Enter the upper coefficient"))

def power(x, n):
    pow = 1
    for i in range(n):
        pow = pow * x

    return pow
print(power(x,n))