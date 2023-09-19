def mutate_string(string, position, character):
    # add code here
    mut = string[:position] + character + string[(position+1):]
    return mut

# pre-provided
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
