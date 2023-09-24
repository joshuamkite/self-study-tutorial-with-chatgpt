def print_rangoli(size):
    # your code goes here

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rangoli = []

    for i in range(size):
        s = "-".join(alphabet[size-1:i:-1] + alphabet[i:size])
        rangoli.append(s.center(4*size-3, '-'))

    print('\n'.join(rangoli[::-1] + rangoli[1:]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
