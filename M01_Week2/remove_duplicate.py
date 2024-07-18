def function_helper(x, data):
    for i in data:
        if x == i:
            return 0
    return 1


def remove_duplicate(data):
    res = []
    for i in data:
        if function_helper(i, res):
            res.append(i)
    return res


assert remove_duplicate([10, 10, 9, 7, 7]) == [10, 9, 7]

print(remove_duplicate([9, 9, 8, 1, 1]))
