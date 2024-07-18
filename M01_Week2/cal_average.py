def cal_average(num_list):
    var = 0
    for i in num_list:
        var += i
    return var/len(num_list)


assert cal_average([4, 6, 8]) == 6
print(cal_average([0, 1, 2]))
