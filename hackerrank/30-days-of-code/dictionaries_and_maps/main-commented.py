# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == '__main__':  # entrypoint to our code - 'main' function
    book = {}  # initialise empty map to which we can add entries
    # get first line input (represents number of entries)
    n = int(input().strip())
    for e in range(n):  # for entries in _next_ `n` lines
        e = input().strip().split(" ")  # make a list split on spaces
        # append to list using first index as key and second index as value
        book[e[0]] = e[1]
    for e in range(n+1, (n*2)+1):  # for _next_ `n` entries
        e = input().strip()  # strip newlines from input
        # use `.get` to return value for key or default value provided here if not found
        r = book.get(e, "Not found")
        if r == "Not found":  # if our entry is "Not Found"
            print(r)  # print that message
        else:  # otherwise
            print(f"{e}={r}")  # print <key>=<value>
