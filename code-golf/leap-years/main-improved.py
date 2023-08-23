for y in range(1800, 2401):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print(y)
