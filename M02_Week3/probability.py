import numpy as np
import random


def create_train_data():
    # # Define possible values for each attribute
    # outlooks = ['Sunny', 'Overcast', 'Rain']
    # temperatures = ['Hot', 'Mild', 'Cool']
    # humidities = ['High', 'Normal']
    # winds = ['Weak', 'Strong']
    # play_tennis = ['yes', 'no']

    # data = []
    # num_rows = 10  # Number of rows you want to generate

    # for _ in range(num_rows):
    #     row = [
    #         random.choice(outlooks),
    #         random.choice(temperatures),
    #         random.choice(humidities),
    #         random.choice(winds),
    #         random.choice(play_tennis)
    #     ]
    #     data.append(row)

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
    # space = len(train_data)

    # no_count = 0
    # yes_count = 0

    # for _ in range(space):
    #     if train_data[_][-1] == 'no':
    #         no_count += 1
    #     else:
    #         yes_count += 1

    # prior_probability = np.array([no_count/space, yes_count/space])

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

# This function is used to return the index of the feature name


# def get_index_from_value(feature_name, list_features):
#     return np.where(list_features == feature_name)[0][0]


train_data = create_train_data()
# print('train_data is:\n', train_data)
prior_probability = compute_prior_probability(train_data)
# print("P(play tennis = No) is", prior_probability[0])
# print("P(play tennis = Yes) is", prior_probability[1])
conditional_probability, list_x_name = compute_conditional_probability(
    train_data)
# print(f'list_x_name is:')
# for i in range(4):
#     print(f'x{i+1} = {list_x_name[i]}')
# print('conditional probability is\n', conditional_probability)
# outlook = list_x_name[0]
# i1 = get_index_from_value("Overcast", outlook)
# i2 = get_index_from_value("Rain", outlook)
# i3 = get_index_from_value("Sunny", outlook)
# print(i1, i2, i3)
print("P(’Outlook’=’Sunny'|'Play Tennis’=’Yes’) = ",
      np.round(conditional_probability['Sunny']['yes'], 2))
print("P(’Outlook’=’Sunny'|'Play Tennis’='No) = ",
      np.round(conditional_probability['Sunny']['no'], 2))
