import sys

for n in sys.argv[1:]:
    p = n.replace('-', '')
    total = sum(int(p[i]) * (10 - i) for i in range(9))
    check = 11 - (total % 11)
    if check == 10:
        check = "X"
    elif check == 11:
        check = 0
    print(f"{n}{check}")
