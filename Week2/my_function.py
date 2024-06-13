def my_function(data, max, min):
    result = []
    for i in data:
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)

    return result


assert my_function([5, 2, 5, 0, 1], 1, 0) == [1, 1, 1, 0, 1]

print(my_function([10, 2, 5, 0, 1], 2, 1))
