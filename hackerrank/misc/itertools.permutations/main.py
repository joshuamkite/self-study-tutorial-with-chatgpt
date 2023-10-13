# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

s = input().split()

mutiz = list(permutations([*s[0]], int(s[1])))

for m in sorted(mutiz):
    print(''.join(m))
