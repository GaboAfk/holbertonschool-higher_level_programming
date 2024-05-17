#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    if isinstance(roman_string, str) and roman_string is not None:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
        len_str = len(roman_string)
        for i in range(len_str):
            if i + 1 == len_str or roman_dict[roman_string[i]] \
                                    >= roman_dict[roman_string[i + 1]]:
                res += roman_dict[roman_string[i]]
            else:
                res -= roman_dict[roman_string[i]]
    return res
