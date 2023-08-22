import sys

alpha = "abcdefghijklmnopqrstuvwxyz"

for arg in sys.argv[1:]:
    if (set([*alpha])).issubset(set([*arg.lower()])):
        print(arg)
