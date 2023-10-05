# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    s = input()
    t = []

    alpha = "abcdefghijklmnopqrstuvwxyz"

    t.extend(sorted(c for c in s if c in alpha))
    t.extend(sorted(c for c in s if c in alpha.upper()))
    t.extend(sorted([c for c in s if c.isdigit() and int(c) % 2 != 0]))
    t.extend(sorted([c for c in s if c.isdigit() and int(c) % 2 == 0]))

    print(''.join(t))
