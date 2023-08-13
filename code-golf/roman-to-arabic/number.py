# interactive version

to_roman = {
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


def split_on_particular_values(query, particular_values):
    # Create a unique token for replacements.
    token_template = "<TOKEN{}>"

    # Replace all 'particular values' in the query with our unique tokens.
    for idx, value in enumerate(particular_values):
        query = query.replace(value, token_template.format(idx))

    # Now, break down the modified query.
    output = []
    buffer = ""  # This buffer will accumulate characters until a token is found.

    idx = 0
    while idx < len(query):
        # Check if the current character starts a token.
        if query[idx:idx+6] == "<TOKEN":
            token_end_idx = query[idx:].find('>') + idx
            token_num = int(query[idx+6:token_end_idx])
            output.append(particular_values[token_num])
            idx = token_end_idx + 1
        else:
            output.append(query[idx])
            idx += 1

    return output


roman = input(f"Please enter a number in Roman numerals: ")
particular_values=["IV", "IX", "XL", "XC", "CD", "CM"]

compound=(split_on_particular_values(roman.upper(),  particular_values))

arabic=int()
for i in compound:
    arabic=arabic + to_roman[i]
print(arabic)