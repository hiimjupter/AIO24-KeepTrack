import numpy as np
import pandas as pd


data = pd.read_csv(
    "/Users/jupternguyen/Projects/EXT10004_AIO24/Homework/AIO24-KeepTrack/M02_Week4/advertising.csv")


def compute_correlation(X, Y):
    N = len(X)
    numerator = 0
    denominator = 0

    multiply_array = np.multiply(X, Y)

    numerator = (N*np.sum(multiply_array)) - (np.sum(X) * np.sum(Y))

    std_X = np.sqrt(N*np.sum(np.power(X, 2)) - np.power(np.sum(X), 2))
    std_Y = np.sqrt(N*np.sum(np.power(Y, 2)) - np.power(np.sum(Y), 2))

    denominator = std_X * std_Y

    return round((numerator/denominator), 2)


# Question 5
x = data['TV']
y = data['Radio']
corr_xy = compute_correlation_cofficient(x, y)

# print(corr_xy)


# Question 6
features = ['TV', 'Radio', 'Newspaper']
for feature_1 in features:
    for feature_2 in features:
        corr_val = compute_correlation(
            data[feature_1], data[feature_2])
        print(
            f'The correlation between {feature_1} and {feature_2} is: {corr_val}')
