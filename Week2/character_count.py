def character_count(string):
    char_dict = {}
    for char in string:
        # Return value = 0 if not found key "{char}"
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict


# Test case
string = 'Happiness'
print(character_count(string))
