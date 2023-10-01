from itertools import groupby

if __name__ == "__main__":
    s = input()

    compressed = [(len(list(group)), int(key)) for key, group in groupby(s)]

    print(*compressed)
