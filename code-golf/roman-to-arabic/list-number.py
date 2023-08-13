# version for Code Golf https://code.golf/r-to-arabic#python

import sys

pv = ["IV", "IX", "XL", "XC", "CD", "CM"]

to_r = {
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


def spv(query, pv):
    token_template = "<TOKEN{}>"
    for idx, value in enumerate(pv):
        query = query.replace(value, token_template.format(idx))
    output = []
    idx = 0
    while idx < len(query):
        if query[idx:idx+6] == "<TOKEN":
            tei = query[idx:].find('>') + idx
            tn = int(query[idx+6:tei])
            output.append(pv[tn])
            idx = tei + 1
        else:
            output.append(query[idx])
            idx += 1
    return output


for r in sys.argv[1:]:
    c = spv(r, pv)
    arabic = 0
    for i in c:
        arabic += to_r[i]
    print(f"{arabic}")
