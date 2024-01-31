def combine_strings(s1, s2):

    len_s1 = len(s1)
    len_s2 = len(s2)
    middle_index_s1 = len_s1 // 2
    middle_index_s2 = len_s2 // 2
    first_char_s1 = s1[0]
    first_char_s2 = s2[0]
    if len_s1 % 2 == 0:
        middle_chars_s1 = s1[middle_index_s1]
    else:
        middle_chars_s1 = s1[middle_index_s1 - 1:middle_index_s1 + 1]

    if len_s2 % 2 == 0:
        middle_chars_s2 = s2[middle_index_s2]
    else:
        middle_chars_s2 = s2[middle_index_s2 - 1:middle_index_s2 + 1]

    last_char_s1 = s1[-1]
    last_char_s2 = s2[-1]
    new_string = first_char_s1 + middle_chars_s1 + last_char_s1 + first_char_s2 + middle_chars_s2 + last_char_s2
    return new_string
