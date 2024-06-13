def function_helper(x):
    if x > 0:
        return 'T'
    return 'N'


def check_pos_val(data):
    res = [function_helper(x) for x in data]
    return res


assert check_pos_val([10, 0, -10, -1]) == ['T', 'N', 'N', 'N']
print(check_pos_val([2, 3, 5, -1]))
