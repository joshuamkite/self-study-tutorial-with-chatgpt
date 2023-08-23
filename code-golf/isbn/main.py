import sys


for n in sys.argv[1:]:
    p = n.replace('-', '')
    total = 0
    m = list(p)
    total += (int(m[0])*10)
    total += (int(m[1])*9)
    total += (int(m[2])*8)
    total += (int(m[3])*7)
    total += (int(m[4])*6)
    total += (int(m[5])*5)
    total += (int(m[6])*4)
    total += (int(m[7])*3)
    total += (int(m[8])*2)
    check = 11-(total % 11)
    if check == 10:
        check = "X"
    if check == 11:
        check = 0
    print(f"%s%s" % (n, check))
