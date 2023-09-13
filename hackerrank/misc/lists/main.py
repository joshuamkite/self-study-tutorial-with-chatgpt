if __name__ == '__main__':
    n = int(input().strip())  # use first line of input
    l = []
    for _ in range(n):  # blank function for remaining lines
        p = input().strip().split(" ")  # subsequent input split on space to list
        if p[0] == "insert":
            l.insert(int(p[1]), int(p[2]))
        elif p[0] == "print":
            print(l)
        elif p[0] == "remove":
            l.remove(int(p[1]))
        elif p[0] == "append":
            l.append(int(p[1]))
        elif p[0] == "sort":
            l.sort()
        elif p[0] == "pop":
            l.pop()
        elif p[0] == "reverse":
            l.reverse()
