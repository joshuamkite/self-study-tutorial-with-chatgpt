def minion_game(string):
    # your code goes here

    # Get all substrings of string - from https://www.geeksforgeeks.org/python-get-all-substrings-of-given-string/
    # Using list comprehension + string slicing
    res = [string[i: j] for i in range(len(string))
           for j in range(i + 1, len(string) + 1)]

    vowels = list("AEIOU")
    stuart = []
    kevin = []
    for e in res:
        if e[0] in vowels:
            kevin.append(e)
        else:
            stuart.append(e)
    if len(stuart) > len(kevin):
        print(f"Stuart {len(stuart)}")
    else:
        print(f"Kevin {len(kevin)}")


if __name__ == '__main__':
    s = input()
    minion_game(s)
