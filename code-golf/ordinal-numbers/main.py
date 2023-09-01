

import sys


for arg in sys.argv[1:]:
    j = int(arg) % 10
    k = int(arg) % 100
    if j == 1 and k != 11:
        s = "st"
    elif j == 2 and k != 12:
        s = "nd"
    elif j == 3 and k != 13:
        s = "rd"
    else:
        s = "th"

    print(f"{arg}{s}")
