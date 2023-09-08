
t = int(input().strip())

for _ in range(t):
    s = input().strip()
    even_chars = [s[i] for i in range(0, len(s), 2)]
    odd_chars = [s[i] for i in range(1, len(s), 2)]
    print(''.join(even_chars), ''.join(odd_chars))
