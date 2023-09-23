if __name__ == '__main__':
    size = input().strip().split(' ')
    n = int(size[0])
    m = int(size[1])
    if m != 3 * n:
        print("second value must be three times first value")
        exit()
    else:
        pattern = '.|.'
        # ascending
        for i in range(1, n, 2):
            print((pattern * i).center(m, '-'))
        # middle
        print('WELCOME'.center(m, '-'))
        # descending
        for i in range(n-2, 0, -2):
            print((pattern * i).center(m, '-'))
