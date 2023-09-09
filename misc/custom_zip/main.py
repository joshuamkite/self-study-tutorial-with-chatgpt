def zap(a, b):
    zop = []
    for i, val in enumerate(a):
        zop.append((val, b[i]))
    return zop
