if __name__ == '__main__':
    size = (input().strip()).split(' ')
    n = int(size[0])
    m = int(size[1])
    if m != 3 * n:
        print("second value must be three times first value")
        exit()
    else:
        # ascending
        for p in range((n-1)//2):
            print(f"{'-'*(((m-2)//2)-3*p)}{'.|.'*(2*p+1)}{'-'*(((m-2)//2)-3*p)}")
        # middle
        print(f"{'-'*((m-7)//2)}WELCOME{'-'*((m-7)//2)}")
        # descending
        for p in range(((n-1)//2)-1, -1, -1):
            print(f"{'-'*(((m-2)//2)-3*p)}{'.|.'*(2*p+1)}{'-'*(((m-2)//2)-3*p)}")
