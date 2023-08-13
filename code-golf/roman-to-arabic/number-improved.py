# interactive version

ROMAN_TO_ARABIC = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000
}


def roman_to_arabic(roman):
    i, total = 0, 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i+2] in ROMAN_TO_ARABIC:
            total += ROMAN_TO_ARABIC[roman[i:i+2]]
            i += 2
        else:
            total += ROMAN_TO_ARABIC[roman[i]]
            i += 1
    return total


query = input(f"Please enter a number in Roman numerals: ")
print(roman_to_arabic(query.upper()))
