def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example Usage
array = [10, 20, 30, 40, 50]
target = 30
print("Element found at index:", linear_search(array, target))
