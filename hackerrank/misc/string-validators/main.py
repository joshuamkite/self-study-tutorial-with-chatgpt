if __name__ == '__main__':
    s = input()
    h = {
        1: False,
        2: False,
        3: False,
        4: False,
        5: False,
    }
    for c in s:
        if c.isalnum():
            h[1] = True
        if c.isalpha():
            h[2] = True
        if c.isdigit():
            h[3] = True
        if c.islower():
            h[4] = True
        if c.isupper():
            h[5] = True
    for k in h:
        print(h[k])
