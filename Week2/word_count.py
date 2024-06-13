def read_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        file.close()
        data.replace('\n', ' ')
        return data.split()


def word_count(file_path):
    counter = {}
    data = read_data(file_path)
    for word in data:
        counter[word] = counter.get(word, 0) + 1
    return counter


# Test case
file_path = 'Week2/P1_data.txt'
result = word_count(file_path)
assert result['who'] == 3
print(result['man'])
