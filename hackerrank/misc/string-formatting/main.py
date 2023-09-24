def print_formatted(number):
    # your code goes here
    width = len(str(bin(number)[2:]))

    for i in range(1, number+1):
        deca = str(i)
        octa = str(oct(i)[2:])
        hexa = str(hex(i)[2:]).upper()
        bina = str(bin(i)[2:])
        myLine = [deca, octa, hexa, bina]
        ourLine = []
        for v in myLine:
            v = v.rjust(width, ' ')
            ourLine.append(v)
        print(*ourLine)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
