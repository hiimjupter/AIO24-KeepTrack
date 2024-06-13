def compare_value(num_list, n):
    return any(num == n for num in num_list)


assert compare_value([1, 3, 9, 4], 9) == True
print(compare_value([1, 2, 3, 4], 2))
