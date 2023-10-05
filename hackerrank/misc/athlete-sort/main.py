if __name__ == '__main__':
    n, m = map(int, input().split())
    records = []
    for athlete in range(n):
        # append object of type list, casting each split item in list to int
        records.append([int(i) for i in input().split()])

    k = int(input())
    # sort records by k element without reassigning variable
    records.sort(key=lambda x: x[k])

    for entry in records:
        print(*entry)
