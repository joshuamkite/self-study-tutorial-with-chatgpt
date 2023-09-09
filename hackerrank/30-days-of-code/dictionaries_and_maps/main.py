# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == '__main__':
    book = {}
    n = int(input().strip())
    for e in range(n):
        e = input().strip().split(" ")
        book[e[0]] = e[1]
    for e in range(n+1, (n*2)+1):
        e = input().strip()
        r = book.get(e, "Not found")
        if r == "Not found":
            print(r)
        else:
            print(f"{e}={r}")
