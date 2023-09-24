def print_formatted(number):
    # your code goes here
    width = len(str(bin(number)[2:]))
    for i in range(1, number+1):
        deca = str(i).rjust(width)
        octa = str(oct(i)[2:]).rjust(width)
        hexa = (str(hex(i)[2:])).upper().rjust(width)
        bina = str(bin(i)[2:]).rjust(width)
        print(deca, octa, hexa, bina)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
