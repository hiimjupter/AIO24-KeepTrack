def max_kernel(num_list, k):
    # Initialize output list
    output = []
    # Iterate through num_list, ending before k index
    for i in range(0, len(num_list) + 1 - k):
        # Find max num at each iteration
        max_number = max(num_list[i: k])
        # Move i and move k to maintain the space
        k += 1
        output.append(max_number)
    return output


# Test case
assert max_kernel([3, 4, 5, 1, -44], 3)
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))
