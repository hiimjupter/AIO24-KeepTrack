def extend_function(x, y):
    x.extend(y)
    return x


assert extend_function(['a', 2, 5], extend_function(
    [1, 1], [0, 0])) == ['a', 2, 5, 1, 1, 0, 0]

print(extend_function([1, 2], extend_function(
    [3, 4], [0, 0])))
