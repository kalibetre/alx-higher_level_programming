#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    ROMANS = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "VI": 6,
        "VII": 7,
        "VIII": 8,
        "IX": 9,
        "X": 10,
        "XX": 20,
        "XXX": 30,
        "XL": 40,
        "L": 50,
        "LX": 60,
        "LXX": 70,
        "LXXX": 80,
        "XC": 90,
        "C": 100,
        "CC": 200,
        "CCC": 300,
        "CD": 400,
        "D": 500,
        "DC": 600,
        "DCC": 700,
        "DCCC": 800,
        "CM": 900,
        "M": 1000,
        "MM": 2000,
        "MMM": 3000
    }

    if roman_string in ROMANS:
        return ROMANS.get(roman_string)

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
