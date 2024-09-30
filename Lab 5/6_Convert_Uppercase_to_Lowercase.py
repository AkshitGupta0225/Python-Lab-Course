def convert_and_remove_duplicates(sequence):
    lower= set(map(str.lower, sequence))
    upper= set(map(str.upper, sequence))
    return lower, upper
sequence = "HelloWorld"
lower, upper = convert_and_remove_duplicates(sequence)
print("Unique lowercase characters:", lower)
print("Unique uppercase characters:", upper)
