def sub_cost(token_1, token_2, row, col):
    if token_1[row - 1] == token_2[col - 1]:
        return 0
    else:
        return 1


def levenshtein_distance(token_1, token_2):
    # Step 1: Create matrix with M rows and N cols
    rows = len(token_1) + 1
    cols = len(token_2) + 1
    matrix = [[0] * cols for _ in range(rows)]

    # Step 2: Replace value of first row and column according to both tokens' lenghth
    for col in range(cols):
        matrix[0][col] = col
    for row in range(rows):
        matrix[row][0] = row

    # Step 3: Calculate D value
    for row in range(1, rows):
        for col in range(1, cols):
            a = matrix[row-1][col] + 1
            b = matrix[row][col-1] + 1
            cost = sub_cost(token_1, token_2, row, col)
            c = matrix[row-1][col-1] + cost
            matrix[row][col] = min(a, b, c)

    # Step 4: Return the shortest way (the value of the last row|column)
    return matrix[rows - 1][cols - 1]


# Test case
source = 'yu'
target = 'you'
print(levenshtein_distance(source, target))
