vowels = "aeiou"


def vowel_check(char):
    if char in vowels:
        return True
    else:
        return False


if __name__ == '__main__':
    w = input().strip()
    v_count = 0
    for character in w:
        if vowel_check(character):
            v_count += 1
    print(v_count)
