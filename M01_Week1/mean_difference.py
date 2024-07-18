# Take reference from questionnaires
def mean_difference_nth_root_error(y, y_hat, n, p):
    # Calc the nth root of y and y_hat
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)

    # Calc the loss (y is not always larger than y_hat)
    loss = (y_root - y_hat_root) ** p

    print(f"The Mean Difference of {n}th Root Error for y={y} and y_hat={y_hat} with degree of loss function={p} is {loss}")

# Test function
mean_difference_nth_root_error(100, 99.5, 2, 1)
mean_difference_nth_root_error(50, 49.5, 2, 1)
