def convert_to_strings(lst, tpl):
    lst_strings = list(map(str, lst))
    tpl_strings = list(map(str, tpl))
    return lst_strings, tpl_strings
lst = [1, 2, 3, 4]
tpl = (5, 6, 7, 8)
lst_strings, tpl_strings = convert_to_strings(lst, tpl)
print("List of strings:", lst_strings)
print("Tuple of strings:", tpl_strings)
