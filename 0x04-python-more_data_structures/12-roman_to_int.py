#!/usr/bin/python3
def roman_to_int2(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    ROMAN_ODDITIES = {
        "IV": "P",
        "IX": "Q",
        "XL": "R",
        "XC": "S",
        "CD": "T",
        "CM": "U",
    }

    ROMANS = {
        "I": 1,
        "P": 4,
        "V": 5,
        "Q": 9,
        "X": 10,
        "R": 40,
        "L": 50,
        "S": 90,
        "C": 100,
        "T": 400,
        "D": 500,
        "U": 900,
        "M": 1000,
    }

    for key in ROMAN_ODDITIES:
        roman_string = roman_string.replace(key, ROMAN_ODDITIES.get(key))

    num = 0
    i = 0
    for ch in roman_string[i:]:
        if ch in ROMANS:
            num += ROMANS.get(ch)
            i += len(ch)
            if i >= len(roman_string):
                break
            ch = roman_string[i]
        else:
            ch += ch

    return num
