# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == '__main__':
    book = {}
    n = int(input().strip())
    for _ in range(n):
        entry = input().strip().split(" ")
        book[entry[0]] = entry[1]

    # Read queries until there's no more input
    while True:
        try:
            query = input().strip()
            result = book.get(query, "Not found")
            if result == "Not found":
                print(result)
            else:
                print(f"{query}={result}")
        except EOFError:
            break
