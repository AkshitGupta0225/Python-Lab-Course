def fib(a):
    b, c = 0, 1
    fib_sequence = []
    for _ in range(a):
        fib_sequence.append(b)
        b, c = c, b + c
    return fib_sequence
def square(x):
    return x ** 2
a = 10  
b = fib(a) 
c = list(map(square, b)) 
print("First", a, "Fibonacci numbers:", b)
print("Squares of Fibonacci numbers:", c)
