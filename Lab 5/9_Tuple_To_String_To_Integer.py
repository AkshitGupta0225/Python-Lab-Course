def get_elements(t, i):
    return [t[x] for x in i]
def str_to_int(s):
    return int(s)
t = (10, 20, 30, 40, 50)
i = [1, 3]
s = "123"
lst = get_elements(t, i)
n = str_to_int(s)
print("New list:", lst)
print("Converted integer:", n)
