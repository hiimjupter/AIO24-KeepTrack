def check_the_number(n):
    num_list = []
    result = ''
    for i in range(1, 5):
        num_list.append(i)
        if n in num_list:
            result = 'True'
        else:
            result = 'False'

    return result


n = 4
assert check_the_number(n) == 'True'

n = 2
results = check_the_number(n)
print(results)
