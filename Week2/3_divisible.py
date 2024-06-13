def three_divisible(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)

    return var


assert three_divisible([3, 9, 4, 5]) == [3, 9]
print(three_divisible([x for x in range(1, 7)]))
