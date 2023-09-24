def print_rangoli(size):
    # your code goes here

    myString = ("abcdefghijklmnopqrstuvwxyz"[:size])

    # top half
    for i in range(len(myString), 0, -1):
        thisString = (myString[i-1:])  # slice `i` characters from alphabet
        # reverse thisString starting from 2nd character
        backString = ((thisString[1:])[::-1])
        line = (backString+thisString)
        # insert `-` between each character
        myline = '-'.join(line[i:i + 1] for i in range(0, len(line), 1))
        # center string at max line length
        myline = myline.center((len(myString)*4)-3, '-')
        print(myline)
    # # bottom half
    for i in range(len(myString)-1):
        thisString = (myString[i+1:])
        backString = ((thisString[1:])[::-1])
        line = (backString+thisString)
        myline = '-'.join(line[i:i + 1] for i in range(0, len(line), 1))
        myline = myline.center((len(myString)*4)-3, '-')
        print(myline)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
