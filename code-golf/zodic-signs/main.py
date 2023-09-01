import sys

ZODIAC = {
    0: "♑",  # add final value back to 'beginning of dict to complete cycle
    120: "♒",
    219: "♓",
    321: "♈",
    420: "♉",
    521: "♊",
    622: "♋",
    723: "♌",
    823: "♍",
    923: "♎",
    1023: "♏",
    1123: "♐",
    1222: "♑",
}

SYMBOL = "♈♉♊♋♌♍♎♏♐♑♒♓"

SUN = {
    0: "♒♓♈♉♊♋♌♍♎♏♐♑",
    200: "♓♈♉♊♋♌♍♎♏♐♑♒",
    400: "♈♉♊♋♌♍♎♏♐♑♒♓",
    600: "♉♊♋♌♍♎♏♐♑♒♓♈",
    800: "♊♋♌♍♎♏♐♑♒♓♈♉",
    1000: "♋♌♍♎♏♐♑♒♓♈♉♊",
    1200: "♌♍♎♏♐♑♒♓♈♉♊♋",
    1400: "♍♎♏♐♑♒♓♈♉♊♋♌",
    1600: "♎♏♐♑♒♓♈♉♊♋♌♍",
    1800: "♏♐♑♒♓♈♉♊♋♌♍♎",
    2000: "♐♑♒♓♈♉♊♋♌♍♎♏",
    2200: "♑♒♓♈♉♊♋♌♍♎♏♐",
}

for a in sys.argv[1:]:
    z = a.split(" ")
    # convert date to an int for numeric comparison
    d = int(z[0].replace("-", ""))
    # return dict of all k:v where k <= d
    g = ({k: v for (k, v) in dict.items(ZODIAC) if k <= d})
    # Get key with maximum value in Dictionary
    zodiac_sign = max(zip(g.keys(), g.values()))[1]

    # convert time to int for numeric comparison
    s = int(z[1].replace(":", ""))
    # return dict of all k:v where k <= s
    t = ({k: v for (k, v) in dict.items(SUN) if k <= s})
    # Get key with maximum value in Dictionary
    u = max(zip(t.keys(), t.values()))[1]
    # zip map SYMBOL with matched row from SUN
    w = {SYMBOL[i]: u[i] for i in range(len(u))}
    # look up appropriate sun sign from constructed map
    sun_sign = (w[zodiac_sign])

    if sun_sign == zodiac_sign:
        print(zodiac_sign)
    else:
        print(f"{zodiac_sign}{sun_sign}")
