def sum_list_values(list_values):
    return sum(list_values)

def symbolic_to_octal(perm_string):
    perms = {"r": 4, "w": 2, "x": 1, "-": 0}
    string_value = []
    symb_to_octal = []

    slicing_values = {"0": perm_string[:3], "1": perm_string[3:6], "2":perm_string[6:9]}

    for perms_key, value in perms.items():
        for string_values in slicing_values.items():
            for v in string_values[1]:
                if v == perms_key:
                    string_value.append(value)
    
    sum_strings = sum_list_values(string_value)
    symb_to_octal.append(sum_strings)

    return (symb_to_octal)

#assert symbolic_to_octal('rwxr-x-w-') == 752

print(symbolic_to_octal('rwxr-x-w-'))