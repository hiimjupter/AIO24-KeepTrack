import numpy as np
import random


def create_train_data():
    data = [
        ['Sunny', 'Hot', 'High', 'Weak', 'no'],
        ['Sunny', 'Hot', 'High', 'Strong', 'no'],
        ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
        ['Overcast', 'Mild', 'High', 'Weak', 'no'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'yes']
    ]

    return np.array(data)


def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))
    total_count = len(train_data)
    for i, y in enumerate(y_unique):
        count = np.sum(train_data[:, -1] == y)
        prior_probability[i] = count / total_count

    return prior_probability


def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = {}
    list_x_name = []

    for i in range(0, train_data.shape[1]-1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)

        for x_val in x_unique:
            conditional_probability[x_val] = {}
            for y_val in y_unique:
                count_y = np.sum(train_data[:, -1] == y_val)
                count_xy = np.sum((train_data[:, i] == x_val) & (
                    train_data[:, -1] == y_val))

                # Naive Bayes
                conditional_probability[x_val][y_val] = count_xy / \
                    count_y if count_y != 0 else 0

    return conditional_probability, list_x_name


def train_naive_bayes(train_data):
    y_unique = ['no', 'yes']
    prior_probability = compute_prior_probability(train_data)

    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)

    return prior_probability, conditional_probability, list_x_name


def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    p_no = prior_probability[0]
    p_yes = prior_probability[1]

    p_no_when_X = p_no
    p_yes_when_X = p_yes

    # Calculate multiplication of x_case when given y_case
    for i in range(len(X)):
        p_no_when_X *= conditional_probability[X[i]]['no']
        p_yes_when_X *= conditional_probability[X[i]]['yes']

    # Normalizaion
    p_no_when_X = np.round(p_no_when_X, 2)
    p_yes_when_X = np.round(p_yes_when_X, 2)

    if p_no_when_X > p_yes_when_X:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred


data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(
    data)

X = [''] * 4
print(f"We only accept input within: {list_x_name[0]}")
X[0] = input("What is the Outlook?\n")
while X[0] not in list_x_name[0]:
    X[0] = input("Invalid input! Please try again")

print(f"We only accept input within: {list_x_name[1]}")
X[1] = input("What is the Temperature?\n")
while X[1] not in list_x_name[1]:
    X[1] = input("Invalid input! Please try again")

print(f"We only accept input within: {list_x_name[2]}")
X[2] = input("What is the Humidity?\n")
while X[2] not in list_x_name[2]:
    X[2] = input("Invalid input! Please try again")

print(f"We only accept input within: {list_x_name[3]}")
X[3] = input("What is the Wind?\n")
while X[3] not in list_x_name[3]:
    X[3] = input("Invalid input! Please try again")


pred = prediction_play_tennis(
    X, list_x_name, prior_probability, conditional_probability)

if (pred == 1):
    print('Hilton should go playing Tennis!')
else:
    print("Hilton shouldn't go playing Tennis!")
