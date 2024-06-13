def character_count(string):
    char_dict = {}
    for _ in string:
        if _ not in char_dict.keys():
            char_dict[_] = 0
        if _ in char_dict.keys():
            char_dict[_] += 1
    return char_dict


# Test case
string = 'Happiness'
print(character_count(string))
