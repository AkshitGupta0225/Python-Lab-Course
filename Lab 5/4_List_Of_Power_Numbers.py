def power(number, length):
    results = []
    
    for i in range(length):
        base = i + 1
        pow = base ** number
        results.append(pow)
    
    return results

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    length = int(input("Enter the length of the list: "))
    pow = pow(num, length)
    print("List of powers:", power)
