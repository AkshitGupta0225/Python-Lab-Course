class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("Akshit", 20)
person2 = Person("Divit", 16)
print(f"Person 1: Name = {person1.name}, Age = {person1.age}")
print(f"Person 2: Name = {person2.name}, Age = {person2.age}")
