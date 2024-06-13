def factorial(n):
    if n < 0:
        raise ValueError('The function do not accept value below 1')
    # Iterative approach
    # var = 1
    # while n > 1:
    #     var *= n
    #     n -= 1
    # return var

    # Recursive approach
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


assert factorial(8) == 40320
print(factorial(4))
