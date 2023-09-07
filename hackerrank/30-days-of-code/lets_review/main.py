# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input().strip())
for a in range(t):
    odd = []
    even = []
    n = [*input().strip()]
    for l in range(0, (len(n)), 2):
        even.append(n[l])
    for m in range(1, (len(n)), 2):
        odd.append(n[m])
    print(f"{''.join(even)} {''.join(odd)}")
