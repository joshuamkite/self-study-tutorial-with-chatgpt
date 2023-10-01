def merge_the_tools(string, k):
    # your code goes here
    # print(string)
    # print(k)

    my_word = list(string)

    for i in range(0, len(my_word), k):
        print(''.join(list(dict.fromkeys(my_word[i:i+k]))))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
