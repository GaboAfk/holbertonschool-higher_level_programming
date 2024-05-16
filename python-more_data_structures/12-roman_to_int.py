#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    if isinstance(roman_string, str):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for letter in roman_string:
            if not res or res >= roman_dict[letter]:
                res += roman_dict[letter]
            else:
                res = roman_dict[letter] - res
    return res
