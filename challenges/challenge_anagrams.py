def count_characters(string):
    character_count = {}
    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


def is_anagram(first_string, second_string):
    if (
        not first_string
        or not second_string
        or len(first_string) != len(second_string)
    ):
        return False

    first_string = first_string.lower()
    second_string = second_string.lower()

    first_string_dict = count_characters(first_string)
    second_string_dict = count_characters(second_string)

    return first_string_dict == second_string_dict
