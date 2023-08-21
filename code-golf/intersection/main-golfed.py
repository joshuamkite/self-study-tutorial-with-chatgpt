import sys

for arg in sys.argv[1:]:
    c = list(map(int, arg.split()))
    x = (min((c[0]+c[2]), (c[4]+c[6]))-max(c[0], c[4]))
    y = (min((c[1]+c[3]), (c[5]+c[7]))-max(c[1], c[5]))
    if x > 0 and y > 0:
        print(x*y)
    else:
        print(0)
