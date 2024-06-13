def reverse_function(x):
    x = list(x)
    left = 0
    right = len(x) - 1
    while left < right:
        x[left], x[right] = x[right], x[left]
        left += 1
        right -= 1
    return ''.join(x)


assert reverse_function('I can do it') == 'ti od nac I'
print(reverse_function('Apricot'))
