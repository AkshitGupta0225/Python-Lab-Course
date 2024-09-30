def add(list1, list2):
    return list(map(lambda x, y: x + y, list1, list2))

def diff(list1, list2):
    return list(map(lambda x, y: x - y, list1, list2))
list1 = [10, 20, 30]
list2 = [1, 2, 3]

added = add(list1, list2)
difference = diff(list1, list2)

print("Added list:", added)
print("Difference list:", difference)