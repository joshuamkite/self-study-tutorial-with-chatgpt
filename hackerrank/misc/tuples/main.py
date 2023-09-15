if __name__ == '__main__':
    n = int(input())
    arr = tuple(map(int, input().split()))
    print(hash(arr))
