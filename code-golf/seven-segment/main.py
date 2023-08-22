
""" 
Using pipes and underscores print the argument as if it were displayed on a seven segment display.

For example the number 0123456789 should be displayed as:

 _     _  _     _  _  _  _  _
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|

 """

import sys

SEGMENTS = {
    0: {
        0: " _ ",
        1: "| |",
        2: "|_|"
    },
    1: {
        0: "   ",
        1: "  |",
        2: "  |"
    },
    2: {
        0: " _ ",
        1: " _|",
        2: "|_ "
    },
    3: {
        0: " _ ",
        1: " _|",
        2: " _|"
    },
    4: {
        0: "   ",
        1: "|_|",
        2: "  |",
    },
    5: {
        0: " _ ",
        1: "|_ ",
        2: " _|",
    },
    6: {
        0: " _ ",
        1: "|_ ",
        2: "|_|",
    },
    7: {
        0: " _ ",
        1: "  |",
        2: "  |",
    },
    8: {
        0: " _ ",
        1: "|_|",
        2: "|_|",
    },
    9: {
        0: " _ ",
        1: "|_|",
        2: " _|",
    }
}

for n in sys.argv[1:]:
    first = []
    second = []
    third = []
    for m in list(n):
        p = int(m)
        first.append(SEGMENTS[p][0])
        second.append(SEGMENTS[p][1])
        third.append(SEGMENTS[p][2])

print(*first, sep='')
print(*second, sep='')
print(*third, sep='')
